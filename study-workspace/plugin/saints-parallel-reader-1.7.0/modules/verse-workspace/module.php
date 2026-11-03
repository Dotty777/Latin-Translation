<?php
defined('ABSPATH') || exit;

const SAINTS_PARALLEL_READER_WORKSPACE_LIVE = false; // False shows the panel to administrators only, while the notes are reviewed.

/** Everyone can see the panel on a staging address. Elsewhere it follows the setting above. */
function saints_parallel_reader_workspace_visible() {
    $staging = '.wpcomstaging.com';
    $host = (string) wp_parse_url(home_url(), PHP_URL_HOST);
    return SAINTS_PARALLEL_READER_WORKSPACE_LIVE
        || substr($host, -strlen($staging)) === $staging
        || current_user_can('manage_options');
}

/**
 * Books with a Study Workspace, by the book's Parallel Reader address, with their chapter counts.
 * Law, Judgement, Salvation, Wisdom and Glory divisions.
 */
function saints_parallel_reader_workspace_books() {
    $books = [
        'law' => ['genesis' => 50, 'exodus' => 40, 'leviticus' => 27, 'numbers' => 36, 'deuteronomy' => 34],
        'judgement' => ['joshua' => 24, 'judges' => 21, 'ruth' => 4, '1-samuel' => 31, '2-samuel' => 24, '1-kings' => 22, '2-kings' => 25, '1-chronicles' => 29, '2-chronicles' => 36, '1-maccabees' => 16, '2-maccabees' => 15, 'ezra' => 10, 'nehemiah' => 13, 'esther' => 10, 'job' => 42],
        'providence' => ['isaiah' => 66, 'jeremiah' => 52, 'ezekiel' => 48, 'daniel' => 12, 'hosea' => 14, 'joel' => 4, 'amos' => 9, 'obadiah' => 1, 'jonah' => 4, 'micah' => 7, 'nahum' => 3, 'habakkuk' => 3, 'zephaniah' => 3, 'haggai' => 2, 'zechariah' => 14, 'malachi' => 3],
        'salvation' => ['matthew' => 28, 'mark' => 16, 'luke' => 24, 'john' => 21],
        'wisdom' => ['psalms' => 151, 'proverbs' => 31, 'ecclesiastes' => 12, 'song-of-songs' => 8, 'lamentations' => 5, 'wisdom-of-solomon' => 19, 'sirach' => 51],
        'glory' => ['revelation' => 22],
    ];
    $out = [];
    foreach ($books as $division => $list) {
        foreach ($list as $book => $count) {
            $out['/bible/'.$division.'/'.$book.'/parallel/'] = ['book' => $book, 'chapters' => $count];
        }
    }
    return $out;
}

/** Kept for older callers: chapters with a data file, by the book's Parallel Reader address. */
function saints_parallel_reader_workspace_chapters() {
    $out = [];
    foreach (saints_parallel_reader_workspace_books() as $path => $entry) {
        $out[$path] = ['book' => $entry['book'], 'chapters' => range(1, $entry['chapters'])];
    }
    return $out;
}

const SAINTS_PARALLEL_READER_WORKSPACE_TYPE = 'saints_ws_chapter';

/** Generated chapter data is kept as private records: "<book>-<chapter>" and "<book>-<chapter>-sources". */
add_action('init', function () {
    register_post_type(SAINTS_PARALLEL_READER_WORKSPACE_TYPE, [
        'label' => 'Study Workspace data',
        'public' => false,
        'show_ui' => false,
        'show_in_rest' => false,
        'rewrite' => false,
        'query_var' => false,
        'can_export' => true,
        'supports' => ['title'],
    ]);
});

/** The stored JSON for a record name, or null when there is none. */
function saints_parallel_reader_workspace_record($name) {
    $name = sanitize_title($name);
    $found = get_posts([
        'post_type' => SAINTS_PARALLEL_READER_WORKSPACE_TYPE,
        'name' => $name,
        'post_status' => 'publish',
        'posts_per_page' => 1,
        'no_found_rows' => true,
        'update_post_term_cache' => false,
        'update_post_meta_cache' => false,
    ]);
    return $found ? ['id' => $found[0]->ID, 'json' => (string) $found[0]->post_content, 'modified' => $found[0]->post_modified_gmt] : null;
}

/** Only the id and last change of a record, without loading its JSON; null when there is none. */
function saints_parallel_reader_workspace_record_stamp($name) {
    global $wpdb;
    $row = $wpdb->get_row($wpdb->prepare(
        "SELECT ID, post_modified_gmt FROM {$wpdb->posts} WHERE post_type = %s AND post_name = %s AND post_status = 'publish' LIMIT 1",
        SAINTS_PARALLEL_READER_WORKSPACE_TYPE,
        sanitize_title($name)
    ));
    return $row ? ['id' => (int) $row->ID, 'modified' => $row->post_modified_gmt] : null;
}

