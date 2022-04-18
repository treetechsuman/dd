//alert("file is loaded");
/**
* Creates an array of coordinates from the content of the MultiGeometryCoordinates node of the GADM database.
*/
 function buildCoordinatesArrayFromString(MultiGeometryCoordinates){
    var finalData = [];
    //var grouped = MultiGeometryCoordinates.split("\n");
    var grouped = MultiGeometryCoordinates.split(" ");

    grouped.forEach(function(item, i){
        let a = item.trim().split(',');

        finalData.push({
            lng: parseFloat(a[0]),
            lat: parseFloat(a[1])
        });
    });

    return finalData;
}

/**
* find the center coordinate of polygone
*/
function polygonCenter(poly) {
    const vertices = poly.getPath();

    // put all latitudes and longitudes in arrays
    const longitudes = new Array(vertices.length).map((_, i) => vertices.getAt(i).lng());
    const latitudes = new Array(vertices.length).map((_, i) => vertices.getAt(i).lat());

    // sort the arrays low to high
    latitudes.sort();
    longitudes.sort();

    // get the min and max of each
    const lowX = latitudes[0];
    const highX = latitudes[latitudes.length - 1];
    const lowy = longitudes[0];
    const highy = longitudes[latitudes.length - 1];

    // center of the polygon is the starting point plus the midpoint
    const centerX = lowX + ((highX - lowX) / 2);
    const centerY = lowy + ((highy - lowy) / 2);
    const myLatLng = { lat: centerX, lng: centerY };
    return myLatLng;
    //return (new google.maps.LatLng(centerX, centerY));
}

/**
* generate randome color code
*/
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

/**
* attach polygone information in side 
*/
  function attachPolygonInfoWindow(polygon,info) {
    var infoWindow = new google.maps.InfoWindow();
    google.maps.event.addListener(polygon, 'mouseover', function (e) {
        // infoWindow.setContent(info);
        // var latLng = e.latLng;
        // infoWindow.setPosition(latLng);
        // infoWindow.open(map);
        //alert("click working");
        console.log(info)
        $("#name").text(info.name);
    });
}