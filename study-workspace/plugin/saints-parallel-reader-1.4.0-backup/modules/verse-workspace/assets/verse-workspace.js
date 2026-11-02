(function () {
  'use strict';

  var config = window.SaintsVerseWorkspace;
  if (!config || !document.body.classList.contains('saints-parallel-page')) return;

  var LEVELS = {
    notable: 'Clear difference',
    minor: 'Subtle difference',
    none: 'No difference in meaning'
  };
  var DIRECTIONS = {
    keeps: 'The Greek keeps',
    loses: 'The Greek loses',
    between: 'Between the translations'
  };
  var PAGES = [
    ['overall', 'Overall Message'],
    ['unseen', 'Unseen Change'],
    ['words', 'Word Study'],
    ['instructions', 'Instructions'],
    ['references', 'Cross-references']
  ];

  var PANEL_GAP = 12;
  var STUDY_WIDTH = 520;
  var CONTENTS_WIDTH = 320;
  var PANEL_MIN_WIDTH = 340;
  var PANEL_MIN_SCREEN = 1100;

  var data, panel, body, title, previous, next, trigger, contents, contentsButton;
  var tabs = {};
  var current = 0;
  var page = 'overall';
  var references = null;

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function button(className, text) {
    var node = el('button', className, text);
    node.type = 'button';
    return node;
  }

  function section(heading, className) {
    var box = el('section', 'svw-section' + (className ? ' ' + className : ''));
    box.append(el('h3', '', heading));
    return box;
  }

  function foldout(heading, open) {
    var box = el('details', 'svw-fold');
    box.open = !!open;
    box.append(el('summary', '', heading));
    return box;
  }

  function rowFor(verse) {
    return document.getElementById('parallel-' + verse.ref.replace(':', '-'));
  }

  function reading(label, text) {
    var box = el('div', 'svw-reading');
    box.append(el('p', 'svw-label', label), el('p', '', text));
    return box;
  }

  function overallPage(verse) {
    var message = section('Overall Message', 'svw-received');
    var meaning = section('What this verse teaches');
    var shared = section('What all four translations say');
    var list = el('ul', 'svw-shared');
    message.append(el('p', '', verse.received));
    meaning.append(el('p', 'svw-explain', verse.explain));
    verse.shared.forEach(function (point) {
      list.append(el('li', '', point));
    });
    shared.append(list);
    return [message, meaning, shared];
  }

  function changesList(verse) {
    var list = el('ul', 'svw-lost');
    verse.lost.forEach(function (item) {
      var row = el('li', 'svw-dir-' + item.dir);
      row.append(el('span', 'svw-dir', DIRECTIONS[item.dir]), el('span', '', item.text));
      list.append(row);
    });
    return list;
  }

  function reviewFold(verse) {
    if (!verse.flags.length) return null;
    var box = foldout('To check in review (' + verse.flags.length + ')', true);
    box.classList.add('svw-review');
    var list = el('ul');
    verse.flags.forEach(function (text) {
      list.append(el('li', '', text));
    });
    box.append(list);
    return box;
  }

  function sourceFold(verse) {
    var box = foldout('Full Hebrew and Greek study');
    box.append(el('p', 'svw-label', 'Hebrew and Greek · ' + verse.badge), el('p', '', verse.siteNote));
    if (verse.whyNote) box.append(el('p', 'svw-label', 'How the difference arose'), el('p', '', verse.whyNote));
    var link = el('a', '', 'Open the full source study');
    link.href = verse.link;
    box.append(link);
    return box;
  }

  function unseenPage(verse) {
    var changes = section('Unseen Change');
    var compare = foldout('Compare the wording');
    var chapter = foldout('Unseen Change in this chapter');
    changes.append(el('p', 'svw-chip svw-chip-' + verse.level, LEVELS[verse.level]), changesList(verse));
    compare.append(
      reading('Hebrew–English', verse.readings.hebrew),
      reading('Latin–English', verse.readings.latin),
      reading('King James', verse.readings.kjv)
    );
    chapter.append(el('p', '', data.chapterNote.lost));
    return [changes, compare, reviewFold(verse), sourceFold(verse), chapter];
  }

  function lexiconSection(heading, verse) {
    var box = section(heading);
    var entries = verse.entries.map(function (id) { return data.lexicon[id]; }).filter(function (entry) {
      return entry.group === heading;
    });
    if (!entries.length) box.append(el('p', 'svw-fine', 'No ' + heading + ' entry matches this verse.'));
    entries.forEach(function (entry) {
      var fold = foldout(entry.name);
      var link = el('a', '', 'Open the full entry');
      link.href = entry.link;
      fold.append(el('p', '', entry.text), link);
      box.append(fold);
    });
    return box;
  }

  function wordsPage(verse) {
    var box = section('Key words in this verse');
    if (!verse.words.length) box.append(el('p', 'svw-fine', 'This verse has no key word study yet.'));
    verse.words.forEach(function (word) {
      var item = el('div', 'svw-word');
      item.append(el('p', 'svw-label', word.word + ' \u00b7 ' + word.greek), el('p', '', word.note));
      if (word.see) item.append(el('p', 'svw-fine', 'See ' + word.see));
      box.append(item);
    });
    return [box, lexiconSection('Terminology', verse), lexiconSection('Lexicon', verse), lexiconSection('Divine Names', verse)];
  }

  function instructionsPage(verse) {
    var box = section('Instructions from this verse');
    var list = el('ul', 'svw-instructions');
    verse.instructions.forEach(function (item) {
      var row = el('li', 'svw-basis-' + item.basis);
      var heading = el('div', 'svw-ref-heading');
      heading.append(
        el('span', 'svw-instruction-type', item.type),
        el('span', 'svw-instruction-basis', item.basis === 'stated' ? 'Stated in the verse' : 'Study reflection')
      );
      row.append(heading, el('p', '', item.text));
      list.append(row);
    });
    box.append(list);
    var direct = verse.instructions.some(function (item) { return item.type === 'Law' || item.type === 'Command'; });
    if (!direct) box.append(el('p', 'svw-fine', 'This verse gives no law or command to mankind.'));
    return [box];
  }

  function referenceCard(row) {
    var card = el('article', 'svw-ref-card');
    var heading = el('div', 'svw-ref-heading');
    var link = el(row.link ? 'a' : 'span', 'svw-ref-link', row.ref);
    if (row.link) link.href = row.link;
    heading.append(link, el('span', 'svw-ref-type', row.type));
    card.append(heading);
    if (!row.readings.length) card.append(el('p', 'svw-fine', 'This passage isn’t in this edition, so its wording can’t be shown.'));
    row.readings.forEach(function (reading) {
      var verseText = el('p', 'svw-ref-text', reading.text);
      if (row.readings.length > 1) {
        verseText.prepend(el('span', 'svw-ref-number', reading.ref + ' '));
      }
      card.append(verseText);
    });
    card.append(el('p', 'svw-ref-how', row.how));
    if (row.why) {
      var why = el('p', 'svw-ref-why');
      why.append(el('strong', '', 'Why it matters: '), document.createTextNode(row.why));
      card.append(why);
    }
    return card;
  }

  function referenceGroup(rows, strength) {
    return rows.filter(function (row) { return row.strength === strength; });
  }

  function fillReferences(nodes, verse) {
    var rows = references.verses[verse.ref.split(':')[1]] || [];
    var strong = referenceGroup(rows, 'supported');
    var loose = referenceGroup(rows, 'weak');
    var unsupported = referenceGroup(rows, 'unsupported');
    var list = section('Referenced verses (' + rows.length + ')');

    if (!rows.length) list.append(el('p', 'svw-fine', 'This verse has no cross-references listed.'));
    strong.forEach(function (row) { list.append(referenceCard(row)); });
    nodes.append(list);
    [['Looser connections', loose], ['Reviewed and not supported', unsupported]].forEach(function (group) {
      if (!group[1].length) return;
      var fold = foldout(group[0] + ' (' + group[1].length + ')', !strong.length);
      group[1].forEach(function (row) { fold.append(referenceCard(row)); });
      nodes.append(fold);
    });
    nodes.append(el('p', 'svw-fine', references.source + ' ' + references.review));
  }

  function referencesPage(verse) {
    var index = current;
    var main = section('Main verse · ' + data.book + ' ' + verse.ref, 'svw-received');
    var list = el('div', 'svw-ref-list');
    main.append(el('p', '', verse.readings.saints));
    if (references) {
      fillReferences(list, verse);
      return [main, list];
    }
    var waiting = el('p', 'svw-fine', 'Loading cross-references…');
    list.append(waiting);
    var failed = function () { waiting.textContent = 'Cross-references could not be loaded.'; };
    fetch(config.referencesUrl)
      .then(function (response) { return response.ok ? response.json() : null; })
      .then(function (loaded) {
        if (!loaded) {
          failed();
          return;
        }
        references = loaded;
        if (page === 'references' && index === current) {
          waiting.remove();
          fillReferences(list, verse);
        }
      })
      .catch(failed);
    return [main, list];
  }

  function render() {
    var verse = data.verses[current];
    var build = { overall: overallPage, unseen: unseenPage, words: wordsPage, instructions: instructionsPage, references: referencesPage }[page];
    title.textContent = data.book + ' ' + verse.ref;
    previous.disabled = current === 0;
    next.disabled = current === data.verses.length - 1;
    PAGES.forEach(function (item) {
      tabs[item[0]].setAttribute('aria-selected', String(item[0] === page));
    });
    body.replaceChildren();
    body.scrollTop = 0;
    build(verse).concat(page === 'words' ? [el('p', 'svw-fine', data.credit)] : []).forEach(function (node) {
      if (node) body.append(node);
    });
    document.querySelectorAll('.svw-active').forEach(function (active) {
      active.classList.remove('svw-active');
    });
    var row = rowFor(verse);
    if (row) {
      row.classList.add('svw-active');
      row.scrollIntoView({ block: 'nearest' });
    }
    history.replaceState(null, '', '#study-' + verse.ref.replace(':', '-'));
  }

  // Keep each panel beside the reading column, so the eye doesn't cross the screen.
  // The page slides over when there isn't room beside it. Narrow screens keep the overlay.
  function placePanels() {
    var main = document.querySelector('main') || document.querySelector('.sgp');
    var column = document.querySelector('.sgp-scroll') || document.querySelector('.sgp');
    var width = document.documentElement.clientWidth;
    if (!main || !column) return;
    main.style.transform = '';
    [panel, contents].forEach(function (node) {
      node.style.left = node.style.right = node.style.width = '';
    });
    if (width < PANEL_MIN_SCREEN) return;

    var box = column.getBoundingClientRect();
    var studyOpen = !panel.hidden;
    var contentsOpen = !contents.hidden;
    var room = width - box.width - PANEL_GAP * 2;
    var studyWidth = Math.max(PANEL_MIN_WIDTH, Math.min(STUDY_WIDTH, room));
    var contentsWidth = Math.max(PANEL_MIN_WIDTH, Math.min(CONTENTS_WIDTH, room));
    var shift = 0;
    if (studyOpen && !contentsOpen) {
      shift = Math.max(-box.left, Math.min(0, width - PANEL_GAP - studyWidth - PANEL_GAP - box.right));
    } else if (contentsOpen && !studyOpen) {
      shift = Math.min(width - box.right, Math.max(0, PANEL_GAP + contentsWidth + PANEL_GAP - box.left));
    }
    if (shift) main.style.transform = 'translateX(' + shift + 'px)';
    if (studyOpen) {
      panel.style.left = Math.min(box.right + shift + PANEL_GAP, width - PANEL_GAP - studyWidth) + 'px';
      panel.style.right = 'auto';
      panel.style.width = studyWidth + 'px';
    }
    if (contentsOpen) {
      contents.style.left = Math.max(box.left + shift - PANEL_GAP - contentsWidth, PANEL_GAP) + 'px';
      contents.style.width = contentsWidth + 'px';
    }
  }

  function open(index, from) {
    current = index;
    trigger = from || trigger;
    panel.hidden = false;
    placePanels();
    render();
    title.focus();
  }

  function close() {
    panel.hidden = true;
    placePanels();
    document.querySelectorAll('.svw-active').forEach(function (active) {
      active.classList.remove('svw-active');
    });
    history.replaceState(null, '', location.pathname + location.search);
    if (trigger) trigger.focus();
  }

  function verseInView() {
    var found = 0;
    data.verses.some(function (verse, index) {
      var row = rowFor(verse);
      if (row && row.getBoundingClientRect().bottom > 120) {
        found = index;
        return true;
      }
      return false;
    });
    return found;
  }

  function buildPanel() {
    var header = el('header', 'svw-header');
    var heading = el('div', 'svw-heading');
    var controls = el('div', 'svw-controls');
    var strip = el('div', 'svw-tabs');
    var shut = button('svw-button', 'Close');

    panel = el('aside', 'svw-panel');
    panel.hidden = true;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Study Workspace');
    title = el('h2', 'svw-title');
    title.tabIndex = -1;
    previous = button('svw-button', '← Previous');
    next = button('svw-button', 'Next →');
    previous.addEventListener('click', function () { current--; render(); });
    next.addEventListener('click', function () { current++; render(); });
    shut.addEventListener('click', close);

    strip.setAttribute('role', 'tablist');
    strip.setAttribute('aria-label', 'Study pages');
    PAGES.forEach(function (item) {
      var tab = button('svw-tab', item[1]);
      tab.setAttribute('role', 'tab');
      tab.addEventListener('click', function () { page = item[0]; render(); });
      tabs[item[0]] = tab;
      strip.append(tab);
    });

    heading.append(title, shut);
    controls.append(previous, next);
    header.append(el('p', 'svw-eyebrow', 'Study Workspace · ' + data.status), heading, controls, strip);
    body = el('div', 'svw-body');
    body.setAttribute('role', 'tabpanel');
    panel.append(header, body);
    document.body.append(panel);

    panel.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') close();
    });
  }

  function closeContents() {
    contents.hidden = true;
    placePanels();
    contentsButton.setAttribute('aria-expanded', 'false');
    contentsButton.focus();
  }

  function contentsGroup(heading) {
    var box = el('section', 'svw-contents-group');
    box.append(el('h3', '', heading));
    return box;
  }

  function chapterLinks() {
    var box = contentsGroup('Chapters');
    var grid = el('div', 'svw-chapters');
    var select = document.getElementById('sgp-chapter');
    Array.prototype.forEach.call(select ? select.options : [], function (option) {
      var link = el('a', '', option.value);
      link.href = location.pathname + '?gp_ch=' + option.value;
      link.setAttribute('aria-label', option.textContent);
      if (option.selected) link.setAttribute('aria-current', 'page');
      grid.append(link);
    });
    box.append(grid);
    return box;
  }

  function headingLinks() {
    var box = contentsGroup(data.book + ' ' + data.chapter);
    var list = el('ul', 'svw-headings');
    data.headings.forEach(function (heading) {
      var index = data.verses.findIndex(function (verse) { return verse.ref === heading.ref; });
      var item = el('li');
      var link = button('svw-link', heading.title);
      link.addEventListener('click', function () {
        var row = rowFor(data.verses[index]);
        if (row) row.scrollIntoView({ block: 'center' });
        current = index;
        if (!panel.hidden) render();
        closeContents();
      });
      item.append(link);
      list.append(item);
    });
    box.append(list);
    return box;
  }

  function buildContents() {
    var header = el('header', 'svw-contents-header');
    var shut = button('svw-button', 'Close');
    var list = el('div', 'svw-contents-body');
    var more = contentsGroup('Translations and books');

    contents = el('aside', 'svw-contents');
    contents.id = 'svw-contents';
    contents.hidden = true;
    contents.setAttribute('role', 'dialog');
    contents.setAttribute('aria-label', 'Contents');
    header.append(el('h2', '', 'Contents'), shut);
    shut.addEventListener('click', closeContents);

    // These controls keep working where they are moved to, and leave the page simpler.
    ['.sgp-columns', '.sgp-book-picker', '.sgp-library-link'].forEach(function (selector) {
      var node = document.querySelector(selector);
      if (node) more.append(node);
    });
    var about = Array.prototype.find.call(document.querySelectorAll('.sgp details'), function (item) {
      return /About the texts/.test(item.textContent);
    });
    if (about) more.append(about);

    list.append(headingLinks(), chapterLinks(), more);
    contents.append(header, list);
    document.body.append(contents);
    contents.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeContents();
    });
  }

  function buildToolbar() {
    var toolbar = document.querySelector('.sgp-toolbar');
    var study = button('svw-main-button svw-main-study', 'Study');
    if (!toolbar) return;
    contentsButton = button('svw-main-button', 'Contents');
    contentsButton.setAttribute('aria-expanded', 'false');
    contentsButton.setAttribute('aria-controls', 'svw-contents');
    contentsButton.addEventListener('click', function () {
      contents.hidden = !contents.hidden;
      placePanels();
      contentsButton.setAttribute('aria-expanded', String(!contents.hidden));
      if (!contents.hidden) contents.querySelector('button').focus();
    });
    study.addEventListener('click', function () { open(panel.hidden ? verseInView() : current, study); });
    toolbar.prepend(contentsButton);
    toolbar.insertBefore(study, toolbar.querySelector('nav'));
    var hint = el('p', 'svw-hint', 'Click a verse number to study that verse.');
    toolbar.after(hint);
  }

  function linkVerses() {
    data.verses.forEach(function (verse, index) {
      var row = rowFor(verse);
      var link = row && row.querySelector('th a');
      if (!link) return;
      link.classList.add('svw-verse', 'svw-level-' + verse.level);
      link.setAttribute('aria-label', 'Study ' + data.book + ' ' + verse.ref + ', ' + LEVELS[verse.level]);
      link.addEventListener('click', function (event) {
        event.preventDefault();
        open(index, link);
      });
    });
  }

  function renamePage() {
    var heading = document.querySelector('h1');
    document.body.classList.add('saints-study-bible');
    if (heading) heading.textContent = data.book + ' — Study Bible';
    document.title = document.title.replace('Parallel Reader', 'Study Bible');
    var trail = document.querySelector('.saints-location');
    if (trail) {
      trail.querySelectorAll('li, span').forEach(function (item) {
        if (!item.children.length && /Parallel Reader/.test(item.textContent)) {
          item.textContent = item.textContent.replace('Parallel Reader', 'Study Bible');
        }
      });
    }
  }

  function start(loaded) {
    if (!document.querySelector('tr[id^="parallel-"]')) return;
    data = loaded;
    renamePage();
    buildPanel();
    buildContents();
    buildToolbar();
    linkVerses();
    window.addEventListener('resize', placePanels);
    var match = location.hash.match(/^#study-(\d+)-(\d+)$/);
    if (match) {
      var index = data.verses.findIndex(function (verse) { return verse.ref === match[1] + ':' + match[2]; });
      if (index >= 0) open(index);
    }
  }

  if (config.data) {
    references = config.references || null;
    start(config.data);
    return;
  }
  // If the data can't load, the Parallel Reader simply stays as it was.
  fetch(config.dataUrl)
    .then(function (response) { return response.ok ? response.json() : null; })
    .then(function (loaded) { if (loaded) start(loaded); })
    .catch(function () {});
}());
