(() => {
  const menuButton = document.querySelector('.menu-btn');
  const nav = document.querySelector('.nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(isOpen));
    });
  }

  document.querySelectorAll('.dropbtn').forEach((button) => {
    button.addEventListener('click', (event) => {
      if (window.innerWidth <= 1050) {
        event.preventDefault();
        const parent = button.closest('.dropdown');
        document.querySelectorAll('.dropdown.open').forEach((item) => {
          if (item !== parent) item.classList.remove('open');
        });
        parent.classList.toggle('open');
        button.setAttribute('aria-expanded', String(parent.classList.contains('open')));
      }
    });
  });

  document.addEventListener('click', (event) => {
    if (window.innerWidth > 1050 && !event.target.closest('.dropdown')) {
      document.querySelectorAll('.dropdown.open').forEach((item) => item.classList.remove('open'));
    }
  });

  document.querySelectorAll('img[data-fallback]').forEach((img) => {
    img.addEventListener('error', () => {
      const fallback = img.getAttribute('data-fallback');
      if (fallback && img.src !== fallback) img.src = fallback;
    }, { once: true });
  });

  const banner = document.querySelector('.cookie-banner');
  if (banner && !localStorage.getItem('kkr-cookie-choice')) banner.classList.add('show');
  document.querySelectorAll('[data-cookie-choice]').forEach((button) => {
    button.addEventListener('click', () => {
      localStorage.setItem('kkr-cookie-choice', button.dataset.cookieChoice);
      banner?.classList.remove('show');
    });
  });
})();
