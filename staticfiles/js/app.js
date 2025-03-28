document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu');
    const navMenu = document.querySelector('.nav-menu');
  
    mobileMenuButton.addEventListener('click', function() {
      navMenu.classList.toggle('active');
    });
  });

  $(document).ready(function(){
    $('.favourites-carousel').slick({
      infinite: true,
      slidesToShow: 3,      // Show 3 slides on large screens
      slidesToScroll: 1,
      responsive: [
        {
          breakpoint: 992, // For tablets
          settings: {
            slidesToShow: 2
          }
        },
        {
          breakpoint: 768, // For mobile devices
          settings: {
            slidesToShow: 1
          }
        }
      ]
    });
  });

  