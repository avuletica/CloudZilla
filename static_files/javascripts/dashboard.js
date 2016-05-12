$(document).ready(function () {

    /* Make left-border same height as parent */
    var rightColumn = $(".file-wrap");
    var parentHeight = rightColumn.parent().height();
    rightColumn.css("height", parentHeight);

    /* Toggle upload view */
    var upload = $(".upload-button");
    var profileContent = $(".profile-widget");
    upload.on("click", handleUploadClick);

    function handleUploadClick() {
        var uploadWidget = $(".upload-widget");
        uploadWidget.fadeIn();
        profileContent.fadeOut();
    }

    /* Prevent empty file submit */
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
        if (res.length > 14)
            res = res.substring(0, 6) + '...' + res.slice(-8);

        var fileLabel = $('#file-label');
        fileLabel.html(res);
    }


    /* Switch to profile view */
    var profile = $(".profile-button");
    profile.on("click", handleProfileClick);

    function handleProfileClick() {
        var uploadWidget = $(".upload-widget");
        profileContent.fadeIn();
        uploadWidget.fadeOut(100);
        $("#id_password").select();
    }
});