/** The book and chapter for this request, or null when this page has no Study Workspace. */
function saints_parallel_reader_workspace_current() {
    $path = wp_parse_url(isset($_SERVER['REQUEST_URI']) ? wp_unslash($_SERVER['REQUEST_URI']) : '', PHP_URL_PATH); // phpcs:ignore
    $books = saints_parallel_reader_workspace_books();
    if (!$path || !isset($books[trailingslashit($path)])) {
        return null;
    }
    $entry = $books[trailingslashit($path)];
    $chapter = isset($_GET['gp_ch']) ? absint($_GET['gp_ch']) : 1; // phpcs:ignore WordPress.Security.NonceVerification
    return $chapter >= 1 && $chapter <= $entry['chapters'] ? ['book' => $entry['book'], 'chapter' => $chapter] : null;
}

add_action('wp_enqueue_scripts', function () {
    if (function_exists('saints_verse_workspace_current')) {
        return; // The older Saints Verse Workspace plugin is active.
    }
    if (!saints_parallel_reader_workspace_visible()) {
        return;
    }
    $current = saints_parallel_reader_workspace_current();
    if (!$current) {
        return;
    }
    $key = $current['book'].'-'.$current['chapter'];
    $record = saints_parallel_reader_workspace_record_stamp($key);
    if (!$record) {
        return;
    }
    $sources = saints_parallel_reader_workspace_record_stamp($key.'-sources');
    $assets = __DIR__.'/assets/';
    wp_enqueue_style('saints-verse-workspace', plugins_url('assets/verse-workspace.css', __FILE__), [], SAINTS_PARALLEL_READER_VERSION.'-'.filemtime($assets.'verse-workspace.css'));
    wp_enqueue_script('saints-verse-workspace', plugins_url('assets/verse-workspace.js', __FILE__), [], SAINTS_PARALLEL_READER_VERSION.'-'.filemtime($assets.'verse-workspace.js'), true);
    wp_localize_script('saints-verse-workspace', 'SaintsVerseWorkspace', [
        'dataUrl' => add_query_arg('v', rawurlencode($record['modified']), rest_url('saints-workspace/v1/data/'.$key)),
        'sourcesUrl' => $sources ? add_query_arg('v', rawurlencode($sources['modified']), rest_url('saints-workspace/v1/data/'.$key.'-sources')) : '',
        'referencesUrl' => rest_url('saints-workspace/v1/references/'.$key),
    ]);
});

/* ---------- Data routes: stored chapter data, and cross-references built from the evidence and its reviews ---------- */

add_action('rest_api_init', function () {
    register_rest_route('saints-workspace/v1', '/data/(?P<name>[a-z0-9-]+-\d+(?:-sources)?)', [
        'methods' => 'GET',
        'permission_callback' => '__return_true',
        'callback' => function ($request) {
            $record = saints_parallel_reader_workspace_record($request['name']);
            if (!$record) {
                return new WP_Error('saints_workspace_no_data', 'No Study Workspace data for this chapter.', ['status' => 404]);
            }
            $response = new WP_REST_Response(['saints_workspace_raw' => $record['json']]);
            $response->header('Cache-Control', 'public, max-age=86400');
            return $response;
        },
    ]);
    register_rest_route('saints-workspace/v1', '/references/(?P<key>[a-z0-9-]+-\d+)', [
        'methods' => 'GET',
        'permission_callback' => '__return_true',
        'args' => ['key' => ['sanitize_callback' => 'sanitize_key']],
        'callback' => function ($request) {
            $data = saints_parallel_reader_workspace_references($request['key']);
            if ($data === null) {
                return new WP_Error('saints_workspace_no_references', 'Cross-references are not available.', ['status' => 404]);
            }
            $response = rest_ensure_response($data);
            $response->header('Cache-Control', 'public, max-age=3600');
            return $response;
        },
    ]);
});

/** Send stored chapter JSON as it is, without decoding and encoding it again. */
add_filter('rest_pre_serve_request', function ($served, $result, $request) {
    if ($served || strpos($request->get_route(), '/saints-workspace/v1/data/') !== 0 || !($result instanceof WP_HTTP_Response)) {
        return $served;
    }
    $data = $result->get_data();
    if (!is_array($data) || !isset($data['saints_workspace_raw'])) {
        return $served;
    }
    header('Content-Type: application/json; charset='.get_option('blog_charset'));
    echo $data['saints_workspace_raw']; // phpcs:ignore WordPress.Security.EscapeOutput -- stored JSON, served as data.
    return true;
}, 10, 3);

