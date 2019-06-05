function waring() {
    let close = document.getElementsByClassName('closebtn')[0];
    close.onclick = function () {
        let parent = document.querySelector('.alert');
        parent.style.opacity = '0';
        setTimeout(() => {
            parent.style.display = "none"
        }, 600);
    }
    console.log("mathais")
}

waring();