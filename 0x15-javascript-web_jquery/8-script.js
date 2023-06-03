const list = document.querySelector('#list_movies');
fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(response => response.json()).then(data => {
    const result = data.results;

    result.forEach(res => {
      const item = document.createElement('li');
      item.textContent = res.title;
      list.append(item);
    });
  }).catch(error => console.log('error: ', error));
