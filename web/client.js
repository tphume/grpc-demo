const {
  IncrementRequest,
  IncrementReply,
  GetCounterRequest,
  GetCounterReply
} = require('./counter_pb.js');
const { CounterClient } = require('./counter_grpc_web_pb.js');

var client = new CounterClient('http://localhost:8080');

// Init script to add event listener
function init() {
  incButton = document.getElementById('incButton');
  fetchButton = document.getElementById('fetchButton');

  incButton.addEventListener('click', incCounter);
  fetchButton.addEventListener('click', fetchCounter);
}

// Increment counter value
function incCounter() {
  var request = new IncrementRequest();
  request.setValue(1);

  client.increment(request, {}, (err, response) => {
    updateCounter(response.getValue())
  });
}

// Fetch counter value
function fetchCounter() {
  var request = new GetCounterRequest();

  client.getCounter(request, {}, (err, response) => {
    updateCounter(response.getValue())
  });
}

// Helper function that will update the display of counter
function updateCounter(value) {
  console.log(value);
  display = document.getElementById("display");
  display.innerHTML = `Current counter value is: ${value}`;
}

// Wait for HTML to load
window.addEventListener('load', init);