(function(){
    'use strict';
    var locationBlock = document.getElementById("demo");
    var mapBlock = document.getElementById("map");

    getLocation();

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(showPosition);
        } else {
            locationBlock.innerHTML = "Geolocation is not supported by this browser.";
        }
    }
    function showPosition(position) {
    }
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([37.41, 8.82]),
            zoom: 4
        })
    });
})();

