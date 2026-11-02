<?php
defined('ABSPATH') || exit;

const SAINTS_PARALLEL_READER_LAYOUT_LIVE = true; // False shows the changes to administrators only.

function saints_parallel_reader_layout_css() {
    $page = 'body.saints-parallel-page';
    $panel = $page.' .sgp-toolbar .spl-appearance-slot>.sr-appearance';
    return
        // The Browse box is narrower than the page and was left at the page's left edge.
        $page.' #saints-book-browser{margin-inline:auto!important}'
        // The row Appearance leaves behind, gone before the first paint so the page doesn't jump.
        // :root outranks the highlight layout's rule for this row under 1440px.
        .':root '.$page.':has(.sgp-toolbar) #saints-reader-panels{display:none!important}'
        // Chapter, Read and Appearance together; the chapter links stay on the right.
        .$page.' .sgp-toolbar{justify-content:flex-start;column-gap:10px}'
        .$page.' .sgp-toolbar nav{margin-left:auto}'
        // The slot holds the closed size, so opening the panel covers the table instead of pushing it down.
        .$page.' .spl-appearance-slot{position:relative;flex:none;align-self:stretch;width:8.5rem;min-height:44px}'
        .$panel.'{position:absolute!important;top:0;left:0;z-index:40;box-sizing:border-box;width:100%!important;height:100%;min-width:0;max-width:none;max-height:70dvh;padding:0;border-radius:6px;font:inherit;overflow:hidden}'
        .$panel.'[open]{width:min(260px,calc(100vw - 32px))!important;height:auto;padding:0 14px 10px;overflow:auto}'
        .$panel.'>summary{display:flex;align-items:center;gap:8px;box-sizing:border-box;height:100%;min-height:42px;padding:0 12px;font-weight:inherit;white-space:nowrap}'
        .$panel.'[open]>summary{height:auto;min-height:46px;margin:0 -14px 8px;padding-bottom:0}';
}

/** Beside the form, not inside it: its radio buttons would otherwise go into the address on Read. */
function saints_parallel_reader_layout_js() {
    return "(function(){'use strict';\n"
        ."function place(){\n"
        ." if(!document.body.classList.contains('saints-parallel-page'))return;\n"
        ." var form=document.querySelector('.sgp-toolbar form'),panel=document.querySelector('#saints-reader-panels>.sr-appearance');\n"
        ." if(!form||!panel)return;\n"
        ." var slot=document.createElement('div');slot.className='spl-appearance-slot';\n"
        ." slot.append(panel);form.after(slot);\n"
        // This far down the page the panel can open past the bottom of the window.
        ." panel.addEventListener('toggle',function(){if(panel.open)panel.scrollIntoView({block:'nearest',behavior:'instant'});});\n"
        ."}\n"
        ."place();document.addEventListener('DOMContentLoaded',place);window.addEventListener('load',place);\n"
        ."}());";
}

add_action('wp_head', function () {
    if (function_exists('saints_parallel_layout_css')) {
        return; // The older Saints Parallel Layout plugin is active.
    }
    if (!SAINTS_PARALLEL_READER_LAYOUT_LIVE && !current_user_can('manage_options')) {
        return;
    }
    echo '<style id="saints-parallel-layout">'.saints_parallel_reader_layout_css().'</style>'."\n"; // phpcs:ignore
}, 99);

add_action('wp_footer', function () {
    if (function_exists('saints_parallel_layout_css')) {
        return; // The older Saints Parallel Layout plugin is active.
    }
    if (!SAINTS_PARALLEL_READER_LAYOUT_LIVE && !current_user_can('manage_options')) {
        return;
    }
    echo '<script id="saints-parallel-layout-js">'.saints_parallel_reader_layout_js().'</script>'."\n"; // phpcs:ignore
}, 99);
