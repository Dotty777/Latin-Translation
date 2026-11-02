<?php
/**
 * Plugin Name: Saints Parallel Reader
 * Description: One home for the Parallel Reader's additions, kept as separate modules. Layout tidies the top of the page, Verse Workspace turns the page into the Study Bible with Contents and a Study Workspace, and Latin Text removes whole Latin verses from displayed pages while keeping short phrases and source links. Each older plugin's module stays silent while that plugin is still active, so the two never run together.
 * Version: 1.5.0
 * Requires PHP: 7.4
 * Author: Saints.Bible
 * License: GPL-2.0-or-later
 */
defined('ABSPATH') || exit;

const SAINTS_PARALLEL_READER_VERSION = '1.5.0';

require_once __DIR__.'/modules/layout.php';
require_once __DIR__.'/modules/latin-text.php';
require_once __DIR__.'/modules/verse-workspace/module.php';
