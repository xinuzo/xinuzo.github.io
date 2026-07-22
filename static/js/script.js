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

    // --- Mobile Navigation Toggle ---
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function() {
            const isOpen = navLinks.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', isOpen);
        });
    }

});
