<?php
/**
 * Plugin Name: Saints Pentateuch Work
 * Description: Staging-only helper for the Genesis–Deuteronomy Parallel Reader corrections. Jobs are written as JSON to the private page "pentateuch-work-control"; results go to private "pentateuch-work-out-*" pages. Edits are exact text replacements in Law, Judgement, Gospel, Wisdom and Revelation comparison pages only, checked against each page's current fingerprint, and saved as normal revisions so every change can be rolled back.
 * Version: 1.13.0
 * Author: Saints.Bible
 */
if (!defined('ABSPATH')) exit;

const SPW_CONTROL = 'pentateuch-work-control';
const SPW_BOOKS = array(1029, 1036, 1037, 1042, 1039, 935, 934, 936, 937, 2488, 2504, 2498, 2673, 2769, 17956, 17957, 1479, 2211, 2214, 2210, 2232, 2228, 2236, 2344, 2444, 2373, 2372, 2424, 2475, 2487, 2486, 2506); // Genesis–Deuteronomy; Matthew–John; Psalms, Proverbs, Ecclesiastes, Song of Songs, Lamentations, Wisdom of Solomon, Sirach; Revelation; Judgement: Joshua, Judges, Ruth, 1–2 Samuel, 1–2 Kings, 1–2 Chronicles, 1–2 Maccabees, Ezra, Nehemiah, Esther, Job

function spw_out($key, $data) {
    $slug = 'pentateuch-work-out-' . preg_replace('/[^a-z0-9-]/', '', strtolower($key));
    // Padding keeps every report large enough that the connector saves it to a file instead of returning it inline.
    $body = '<!-- wp:html --><pre>' . base64_encode(gzcompress(wp_json_encode($data), 9)) . '</pre><!-- pad ' . base64_encode(random_bytes(120000)) . ' --><!-- /wp:html -->';
    $existing = get_page_by_path($slug, OBJECT, 'page');
    $post = array('post_title' => $slug, 'post_name' => $slug, 'post_type' => 'page', 'post_status' => 'private', 'post_content' => $body);
    kses_remove_filters();
    if ($existing) { $post['ID'] = $existing->ID; wp_update_post(wp_slash($post)); }
    else { wp_insert_post(wp_slash($post)); }
    kses_init_filters();
}

function spw_allowed($id) {
    $p = get_post($id);
    if (!$p || $p->post_type !== 'page') return false;
    $parent = (int) $p->post_parent;
    if (in_array($parent, SPW_BOOKS, true)) return true;
    $gp = $parent ? (int) get_post_field('post_parent', $parent) : 0; // sub-pages one level down
    return in_array($gp, SPW_BOOKS, true);
}

function spw_fetch($url, $sha) {
    if (!preg_match('#^https://raw\.githubusercontent\.com/Dotty777/#i', $url)) return new WP_Error('url', 'only Dotty777 GitHub files');
    $r = wp_remote_get($url, array('timeout' => 60));
    if (is_wp_error($r)) return $r;
    $body = wp_remote_retrieve_body($r);
    if (hash('sha256', $body) !== strtolower($sha)) return new WP_Error('sha', 'sha256 mismatch');
    if (substr($url, -3) === '.gz') $body = gzdecode($body);
    $j = json_decode($body, true);
    return is_array($j) ? $j : new WP_Error('json', 'bad json');
}

