$(document).ready(function () {

    /* Setup */
    $("body").on("hover", ".movie", function () {
        $(this).css("margin", "5px");
        $(this).children("img").css("width", "170px");
    }, function () {
        $(this).css("margin", "10px");
        $(this).children("img").css("width", "160px");
    });

    /* Ajax */

    $.ajax({
        url: "http://127.0.0.1:5000/movies",
        success: function (result) {
            for (var i = 0; i < result["showing_movies"].length; i++) {
                var movie = result["showing_movies"][i];
                paint_movie(movie);
            };

        },
        error: function (xhr) {
            alert("Error (" + xhr.status + ") :  " + xhr.statusText);
        }
    });

    /* Modal */

    $(".content").on("click", ".movie_card", function () {
        var movie = {};
        movie["name"] = $(this).children("h4").text();
        movie["id"] = $(this).attr("movie_id");
        $(".modal-header").text(movie["name"]);
        paint_modal(movie);
    });

});

function paint_movie(movie) {
    if (!$(".row:last > div").length < 12) {
        $(".content").append("<div class='row'></div>");
    };
    $.get("movie_card.html", function (data) {
        $(".content > .row:last").append(data);
        $(".movie_card:last").attr("movie_id", movie["id"]);
        var movie_dom = $('.movie_card[movie_id=' + movie["id"] + ']');
        movie_dom.data(movie);
        movie_dom.children("h4").text(movie["name"]);
        movie_dom.prepend("<img class='poster' src='posters/" + movie["name"].split(' ').join('+') + ".jpg'>");
    });
};

function paint_modal(movie) {
    $.ajax({
        url: "http://127.0.0.1:5000/movie/" + movie["id"] + "/screenings",
        success: function (result) {
            $(".modal-body").html("");
            $.get("reservation-modal-body.html", function (data) {
                $(".modal-body").append(get_poster_dom(movie));
                $(".modal-body").append(data);
                $("#modal-movie-title").text(movie["name"]);
                for (var i = 0; i < result["screenings"].length; i++) {
                    var screening = {};
                    screening["id"] = result["screenings"][i]["id"];
                    screening["screening_time"] = result["screenings"][i]["screening_time"];
                    screening["room_id"] = result["screenings"][i]["room_id"];
                    screening["movie_id"] = result["screenings"][i]["movie_id"];
                    $("#modal-screening-sel").append("<option>" + screening["screening_time"] + "</option>");
                };
            });

            $("#reservation-modal").modal("show");
        },
        error: function (xhr) {
            alert("Error (" + xhr.status + ") :  " + xhr.statusText);
        }
    });
};

function get_poster_dom(movie) {
    return $(".movie_card[movie_id='" + movie['id'] + "']").children("img").clone();
};

function moviesearch() {
    var input, filter, movies;
    input = document.getElementById("movie_search");
    filter = input.value.toUpperCase();
    movies = $(".movie_card");
    for (i = 0; i < movies.length; i++) {
        if (movies.eq(i).data("name").toUpperCase().indexOf(filter) > -1) {
            movies.eq(i).css("display", "");
            console.log(movies.eq(i).data("name"));
            console.log(filter);
        } else {
            movies.eq(i).css("display", "none");
        };
    };
}