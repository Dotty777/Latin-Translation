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

/** Chapters with a finished data file, by the book's Parallel Reader address. */
function saints_parallel_reader_workspace_chapters() {
    return ['/bible/law/genesis/parallel/' => ['book' => 'genesis', 'chapters' => [1]]];
}

/** The book and chapter for this request, or null when no data file exists for it. */
function saints_parallel_reader_workspace_current() {
    $path = wp_parse_url(isset($_SERVER['REQUEST_URI']) ? wp_unslash($_SERVER['REQUEST_URI']) : '', PHP_URL_PATH); // phpcs:ignore
    $books = saints_parallel_reader_workspace_chapters();
    if (!$path || !isset($books[trailingslashit($path)])) {
        return null;
    }
    $entry = $books[trailingslashit($path)];
    $chapter = isset($_GET['gp_ch']) ? absint($_GET['gp_ch']) : 1; // phpcs:ignore WordPress.Security.NonceVerification
    return in_array($chapter, $entry['chapters'], true) ? ['book' => $entry['book'], 'chapter' => $chapter] : null;
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
    $file = $current['book'].'-'.$current['chapter'].'.json';
    wp_enqueue_style('saints-verse-workspace', plugins_url('assets/verse-workspace.css', __FILE__), [], SAINTS_PARALLEL_READER_VERSION);
    wp_enqueue_script('saints-verse-workspace', plugins_url('assets/verse-workspace.js', __FILE__), [], SAINTS_PARALLEL_READER_VERSION, true);
    wp_localize_script('saints-verse-workspace', 'SaintsVerseWorkspace', [
        'dataUrl' => plugins_url('data/'.$file, __FILE__).'?ver='.SAINTS_PARALLEL_READER_VERSION,
        'referencesUrl' => plugins_url('data/'.$current['book'].'-'.$current['chapter'].'.references.json', __FILE__).'?ver='.SAINTS_PARALLEL_READER_VERSION,
    ]);
});
