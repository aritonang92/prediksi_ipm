function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var harapanhidup = document.getElementById("uiiniHarapanHidup");
    var pengeluaran = document.getElementById("uiiniPengeluaran");
    var lamasekolah = document.getElementById("uiiniLamaSekolah");
    var harapanls = document.getElementById("uiiniHarapanLamaSekolah");
    var estIPM = document.getElementById("uiEstimateHDI");
    var provinsi = document.getElementById("uiLocations");
  
    var url = "http://127.0.0.1:5000/predict_ipm"; 
  
    $.post(url, {
        provinsi: provinsi.value,
        ls_mean : parseFloat(lamasekolah.value),
        hls : parseFloat(harapanls.value),
        ppk : pengeluaran.value,
        harapan_hidup : parseFloat(harapanhidup.value),
    },function(data, status) {
        console.log(data.predicts_ipm);
        estIPM.innerHTML = data.predicts_ipm;
        console.log(status);
    });
}
  
function onPageLoad() {
    console.log( "document loaded" );

    var url = "http://127.0.0.1:5000/nama_provinsi"; 

    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;
  
  