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
    console.log("Hello World from getSignedRequest");
    var data = {};
    data['filename'] = file.name;
    data['filetype'] = file.type;
    $.ajax({ 
        url: '/s3uploadtoken',
        dataType: 'json',
        data: data,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8'
    }).done(function(response) {
        console.log(response);
        uploadFile(response, file);
    });

}

function initUpload() {
    var files = document.getElementById('file-input').files;
    var file = files[0];

    if (!file) { return alert('No file selected.'); }

    getSignedRequest(file)
}

$('#file-input').on('change', initUpload)
