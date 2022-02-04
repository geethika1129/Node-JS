/* const http = require('http');
const server = http.createServer(function(req, res) {
    console.log(req.url)
    res.end('Hello Node js')
})
server.listen(3000) */

/* => => will give hello node js in page */

/* const http = require('http');
const server = http.createServer(function(req, res) {
    if (req.url == '/about')
        res.end('The about page')
    else {
        res.write(404)
        res.end('page not found')
    }
})
server.listen(3000) 

=> => prints in write (developer tools)

*/

/* const http = require('http')
const fs = require('fs')
const aboutPage = fs.readFileSync('about.html')
const server = http.createServer(function(req, res) {
    if (req.url == '/about')
        res.end(aboutPage)
    else {
        res.write(404)
        res.end('page not found')
    }
})
server.listen(8000)

=> =>prints the html page

*/


/* Express Ch2 */