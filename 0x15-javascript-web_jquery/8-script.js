$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus, jqXHR) {
  for (let p = 0; p < data.count; p++) {
    $('UL#list_movies').append('<li>' + data.results[p].title + '</li>');
  }
});
