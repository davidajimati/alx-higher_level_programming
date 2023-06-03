const mydiv = document.querySelector("#hello");

fetch("https://fourtonfish.com/hellosalut/?lang=fr")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => console.log("error", error));
