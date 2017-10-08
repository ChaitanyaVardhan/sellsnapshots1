/*
function to upload data to mlab db
*/
function uploadMlab(fileName) {
    var data = {};
    data['filename'] = fileName;

    $.ajax({
      url: '/mlabupload',
      data: data
    })
}

/*
  Function to carry out the actual POST request to S3 using the signed request from the Python app.
*/
function uploadFile(response, file){
    const xhr = new XMLHttpRequest();
    xhr.open('POST', response.data.url);
    xhr.setRequestHeader('x-amz-acl', 'public-read');
    const postData = new FormData();
    for(key in response.data.fields){
        postData.append(key, response.data.fields[key]);
    }
    postData.append('file', file);
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4){
            if(xhr.status === 200 || xhr.status === 204){
		alert('file uploaded');
                uploadMlab(file.name);                            
            }
            else{
		alert('Could not upload file.');
            }
        }
    };
    xhr.send(postData);
}
/*
function uploadFile(response, file) {
    var postData = new FormData();
    for (key in response.data.fields) {
        postData[key] = response.data.fields[key]
    }
    postData['file'] = file;
    console.log('calling s3');
    console.log(postData);
    console.log(response.data.url);

    $.ajax({
      url: response.data.url,
      method: "POST",
      data: postData,
      dataType: 'json',
      processData: false,
      contentType: 'multipart/form-data'
    })
    .success(function(response) {
      console.log('response from s3');
      console.log(response);
    })
    .error(function() {
      console.log(arguments);
    });

}
*/

function getSignedRequest(file) {
    var data = {};
    data['filename'] = file.name;
    data['filetype'] = file.type;
    $.ajax({ 
        url: '/s3uploadtoken',
        dataType: 'json',
        data: data,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8'
    }).done(function(response) {
        uploadFile(response, file);
    });

}

var files = [];

/* get the list of selected file */

$('#file-input').on('change', function() {
    files = document.getElementById('file-input').files;
});

/*upload the files */

$('#photo_upload').on('click', function() {
    if (files.length === 0) { return alert('No file selected.'); }

    for (var i=0; i<files.length; i++) {
        console.log('file: ' + files[i]);
        getSignedRequest(files[i]);
    }
});
