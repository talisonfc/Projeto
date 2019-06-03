/**
 * Primary file for the API
 */

// Dependency
const http = require("http")
const url = require("url")

// The server shoud response with a string
var server = http.createServer(function(req, res){
    // Get the URL and parse it
    var parsedUrl = url.parse(req.url, true)
    // Get the path
    var path = parsedUrl.pathname
    var trimmedPath = path.replace(/^\/+|\/+$/g,'')
    // Send the response
    res.end('Hello world')

    // Log the request path
    console.log('Request received on path '+trimmedPath)
})

// Start the serve, and have it listen on port 3000
server.listen(3000, function(){
    console.log("The server is lintenning on port 3000 now")
})