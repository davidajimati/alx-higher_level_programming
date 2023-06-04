document.addEventListener("DOMContentLoaded", function () {

  const button = document.querySelector("#btn_translate");

  button.onclick = () => {
    const lang = document.querySelector("#language_code").value
    if (lang.length > 0) {
      fetch("https://hellosalut.stefanbohacek.dev/?lang=" + lang)
        .then(response => response.json())
        .then(data => {
          const out = data.hello;
          document.querySelector("#hello").textContent = out;
        }).catch(error => console.log("Error: ", error));
    }
  }
})
