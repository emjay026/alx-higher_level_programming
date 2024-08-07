// script that fetches and prints how
// to say “Hello” depending on the language
$(document).ready(function () {
  function fetchHello () {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the ENTER key
      fetchHello();
    }
  });
});
