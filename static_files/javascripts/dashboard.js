$(document).ready(function () {
    var wrap = $(".row-wrap");

    var initialHeight = wrap.height();
    if (initialHeight < 200) {
        initialHeight = wrap.height() * 4;
        wrap.height(initialHeight);
    }


    /* Make left-border same height as parent */
    var rightColumn = $(".file-content");
    var parentHeight = rightColumn.parent().height();
    rightColumn.css("height", parentHeight);
});