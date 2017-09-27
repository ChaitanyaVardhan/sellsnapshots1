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
    });

}

function initUpload() {
    var files = document.getElementById('file-input').files;
    var file = files[0];

    if (!file) { return alert('No file selected.'); }

    getSignedRequest(file)
}

$('#file-input').on('change', initUpload)