function spw_job_probe($job) {
    $r = array('php' => PHP_VERSION, 'unfiltered_html' => current_user_can('unfiltered_html'), 'user' => get_current_user_id());
    $g = wp_remote_get('https://raw.githubusercontent.com/Dotty777/hebrew-translation/main/README.md', array('timeout' => 20));
    $r['github'] = is_wp_error($g) ? 'error: ' . $g->get_error_message() : wp_remote_retrieve_response_code($g) . ' ' . strlen(wp_remote_retrieve_body($g));
    $fns = get_defined_functions();
    $pat = isset($job['fn_pattern']) ? $job['fn_pattern'] : '/parallel|_gp_|sgp|prh|vulgate|masoretic/i';
    $r['functions'] = array_values(array_filter($fns['user'], function ($f) use ($pat) { return preg_match($pat, $f); }));
    $files = array();
    foreach ((array) (isset($job['dirs']) ? $job['dirs'] : array('saints-study-tools')) as $d) {
        $dir = WP_PLUGIN_DIR . '/' . basename($d);
        if (!is_dir($dir)) continue;
        $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir, FilesystemIterator::SKIP_DOTS));
        foreach ($it as $f) $files[basename($d) . '/' . substr($f->getPathname(), strlen($dir) + 1)] = $f->getSize();
    }
    ksort($files);
    $r['files'] = $files;
    $src = array();
    foreach ((array) (isset($job['read']) ? $job['read'] : array()) as $p) {
        $p = str_replace('..', '', $p);
        $full = WP_PLUGIN_DIR . '/' . $p;
        if (is_file($full) && filesize($full) < 3000000) $src[$p] = file_get_contents($full);
    }
    $r['sources'] = $src;
    $tr = array();
    if (!empty($job['transients'])) {
        global $wpdb;
        $tr = $wpdb->get_col($wpdb->prepare("SELECT option_name FROM {$wpdb->options} WHERE option_name LIKE %s LIMIT 500", '%' . $wpdb->esc_like($job['transients']) . '%'));
    }
    $r['options'] = $tr;
    return $r;
}

function spw_job_dump($job) {
    $out = array();
    foreach ((array) $job['ids'] as $id) {
        $id = (int) $id;
        if (!spw_allowed($id)) { $out[$id] = array('error' => 'not allowed'); continue; }
        $p = get_post($id);
        $out[$id] = array('slug' => $p->post_name, 'parent' => (int) $p->post_parent, 'modified' => $p->post_modified_gmt, 'md5' => md5($p->post_content), 'content' => $p->post_content);
    }
    return $out;
}

function spw_job_list($job) {
    $out = array();
    foreach (SPW_BOOKS as $b) {
        $q = get_pages(array('child_of' => $b, 'post_status' => 'publish,private,draft'));
        foreach ($q as $p) $out[] = array($p->ID, $p->post_parent, $p->post_name, strlen($p->post_content), md5($p->post_content));
    }
    return $out;
}

function spw_job_apply($job) {
    $edits = isset($job['url']) ? spw_fetch($job['url'], $job['sha256']) : (isset($job['pages']) ? $job : null);
    if (is_wp_error($edits)) return array('error' => $edits->get_error_message());
    $pages = isset($edits['pages']) ? $edits['pages'] : array();
    $res = array();
    $dry = !empty($job['dry_run']);
    foreach ($pages as $pg) {
        $id = (int) $pg['id'];
        if (!spw_allowed($id)) { $res[$id] = 'not allowed'; continue; }
        $content = get_post_field('post_content', $id, 'raw');
        if (md5($content) !== $pg['md5']) { $res[$id] = 'skipped: page changed (md5 ' . md5($content) . ')'; continue; }
        $new = isset($pg['content']) ? $pg['content'] : $content; $bad = array();
        foreach ((isset($pg['edits']) ? $pg['edits'] : array()) as $i => $e) {
            $n = substr_count($new, $e['old']);
            $want = isset($e['count']) ? (int) $e['count'] : 1;
            if ($n !== $want) { $bad[] = "edit $i found $n, expected $want"; continue; }
            $new = str_replace($e['old'], $e['new'], $new);
        }
        if ($bad) { $res[$id] = 'skipped: ' . implode('; ', $bad); continue; }
        if (isset($pg['new_md5']) && md5($new) !== $pg['new_md5']) { $res[$id] = 'skipped: result md5 ' . md5($new) . ' differs from expected'; continue; }
        if ($dry) { $res[$id] = 'dry-run ok ' . md5($new); continue; }
        kses_remove_filters();
        $u = wp_update_post(wp_slash(array('ID' => $id, 'post_content' => $new)), true);
        kses_init_filters();
        clean_post_cache($id);
        $after = md5(get_post_field('post_content', $id, 'raw'));
        $res[$id] = is_wp_error($u) ? 'error: ' . $u->get_error_message() : ($after === md5($new) ? 'ok ' . $after : 'saved but md5 ' . $after);
    }
    if (!empty($job['flush']) && !$dry) {
        global $wpdb;
        foreach ((array) $job['flush'] as $like) {
            $names = $wpdb->get_col($wpdb->prepare("SELECT option_name FROM {$wpdb->options} WHERE option_name LIKE %s", '_transient_%' . $wpdb->esc_like($like) . '%'));
            foreach ($names as $n) delete_transient(substr($n, strlen('_transient_')));
            $res['flushed_' . $like] = count($names);
        }
        if (function_exists('wp_cache_flush')) wp_cache_flush();
    }
    return $res;
}

