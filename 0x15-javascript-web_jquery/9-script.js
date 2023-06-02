$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function (response) {
      $('div#hello').text(response.hello);
    },
    error: function (error) {
      console.log(error);
    }
  });
});
