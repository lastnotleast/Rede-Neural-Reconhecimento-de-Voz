var buttonRecord = document.getElementById("record");
var teste = document.getElementById("teste");
//var buttonStop = document.getElementById("stop");

//buttonStop.disabled = true;

buttonRecord.onclick = function() {

    teste.src = "static/img/CapturandoSom.png"

    // var url = window.location.href + "record_status";
    buttonRecord.disabled = true;
    //buttonStop.disabled = false;

    // disable download link
    var downloadLink = document.getElementById("download");
    downloadLink.text = "";
    downloadLink.href = "";

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "true" }));

    sleep(3000);
    buttonRecord.disabled = false;
    console.log("Funcionou")
    teste.src = "static/img/CaptarVoz.png"
};
/*
buttonStop.onclick = function() {
    buttonRecord.disabled = false;
    buttonStop.disabled = true;

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);

            // enable download link
            //var downloadLink = document.getElementById("download");
            //downloadLink.text = "Download Audio";
            //downloadLink.href = "/static/file.wav";
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};*/

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}