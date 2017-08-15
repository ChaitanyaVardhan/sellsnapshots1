var async = require('async'),
    fs = require('fs'),
    gm = require('gm')


var images_arr = [];

var PATH = '.' + '/tmp';

var CONCURRENT_DOWNLOAD_LIMIT = 25;

var RESIZE_DIR = '.' + '/resized';

var getFiles = function(path) {
    fs.readdir(path, function(err, files) {
        if (err) {
            console.log("Error: " + err.message);
        } else {
	    files.forEach(function(file) {
		images_arr.push(file)
	    });
        }
    })    
}


var resizeImg = function(item, callback) {
    var origImg = PATH + '/' + item;
    var resizeImg = RESIZE_DIR + '/' + item;
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

async.mapLimit(images_arr, CONCURRENT_DOWNLOAD_LIMIT, resizeImg, function(err, results) {
    if (err) {
        console.log("Error: " + err.message);
    } else {
        console.log("Successfully resized all images to " + RESIZE_DIR + ".");
    }
})
