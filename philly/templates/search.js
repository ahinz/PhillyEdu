String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

function table_row(ar,params) { 
    var href = []
    for(var key in params) {
        href.push(key + "=" + params[key])
    }
    href = href.join("&") 

    return '<a href="/school/' + ar['locationnumber'] + '?' + href + '"><div class="box" id="'+ ar['id'] +'"><div class="school-name">' + ar['name'].capitalize() + "</div><div class=\"grad-rate\">Graduation Rate<h2>80%</h2></div></div></a>"; 
}

function generate_section(schoolType, section, params) {
    var tbl = '<br /><div style="span8">' + "<h2>" + schoolType.capitalize() + " (" + section.length + ")</h2>\n";
    $.map(section, function(val,idx) {
        tbl += table_row(val, params);
    });
    return tbl + "</div>\n"
}

function generate_table(sections, params) {
    var tbl = "";
    for(var schoolType in sections) {
        tbl += generate_section(schoolType, sections[schoolType], params);
    }

    return tbl;
}

function get_form_params() {
    var map = {}
    $("#searchform :input").map(function(idx,jq) {
        if (jq.name && jq.name.length > 0) {
            map[jq.name] = jq.value;
        }
    });

    return map;
}

function do_search() {
    var params = get_form_params()
    var url = '{{ API_URL }}/api/search'
    $.ajax({
        url: url,
        dataType: 'json',
        data: params,
        success: function(resp) {
            // render_table(resp, params);
            markSchools(resp);
        }
    });
}

function markSchools(sections) {
    $('.box').removeClass('highlight');
    for(var schoolType in sections) {

        for(var i=0; i < sections[schoolType].length; i++) {
            $('#'+sections[schoolType][i].id).addClass('highlight');
        }
    }
}

function get_all() {
    var url = '{{ API_URL }}/api/list'
    $.ajax({
        url: url,
        dataType: 'json',
        success: function(resp) {
            render_table(resp, null);
            $('.box').addClass('highlight');
        }
    });
}



function render_table(data, params) {
    $('#citywide').empty();
    $('#selective').empty();
    $('#neighborhood').empty();

    $('#citywide').append(generate_section("citywide", data["citywide"], params));
    $('#selective').append(generate_section("selective", data["selective"], params));
    $('#neighborhood').append(generate_section("neighborhood", data["neighborhood"], params));
}    

$(function() {
    $("#searchform :input").map(function(idx,jq) {
        $(jq).change(do_search);
    });


    $("#run_search").click(do_search);
    get_all();
});
