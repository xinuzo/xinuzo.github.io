/* =================================
 * FILE: script.js
 * DESCRIPTION: Minimal JavaScript for dynamic elements.
 * =================================
 */

document.addEventListener('DOMContentLoaded', function() {

    // --- Dynamic Copyright Year ---
    const copyrightYearEl = document.getElementById('copyright-year');
    if (copyrightYearEl) {
        copyrightYearEl.textContent = new Date().getFullYear();
    }

});
