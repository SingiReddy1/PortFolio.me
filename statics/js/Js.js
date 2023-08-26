

const sections = document.querySelectorAll(".box");
const navLi = document.querySelectorAll("header li a");
window.onscroll = () => {
  var current = "";

  sections.forEach((box) => {
    const boxTop = box.offsetTop;
    if (scrollY >= boxTop - 60) {
      current = box.getAttribute("id"); }
  });

  navLi.forEach((a) => {
    a.classList.remove("active");
    if (a.classList.contains(current)) {
      a.classList.add("active");
    }
  });
};




