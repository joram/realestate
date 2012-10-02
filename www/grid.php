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
    <script src="grid.js"></script>
    <script>
	 <? csvToMapData("priceData.csv", "priceData"); ?>
    </script>
  </head>

  <body onload="initialize()">
	<? weekSelector(); ?>
    <div id="map_canvas" ></div>
  </body>
</html>

