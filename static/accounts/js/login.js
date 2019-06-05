function waring() {
  let close = document.querySelector('.closebtn');
  close.onclick = function () {
    let parent = document.querySelector(".alert");
    parent.style.opacity = "0";
    setTimeout(() => {
      parent.style.display = "none";
    }, 600);
  };
}

waring();