//crud operations
const mongoose = require('mongoose')
const BlogPost = require('./models/BlogPost') //import the blogpost moel
mongoose.connect('mongodb://localhost/my_database', { useNewUrlParser: true }); //create new database and coonect (if it doesnt exist it will be created)

BlogPost.create({
    title: 'What is Mongo DB',
    body: 'Having established the connection to MongoDB, we next illustrate CRUD(create, read, update, delete) operations via Mongoose. For sake of simplicity,   we will illustrate CRUD in a separate test file to understand the conceptsbefore applying them to our project'
}, (error, blogpost) => {
    console.log(error, blogpost)
})