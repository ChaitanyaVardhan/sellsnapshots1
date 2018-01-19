'use strict';

var img_arr = [];
var img_idx = [];

function fillInputTagValue(name) {
    var img_node = document.getElementById(name);
//    window.img_arr = img_node.getElementsByTagName('IMG');
    window.img_arr = img_node.getElementsByClassName('contained_img');
    window.img_idx = img_node.getElementsByTagName('INPUT');

    for (var i=0; i<img_arr.length; i++) {
        window.img_idx[i].value = i;
    }
}

function queryImageModal () {
    var imageModal = {};
    var imageDiv = document.getElementById('imageDIV');
    var $imgTag = imageDiv.getElementsByTagName('IMG');
    var $inputTag = imageDiv.getElementsByTagName('INPUT');

    imageModal['IMG'] = $imgTag[3];
    imageModal['leftNav'] = $imgTag[1];
    imageModal['rightNav'] = $imgTag[2];
    imageModal['input'] = $inputTag[0];

    return imageModal;
}

function showImageModal (idx, src) {
	var t1 = document.getElementById('imageDIV');
	var t2 = t1.getElementsByTagName('IMG')[3];
	t2.src = src;

        if (t2.naturalWidth > t2.naturalHeight) {
            t2.style.width = '100%';
            t2.style.height = 'auto';
        } else {
            t2.style.height = '100%';
            t2.style.width = 'auto';
        }

        var imgClose = t1.getElementsByTagName('IMG')[0];
        imgClose.src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/x.png"
         
        var leftNav = t1.getElementsByTagName('IMG')[1];
        leftNav.src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/nav-arrow-left.png";        

        var rightNav = t1.getElementsByTagName('IMG')[2];
        rightNav.src = "https://s3.ap-south-1.amazonaws.com/sellsnapshots/assets/nav-arrow-right.png";

        var imageModalIdx = t1.getElementsByTagName('INPUT')[0];
        imageModalIdx.value = idx;


        leftNav.style.display = 'block';
        rightNav.style.display = 'block';

        if (imageModalIdx.value == 0) {leftNav.style.display='none'}

        if(imageModalIdx.value == img_idx.length - 1) { rightNav.style.display='none'}

	showObj('imageDIV');
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
        showImageModal(imageIdx, src);
}

$('#featured').on('click', '.photo', showImage)

$('#photodiv').on('click', '.photo .contained_img', showImage)

function hideImage(e) {
	hideObj('imageDIV');
}

$('#imageDIV').on('click', '#img_close_wrap', hideImage)

function showPrevImage() {
    var obj = queryImageModal();

    var idx = --obj['input'].value;
    var src = img_arr[idx].src;

    showImageModal(idx, src);
}

$('#imageDIV').on('click', '#nav_left_arrow_wrap', showPrevImage);

function showNextImage() {
    var obj = queryImageModal();

    var idx = ++obj['input'].value;
    var src = img_arr[idx].src;

    showImageModal(idx, src);
}

$('#imageDIV').on('click', '#nav_right_arrow_wrap', showNextImage);
});

