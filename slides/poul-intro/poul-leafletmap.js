// This script initializes a Leaflet map centered to POuL headquarters
// Docs: https://leafletjs.com/examples/quick-start/

let poul_position = [45.4771659, 9.2297918];
var map = L.map('map', {
  keyboard: false
});

let layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors'
}).addTo(map);

map.setView([45.47812, 9.22812], 17);

var marker = L.marker(poul_position).addTo(map);
marker.bindPopup('<b>We are here!</b><br>POuL headquarters<br> Politecnico di Milano (Leonardo),<br>Building 9A, ground floor<br><a href="https://go.polimi.it/maps/MIA0113">PoliMaps</a> &bullet; <a href="https://www.openstreetmap.org/node/6284640534">OpenStreetMap</a>', offset=L.point(0,700));

// The map container changes size once displayed. We force map redraw when we reach the map slide. (This is a workaround)
Reveal.on( 'slidechanged', event => {
  if (Reveal.getCurrentSlide().className.includes("poul-map")) {
  map.invalidateSize();
  }
} );
