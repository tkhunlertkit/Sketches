var http = require("http");

var options = {
    host: 'localhost',
    port: '8081',
    path: '/index.html'
};

var callback = function(response) {
    var body = '';
    var eventNames = response.eventNames();
    
    console.log(eventNames);
    response.on('data', function(data) {
        console.log("In 'data' callback listener");
        body += data;
    });

    response.on('test', function() {
        console.log("Simple test...");
    });

    response.on('end', function() {
        console.log("In 'end' callback listener");
        console.log(body);
    });
}

var req = http.request(options, callback);
req.end();