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

const burger = document.querySelector('.header__burger');
const mobileNav = document.querySelector('.mobile-nav');

burger.addEventListener('click', () => {
    burger.classList.toggle('active');
    mobileNav.classList.toggle('active');
});

mobileNav.addEventListener('click', (e) => {
    console.log('Click detected on:', e.target);
    console.log('Classes:', e.target.classList);
    
    if (e.target.classList.contains('mobile-nav__link--catalog')) {
        console.log('Catalog link clicked!');
        e.preventDefault();
        const catalogMenu = document.querySelector('.catalog-menu');
        console.log('Catalog menu element:', catalogMenu);
        catalogMenu.classList.add('active');
        console.log('Active class added');
    } else if (e.target.classList.contains('mobile-nav__link')) {
        console.log('Other nav link clicked');
        burger.classList.remove('active');
        mobileNav.classList.remove('active');
    }
});

const catalogMenu = document.querySelector('.catalog-menu');
const catalogClose = document.querySelector('.catalog-menu__close');
const desktopCatalogLink = document.querySelector('.header__nav-link');

desktopCatalogLink.addEventListener('click', (e) => {
    e.preventDefault();
    catalogMenu.classList.add('active');
});

catalogClose.addEventListener('click', () => {
    catalogMenu.classList.remove('active');
});