function spw_job_render($job) {
    $id = (int) $job['page_id'];
    if (!spw_allowed($id)) return array('error' => 'not allowed');
    foreach ((array) (isset($job['get']) ? $job['get'] : array()) as $k => $v) { $_GET[$k] = $v; $_REQUEST[$k] = $v; }
    global $post;
    $post = get_post($id);
    setup_postdata($post);
    $html = apply_filters('the_content', $post->post_content);
    wp_reset_postdata();
    return array('html' => $html);
}


/* ---------- Highlight colours: keep each corrected reading's existing colours ---------- */

function spw_letters() {
    static $map = null;
    if ($map !== null) return $map;
    $map = array();
    if (!function_exists('saints_rainbow_additional_profile_plan')) return $map;
    foreach (str_split('roygbiv') as $l) {
        $one = saints_rainbow_additional_profile_plan(array('h' => str_repeat('0', 64), 'c' => $l));
        if (is_array($one) && !empty($one['ranges'][0])) $map[wp_json_encode($one['ranges'][0][2])] = $l;
    }
    return $map;
}

/** Words of a reading body and one colour letter per word as the Parallel Reader paints it now ('-' = none). */
function spw_reading_colours($body, $index) {
    if (!function_exists('saints_rainbow_scan')) return array('status' => 'no-rainbow');
    $scan = saints_rainbow_scan($body, 0, '0');
    if (isset($scan['error']) || empty($scan['words'])) return array('status' => 'no-words');
    $words = array(); foreach ($scan['words'] as $w) $words[] = $w[2];
    $key = substr((string)$scan['sha256'], 0, 16);
    $wkey = 'w' . substr(hash('sha256', implode(' ', $words)), 0, 16);
    $out = array('words' => $words, 'key' => $key, 'wkey' => $wkey, 'status' => 'no-plan', 'colours' => str_repeat('-', count($words)));
    $relaxed = false;
    if (isset($index[$key])) $value = $index[$key];
    elseif (isset($index[$wkey])) { $value = $index[$wkey]; $relaxed = true; }
    else return $out;
    $fill = ''; $over = '';
    if (is_string($value) && strpos($value, '!') !== false) list($value, $over) = explode('!', $value, 2);
    if (is_string($value) && strpos($value, '#') !== false) list($value, $fill) = explode('#', $value, 2);
    if ($relaxed && is_string($value) && substr($value, 0, 1) === 'x') $plan = saints_rainbow_additional_profile_plan(array('h' => (string)$scan['sha256'], 'c' => substr($value, 1)));
    else $plan = $relaxed && is_string($value) && substr($value, 0, 1) === 'c' ? saints_prh_composite_plan($value, count($words)) : saints_prh_plan($value);
    if (!is_array($plan) || !isset($plan['ranges'])) { $out['status'] = 'invalid-plan'; return $out; }
    if ($fill !== '') $plan = saints_prh_fill_plan($plan, $fill, count($words));
    if ($over !== '') $plan = saints_prh_override_plan($plan, $over, count($words));
    $letters = spw_letters(); $c = str_split($out['colours']);
    foreach ($plan['ranges'] as $r) {
        $l = isset($letters[wp_json_encode($r[2])]) ? $letters[wp_json_encode($r[2])] : '?';
        for ($i = max(0, (int)$r[0]); $i < min(count($c), (int)$r[1]); $i++) $c[$i] = $l;
    }
    $out['colours'] = implode('', $c); $out['status'] = 'applied';
    return $out;
}

