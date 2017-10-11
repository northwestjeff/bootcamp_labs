

var options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0
};

function success(pos) {
    var crd = pos.coords;

    $.ajax({
        url: 'http://api.openweathermap.org/data/2.5/weather',
        type: 'GET',
        data: {
            APPID: 'a4c0e8e842ba6b3f06d47fbb4dd5dab3',
            lat: crd.latitude.toFixed(2),
            lon: crd.longitude.toFixed(2),
            units: "imperial"
        },
        success: function (response) {
            console.log(response)
            $('#city').html(response.name)
            $('#temp').html(response.main.temp.toFixed(0) + " F")
            $('#wind').html(response.wind.speed.toFixed(0) + " mph")
            for (i = 0; i < response.weather.length; i++) {
                $('#prec').append('<li>' + response.weather[i].description + '</li>')
            }
            if (response.weather[0].description.includes("rain") === true) {
              $('.main').css('background-image', 'url("rain.jpeg")');

            } else if ($('.datapoint')[2].children[0].innerHTML.includes("snow") === true) {
                $('.main').css('background-image', 'url("snow.jpeg")');
            } else if ($('.datapoint')[2].children[0].innerHTML.includes("cloud") === true) {
                $('.main').css('background-image', 'url("cloudy.jpeg")');
            } else if ($('.datapoint')[2].children[0].innerHTML.includes("clear") === true) {
                $('.main').css('background-image', 'url("sunnyportland.jpeg")');
            } else {
                $('.main').css('background-image', 'url("water.jpeg")');
        }
    }
})
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
};

navigator.geolocation.getCurrentPosition(success, error, options);



$('#search').submit(function () {
  console.log("submit")
  event.preventDefault()

  $.ajax({
      url: 'http://api.openweathermap.org/data/2.5/weather',
      type: 'GET',
      data: {
          APPID: 'a4c0e8e842ba6b3f06d47fbb4dd5dab3',
          // lat: crd.latitude.toFixed(2),
          // lon: crd.longitude.toFixed(2),
          q: $('#city-search').val(),
          units: "imperial"
      },
      success: function(response) {
          console.log(response)
          $('#city').html(response.name)
          $('#temp').html(response.main.temp.toFixed(0) + " F")
          $('#wind').html(response.wind.speed.toFixed(0) + " mph")
          for (i = 0; i < response.weather.length; i++) {
              $('#prec').append('<li>' + response.weather[i].description + '</li>')
            }


          }
      }
)
});


