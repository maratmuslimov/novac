var zmq = require('zmq')
  , sock = zmq.socket('pull');

sock.connect('tcp://127.0.0.1:5556');
console.log('Worker connected to port 3000');