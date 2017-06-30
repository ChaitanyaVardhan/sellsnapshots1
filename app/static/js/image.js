'use strict';

$(document).ready(function() {

function showImage(e) {
	var t = e.target;
	while (t.nodeName != 'IMG') { t=t.childNode }
	var src = t.getAttribute('src');
	var imageId = t.getAttribute('id');
	var t1 = document.getElementById('imageDIV');
	var t2 = t1.getElementsByTagName('IMG')[1];
	t2.src = src;
//	var t3 = t1.getElementsByTagName('a')[0];
//	var href = t3.getAttribute('href');
//	t3.href = '/buy/' + imageId;
	showObj('imageDIV');
}

$('#featured').on('click', '.photo', showImage)

$('#photodiv').on('click', '.photo', showImage)

function hideImage(e) {
	hideObj('imageDIV');
}

$('#imageDIV').on('click', '#img_close_wrap', hideImage)

});