function spw_reader_readings($book, $ch, $cols) {
    $rows = saints_parallel_data($book, (int)$ch);
    $out = array();
    foreach ((array)$rows as $ref => $eds) foreach ($cols as $col) {
        if (empty($eds[$col])) continue;
        foreach ($eds[$col] as $k => $e) if (!empty($e['text'])) $out[] = array('ref' => $ref, 'col' => $col, 'k' => (string)$k, 'body' => saints_parallel_reading_html($e['text'], $book, $ref), 'text' => $e['text']);
    }
    return $out;
}

function spw_job_colsnap($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $cols = (array)$job['cols'];
    $index = saints_prh_index($book); $snap = get_option('spw_colsnap_' . $book, array()); $stats = array();
    foreach ((array)$job['chapters'] as $ch) {
        $snap[$ch] = array(); $n = 0; $a = 0;
        foreach (spw_reader_readings($book, $ch, $cols) as $r) {
            $c = spw_reading_colours($r['body'], $index); $n++; if ($c['status'] === 'applied') $a++;
            $snap[$ch][$r['ref'] . '|' . $r['col'] . '|' . $r['k']] = array(isset($c['words']) ? $c['words'] : array(), isset($c['colours']) ? $c['colours'] : '', $c['status']);
        }
        $stats[$ch] = "$a/$n";
    }
    update_option('spw_colsnap_' . $book, $snap, false);
    $test = array();
    foreach (array('-', '.', '0', '_') as $none) { $p = saints_rainbow_additional_profile_plan(array('h' => str_repeat('0', 64), 'c' => 'r' . $none . 'r')); $test[$none] = $p; }
    return array('stats' => $stats, 'letters' => spw_letters(), 'none_test' => $test);
}

/** Longest common subsequence alignment of two word lists (case-insensitive). Returns new index => old index. */
function spw_align($old, $new) {
    $n = count($old); $m = count($new); $L = array_fill(0, $n + 1, array_fill(0, $m + 1, 0));
    for ($i = $n - 1; $i >= 0; $i--) for ($j = $m - 1; $j >= 0; $j--)
        $L[$i][$j] = strtolower($old[$i]) === strtolower($new[$j]) ? $L[$i + 1][$j + 1] + 1 : max($L[$i + 1][$j], $L[$i][$j + 1]);
    $map = array(); $i = 0; $j = 0;
    while ($i < $n && $j < $m) {
        if (strtolower($old[$i]) === strtolower($new[$j])) { $map[$j] = $i; $i++; $j++; }
        elseif ($L[$i + 1][$j] >= $L[$i][$j + 1]) $i++; else $j++;
    }
    return $map;
}

function spw_extra($book) {
    $all = get_option('spw_colour_extra', array());
    return isset($all[$book]) && is_array($all[$book]) ? $all[$book] : array();
}

function spw_job_colcarry($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $cols = (array)$job['cols']; $none = isset($job['none']) ? $job['none'] : '-';
    $extra = spw_extra($book); $index = array_merge(saints_prh_index($book), $extra);
    $snap = get_option('spw_colsnap_' . $book, array()); $added = array(); $stats = array();
    foreach ((array)$job['chapters'] as $ch) {
        $ok = 0; $n = 0; $new = 0; $left = array();
        foreach (spw_reader_readings($book, $ch, $cols) as $r) {
            $n++;
            $c = spw_reading_colours($r['body'], $index);
            if ($c['status'] === 'applied') { $ok++; continue; }
            if (empty($c['words'])) { $left[] = $r['ref'] . ' ' . $r['col'] . ' ' . $c['status']; continue; }
            $sk = $r['ref'] . '|' . $r['col'] . '|' . $r['k'];
            $old = isset($snap[$ch][$sk]) ? $snap[$ch][$sk] : null;
            if (isset($job['moved'][$ch . ' ' . $sk])) { list($mch, $mk) = explode(' ', $job['moved'][$ch . ' ' . $sk], 2); $old = isset($snap[$mch][$mk]) ? $snap[$mch][$mk] : null; }
            if (!$old || $old[2] !== 'applied') { $left[] = $r['ref'] . ' ' . $r['col'] . ' no-snapshot'; continue; }
            $map = spw_align($old[0], $c['words']); $colours = ''; $any = false;
            foreach ($c['words'] as $j => $w) { $l = isset($map[$j]) ? substr($old[1], $map[$j], 1) : $none; if ($l === '-') $l = $none; if ($l !== $none) $any = true; $colours .= $l; }
            if (!$any) { $left[] = $r['ref'] . ' ' . $r['col'] . ' nothing-to-carry'; continue; }
            // Every word needs a colour: a new word takes the colour of the word before it (or after it, at the start).
            $cs = str_split($colours); $last = '';
            foreach ($cs as $i => $l) { if ($l === $none) { if ($last !== '') $cs[$i] = $last; } else $last = $l; }
            $next = '';
            for ($i = count($cs) - 1; $i >= 0; $i--) { if ($cs[$i] === $none) { if ($next !== '') $cs[$i] = $next; } else $next = $cs[$i]; }
            $colours = implode('', $cs);
            $extra[$c['wkey']] = 'x' . $colours; $index[$c['wkey']] = 'x' . $colours; $added[$c['wkey']] = 'x' . $colours; $new++;
        }
        $stats[$ch] = array('readings' => $n, 'already' => $ok, 'carried' => $new, 'left' => $left);
    }
    if ($added && empty($job['dry_run'])) { $all = get_option('spw_colour_extra', array()); $all[$book] = $extra; update_option('spw_colour_extra', $all, false); }
    return array('stats' => $stats, 'added' => count($added), 'entries' => $added);
}

