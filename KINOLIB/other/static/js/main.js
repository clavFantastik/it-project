function ToggleTheme(){
   themeToggle.classList.toggle('dark')

}

const swiper = new Swiper('.swiper', {
   // Optional parameters
   direction: 'horizontal',
   loop: true,

   // If we need pagination
   pagination: {
       el: '.swiper-pagination',
   },

   // Navigation arrows
   navigation: {
       nextEl: '.swiper-button-next',
       prevEl: '.swiper-button-prev',
   },

   autoplay: {
       delay: 3000
   },
   slidesPerView: 3,

   // And if we need scrollbar
   scrollbar: {
       el: '.swiper-scrollbar',
   },
});