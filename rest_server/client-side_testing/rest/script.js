$(document).ready(function() {

    $('.bt2').click(function() {
        $.ajax({
            url: "http://127.0.0.1:5000/movies",
            success: function(result) {
                $(".movies").html("<h3>Showing Movies: </h3>");
                for (var i = 0;result["showing_movies"].length > i;i++ ) {
                    $.ajax({
                        url: "http://127.0.0.1:5000/movies/" + result["showing_movies"][i]["movie_id"],
                        success: function(result) {
                            $(".movies").append("<p>" + result["name"] + "</p>");
                            
                        }});
                };
                
            }
        });
    });

    $('.bt1').click(function() {
        var movie_id = $('#moviein').val();
        if (movie_id == "") {
            return "Error"
        };
        movie_id = parseInt(movie_id);
        if (typeof movie_id === "number") {
            $.ajax({
                url: "http://127.0.0.1:5000/movies/" + movie_id,
                success: function(result) {
                    $(".movies").append("<h3>Your Movie:</h3>");
                    $(".movies").append(result["id"] + " | " + result["name"] + " (" + result["release_date"] + ")");
                }, error: function(xhr) {
                    $(".movies").html(xhr.status + " - " + xhr.statusText);
                }
            });
        } else {
            console.log("NaN - Try again");
        };
        
    });

    $('.bt3').click(function() {
        var movie_id = $('#moviein').val();
        if (movie_id == "") {
            return "Error"
        };
        $.ajax({
            type: "DELETE",
            url: "http://127.0.0.1:5000/movie/delete/" + movie_id,
            success: function() {
                $(".movies").html("<h3>Deleted Movie!</h3>");

            }
        });
    });

    $('.bt4').click(function() {
        var data = {"name":"","length":"","release_date":""};
        data["name"] = $("#name").val();
        data['length'] = $("#length").val();
        data["release_date"] = $("#year").val();

        console.log(data);

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/movie/add",
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            success: function(result) {
               alert(result["name"] + " has been added!");
            },
            error: function(xhr) {
                alert(xhr.status + " - " + xhr.statusText);
            }
        });

    });

    $('.bt5').click(function() {
        $.ajax({
            url: "http://127.0.0.1:5000/movies/all",
            success: function(result) {
                $(".movies").html("<h3>All Movies: </h3>");
                for (var i = 0;result["Movies"].length > i;i++ ) {
                    $(".movies").append("<p>" + result["Movies"][i]["name"] + " (" + result["Movies"][i]["release_date"] + ")"  + " | id: " + result["Movies"][i]["id"] + "</p>");
                };
                
            }
        });
    });

});
