let API_KEY_GOOGLE = 'AIzaSyAYSeZRkkIEUkvEc1Ut7UYs7q0lLRZds94';
let API_KEY_WEATHER = '9beedacb0acd83bf9212f36febc74f25';

let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 16
  });
}

function findWeather() {
  let inputAddress = document.getElementById('input-address');
  let address = inputAddress.value;

  fetch('https://maps.googleapis.com/maps/api/geocode/json?address=' + encodeURI(address) + '&key=' + API_KEY_GOOGLE)
  .then(response => response.json())
  .then(displayCoordinate)
  .catch('Eroor'+ 'apiError')
}

function displayCoordinate(result) {
  if (result == null) {
    return;
  }
  let location = result.results[0].geometry.location;
  let inputLatitude = document.getElementById('latitude');
  let inputLongitude = document.getElementById('longitude');
  inputLatitude.textContent = location.lat;
  inputLongitude.textContent = location.lng;
  let lat = location.lat;
  let lon = location.lng;

  fetch('http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_KEY_WEATHER)
  .then(response => response.json())
  .then(function(json) {
    let city = document.getElementById('city');
    let weather = document.getElementById('td-weather')
    let temperature = document.getElementById('td-temperature');
    let humidity = document.getElementById('td-humidity')
    let pressure = document.getElementById('td-pressure');
  
    city.textContent = json.name;
    weather.textContent = json.weather[0].main
    temperature.textContent = json.main.temp;
    humidity.textContent = json.main.humidity
    pressure.textContent = json.main.pressure;
  })
  .then(setMapCenter)

  function setMapCenter(resullt) {
    map.setCenter({ lat: Number(lat), lng: Number(lon) });
  }
}