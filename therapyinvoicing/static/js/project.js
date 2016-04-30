/* Project specific Javascript goes here. */



var monthlyreportvars;

function nextyear() {
    if (monthlyreportvars.yearlist.length > (monthlyreportvars.selectedyearloc + 1)) {
        monthlyreportvars.selectedyearloc++;
    }
    monthlyreport_barupdate();
}

function prevyear() {

    if (monthlyreportvars.selectedyearloc > 0) {
        monthlyreportvars.selectedyearloc--;
    }
    monthlyreport_barupdate();
}

function monthlyreport_createchartbase() {

    var x = d3.scale.linear()
            .domain([0, monthlyreportvars.numberofbars])
            .range([0, monthlyreportvars.width - monthlyreportvars.leftmargin - monthlyreportvars.rightmargin]);
        var y = d3.scale.linear()
            .domain([0, monthlyreportvars.yaxismax])
            .rangeRound([0, monthlyreportvars.height - monthlyreportvars.bottommargin - monthlyreportvars.topmargin])
    // add svg
    d3.select("#" + monthlyreportvars.chartid)
        .append("svg:svg")
        .attr("width", monthlyreportvars.width )
        .attr("height", monthlyreportvars.height);

    // add bar area
    d3.select("#" + monthlyreportvars.chartid)
        .select("svg")
        .append("svg:rect")
        .attr("x", monthlyreportvars.leftmargin)
        .attr("y", monthlyreportvars.topmargin)
        .attr("height", monthlyreportvars.height - monthlyreportvars.bottommargin - monthlyreportvars.topmargin)
        .attr("width", monthlyreportvars.width - monthlyreportvars.leftmargin - monthlyreportvars.rightmargin)
        .attr("fill", "#AACCB1");

    // draw xAxis
    d3.select("#" + monthlyreportvars.chartid)
        .select("svg")
        .append("svg:line")
        .attr("x1", monthlyreportvars.leftmargin)
        .attr("y1", monthlyreportvars.height - monthlyreportvars.bottommargin)
        .attr("x2", monthlyreportvars.width - monthlyreportvars.rightmargin + 10)
        .attr("y2", monthlyreportvars.height - monthlyreportvars.bottommargin)
        .attr("stroke", "black")

    // draw yAxis
    d3.select("#" + monthlyreportvars.chartid)
        .select("svg")
        .append("svg:line")
        .attr("x1", monthlyreportvars.leftmargin)
        .attr("y1", monthlyreportvars.height - monthlyreportvars.bottommargin)
        .attr("x2", monthlyreportvars.leftmargin)
        .attr("y2", monthlyreportvars.topmargin - 10)
        .attr("stroke", "black")


     // draw horizontal lines to chart area, spacing 500
    d3.selectAll("#" + monthlyreportvars.chartid)

        .selectAll("svg")
        .selectAll("line.horLines")
        .data(d3.range(0, parseInt(monthlyreportvars.yaxismax/500) + 1))
         .enter()
        .append("svg:line")

        .attr("x1", monthlyreportvars.leftmargin)
        .attr("y1", function(d) {return monthlyreportvars.height - monthlyreportvars.bottommargin- y(500 * d)})
        .attr("x2", monthlyreportvars.width - monthlyreportvars.rightmargin)
        .attr("y2", function(d) {return monthlyreportvars.height - monthlyreportvars.bottommargin - y(500 * d)})
        .attr("stroke", "grey")
        .attr("class", "horLines")

    // yAxis lables
    d3.selectAll("#" + monthlyreportvars.chartid)

        .selectAll("svg")
        .selectAll("text.yAxisLables")
        .data(d3.range(0, parseInt(monthlyreportvars.yaxismax/500) + 1))
         .enter()
        .append("svg:text")

        .attr("x", monthlyreportvars.leftmargin - 5)
        .attr("y", function(d) {return monthlyreportvars.height - monthlyreportvars.bottommargin- y(500 * d)})
        .attr("text-anchor", "end")
        .attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif")
        .text(function(d) {return (500*d) + "€";})
        .attr("class", "yAxisLables")

        // xAxis lables
        d3.selectAll("#" + monthlyreportvars.chartid)

        .selectAll("svg")
        .selectAll("text.xAxisLables")
        .data(monthlyreportvars.chartdata[monthlyreportvars.selectedyearloc].data)
         .enter()
        .append("svg:text")

        .attr("x", function(d, index) { return monthlyreportvars.leftmargin + x(index) + monthlyreportvars.barwidth; })
        .attr("y", monthlyreportvars.height - monthlyreportvars.bottommargin)
        .attr("dx", -monthlyreportvars.barwidth/2)
        .attr("text-anchor", "center")
            .attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif")
        .text(function(d) {return (d.month);})
            .attr("transform", "translate(0, 18)")
        .attr("class", "xAxisLables")

            // xAxis title

       // xAxis lables
        d3.selectAll("#" + monthlyreportvars.chartid)

        .selectAll("svg")
        .selectAll("text.xAxisLablesTitles")
        .data(["Kuukausi"])
         .enter()
        .append("svg:text")

        .attr("x", monthlyreportvars.leftmargin + (monthlyreportvars.width - monthlyreportvars.leftmargin - monthlyreportvars.rightmargin)/2)
        .attr("y", monthlyreportvars.height - monthlyreportvars.bottommargin+ 15)

        .attr("text-anchor", "middle")
            .attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif")
        .text(function(d) {return d;})
            .attr("transform", "translate(0, 18)")
        .attr("class", "xAxisLablesTitles")


        // add year total area
    d3.select("#" + monthlyreportvars.chartid)
        .select("svg")
        .append("svg:rect")
        .attr("x", monthlyreportvars.width - monthlyreportvars.rightmargin + 10)
        .attr("y", monthlyreportvars.topmargin)
        .attr("height", (monthlyreportvars.height - monthlyreportvars.bottommargin - monthlyreportvars.topmargin)/2)
        .attr("width", monthlyreportvars.rightmargin - 10)
        .attr("fill", "#AACCB1");

       // xAxis lables
        d3.selectAll("#" + monthlyreportvars.chartid)

        .selectAll("svg")
        .selectAll("text.legendLabel")
        .data([
            {label: "Vuosi yhteensä",
                x: monthlyreportvars.width - monthlyreportvars.rightmargin + (monthlyreportvars.rightmargin/2) - 10,
                y: monthlyreportvars.topmargin + 30,
                style: "font-size: 12; font-color: white; font-family: Helvetica, sans-serif",
                idsuffix: "Title"},

            {label: parseInt(monthlyreportvars.yeartotallist[monthlyreportvars.selectedyearloc]) + "€",
                x: monthlyreportvars.width - monthlyreportvars.rightmargin + (monthlyreportvars.rightmargin/2) - 10,
                y: monthlyreportvars.topmargin + 55,
            style: "font-size: 20; font-weight: bold; font-color: white; font-family: Helvetica, sans-serif",
            idsuffix: "Value"}
        ])
         .enter()
        .append("svg:text")
            .attr("x", function(d) {return d.x;})
        .attr("y", function(d) {return d.y;})

        .attr("text-anchor", "middle")
            .attr("style", function(d) {return d.style;})
        .text(function(d) {return d.label;})
            .attr("transform", "translate(15, 15)")
        .attr("class", "legendLabel")
            .attr("id", function (d) {return "yeartotal" + d.idsuffix})


}

