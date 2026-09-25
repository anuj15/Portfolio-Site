// Theme toggle (persisted in localStorage)
const THEME_KEY = 'portfolio.theme';
const root = document.documentElement;
const themeToggle = document.getElementById('theme-toggle');

function applyTheme(theme) {
  root.setAttribute('data-theme', theme);
  if (themeToggle) {
    themeToggle.textContent = theme === 'light' ? '🌙' : '☀️';
    themeToggle.setAttribute('aria-label', theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
  }
}

const savedTheme = localStorage.getItem(THEME_KEY);
const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
applyTheme(savedTheme || (prefersLight ? 'light' : 'dark'));

themeToggle?.addEventListener('click', () => {
  const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  localStorage.setItem(THEME_KEY, next);
  applyTheme(next);
});

// Mobile nav toggle
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

navToggle?.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

navLinks?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
  });
});

// Contact form: client-side only (no backend). Replace the action URL with a
// real endpoint (e.g. Formspree) to actually receive submissions.
const contactForm = document.getElementById('contact-form');
const formStatus = document.getElementById('form-status');

contactForm?.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = /** @type {HTMLInputElement} */ (document.getElementById('contact-name')).value.trim();
  const email = /** @type {HTMLInputElement} */ (document.getElementById('contact-email')).value.trim();
  const message = /** @type {HTMLTextAreaElement} */ (document.getElementById('contact-message')).value.trim();

  if (!name || !email || !message) {
    formStatus.textContent = 'Please fill in all fields.';
    formStatus.dataset.state = 'error';
    return;
  }

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    formStatus.textContent = 'Please enter a valid email address.';
    formStatus.dataset.state = 'error';
    return;
  }

  // TODO: wire this up to Formspree, Netlify Forms, or your own backend.
  formStatus.textContent = `Thanks, ${name}! This demo form doesn't send messages yet — email me directly instead.`;
  formStatus.dataset.state = 'success';
  contactForm.reset();
});

// Footer year
const yearEl = document.getElementById('current-year');
if (yearEl) {
  yearEl.textContent = String(new Date().getFullYear());
}
