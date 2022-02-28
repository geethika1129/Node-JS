//mongoose
const mongoose = require('mongoose')
mongoose.connect('mongodb://localhost/my_database', { useNewUrlParser: true })
    //defining models
const BlogPostSchema = new Schema({
    title: String,
    body: String
});
//collection
const BlogPost = mongoose.model('BlogPost', BlogPostSchema)
module.exports = BlogPost