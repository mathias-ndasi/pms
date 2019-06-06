window.onload = function () {
  let btn = document.querySelector(".submit button");

  btn.addEventListener("mousedown", e => {
    let target = e.target;
    let container = target.getBoundingClientRect();
    let ripple = document.createElement("span");
    ripple.classList.add("ripple");
    ripple.style.height = ripple.style.width = Math.max(container.height, container.width) + "px";
    target.appendChild(ripple);
    let top = e.pageY - container.top - ripple.offsetHeight / 2 - document.body.scrollTop + "px";
    let left = e.pageX - container.left - ripple.offsetWidth / 2 - document.body.scrollLeft + "px";
    ripple.style.top = top;
    ripple.style.left = left;
    return false;
  });

  // function for alert messages
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
}