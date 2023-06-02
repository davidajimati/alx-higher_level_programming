$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (response) {
      $('div#character').text(response.name);
    },
    error: function (error) {
      console.log(error);
    }
  });
});