function monthlyreport_barcreate() {
        var x = d3.scale.linear()
            .domain([0, monthlyreportvars.numberofbars])
            .range([0, monthlyreportvars.width - monthlyreportvars.leftmargin - monthlyreportvars.rightmargin]);
        var y = d3.scale.linear()
            .domain([0, monthlyreportvars.yaxismax])
            .rangeRound([0, monthlyreportvars.height - monthlyreportvars.bottommargin - monthlyreportvars.topmargin])

            d3.selectAll("#" + monthlyreportvars.chartid)
        .selectAll("svg")
                .selectAll("rect.bars")
                .data(monthlyreportvars.chartdata[monthlyreportvars.selectedyearloc].data)
                .enter()
                .append("svg:rect")
                .attr("x", function(rev, index) { return monthlyreportvars.leftmargin + x(index) + 5; })
                .attr("y", function(rev) { return monthlyreportvars.height - monthlyreportvars.bottommargin - y(rev.customerRevenue + rev.kelaRevenue); })
                .attr("height", function(rev) { return y(rev.customerRevenue + rev.kelaRevenue); })
                .attr("width", monthlyreportvars.barwidth)
                .attr("fill", "#68B3AF")
                .attr("class" , "bars");
    d3.select("#yearTitle")
            .text("Liikevaihto " + monthlyreportvars.yearlist[monthlyreportvars.selectedyearloc])
}