/** Readings whose wording was corrected keep their colours: paint them from the carried-over plans after the Highlights add-on. */
add_filter('do_shortcode_tag', function ($output, $tag, $attributes) {
    if (!is_string($output) || ($tag !== 'saints_parallel' && $tag !== 'saints_genesis_parallel') || is_admin()) return $output;
    if (!function_exists('saints_prh_ready') || !saints_prh_ready()) return $output;
    $book = $tag === 'saints_genesis_parallel' ? 'genesis' : (is_array($attributes) && isset($attributes['book']) ? strtolower((string)$attributes['book']) : '');
    $extra = spw_extra($book);
    if (!$extra) return $output;
    $done = preg_replace_callback('~(<div class="sgp-reading">(?:(?!</?div\b).)*?<div data-saints-scripture-text="true">)((?:(?!</?div\b).)*?)(</div>)~s', function ($m) use ($extra) {
        list($body, $status) = saints_prh_paint_body($m[2], $extra);
        return $m[1] . ($status === 'applied' ? $body : $m[2]) . $m[3];
    }, $output);
    return is_string($done) ? $done : $output;
}, 20, 3);

function spw_job_colcheck($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $cols = (array)$job['cols'];
    $index = array_merge(saints_prh_index($book), spw_extra($book)); $stats = array();
    foreach ((array)$job['chapters'] as $ch) {
        $n = 0; $a = 0; $miss = array();
        foreach (spw_reader_readings($book, $ch, $cols) as $r) { $c = spw_reading_colours($r['body'], $index); $n++; if ($c['status'] === 'applied') $a++; else $miss[] = $r['ref'] . ' ' . $r['col'] . ' ' . $c['status']; }
        $stats[$ch] = array("$a/$n", $miss);
    }
    return $stats;
}

/** Reader readings as the Parallel Reader shows them (text only), for checking corrections. */
/** Read-only look at the Saints plugins' own files (for checking how the reader works). */
function spw_job_files($job) {
    $slug = preg_replace('/[^a-z0-9-]/', '', $job['plugin']);
    if (strpos($slug, 'saints-') !== 0) return array('error' => 'saints plugins only');
    $base = WP_PLUGIN_DIR . '/' . $slug; if (!is_dir($base)) return array('error' => 'no such plugin');
    $out = array('list' => array(), 'files' => array());
    $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($base, FilesystemIterator::SKIP_DOTS));
    foreach ($it as $f) { $out['list'][substr($f->getPathname(), strlen($base) + 1)] = $f->getSize(); }
    foreach ((array)(isset($job['read']) ? $job['read'] : array()) as $rel) {
        $path = realpath($base . '/' . $rel);
        if (!$path || strpos($path, realpath($base) . '/') !== 0 || !is_file($path)) { $out['files'][$rel] = null; continue; }
        $out['files'][$rel] = filesize($path) > 3000000 ? 'too large' : file_get_contents($path);
    }
    return $out;
}

