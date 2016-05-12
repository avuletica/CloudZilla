$(document).ready(function () {

    /* Make left-border same height as parent */
    var rightColumn = $(".file-wrap");
    var parentHeight = rightColumn.parent().height();
    rightColumn.css("height", parentHeight);

    var upload = $(".upload-button");
    upload.on("click", handleUploadClick);

    function handleUploadClick() {
        var uploadWidget = $(".upload-widget");
        uploadWidget.show();
    }

    $('.form-upload').submit(function () {
        var uploadWidget = $(".upload-widget");
        var $upload = $.trim($('#id_file').val());

        // Check if empty of not
        if ($upload === '') {
            alert("Please select file to upload");
            return false;
        }
        else
            uploadWidget.hide();
    });

    /* Change label text to file name on event */
    var fileInput = $('.controls input');
    fileInput.on('change', handleFileChange);

    function handleFileChange() {
        /* Minify file name */
        var fileName = fileInput.val();
        var res = fileName.split('\\').pop();
        res = res.substring(0, 6) + '...' + res.slice(-6);

        var fileLabel = $('#file-label');
        fileLabel.html(res);
    }

});