google.charts.load("current", { packages: ["corechart", "bar", 'line'] });
google.charts.setOnLoadCallback(drawHistogram);
function drawHistogram() {
    console.log("histogram", histogram_data)
    let data = google.visualization.arrayToDataTable(histogram_data);
    var options = {
        title: translations[selectedLanguage].histogram.title,
        hAxis: {
            title: translations[selectedLanguage].histogram.hAxis,
        },
        vAxis: {
            title: translations[selectedLanguage].histogram.vAxis,
            viewWindow: {
                min: 0,
                max: 100
              },
            ticks: [0, 20, 40, 60, 80, 100]
        },
        legend: { position: 'none' },
    };
    var chartHistogram = new google.visualization.ColumnChart(document.getElementById('histogram_div'));
    chartHistogram.draw(data, options);
}

google.charts.setOnLoadCallback(drawHistogramPred);
function drawHistogramPred() {
    let data = google.visualization.arrayToDataTable(histogram_pred_data);
    var options = {
        title: translations[selectedLanguage].histogram.historical_title,
        hAxis: {
            title: translations[selectedLanguage].histogram.hAxis,
        },
        vAxis: {
            title: translations[selectedLanguage].histogram.vAxis,
            viewWindow: {
                min: 0,
                max: 100
              },
            ticks: [0, 20, 40, 60, 80, 100]
        },
        legend: { position: 'none' },
    };
    var chartHistogram = new google.visualization.ColumnChart(document.getElementById('histogram_pred_div'));
    chartHistogram.draw(data, options);
}



google.charts.setOnLoadCallback(drawHistogram_n);
function drawHistogram_n() {
    let data = google.visualization.arrayToDataTable(histogram_data_n);
    var options = {
        colors: ['#e7711c'],
        title: translations[selectedLanguage].histogram.title,
        hAxis: {
            title: translations[selectedLanguage].histogram.hAxis,
        },
        vAxis: {
            title: translations[selectedLanguage].histogram.vAxis,
            viewWindow: {
                min: 0,
                max: 100
              },
            ticks: [0, 20, 40, 60, 80, 100]
        },
        legend: { position: 'none' },
        histogram: {
            maxValue: 100
        }
    };
    var chartHistogram = new google.visualization.ColumnChart(document.getElementById('histogram_n_div'));
    chartHistogram.draw(data, options);
}


google.charts.setOnLoadCallback(drawHistogramPred_n);
function drawHistogramPred_n() {
    let data = google.visualization.arrayToDataTable(histogram_pred_data_n);
    var options = {
        colors: ['#e7711c'],
        title: translations[selectedLanguage].histogram.historical_title,
        hAxis: {
            title: translations[selectedLanguage].histogram.hAxis,
        },
        vAxis: {
            title: translations[selectedLanguage].histogram.vAxis,
            viewWindow: {
                min: 0,
                max: 100
              },
            ticks: [0, 20, 40, 60, 80, 100]
        },
        legend: { position: 'none' },
    };
    var chartHistogram = new google.visualization.ColumnChart(document.getElementById('histogram_pred_n_div'));
    chartHistogram.draw(data, options);
}



google.charts.setOnLoadCallback(drawScatter);
function drawScatter() {
    var data = google.visualization.arrayToDataTable(scatter_data)
    var options = {
        title: translations[selectedLanguage].scatter.title,
        hAxis: {
            title: translations[selectedLanguage].scatter.hAxis,
            minValue: 0, maxValue: 15 
        },
        vAxis: {
            title: translations[selectedLanguage].scatter.vAxis,
            minValue: 0, maxValue: 1 
        },
        // legend: 'none',
        trendlines: { 0: {showR2: true,
            visibleInLegend: true }} 
    };
    var chartScatter = new google.visualization.ScatterChart(document.getElementById('scatter_div'));
    chartScatter.draw(data, options);
}


google.charts.setOnLoadCallback(drawTop);
function drawTop() {
    var data = google.visualization.arrayToDataTable(top_data);
    var options = {
        title: translations[selectedLanguage].topbottom.title_top,
        width: 600,
        height: 400,
        bar: { groupWidth: "80%" },
        legend: { position: "none" },
        hAxis: {
            title: translations[selectedLanguage].topbottom.hAxis_top,
        },
        vAxis: {
            title: translations[selectedLanguage].topbottom.vAxis,
        },
        orientation: 'vertical'
    };
    var chart = new google.visualization.BarChart(document.getElementById('top_div'));
    chart.draw(data, options);
}

google.charts.setOnLoadCallback(drawBottom);
function drawBottom() {
    var data = google.visualization.arrayToDataTable(bottom_data);
    var options = {
        title: translations[selectedLanguage].topbottom.title_bottom,
        width: 600,
        height: 400,
        bar: { groupWidth: "80%" },
        legend: { position: "none" },
        hAxis: {
            title: translations[selectedLanguage].topbottom.hAxis_bottom,
        },
        vAxis: {
            title: translations[selectedLanguage].topbottom.vAxis,
        },
        orientation: 'vertical'
    };
    var chart = new google.visualization.BarChart(document.getElementById('bottom_div'));
    chart.draw(data, options);
}