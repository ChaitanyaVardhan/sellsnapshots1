var pics = []
var cnt = 5;

//move 5 images into the pics array, start with index 1 instead of 0
function loadPics() {
	for(i=1; i<=cnt; i++) {
		pics[i] = new Image();
		pics[i].src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/bg" + i + "_sz.jpg"
	}
}

//start with the 2nd image and cycle through all images
var idx = 2;
function setPics() {
	var obj = document.getElementById("pretty");
	obj.style.backgroundImage = "url('" + pics[idx++].src + "')";
	if (idx > 5) idx = 1;
}

var text1 = ["sellsnapshots is a platform for professional photographers",
"are you a professional photographer?",
"create your portfolio page on sellsnapshots,",
"list your buisness address on Google Maps,",
"offer photography services and",
"get contacted by people looking for photography services"
];

function fadeIn(id, duration) {
    return $(id).fadeIn(duration);
}

function fadeOut(id, duration) {
    return $(id).fadeOut(duration);
}

var idx2=0;
function setText1() {
	var obj = document.getElementById("pretty_blurb");
	if (idx2 >= text1.length) idx2 = 0;
	obj.innerHTML = text1[idx2++];
  	fadeIn("#pretty_blurb", 500);
  	setTimeout( function () { fadeOut("#pretty_blurb", 500) }, 2500);	
}

function cycleItems(func, interval) {
	setInterval(func, interval);
}

function getAssets() {
	var obj1 = document.getElementById("pretty_logo_img");
	obj1.src = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/sellsnapshots_front.png';

	var obj2 = document.getElementById("menu_img");
	obj2.src = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/menu.png'

	var obj3 = document.getElementById("img_close");
	obj3.src = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/x.png'
}

function init() {
	loadPics();
        setText1();
	cycleItems(setPics, 4800);
	cycleItems(setText1, 3500);
	getAssets();
}

window.addEventListener("scroll", function() {
  var top = document.getElementById("header");
  top.style.display = (document.body.scrollTop > 60) ? "block" : "none";
}, false);
