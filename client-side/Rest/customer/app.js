var movie_img = "<img src='img/avengers.jpg'>"

$(document).ready(function() {
    $.get("movie_card.html", function( movie ) {
        for (var i = 0; i < 30; i++) {
            $("body").prepend(movie);
        };
        $(".movie").prepend(movie_img);
    });

    $("body").on("hover", ".movie" , function() {
        $(this).css("margin","5px");
        $(this).children("img").css("width","170px");
    }, function() {
        $(this).css("margin","10px");
        $(this).children("img").css("width","160px");
    });
});