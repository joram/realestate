<?
include "csvToMapData.php";
?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>beta: Realestate pricing heatmap of Victoria</title>
    <link href="style.css" rel="stylesheet">
    <script src="https://maps.googleapis.com/maps/api/js?sensor=false&libraries=visualization"></script>
    <script>
	<? csvToMapData("priceData.csv", "priceData"); ?>

      function initialize() {
        
	// construct map
	var mapOptions = {
          zoom: 12,
          center: new google.maps.LatLng(48.463297,-123.372779),
          mapTypeId: google.maps.MapTypeId.TERRAIN 
        };
	map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
        pointArray = new google.maps.MVCArray(priceData);
        heatmap = new google.maps.visualization.HeatmapLayer({
          data: pointArray
        });
        heatmap.setMap(map);

        var gradient = [
          'rgba(0, 0, 255,  0)',
          'rgba(0, 0, 255,   1)',
          'rgba(100, 0, 100,   1)',
          'rgba(255, 0,   0, 1)'
        ]
        heatmap.setOptions({gradient: gradient});
        heatmap.setOptions({radius: 20});
        heatmap.setOptions({opacity: 1});
        heatmap.setOptions({dissipating: 1});
        heatmap.setOptions({maxIntensity: 8});
      }
    </script>
  </head>

  <body onload="initialize()">
	<? weekSelector(); ?>
    <div id="map_canvas" ></div>
  </body>
</html>

