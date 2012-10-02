
function jHeatMap(){
	this.grid = new Array();
	this.rez = 0.01;
	this.rectPos = hmRectPos;
	this.addData = hmAddData;
	this.draw = hmDraw;
	this.loadData = hmLoadData;
}

function hmLoadData(data){
	for(i in data){
		var val = data[i].weight;
		var lat = data[i].lat;
		var lng = data[i].lng;
		this.addData(val,lat,lng);
	}
}


function hmRectPos(lat, lng){
	var x = lat - (lat%this.rez);
	var y = lng - (lng%this.rez);
	return new google.maps.LatLng(x,y);
}

function hmAddData(val, lat, lng){
		
	// cell exists
	var pos = this.rectPos(lat,lng);
	if( this.grid[pos]==null ){
		var ds = new dataSquare();
		var SE = new google.maps.LatLng(pos.lat(), pos.lng()-this.rez);
		var NW = new google.maps.LatLng(pos.lat()+this.rez, pos.lng());
		ds.bounds = new google.maps.LatLngBounds(SE,NW);
		this.grid[pos] = ds;
	}

	// add data to cell
	this.grid[pos].addDatum(val);
}

function hmDraw(map){

	var uniqueVals = [];
	var max = 0;
	var min = -1;
	for(key in this.grid){
		var weight = this.grid[key].weight;
		if( weight>max )
			max = weight;
		if( min==-1 || weight<min)
			min = weight;
		uniqueVals.push(weight);
	}

	// find pos	
	uniqueVals.sort();
	var total = uniqueVals.length;
	
	for(key in this.grid){
		var weight = this.grid[key].weight;
		var pos = uniqueVals.indexOf(weight);
		this.grid[key].draw(map, min,max, pos,total);
	}
}


function dataSquare() {
	this.vals = [];
	this.rect = new google.maps.Rectangle();
	this.addDatum = dsAddDatum;
	this.draw = dsDraw;
	this.bounds;
	this.weight = 0;
}

function dsAddDatum(val){
	this.vals.push(val);

	var sum = 0;
	for(key in this.vals){
		sum += this.vals[key];
	}
	this.weight = sum/this.vals.length;
}

function colorToHex(color) {
    if (color.substr(0, 1) === '#') {
        return color;
    }
    var digits = /(.*?)rgb\((\d+), (\d+), (\d+)\)/.exec(color);
    
    var red = parseInt(digits[2]);
    var green = parseInt(digits[3]);
    var blue = parseInt(digits[4]);
    
    var rgb = blue | (green << 8) | (red << 16);
    return digits[1] + '#' + rgb.toString(16);
};

function dsDraw(map, min,max, pos,total){
	alert(pos+" / "+total);
	if( this.vals.length==0 ){
		return;
	}
	

	//var ratio = this.weight/max;
	var ratio = pos/total;
	var red = (256*ratio);
	var green = (256*(1-ratio));
	var colourStr = "rgb("+Math.round(red)+", "+Math.round(green)+", 000)";
//	alert(colourStr);
	var colour = colorToHex(colourStr);
//	alert(red+","+green+" -> "+colour);
	var rectOptions = {
		strokeColor: "#222222",
		strokeOpacity: 0.7,
		strokeWeight: 1,
		//fillColor: "#FF0000",
		fillColor: colour,
		fillOpacity: ratio,
		map: map,
		bounds: this.bounds
	};
	this.rect.setOptions(rectOptions);

}


		
function initialize() {
        
	// construct map
	var mapOptions = {
          zoom: 12,
          center: new google.maps.LatLng(48.463297,-123.372779),
          mapTypeId: google.maps.MapTypeId.TERRAIN 
        };
	map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);

	var hm = new jHeatMap();
	hm.loadData(priceData);
	hm.draw(map);

}