/** One page-relative address for a site link, so the panel works on every copy of the site. */
function saints_parallel_reader_workspace_link($url) {
    $url = (string) $url;
    return $url === '' ? '' : wp_make_link_relative($url);
}

/**
 * The cross-references of one chapter ("genesis-1"), grouped by verse, in the shape the Study Workspace reads.
 * Reviewed links carry their verdict; links not yet reviewed are kept with their evidence note.
 */
function saints_parallel_reader_workspace_references($key) {
    $key = sanitize_key($key);
    if (!preg_match('/^([a-z0-9-]+)-(\d+)$/', $key, $m) || !function_exists('saints_xref_evidence_load_json')) {
        return null;
    }
    $data = saints_xref_evidence_load_json('chapters', $key);
    $reviews = class_exists('Saints_Xref_Reviews') ? Saints_Xref_Reviews::reviews_for_chapter($key) : [];
    $source = class_exists('Saints_Xref_Reviews') && method_exists('Saints_Xref_Reviews', 'chapter_source_hash') ? (string) Saints_Xref_Reviews::chapter_source_hash($key) : '';
    $cache = 'svw_refs_'.md5($key.'|'.SAINTS_PARALLEL_READER_VERSION.'|'.$source.'|'.md5(wp_json_encode($reviews)));
    $cached = get_transient($cache);
    if (is_array($cached)) {
        return $cached;
    }
    $out = [
        'source' => 'Cross-references: OpenBible.info and the Treasury of Scripture Knowledge (CC BY).',
        'review' => 'Relationship notes were reviewed automatically and have not yet been checked by a person. Links not yet reviewed are imported candidates, shown with their evidence note.',
        'verses' => new stdClass(),
    ];
    if (!is_array($data) || empty($data['groups']) || !is_array($data['groups'])) {
        set_transient($cache, $out, DAY_IN_SECONDS);
        return $out;
    }
    $verses = [];
    foreach ($data['groups'] as $group) {
        if (!is_array($group) || empty($group['edges']) || !is_array($group['edges'])) {
            continue;
        }
        $reference = isset($group['reference']) ? (string) $group['reference'] : '';
        $verse = preg_match('/:(\d+[a-z]?)\s*$/', $reference, $vm) ? $vm[1] : '';
        if ($verse === '') {
            continue;
        }
        foreach ($group['edges'] as $edge) {
            if (!is_array($edge)) {
                continue;
            }
            $id = isset($edge['id']) ? (string) $edge['id'] : '';
            $label = isset($edge['label']) ? (string) $edge['label'] : (isset($edge['originalReference']) ? (string) $edge['originalReference'] : '');
            $readings = [];
            $link = '';
            foreach ((isset($edge['targets']) && is_array($edge['targets']) ? $edge['targets'] : []) as $pointer) {
                $record = function_exists('saints_xref_evidence_record') ? saints_xref_evidence_record($pointer) : null;
                if (!is_array($record)) {
                    continue;
                }
                $readings[] = ['ref' => isset($record['reference']) ? (string) $record['reference'] : '', 'text' => isset($record['text']) ? (string) $record['text'] : ''];
                if ($link === '' && !empty($record['url'])) {
                    $link = saints_parallel_reader_workspace_link($record['url']);
                }
            }
            $review = isset($reviews[$id]) && is_array($reviews[$id]) ? $reviews[$id] : null;
            $evidence = isset($edge['evidence']) && is_array($edge['evidence']) ? $edge['evidence'] : [];
            if ($review) {
                $row = [
                    'ref' => $label,
                    'link' => $link,
                    'type' => isset($review['category']) ? (string) $review['category'] : '',
                    'strength' => isset($review['verdict']) ? (string) $review['verdict'] : 'unreviewed',
                    'how' => isset($review['summary']) ? (string) $review['summary'] : '',
                    'why' => isset($review['why']) ? (string) $review['why'] : '',
                    'readings' => $readings,
                ];
            } else {
                $row = [
                    'ref' => $label,
                    'link' => $link,
                    'type' => 'Not yet reviewed',
                    'strength' => 'unreviewed',
                    'how' => isset($evidence['explanation']) ? (string) $evidence['explanation'] : '',
                    'why' => '',
                    'readings' => $readings,
                ];
            }
            $verses[$verse][] = $row;
        }
    }
    $out['verses'] = $verses ? $verses : new stdClass();
    set_transient($cache, $out, DAY_IN_SECONDS);
    return $out;
}
