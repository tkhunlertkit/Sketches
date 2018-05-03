var http = require("http");
var url  = require("url");
var fs   = require("fs");

http.createServer(function (request, response) {
    var path = url.parse(request.url).pathname;
    console.log("Pathname is " + path);
    
    fs.readFile(path.substr(1), function (err, data) {
        var contentType = {'Content-Type':'text/html'};
        if (err) {
            console.log(err);
            response.writeHead(404, contentType);
        } else {
            response.writeHead(200, contentType);
            response.write(data.toString());
        }
        response.end(); 
        console.log("returning response");   
    });
}).listen(8081);

console.log("Server running...")