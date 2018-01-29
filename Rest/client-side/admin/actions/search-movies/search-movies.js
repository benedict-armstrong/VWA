$("#movie-search-btn").click(function() {
    $("movie-search-table").empty();
    var tablehead = "<thead><tr><th tag='id'>ID</th><th tag='name'>Name</th><th tag='release_date'>Release Date</th></tr></thead>"
    var selection = $("#movie-search-sel").find("option:selected").html();
    var search = $("#movie-search-inp").val();

    if (selection == "All") {
        $.ajax({
            url: "http://127.0.0.1:5000/movies/all",
            success: function(result) {
                $(".movie-search-table").html(tablehead);
                $(".movie-search-table").append("<tbody></tbody>");
                for (var i = 0; i < result["Movies"].length;i++) {
                    $(".movie-search-table > tbody").append("<tr>" + "<th>" + result["Movies"][i]["id"] + "</th>" + "<th>" +  result["Movies"][i]["name"] + "</th>" + "<th>" + result["Movies"][i]["release_date"] + "</th>" + "</tr>");
                };
            }, error: function(xhr) {
                $(".movie-search-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
            }
        }); 
    } else if (!search) {$(".movie-search-result").html("<h3>Please enter Something!</h3>");} else {
        switch(selection) {
            case "Movie ID":
                var movie_id = parseInt(search);
                $.ajax({
                    url: "http://127.0.0.1:5000/movies/" + movie_id,
                    success: function(result) {
                        $(".movie-search-table").html(tablehead);
                        $(".movie-search-table").append("<tbody></tbody>");
                        $(".movie-search-table > tbody").append("<tr>" + "<th>" + result["id"] + "</th>" + "<th>" +  result["name"] + "</th>" + "<th>" + result["release_date"] + "</th>" + "</tr>");
                    }, error: function(xhr) {
                        $(".movie-search-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
                    }
                }); 
                break;
            case "Name":
                $.ajax({
                    url: "http://127.0.0.1:5000/movies/name/" + search,
                    success: function(result) {
                        $(".movie-search-table").html(tablehead);
                        $(".movie-search-table").append("<tbody></tbody>");
                        $(".movie-search-table > tbody").append("<tr>" + "<th>" + result["id"] + "</th>" + "<th>" +  result["name"] + "</th>" + "<th>" + result["release_date"] + "</th>" + "</tr>");
                    }, error: function(xhr) {
                        $(".movie-search-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
                    }
                });
                break;
            case "Release Date":
                var release_date = parseInt(search);
                $.ajax({
                    url: "http://127.0.0.1:5000/movies/year/" + release_date,
                    success: function(result) {
                        $(".movie-search-table").html(tablehead);
                        $(".movie-search-table").append("<tbody></tbody>");
                        for (var i = 0; i < result.length;i++) {
                            $(".movie-search-table > tbody").append("<tr>" + "<th>" + result[i]["id"] + "</th>" + "<th>" +  result[i]["name"] + "</th>" + "<th>" + result[i]["release_date"] + "</th>" + "</tr>");
                        };
                    }, error: function(xhr) {
                        $(".movie-search-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
                    }
                });
                break;
            default:
                console.log("Invalid - Entry");
        };
    };
});