$(".screenings-list-table").html("<thead><tr><th>ID</th><th>Movie</th><th>Room</th><th>Time</th><th>Repeat</th></tr></thead>");

$.ajax({
    url: "http://127.0.0.1:5000/screenings",
    success: function(result) {
        $(".screenings-list-table").append("<tbody></tbody>");
        for (var i = 0; i < result.length;i++) {
            $(".screenings-list-table > tbody").append("<tr>" + "<th>" + result[i]["id"] + "</th>" + "<th>" +  result[i]["movie_id"] + "</th>" + "<th>" + result[i]["room_id"] + "</th>" + "<th>" + result[i]["screening_time"] + "</th>" + "<th>" + "false" + "</th>" + "</tr>");
        };
    }, error: function(xhr) {
        $(".screenings-list-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
    }
});