var zerorpc = require("zerorpc");

var client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");

var text = document.getElementById("text").value;
var result = document.getElementById("result").value;
var resultText = document.getElementById("resultText");

// client.invoke("streaming_range", document.getElementById("text").value, function(error, res, more) {
//     console.log(res);
// });

calc = function() {
  client.invoke("streaming_range", text, function(error, res, more) {
    console.log(res);
    resultText.innerHTML = res;
    resul = res;
  })
};


//
// var zerorpc = require("zerorpc");
//
// var client = new zerorpc.Client();
// client.connect("tcp://127.0.0.1:4242");
//
// client.invoke("hello", "RPC", function(error, res, more) {
//     console.log(res);
// });
