var zerorpc = require("zerorpc");

var client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");

var text = document.getElementById("text");
//var result = document.getElementById("result").value;
var resultText = document.getElementById("resultText");
var inputAmount = document.getElementById("input-amount");


// inputs start

var P_1 = document.getElementById("P_1");
var V_ap = document.getElementById("V_ap");
var q = document.getElementById("q");
var T = document.getElementById("T");
var P_2 = document.getElementById("P_2");

//inputs end

// client.invoke("streaming_range", document.getElementById("text").value, function(error, res, more) {
//     console.log(res);
// });

calc = function() {
  client.invoke("streaming_range", text.value, function(error, res, more) {
    console.log(res);
    resultText.innerHTML = res;
    result = res;
  })
};

getInputsValue = function() {
  console.log("{" +
  '"' + P_1.name + '"' + ":" , P_1.value + ",",
  '"' + V_ap.name + '"' + ":" , V_ap.value + ",",
  '"' + q.name + '"' + ":" , q.value + ",",
  '"' + T.name + '"' + ":" , T.value + ",",
  '"' + P_2.name + '"' + ":" , P_2.value +
  "}");
}

function addInputs() {
  var number = inputAmount.value;
  var container = document.getElementById("inputsContainer");
  while (container.hasChildNodes()) {
      container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        container.appendChild(document.createTextNode("Member " + (i+1)));
        var input = document.createElement("input");
        input.type = "text";
        container.appendChild(input);
        container.appendChild(document.createElement("br"));
      }
}

inputAmount.addEventListener("input", addInputs);

//
// var zerorpc = require("zerorpc");
//
// var client = new zerorpc.Client();
// client.connect("tcp://127.0.0.1:4242");
//
// client.invoke("hello", "RPC", function(error, res, more) {
//     console.log(res);
// });
