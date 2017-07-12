var photolist = [];

$.ajax({
    url: 'api/v1/photos',
    dataType: 'json',
})
    .done(function(data) {
        for (i=0; i<data.length; i++) {
            photolist[i] = data[i];
        }
    });

//var s3Path = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/preview/';

function loadPhotos(id, cnt) {
	cnt = (!cnt) ? photolist.length : cnt;
	var div = document.getElementById(id);

	photos = ""
	for (i=0; i<cnt; i++) {
		photos += "<div class='photo'><img id='" + photolist[i] + "' src='" +  photolist[i].image_url + "'></img><input type='hidden' class='img_idx' name='img_idx' value=''></div>";		
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


