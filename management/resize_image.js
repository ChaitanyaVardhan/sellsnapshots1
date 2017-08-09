var async = require('async'),
    fs = require('fs'),
    gm = require('gm')


var images_arr = [];

var PATH = '.' + '/tmp';

var getFiles = function(path) {
    fs.readdir(path, function(err, files) {
	files.forEach(function(file) {
            images_arr.push(file)
	});
    })    
}


var resizeImg = function(item, callback) {
    gm(origImg)
    .resize(WIDTH, HEIGHT)
    .write(resizeImg, function(err) {
        if (err) callback(err);
        else {
            console.log("Successfully resized image.");
        }
    })
}

getFiles(PATH);

async.mapLimit(images_arr, resizeImg, function(err, results) {
    if (err) {
        console.log("Error: " + err.message);
    } else {
        console.log("Successfully resized all images to " + RESIZE_DIR + ".");
    }
})
