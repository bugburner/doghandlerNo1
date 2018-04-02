function ToggleBox (obj){ 
	theObject = document.getElementById(obj); 
	if (theObject.style.display == "block"){ 
		theObject.style.display = "none"; 
	}else{ 
		theObject.style.display = "block"; 
	} 
}

function ToggleBoxDet (obj){ 
	theObject = document.getElementById(obj); 
	if (theObject.style.display == "block"){ 
		theObject.style.display = "none"; 
	}else{ 
		theObject.style.display = "block"; 
	} 
}

function sf(obj){
	document.getElementById(obj).focus();
}

// highlight the object and take us there
function highlightObject(obj){ 
	// get the node
	theObject = document.getElementById(obj); 

	// highlight the object
	theObject.style.backgroundColor  = "#FFBA00";
	
	// take us to the highlighted object
	location.hash = obj;
}

function blink(speed){
	if (speed) {
		window.setInterval("blink()", speed*1000);
		return;
	}

	var blink = document.getElementsByTagName("span");
	for (var i=0; i<blink.length; i++) {
		if(blink[i].className == "blinkme") {
			blink[i].style.visibility = blink[i].style.visibility == "" ? "hidden" : "";
		}
	}
}

function blinkc(speed,color1,color2){
	if (speed > 0) {
		window.setInterval("blinkc(0,\'"+color1+"\',\'"+color2+"\')", speed*1000);
		return;
	}

	var blink = document.getElementsByTagName("span");
	for (var i=0; i<blink.length; i++) {
		if(blink[i].className == "blinkmec") {
			blink[i].style.color = blink[i].style.color == color1 ? color2 : color1;
		}
	}
}

