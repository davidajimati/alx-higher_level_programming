$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      const movies = response.results;
      const list = $('ul#list_movies');
      $.each(movies, function (index, movie) {
        const listItem = $('<li>').text(movie.title);
        list.append(listItem);
      });
    },
    error: function (error) {
      console.log(error);
    }
  });
});
