const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (info) {
  $('div#character').text(info.name);
});
