var selectedLanguage = "English"

var translations = {
    'English': {
        'english_option': "English",
        'hungarian_option': "Hungarian",
        'chart_1_title': "Strict Lateness Check (Any lateness greater than 0 seconds)",
        'chart_2_title': "Lenient Lateness Check (Any lateness greater than 60 seconds)",
        'histogram': {
            title: "Lateness per hour",
            historical_title: "Historical Average Lateness per hour",
            hAxis: "Hour of the day",
            vAxis: "Percentage of vehicles late"
        },
        'scatter': {
            title: "Lateness vs. Speed comparison",
            hAxis: "Lateness (s)",
            vAxis: "Speed (km/h)"
        },
        'topbottom':{
            title_top: "The least late routes in the last hour",
            title_bottom: "The most late routes in the last hour",
            hAxis_top: "Average Lateness in Seconds",
            hAxis_bottom: "Average Lateness in Minutes",
            vAxis: "Vehicle Line Name"
        }
    },
    'Hungarian': {
        'english_option': "Angolul",
        'hungarian_option': "Magyarul",
        'chart_1_title': "Szigorú késési ellenőrzés (bármilyen 0 másodpercnél hosszabb késés)",
        'chart_2_title': "Enyhe késés ellenőrzése (60 másodpercnél hosszabb késés)",
        'histogram': {
            title: "Késés óránként",
            historical_title: "Történelmi átlagos késés óránként",
            hAxis: "A nap órája",
            vAxis: "Késő járművek százalékos aránya"
        },
        'scatter': {
            title: "Késés vs. sebesség összehasonlítás",
            hAxis: "Késés (másodperc)",
            vAxis: "Sebesség (km/h)"
        },
        'topbottom':{
            title_top: "A legkevésbé késett útvonalak az elmúlt órában",
            title_bottom: "A legkésőbb útvonalak az elmúlt órában",
            hAxis_top: "Átlagos késés másodpercben",
            hAxis_bottom: "Átlagos késés percekben",
            vAxis: "Járműsor neve"
        }
    }
};

var title_chart_lateness_per_hour = 'Lateness per hour';
var title_chart_historical_lateness_per_hour = 'Historical Average Lateness per hour';

function drawAll(){
    addPoints();
    drawHistogram();
    drawHistogramPred();
    drawHistogram_n();
    drawHistogramPred_n();
    drawScatter();
    drawTop();
    drawBottom();
}

function languageChanged() {
    selectedLanguage = document.getElementById('language-dropdown').value;

    //go through class "translate"
    var elements = document.getElementsByClassName("translate")
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        if (element.id in translations[selectedLanguage]) {
            element.innerHTML = translations[selectedLanguage][element.id];
        }

    }


    //go through graph texts
    drawAll();

}