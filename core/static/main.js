// Mobile navigation toggle
const burger = document.getElementById('navBurger');
const mobileNav = document.getElementById('navMobile');

if (burger && mobileNav) {
  burger.addEventListener('click', () => {
    const isOpen = mobileNav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(isOpen));
  });

  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    });
  });
}

// "Смотреть видео" — placeholder action
const watchVideoBtn = document.getElementById('watchVideoBtn');
if (watchVideoBtn) {
  watchVideoBtn.addEventListener('click', (e) => {
    e.preventDefault();
    alert('Видео скоро появится здесь.');
  });
}

// Booking form submit
const bookingForm = document.getElementById('bookingForm');
if (bookingForm) {
  bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = bookingForm.fullName.value.trim();
    alert(`Спасибо${name ? ', ' + name : ''}! Ваш запрос на бронирование получен — мы свяжемся с вами для подтверждения.`);
    bookingForm.reset();
  });
}
