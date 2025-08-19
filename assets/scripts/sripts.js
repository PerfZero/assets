const productsSwiper = new Swiper('.products__slider', {
    slidesPerView: 4,
    slidesPerGroup: 4,
    spaceBetween: 0,

    pagination: {
        el: ".swiper-pagination",
        type: "progressbar",
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            slidesPerGroup: 1,
            spaceBetween: 0
        },
        768: {
            slidesPerView: 2,
            slidesPerGroup: 2,
            spaceBetween: 0
        },
        1024: {
            slidesPerView: 3,
            slidesPerGroup: 3,
            spaceBetween: 0
        },
        1200: {
            slidesPerView: 4,
            slidesPerGroup: 4,
            spaceBetween: 0
        }
    }
});