/** The Parallel Reader's own data for chapters, as it builds them (every key of every entry). */
function spw_job_pdata($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $out = array();
    $pages = array();
    foreach ((array)$job['chapters'] as $ch) {
        $out[$ch] = saints_parallel_data($book, (int)$ch);
        if (!empty($job['pages'])) foreach ((array)$out[$ch] as $row) foreach ((array)$row as $col => $eds) foreach ((array)$eds as $e) {
            if (empty($e['url'])) continue;
            $u = preg_replace('~#.*$~', '', $e['url']); $base = preg_replace('~/\d+/$~', '/', $u);
            if (isset($pages[$base])) continue;
            $id = url_to_postid($base); $c = $id ? get_post_field('post_content', $id, 'raw') : '';
            $pages[$base] = array($id, $id ? md5($c) : '', strlen($c));
        }
        if (!empty($job['pages_only'])) unset($out[$ch]);
    }
    if (!empty($job['pages'])) $out['_pages'] = $pages;
    return $out;
}

/** Cross-reference evidence and reviews for chapters (key "<book>-<chapter>"). raw=1 returns the chapter data as stored. */
function spw_job_xref($job) {
    $out = array();
    if (!function_exists('saints_xref_evidence_load_json')) return array('error' => 'evidence plugin missing');
    foreach ((array)$job['keys'] as $key) {
        $key = sanitize_key($key);
        $data = saints_xref_evidence_load_json('chapters', $key);
        if (!is_array($data)) { $out[$key] = null; continue; }
        $rev = class_exists('Saints_Xref_Reviews') ? Saints_Xref_Reviews::reviews_for_chapter($key) : array();
        if (!empty($job['raw'])) { $out[$key] = array('data' => $data, 'reviews' => $rev); continue; }
        $groups = array();
        foreach ((array)$data['groups'] as $g) {
            $edges = array();
            foreach ((array)$g['edges'] as $e) {
                $t = array();
                foreach ((array)(isset($e['targets']) ? $e['targets'] : array()) as $ptr) { $r = saints_xref_evidence_record($ptr); if (is_array($r)) $t[] = array(isset($r['reference']) ? $r['reference'] : '', isset($r['text']) ? $r['text'] : '', isset($r['url']) ? $r['url'] : ''); }
                $id = isset($e['id']) ? $e['id'] : '';
                $ev = isset($e['evidence']) && is_array($e['evidence']) ? $e['evidence'] : array();
                $rv = isset($rev[$id]) && is_array($rev[$id]) ? $rev[$id] : null;
                if (!empty($job['compact'])) {
                    $edges[] = array($id, isset($e['label']) ? $e['label'] : (isset($e['originalReference']) ? $e['originalReference'] : ''), $t,
                        $rv ? array(isset($rv['verdict']) ? $rv['verdict'] : '', isset($rv['category']) ? $rv['category'] : '', isset($rv['summary']) ? $rv['summary'] : '', isset($rv['why']) ? $rv['why'] : '') : null,
                        $rv ? null : array(isset($ev['category']) ? $ev['category'] : '', isset($ev['explanation']) ? $ev['explanation'] : ''));
                    continue;
                }
                $edges[] = array('id' => $id, 'label' => isset($e['label']) ? $e['label'] : (isset($e['originalReference']) ? $e['originalReference'] : ''), 'evidence' => $ev, 'targets' => $t, 'review' => $rv, 'extra' => array_diff_key($e, array('id' => 1, 'label' => 1, 'targets' => 1, 'evidence' => 1)));
            }
            $groups[] = array('reference' => isset($g['reference']) ? $g['reference'] : '', 'edges' => $edges);
        }
        $out[$key] = $groups;
    }
    return $out;
}

/* ---------- Study Workspace data (Saints Parallel Reader) ---------- */

