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
/* const express = require('express') //require express module
const app = express() //calls express function to start new express calls
app.listen(3000, () => {
    console.log("Hello World port 3000");
})
=> => outputs hello world port 3000 */

/* const express = require('express') //calls express module
const app = express() //calls express function to start new express calls
app.listen(3000, () => {
    console.log("Hello World port 3000")
})

app.get('/', (req, res) => {
    res.json({
        name: 'geethika'
    })
//this is known as routing this is how u build an api
}) */

const path = require('path')
const express = require('express') //calls express module
const app = express() //calls express function to start new express calls
app.listen(1080, () => {
    console.log("Hello World port 3000")
})
app.get('/', (req, res) => {
        res.sendFile(path.resolve(__dirname, 'about.html')) //to make it operatable with all os
    })
    //change the port to get result when ever u receive the error error cant get


//using public 
const express = require('express') //calls express module
const app = express()
const path = require('path')
app.use(express.static('public'))
app.listen(8000, () => {
    console.log("Hello World 2003 here");
})