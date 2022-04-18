function myMap() {
    // Initialize some map with center at Kathmandu
    var map = new google.maps.Map(document.getElementById('googleMap'), {
        center: {
            lat: 28.83232,
            lng: 84.29123
        },
        zoom: 7,
        mapTypeId: 'roadmap'
    });
      
    
    //get data of province from backend
    $.get("http://127.0.0.1:8000/api/provinces/", function(data, status){
        //alert("Data: " + data + "\nStatus: " + status);
        //console.log(data);
        //loop through province data
        $.each(data, function(key, value) { 
            //loop through districts data     
            $.each(value.districts,function(key,value){
                //console.log(value);
                //get request for individual district
                $.get(value,function(data,status){
                    //district level
                    //console.log(data.name);
                    // if district coordinate is not empty
                    if(data.coordinate!=""){
                        //convert string to coordinates array 
                        var districCoordinate = buildCoordinatesArrayFromString(data.coordinate);
                        // Construct the polygon.
                        var districPolygon = new google.maps.Polygon({
                            paths: districCoordinate,
                            strokeColor: '#fc1100',
                            strokeOpacity: 0.9,
                            strokeWeight: 1,
                            fillColor: getRandomColor(),
                            fillOpacity: 0.8
                        });
                        //to find center of District
                        var bounds = new google.maps.LatLngBounds();
                        districCoordinate.forEach(function(districCoordinate, index)
                        {
                            bounds.extend(districCoordinate);
                        });
                        attachPolygonInfoWindow(districPolygon,data)
                        //draw polygon on map
                        districPolygon.setMap(map); 
                    }
    
                    //loop through Municipaliteis data
                    $.each(data.municipalities,function(key,value){
                        //get request for individual municipality
                        $.get(value,function(data,status){
                            //console.log(data.name);
                            if(data.coordinate!=""){
                                //convert string to coordinates array 
                                var municipalityCoordinate = buildCoordinatesArrayFromString(data.coordinate);
                                
                                //console.log(districCoordinate);
                                // Construct the polygon.
                                var municipalityPolygon = new google.maps.Polygon({
                                    paths: municipalityCoordinate,
                                    strokeColor: '#fc1100',
                                    strokeOpacity: 0.6,
                                    strokeWeight: 0,
                                    fillColor: getRandomColor(),
                                    fillOpacity: 0.8,
                                    label:"suman"
                                }); 
                                //to find center of municipality
                                var bounds = new google.maps.LatLngBounds();
                                municipalityCoordinate.forEach(function(municipalityCoordinate, index)
                                {
                                    bounds.extend(municipalityCoordinate);
                                });
                                attachPolygonInfoWindow(municipalityPolygon,data)
                                municipalityPolygon.setMap(map);
                            }
                        });
                    });
                });
            });        
        });//end of each loop
    });//end of get province
    
    
    }//end mymap function