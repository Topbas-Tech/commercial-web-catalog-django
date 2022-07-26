var swiper = new Swiper(".mySwiper", {
    slidesPerView: 'auto',
    spaceBetween: 25,
    centeredSlides: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
      },
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });