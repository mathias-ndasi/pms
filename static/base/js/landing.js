// window.onload = function () {
// start div animations
let animItem = document.querySelectorAll('.animatable');

function checkScroll(e) {
    animItem.forEach(item => {

        let slideInAt = (window.pageYOffset + window.innerHeight) - item.getBoundingClientRect().height / 3;
        // buttom of the image
        let slideBottom = item.offsetTop + item.getBoundingClientRect().height;
        let isHalfShown = slideInAt > item.offsetTop;
        let isNotScrolledPassed = window.pageYOffset < slideBottom;

        if (isHalfShown && isNotScrolledPassed) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }

    });
}

window.addEventListener('scroll', checkScroll);
// }