$(document).ready(function() {
    $(".item-inner").on("click", function() {
        expand_actions($(this).attr("action"), true);
    });

    $(".actions").on("click",".table tbody tr", function() {
        var row = {};
        var head = $(this).parents("tbody").siblings("thead").children("tr").children("th");
        for (var i = 1; i <= head.length;i++) {
            row[$(this).parents("tbody").siblings("thead").children("tr").children("th:nth-child(" + i + ")").attr("tag")] = $(this).children("th:nth-child(" + i + ")").text();
        };
        expand_actions("edit-movies", false, row);
    });

    /*
    $("#myModal").on("hidden.bs.modal", function() {
        $(".modal-body").empty();
    });*/
});

/*var populatemodal = function(element) {
    var title = $(element).attr("action");
    var url = "modals/" + title + "/" + title + ".html"
    var url2 = "modals/" + title + "/" + title + ".js"
    $("#myModal").modal("show");
    $(".modal-title").text($(element).children("h1").text());
    $(".modal-body").html("");
    $(".modal-body").load(url, function() {$.getScript(url2);});
};*/

var expand_actions = function(title, clear, options) {
    if (clear) {
        clear_actions();
    };
    $(".actions").append('<div class="action"></div>');
    var url = "actions/" + title + "/" + title + ".html";
    var url2 = "actions/" + title + "/" + title + ".js";
    $(".actions .action:last").append('<div class="text-center"><img class="arrow text-center" src="img/up_arrow.png"></img></div>');
    $(".arrow:last").click(function() { $('html, body').animate( {scrollTop: 0}, 600, "swing", clear_actions) });
    $(".actions .action:last").append('<div class="actions-header"></div><div class="actions-body"></div>');
    $(".actions-header:last").html("<h3>" + title + "</h3");
    $(".actions-body:last").load(url, function() {$.getScript(url2); });
    if ($(".actions .action:last").height() < $(window).height()) {
        $(".actions .action:last").height($(window).height());
    };

    $('html, body').animate({
        scrollTop: ($(document).height() - $(".actions .action:last").height())
    }, 600);

};

var clear_actions = function() {
    $(".actions").empty();
    $(".actions").height(0);
};