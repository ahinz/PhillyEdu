String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

function table_row(ar,params) { 
    var href = []
    for(var key in params) {
        href.push(key + "=" + params[key])
    }
    href = href.join("&") 

    return '<tr><td><a href="/school/' + ar['locationnumber'] + '?' + href + '">' + ar['name'].capitalize() + "</a></td></tr>"; 
}

function generate_section(schoolType, section, params) {
    var tbl = '<div style="span8">' + "<h2>" + schoolType.capitalize() + "</h2>\n";
    tbl += '<table class="table-bordered table-striped" style="width:100%">';
    $.map(section, function(val,idx) {
        tbl += table_row(val, params);
    });
    return tbl + "</table></div>\n"
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
            render_table(resp, params);
        }
    });
}

function render_table(data, params) {
    $('#results').empty();
    $('#results').append(generate_table(data, params));
}    

$(function() {
    $("#searchform :input").map(function(idx,jq) {
        $(jq).change(do_search);
    });


    $("#run_search").click(do_search);
    do_search();

});
