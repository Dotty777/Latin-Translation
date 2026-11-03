<?php
defined('ABSPATH') || exit;

const SAINTS_PARALLEL_READER_LATIN_PHRASE_WORDS = 8; // Latin outside a verse block may stay as a phrase up to this length.

/** Labels of the expandable blocks that exist to hold a whole Latin verse. */
function saints_parallel_reader_latin_labels() {
    return ['Read the Clementine Latin', 'Latin wording and source links', 'Latin wording and translation source', 'Latin prologue'];
}

/** Where the element opening at $start ends, allowing for the same tag nested inside it. */
function saints_parallel_reader_latin_element_end($html, $tag, $start) {
    $depth = 0;
    $offset = $start;
    while (preg_match('~<(/?)'.$tag.'\b[^>]*>~i', $html, $match, PREG_OFFSET_CAPTURE, $offset)) {
        $offset = $match[0][1] + strlen($match[0][0]);
        $depth += '' === $match[1][0] ? 1 : -1;
        if (0 === $depth) {
            return $offset;
        }
    }
    return false;
}

/** Whether $start sits inside an expandable block labelled as a Latin verse. */
function saints_parallel_reader_latin_in_block($html, $start) {
    $summary = strrpos(substr($html, max(0, $start - 4000), min($start, 4000)), '<summary');
    if (false === $summary) {
        return false;
    }
    $summary += max(0, $start - 4000);
    $between = substr($html, $summary, $start - $summary);
    if (false !== stripos($between, '</details>')) {
        return false;
    }
    $label = trim(wp_strip_all_tags(substr($between, 0, (int) stripos($between, '</summary>'))));
    foreach (saints_parallel_reader_latin_labels() as $known) {
        if (0 === strpos($label, $known)) {
            return true;
        }
    }
    return false;
}

/** Keep the links a Latin block also holds, and drop the block when nothing is left. */
function saints_parallel_reader_latin_tidy($html) {
    $labels = implode('|', array_map(function ($label) { return preg_quote($label, '~'); }, saints_parallel_reader_latin_labels()));
    $tidied = preg_replace_callback(
        '~(<details\b[^>]*>\s*<summary[^>]*>)\s*(?:'.$labels.')[^<]*(</summary>)((?:(?!</?details\b).)*)(</details>)~is',
        function ($match) {
            if ('' === trim(wp_strip_all_tags($match[3])) && false === stripos($match[3], '<a ')) {
                return '';
            }
            return $match[1].'Source links'.$match[2].$match[3].$match[4];
        },
        $html
    );
    return null === $tidied ? $html : $tidied;
}

/** Remove whole Latin verses from a page, leaving short phrases in the surrounding notes. */
function saints_parallel_reader_latin_filter($html) {
    if (!is_string($html) || !preg_match('~\blang=["\']la["\']~i', $html)) {
        return $html;
    }
    $output = '';
    $position = 0;
    while (preg_match('~<(p|span|div)\b[^>]*\blang=["\']la["\'][^>]*>~i', $html, $match, PREG_OFFSET_CAPTURE, $position)) {
        $start = $match[0][1];
        $end = saints_parallel_reader_latin_element_end($html, strtolower($match[1][0]), $start);
        if (false === $end) {
            break;
        }
        $text = trim(wp_strip_all_tags(substr($html, $start, $end - $start)));
        $words = count(preg_split('~\s+~u', $text, -1, PREG_SPLIT_NO_EMPTY));
        $numbered = preg_match('~^Latin\s+\d+:\d+~', $text); // A verse reference means a whole verse, however short.
        $keep = !$numbered && $words <= SAINTS_PARALLEL_READER_LATIN_PHRASE_WORDS && !saints_parallel_reader_latin_in_block($html, $start);
        $output .= substr($html, $position, ($keep ? $end : $start) - $position);
        $position = $end;
    }
    return saints_parallel_reader_latin_tidy($output.substr($html, $position));
}

add_filter('the_content', 'saints_parallel_reader_latin_filter', 9999);
