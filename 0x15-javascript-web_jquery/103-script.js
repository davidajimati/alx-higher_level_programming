$(document).ready(function () {
  $("input#btn_translate").click(function () {
    var languageCode = $("input#language_code").val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.getJSON(apiUrl, { lang: languageCode }, function (response) {
      $("div#hello").text(response.hello);
    }).fail(function (error) {
      console.log(error);
    });
  });
});
