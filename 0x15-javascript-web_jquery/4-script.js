const toggle = document.querySelector("#toggle_header");
const header = document.querySelector("header");
toggle.onclick = () => {
  header.classList.toggle("green");
  header.classList.toggle("red");
}
