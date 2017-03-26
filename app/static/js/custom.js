/*
var photolist = [
["photo6.jpg"],
["photo7.jpg"],
["photo8.jpg"],
["photo9.jpg"],
["photo10.jpg"],
["photo11.jpg"],
["photo12.jpg"],
["photo13.jpg"],
["photo14.jpg"],
["photo15.jpg"],
["photo16.jpg"],
["photo17.jpg"],
["photo18.jpg"],
];
*/
var photolist = [
["photo6"],
["photo7"],
["photo8"],
["photo9"],
["photo10"],
["photo11"],
["photo12"],
["photo13"],
["photo14"],
["photo15"],
["photo16"],
["photo17"],
["photo18"],
];
var s3Path = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/preview/';

function loadPhotos(id, cnt) {
	cnt = (!cnt) ? photolist.length : cnt;
	var div = document.getElementById(id);

	photos = ""
	for (i=0; i<cnt; i++) {
		photos += "<div class='photo'><img id='" + photolist[i][0] + "' src='" + s3Path + photolist[i][0] + ".jpg" + "'></img></div>"		
	}

	div.innerHTML = photos;
};

function setHeader(id) {
  if (id != null) {
    var obj = document.getElementById("header").contentWindow.document.getElementById(id);
    obj.style.borderColor = "#33DDFF";
  }
}

function hideObj(id) {
	var obj = document.getElementById(id);
	obj.style.opacity = 0;
	obj.style.display = 'none';
}

function showObj(id) {
	var obj = document.getElementById(id);
	obj.style.opacity = 100;
	obj.style.display = 'block';
}

window.addEventListener("scroll", function() {
  if (document.getElementById("menuDIV").style.display == "block") hideMenu();
}, false);


