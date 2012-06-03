function render_page(data) {
    console.log(data);
    $("#school_name").text(data["name"]);
    $("#grade_info").text(data["grades"]);

    $("#missing").text(data["allowed_absences"]);
    $("#late").text(data["allowed_tardy"]);

    var behavior = data["behavior_time"];
    var btext = "";
    if (behavior == 0) {
        btext = "No negative reports on most recent report card";
    } else {
        btext = "No negative reports";
    }

    $("#behavior").text(btext);

    var norm = data["national_norm"];
    if (norm == 0) {
        $("#norm").text("Unavailable");
    } else {
        $("#norm").text(norm + "%");
    }

    $("#bar_reading_" + data["pssa_reading"]).html("&#x25BC;");
    $("#bar_math_" + data["pssa_math"]).html("&#x25BC;");

    $("#mission").text(data["mission"]);
    $("#pride").text(data["pride"]);
    $("#highlights").text(data["highlights"]);
    $("#partnerships").text(data["partnerships"]);
    $("#extracurriculars").text(data["extracurriculars"]);

    if (parseInt(data["locationnumber"]) > 0) {
        $("#moreinfo").html('<a href="https://webapps.philasd.org/school_profile/view/' + data["locationnumber"] + '">Philadelphia School District Info</a>');
    } else {
        $("#moreinfo").html('No information yet');
    }
}

function do_search(id) {
//    var params = get_form_params()
    var url = '{{ API_URL }}/api/info/' + id
    $.ajax({
        url: url,
        dataType: 'json',
//        data: params,
        success: function(resp) {
            render_page(resp);
        }
    });
}

var currentSchoolCode = null;

$(function() { 
    currentSchoolCode = window.location.pathname.split("/")[2];

    var search = {}

    $.map(window.location.search.substring(1).split("&"), function(v) {
        var vv = v.split("=")
        search[vv[0]] = vv[1];
    });

    if (search["pssa_math"] != "-1") {
        $("#bar_math_student_" + search["pssa_math"]).html("&#x25B2;");        
    }

    if (search["pssa_reading"] != "-1") {
        $("#bar_reading_student_" + search["pssa_reading"]).html("&#x25B2;");        
    }

    
    do_search(currentSchoolCode);
});