/** Store a bundle of Study Workspace chapter records from GitHub: {"files": {"genesis-1.json": "...", "genesis-1.sources.json": "..."}}. */
function spw_job_wsdata($job) {
    $bundle = spw_fetch($job['url'], $job['sha256']);
    if (is_wp_error($bundle)) return array('error' => $bundle->get_error_message());
    $type = 'saints_ws_chapter'; $done = 0; $same = 0; $bad = array(); $bytes = 0;
    foreach ((array) (isset($bundle['files']) ? $bundle['files'] : array()) as $file => $content) {
        if (!preg_match('/^([a-z0-9-]+-\d+)(\.sources)?\.json$/', $file, $m) || !is_string($content) || !is_array(json_decode($content, true))) { $bad[] = $file; continue; }
        $name = $m[1] . (empty($m[2]) ? '' : '-sources');
        $old = get_posts(array('post_type' => $type, 'name' => $name, 'post_status' => 'any', 'posts_per_page' => 1, 'no_found_rows' => true));
        if ($old && $old[0]->post_content === $content) { $same++; continue; }
        $post = array('post_type' => $type, 'post_name' => $name, 'post_title' => $name, 'post_status' => 'publish', 'post_content' => wp_slash($content));
        if ($old) $post['ID'] = $old[0]->ID;
        $id = $old ? wp_update_post($post, true) : wp_insert_post($post, true);
        if (is_wp_error($id)) { $bad[] = $file . ': ' . $id->get_error_message(); continue; }
        if (get_post_field('post_content', $id, 'raw') !== $content) { $bad[] = $file . ': stored text differs'; continue; }
        $done++; $bytes += strlen($content);
    }
    return array('stored' => $done, 'unchanged' => $same, 'bytes' => $bytes, 'bad' => $bad);
}

/** List the stored Study Workspace records: name => [length, md5]. */
function spw_job_wslist($job) {
    global $wpdb; $out = array();
    $rows = $wpdb->get_results($wpdb->prepare("SELECT post_name, LENGTH(post_content) AS n, MD5(post_content) AS h FROM {$wpdb->posts} WHERE post_type = %s AND post_status = 'publish'", 'saints_ws_chapter'));
    foreach ($rows as $r) $out[$r->post_name] = array((int) $r->n, $r->h);
    return array('count' => count($out), 'records' => $out);
}

/** Build the Study Workspace cross-references for chapters, as the REST route serves them: counts by strength. */
function spw_job_wsrefs($job) {
    if (!function_exists('saints_parallel_reader_workspace_references')) return array('error' => 'reader module missing');
    $out = array();
    foreach ((array) $job['keys'] as $key) {
        $t = microtime(true);
        $r = saints_parallel_reader_workspace_references($key);
        if (!is_array($r)) { $out[$key] = null; continue; }
        $n = array(); $rows = 0;
        foreach ((array) $r['verses'] as $v => $list) foreach ($list as $row) { $rows++; $n[$row['strength']] = (isset($n[$row['strength']]) ? $n[$row['strength']] : 0) + 1; }
        $out[$key] = array('verses' => count((array) $r['verses']), 'rows' => $rows, 'strength' => $n, 'seconds' => round(microtime(true) - $t, 2));
        if (!empty($job['sample'])) $out[$key]['sample'] = array_slice((array) $r['verses'], 0, 1, true);
    }
    return $out;
}

/** Check the Study Workspace as a reader would get it: the data routes, and what a Parallel Reader page enqueues. */
function spw_job_wscheck($job) {
    $out = array();
    foreach ((array) (isset($job['routes']) ? $job['routes'] : array()) as $route) {
        $res = rest_do_request(new WP_REST_Request('GET', $route));
        $data = $res->get_data();
        $raw = is_array($data) && isset($data['saints_workspace_raw']) ? $data['saints_workspace_raw'] : wp_json_encode($data);
        $j = json_decode($raw, true);
        $out['routes'][$route] = array('status' => $res->get_status(), 'bytes' => strlen($raw), 'json' => is_array($j), 'keys' => is_array($j) ? array_slice(array_keys($j), 0, 12) : null, 'head' => substr($raw, 0, 160));
    }
    foreach ((array) (isset($job['pages']) ? $job['pages'] : array()) as $pg) {
        $_SERVER['REQUEST_URI'] = $pg['path'] . '?gp_ch=' . (int) $pg['ch']; $_GET['gp_ch'] = (string) (int) $pg['ch'];
        wp_dequeue_script('saints-verse-workspace'); wp_deregister_script('saints-verse-workspace');
        do_action('wp_enqueue_scripts');
        $s = wp_scripts()->query('saints-verse-workspace');
        $out['pages'][$pg['path'] . ' ' . $pg['ch']] = array('enqueued' => wp_script_is('saints-verse-workspace', 'enqueued'), 'src' => $s ? $s->src : null, 'data' => $s ? substr((string) $s->extra['data'], 0, 600) : null);
    }
    return $out;
}

