(function(){
    'use strict';
    var locationBlock = document.getElementById("demo");

    getLocation();
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(showPosition);
        } else {
            locationBlock.innerHTML = "Geolocation is not supported by this browser.";
        }
    }
    function showPosition(position) {
        locationBlock.innerHTML = ["Latitude:", position.coords.latitude, 
        "<br>Longitude:", position.coords.longitude].join(" "); 
}
})();

