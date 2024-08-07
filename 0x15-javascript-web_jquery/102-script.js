// script that fetches and prints how to
// say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
