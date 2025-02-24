document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu');
    const navMenu = document.querySelector('.nav-menu');
  
    mobileMenuButton.addEventListener('click', function() {
      navMenu.classList.toggle('active');
    });
  });
  