/** The pages under book pages, without their text: parent => [[id, slug, length], ...]. */
function spw_job_children($job) {
    global $wpdb; $out = array();
    foreach ((array) $job['parents'] as $parent) {
        $parent = (int) $parent;
        if (!in_array($parent, SPW_BOOKS, true)) { $out[$parent] = 'not allowed'; continue; }
        $rows = $wpdb->get_results($wpdb->prepare("SELECT ID, post_name, LENGTH(post_content) AS n FROM {$wpdb->posts} WHERE post_type = 'page' AND post_parent = %d AND post_status IN ('publish','private','draft')", $parent));
        $out[$parent] = array();
        foreach ($rows as $r) $out[$parent][] = array((int) $r->ID, $r->post_name, (int) $r->n);
    }
    return $out;
}

/** Several jobs of one kind in one run: {"job":"multi","of":"pdata","items":[{...},{...}]} */
function spw_job_multi($job) {
    $fn = 'spw_job_' . preg_replace('/[^a-z]/', '', $job['of']); $out = array();
    if (!function_exists($fn) || $job['of'] === 'multi') return array('error' => 'bad job');
    foreach ((array)$job['items'] as $i => $item) { $item['job'] = $job['of']; $out[$i] = call_user_func($fn, $item); }
    return $out;
}

function spw_job_readings($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $out = array();
    foreach ((array)$job['chapters'] as $ch) foreach (spw_reader_readings($book, $ch, (array)$job['cols']) as $r) $out[$ch][] = array($r['ref'], $r['col'], $r['text']);
    return $out;
}

/** Reader entries for record keeping: row ref, the label the reader shows, card anchor and text. */
function spw_job_capture($job) {
    $book = preg_replace('/[^a-z0-9-]/', '', $job['book']); $col = preg_replace('/[^a-z]/', '', $job['col']); $out = array();
    foreach ((array)$job['chapters'] as $ch) {
        $rows = saints_parallel_data($book, (int)$ch); $out[$ch] = array();
        foreach ((array)$rows as $ref => $eds) if (!empty($eds[$col])) foreach ($eds[$col] as $k => $e)
            $out[$ch][] = array((string)$ref, isset($e['ref']) ? (string)$e['ref'] : '', isset($e['anchor']) ? (string)$e['anchor'] : (string)$k, isset($e['text']) ? (string)$e['text'] : '');
    }
    return $out;
}

add_action('save_post_page', function ($post_id, $post) {
    static $running = false;
    if ($running || wp_is_post_revision($post_id) || $post->post_name !== SPW_CONTROL || !current_user_can('manage_options')) return;
    $raw = html_entity_decode(wp_strip_all_tags($post->post_content), ENT_QUOTES);
    $a = strpos($raw, '{'); $b = strrpos($raw, '}');
    $job = ($a !== false && $b !== false) ? json_decode(substr($raw, $a, $b - $a + 1), true) : null;
    if (!is_array($job) || empty($job['job']) || empty($job['key'])) return;
    $running = true;
    @set_time_limit(300);
    $fn = 'spw_job_' . preg_replace('/[^a-z]/', '', $job['job']);
    $t = microtime(true);
    $result = function_exists($fn) ? call_user_func($fn, $job) : array('error' => 'unknown job');
    spw_out($job['key'], array('job' => $job['job'], 'key' => $job['key'], 'seconds' => round(microtime(true) - $t, 2), 'time' => gmdate('c'), 'result' => $result));
    $running = false;
}, 10, 2);

register_activation_hook(__FILE__, function () {
    if (!get_page_by_path(SPW_CONTROL, OBJECT, 'page')) {
        wp_insert_post(array('post_title' => SPW_CONTROL, 'post_name' => SPW_CONTROL, 'post_type' => 'page', 'post_status' => 'private', 'post_content' => '{}'));
    }
    spw_out('probe', array('job' => 'probe', 'result' => spw_job_probe(array('read' => array()))));
});
