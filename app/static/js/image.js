'use strict';

function fillInputTagValue() {
    var img_node = document.getElementById('photos');
    var img_arr = img_node.getElementsByTagName('IMG');
    var img_idx = img_node.getElementsByTagName('INPUT');

    for (var i=0; i<img_arr.length; i++) {
        img_idx[i].value = i;
    }
}

$(document).ready(function() {



function showImage(e) {
	var t = e.target;
        var targetNode = t;
	while (t.nodeName != 'IMG') { t=t.childNode }
	var src = t.getAttribute('src');
	var imageId = t.getAttribute('id');
        while (targetNode.nodeName != 'DIV') { targetNode=targetNode.parentNode }
        var imageIdx = targetNode.getElementsByTagName('INPUT')[0].value;
	var t1 = document.getElementById('imageDIV');
	var t2 = t1.getElementsByTagName('IMG')[3];
	t2.src = src;
        var leftNav = t1.getElementsByTagName('IMG')[1];
        leftNav.src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/nav-arrow-left.png";        
        var rightNav = t1.getElementsByTagName('IMG')[2];
        rightNav.src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/nav-arrow-right.png";
        var imageModalIdx = t1.getElementsByTagName('INPUT')[0];
        imageModalIdx.value = imageIdx;
        if (imageModalIdx.value == 0) {leftNav.style.display='none'}
//        if (imageModalIdx.value == img_idx.length - 1) { rightNav.style.display='none'}
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

function showPrevImage() {
    console.log('clicked left arrow');
}

$('#imageDIV').on('click', '#nav_left_arrow_wrap', showPrevImage);

function showNextImage() {
    console.log('clicked right arrow');
}

$('#imageDIV').on('click', '#nav_right_arrow_wrap', showNextImage);
});

