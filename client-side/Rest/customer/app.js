var movie_img = "<img src='img/avengers.jpg'>";

$(document).ready(function() {

    /* Setup */

    $("body").on("hover", ".movie" , function() {
        $(this).css("margin","5px");
        $(this).children("img").css("width","170px");
    }, function() {
        $(this).css("margin","10px");
        $(this).children("img").css("width","160px");
    });

    /* Ajax */

    $.ajax({
        url: "http://127.0.0.1:5000/movies",
        success: function(result) {
            for (var i = 0; i < result["showing_movies"].length;i++) {
                $.ajax({
                    url: "http://127.0.0.1:5000/movie/" + result["showing_movies"][i]["id"],
                    success: function(result2) {
                        $.get("movie_card.html", function(data) {
                            $("body").append(data);
                            $(".movie:last").attr("movie_id",result2["id"]);
                            var movie = $('.movie[movie_id=' + result2["id"] + ']');
                            movie.children("h4").text(result2["name"]);
                            movie.prepend(movie_img);
                        });
                    }, error: function(xhr2) {
                        alert("Error2 (" + xhr2.status + ") :  " + xhr2.statusText);
                    }
                });
            };
            
        }, error: function(xhr) {
            alert("Error (" + xhr.status + ") :  " + xhr.statusText);
        }
    }); 



});