function monthlyreport_barupdate() {
                var x = d3.scale.linear()
            .domain([0, monthlyreportvars.numberofbars])
            .range([0, monthlyreportvars.width - monthlyreportvars.leftmargin - monthlyreportvars.rightmargin]);
        var y = d3.scale.linear()
            .domain([0, monthlyreportvars.yaxismax])
            .rangeRound([0, monthlyreportvars.height - monthlyreportvars.bottommargin - monthlyreportvars.topmargin])

            d3.selectAll("#" + monthlyreportvars.chartid)
        .selectAll("svg")
                .selectAll("rect.bars")
                .data(monthlyreportvars.chartdata[monthlyreportvars.selectedyearloc].data)
                .attr("y", function(rev) { return monthlyreportvars.height - monthlyreportvars.bottommargin - y(rev.customerRevenue + rev.kelaRevenue); })
                .attr("height", function(rev) { return y(rev.customerRevenue + rev.kelaRevenue); })
                .attr("fill", "#68B3AF")

    d3.select("#yearTitle")
            .text("Liikevaihto " + monthlyreportvars.yearlist[monthlyreportvars.selectedyearloc])

    d3.select("#yeartotalValue")
            .text(parseInt(monthlyreportvars.yeartotallist[monthlyreportvars.selectedyearloc]) + "€")


}

function monthlyreport_init(apiurl) {

    monthlyreportvars = {
    apiurl: "",
     chartid: "monthlyreport",
    width: 600,
    height: 300,
    topmargin: 30, // top margin above bar draw area
    bottommargin: 40, // bottom margin above bar draw area, e.g. xaxis labels goes to this area
    rightmargin: 150,// right margin above bar draw area, e.g. place for legends or other info
    leftmargin: 100, // left margin outside bar draw area, e.g. y labels goes to this area
        barwidth: 20,
    yearlist: ["2015", "2016"],
        yeartotallist: [0,0], //total revenues
    selectedyearloc: 0,
    chartdata: [{year: "2015", data: []}],

    yaxismax: 2500,
    numberofbars: 12, // how many bars will be drawn

}
    monthlyreportvars.apiurl = apiurl;



    d3.json(monthlyreportvars.apiurl, function(error, datafromapi) {

        // LOAD DATA FROM API
        //get only year values from data
        datafromapi.forEach(function(obj) { monthlyreportvars.yearlist.push(obj['year'])})
        //get unique year values using jquery
        monthlyreportvars.yearlist = $.grep(monthlyreportvars.yearlist, function(v, k){
            return $.inArray(v ,monthlyreportvars.yearlist) === k;
        });
        monthlyreportvars.selectedyear = monthlyreportvars.yearlist[monthlyreportvars.yearlist.length - 1]; // select current year as default
        //create chartdata
        monthlyreportvars.chartdata = [];
        monthlyreportvars.yearlist.forEach(function(yearvalue) {
            monthlyreportvars.chartdata.push({
                year: yearvalue,
                data: datafromapi.filter(function(obj) {return (obj.year === yearvalue)})
            })
        })
        monthlyreportvars.yaxismax = 500 * (parseInt((d3.max(datafromapi, function(rev) { return rev.customerRevenue + rev.kelaRevenue; }))/500) + 1)
        monthlyreport_calcyeartotals()
        monthlyreport_createchartbase()
        monthlyreport_barcreate()

    })

}

function monthlyreport_calcyeartotals() {
    monthlyreportvars.yeartotallist = []
    monthlyreportvars.chartdata.forEach(function(d){
        monthlyreportvars.yeartotallist.push(d3.sum(d.data, function(r) {return r.customerRevenue + r.kelaRevenue}))
    })
}






