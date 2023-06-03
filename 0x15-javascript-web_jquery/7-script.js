fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
  .then(response => response.json()).then(data => {
    const content = data.name;
    document.querySelector("#character").textContent = content;
  }).catch(error => {
    console.log("error:", error);
  });
