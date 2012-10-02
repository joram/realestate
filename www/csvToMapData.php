<?

function csvToMapData($filename, $listName){
        $fp = fopen( $filename, "r" ) or die("Couldn't open $filename");
        $firstLine = True;

	$count = 0;
	$max = 0;
	echo "var $listName = [\n";
        while( !feof($fp) ) {
                $line = fgets($fp);
                $parts = split("[,]",$line);
                if( sizeof($parts)==3 ){
                        //$price = intval($parts[0])/1000000;
                        $price = intval($parts[0]);
                        $lat = $parts[1];
                        $lng = $parts[2];
                        $lng = trim($lng);

                        if($firstLine){
                                $firstLine = False;
                        }else{
                                echo ",\n";
                        }
                        //echo "\t\t{location:new google.maps.LatLng($lat,$lng),weight:$price}";
                       	$price = $price/1000000;
			echo "\t\t{location: new google.maps.LatLng($lat,$lng), lat:$lat, lng:$lng, weight: ",($price),"}";
			$count ++;
			$max = max($price,$max);
			
                }
        }
        echo "\n];\n";
	echo "var $listName","_max = $max;";
	echo "// $listName contains $count data points\n";


}

function weekSelector(){
	$weeksOfData = array("2012_38","2012_39");

	echo "<select>\n";
	foreach ( $weeksOfData as $week){
  		echo "<option value='$week'>$week</option>\n";
	}
	echo "</select>\n";

}

?>