function monthlyreport_update() {

    d3.json(apisourceurl, function(error, datafromapi) {
        var data = datafromapi.filter(function(obj) {return (obj.year === selectedyear)});
        var barWidth = 40;
        var width = ((barWidth + 10) * data.length) + 50
        var height = 250
        ymax = d3.max(data, function(rev) { return rev.customerRevenue + rev.kelaRevenue; })
        var x = d3.scale.linear().domain([0, data.length]).range([0, width - 50]);
        var y = d3.scale.linear().domain([0, d3.max(data, function(rev) { return rev.customerRevenue + rev.kelaRevenue ; }) ]).
            rangeRound([0, height])
        d3.select('svg').selectAll('rect')
            .data(data)
            .attr("y", function(rev) { return height - y(rev.customerRevenue + rev.kelaRevenue); })
            .attr("height", function(rev) { return y(rev.customerRevenue + rev.kelaRevenue); });

            d3.selectAll('text.yearTitle')
            .text("Vuosi " + selectedyear );

        //redraw horizontal line every 500€
        d3.select('svg').selectAll('.yTicks')
            .remove()
            .data(d3.range(-1, parseInt(ymax/500) + 1))
            .enter()
            .append("svg:line")
            .attr("x1", -5).
            // Round and add 0.5 to fix anti-aliasing effects (see above)
            attr("y1", function(d) { return height - y(500 * d); }).
            attr("x2", width-45).
            attr("y2", function(d) { return height - y(500 * d); }).
            attr("stroke", "black").
            attr("class", "yTicks");

        d3.select('svg').selectAll("text.yAxis")
            .remove().
            data(d3.range(-1, parseInt(ymax/500) + 1)).
            enter().append("svg:text").
            attr("x", width - 40).
            attr("y", function(d) { return (height - y(500 * d)) - 12 ; }).
            attr("text-anchor", "left").
            attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif").
            text(function(d) {return (500*d);}).
            attr("transform", "translate(0, 18)").
            attr("class", "yAxis");

        d3.select('svg').selectAll("text.xAxis")
            .remove().
            data(data).
            enter().append("svg:text").
            attr("x", function(rev, index) { return x(index) + barWidth; }).
            attr("y", height).
            attr("dx", -barWidth/2).
            attr("text-anchor", "middle").
            attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif").
            text(function(rev) {return rev.month;}).
            attr("transform", "translate(0, 18)").
            attr("class", "xAxis");

        d3.select("#yearTitle")
            .text("Liikevaihto " + selectedyear)

    });
}
//built from scratch
function monthlyreport_barchart(apiurl,reportid) {


    apisourceurl = apiurl

    d3.json(apiurl, function(error, datafromapi) {


        var years = [];

        //get only year values from data
        datafromapi.forEach(function(obj) { yearlist.push(obj['year'])})
        //get unique year values using jquery
       yearlist = $.grep(yearlist, function(v, k){
    return $.inArray(v ,yearlist) === k;
});
        if (selectedyear === "") {
        selectedyear = yearlist.pop();
        yearlist.push(selectedyear);
}
        var data = datafromapi.filter(function(obj) {return (obj.year === selectedyear)});

        var barWidth = 40;
        var width = ((barWidth + 10) * data.length) + 50
        var height = 250
        ymax = d3.max(data, function(rev) { return rev.customerRevenue + rev.kelaRevenue; })
        var x = d3.scale.linear().domain([0, data.length]).range([0, width - 50]);
        var y = d3.scale.linear().domain([0, d3.max(data, function(rev) { return rev.customerRevenue + rev.kelaRevenue ; }) ]).
            rangeRound([0, height])


        var monthReport = d3.select("#" + reportid).
        append("svg:svg").
        attr("width", width ).
        attr("height", height + 30);



        monthReport.selectAll("svg").
            data(data).
            enter().
            append("svg:rect").
            attr("x", function(rev, index) { return x(index) ; }).
            attr("y", function(rev) { return height - y(rev.customerRevenue + rev.kelaRevenue); }).
            attr("height", function(rev) { return y(rev.customerRevenue + rev.kelaRevenue); }).
            attr("width", barWidth).
            attr("fill", "#68B3AF");



        monthReport.selectAll("crevbartext").
            data(data).
            enter().
            append("svg:text").
            attr("x", function(rev, index) { return x(index) + barWidth; }).
            attr("y", function(rev) { return height - y(rev.customerRevenue + rev.kelaRevenue); }).
            attr("dx", -barWidth/2).
            attr("dy", "1.2em").
            attr("text-anchor", "middle").
            text(function(rev) { if (parseInt(rev.customerRevenue + rev.kelaRevenue) !== 0) { return parseInt(rev.customerRevenue + rev.kelaRevenue );} else { return "";}}).
            attr("fill", "white");



        monthReport.selectAll("text.xAxis").
            data(data).
            enter().append("svg:text").
            attr("x", function(rev, index) { return x(index) + barWidth; }).
            attr("y", height).
            attr("dx", -barWidth/2).
            attr("text-anchor", "middle").
            attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif").
            text(function(rev) {return rev.month;}).
            attr("transform", "translate(0, 18)").
            attr("class", "xAxis");

        monthReport.selectAll(".yTicks").
            data(d3.range(0, parseInt(ymax/500) + 1)).
            enter().append("svg:line").
            attr("x1", -5).
            attr("y1", function(d) { return height - y(500 * d); }).
            attr("x2", width-45).
            attr("y2", function(d) { return height - y(500 * d); }).
            attr("stroke", "black").
            attr("class", "yTicks");

         monthReport.selectAll("text.yAxis").
            data(d3.range(0, parseInt(ymax/500) + 1)).
            enter().append("svg:text").
            attr("x", width - 40).
            attr("y", function(d) { return (height - y(500 * d)) - 12 ; }).
            attr("text-anchor", "left").
            attr("style", "font-size: 12; font-color: white; font-family: Helvetica, sans-serif").
            text(function(d) {return (500*d);}).
            attr("transform", "translate(0, 18)").
            attr("class", "yAxis");

        d3.select("#yearTitle")
                .text("Liikevaihto " + selectedyear)



            })

}



