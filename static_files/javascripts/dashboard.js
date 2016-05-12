$(document).ready(function () {

    /* Make left-border same height as parent */
    var rightColumn = $(".file-wrap");
    var parentHeight = rightColumn.parent().height();
    rightColumn.css("height", parentHeight);

    var upload = $(".upload-button");
    upload.on("click", handleUploadClick);

    function handleUploadClick() {
        var uploadWidget = $(".upload-widget");
        $(".control-label").val('Bew');
        uploadWidget.show();
    }
});