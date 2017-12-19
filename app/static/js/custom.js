var imageList = [];

function getImageList() {
    return $.ajax({
        url: 'api/v1/photos',
        dataType: 'json',
    })
}

var buildImageList = getImageList().done(function(data) {
        var dfd = $.Deferred();

        for (i=0; i<data.length; i++) {
            imageList[i] = data[i];
        }

        dfd.resolve;
        return dfd.promise();
    });

//var s3Path = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/preview/';

function buildPhotoDiv(div, cnt) {
	photos = ""
	for (i=0; i<cnt; i++) {
		photos += "<div class='photo'><img class='contained_img' src='" +  imageList[i].image_url + "'></img><input type='hidden' class='img_idx' name='img_idx' value=''></div>";		
	}

	div.innerHTML = photos;
}

function loadPhotos(id, cnt) {
	cnt = (!cnt) ? imageList.length : cnt;
	var div = document.getElementById(id);

        buildImageList.done(buildPhotoDiv(div, cnt));

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

//function to display photo menu div
function showPhotoMenu(e) {
    var t = e.target;
    while (t.className != 'photo') { t = t.parentNode }
    var imgNode = t.getElementsByTagName('IMG')[0];
    var src = imgNode.getAttribute('src');
    src = src.split('/');
    var imageName = src[src.length -1];

    var $photoMenu = document.getElementById('photoMenuDIV');
    var $input = $photoMenu.getElementsByTagName('INPUT')[0];

    $input.setAttribute('value', imageName);

    showObj('photoMenuDIV');
}

//event handler that displays the photo menu div when option dots are clicked
$("#photodiv").on('click', '.photo .option_dots', showPhotoMenu);


//delete photo ajax call
function deletePhoto() {
    var data = {};
    data['imageName'] = document.getElementById('delete_file_name').getAttribute('value');
    $.ajax({
      url: '/deletephoto',
      data: data,
      dataType: 'json'
    })
    .done(function(response){
      console.log(response);
    });
}

//event handler for click on the delete photo option
$('#photoMenuDIV').on('click', '#delete_photo_option', deletePhoto)
