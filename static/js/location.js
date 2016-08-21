(function(){
    'use strict';
    var locationBlock = document.getElementById("demo");
    var mapBlock = document.getElementById("map");

    var socket = new WebSocket("ws://127.0.0.1:8888/ws");
    socket.onmessage = function(event){
        console.log(event.data);
    };

    getLocation();

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(showPosition);
        } else {
            locationBlock.innerHTML = "Geolocation is not supported by this browser.";
        }
    }
    function showPosition(position) {
        socket.send(["Lat: " + position.coords.latitude,
                     "Long: " + position.coords.longitude].join("\n"));
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

