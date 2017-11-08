var paint_room = function() {
    var tablehead = "<thead><tr><th tag='id'>ID</th><th tag='number'>Room Number</th><th tag='cinema_id'>Cinema ID</th></tr></thead>"
    $.ajax({
        url: "http://127.0.0.1:5000/rooms",
        success: function(result) {
            $(".rooms-body").html('<table class="room-table table table-hover"></table>');
            $(".room-table").html(tablehead);
            $(".room-table").append("<tbody></tbody>");
            for (var i = 0; i < result["rooms"].length;i++) {
                $(".room-table > tbody").append("<tr>" + "<th>" + result["rooms"][i]["id"] + "</th>" + "<th>" +  result["rooms"][i]["number"] + "</th>" + "<th>" + result["rooms"][i]["cinema_id"] + "</th>" + "</tr>");
            };
        }, error: function(xhr) {
            $(".room-table").html("<h3>" + xhr.status + " - " + xhr.statusText + "</h3>");
        }
    });
};

paint_room();

$("#room-new-btn").click(function() {
    $.ajax({
        url: "http://127.0.0.1:5000/cinemas",
        success: function(result) {
            $(".rooms-body").html('<label for="cinema-sel">Select Cinema</label><select class="form-control" id="cinema-sel"></select>');
            for (var i = 0;i < result["cinemas"].length;i++) {
                $("#cinema-sel").append("<option cinema_id=" + result["cinemas"][i]["id"] + ">" + result["cinemas"][i]["name"] + "</option>");  
            };
            $(".rooms-body").append('<div class="form-group">Room Number<label for="room-create-inp"></label><input type="text" class="form-control" id="room-create-inp"></div>');
            $(".rooms-body").append('<button type="button" id="room-create-btn" class="btn btn-primary">Create Room</button>');
            $("#room-create-btn").click(function() {
                var data = {"cinema_id":$("#cinema-sel").find("option:selected").attr("cinema_id"),"number":$("#room-create-inp").val()};
                $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:5000/room/new",
                    data: JSON.stringify(data),
                    contentType: "application/json",
                    dataType: "json",
                    success: function(result) {
                        console.log(result);
                        alert(result["id"] + " has been added!");
                        paint_room();
                    },
                    error: function(xhr) {
                        alert(xhr.status + " - " + xhr.statusText);
                    }
                });
            });
        }
    });
});

$("#room-delete-btn").click(function() {
    $(".rooms-body").html('<div class="form-group">Room ID to Delete<label for="room-remove-inp"></label><input type="text" class="form-control" id="room-remove-inp"></div>');
    $(".rooms-body").append('<button type="button" id="room-remove-btn" class="btn btn-danger">Remove Room</button>');
    $("#room-remove-btn").click(function() {
        $.ajax({
            type: "DELETE",
            url: "http://127.0.0.1:5000/room/delete/" + $("#room-remove-inp").val(),
            success: function() {
                alert("Deleted Room");
                paint_room();
            }
        });
    });
});

$("#rooms-btn").click(function() {
    paint_room();
});
