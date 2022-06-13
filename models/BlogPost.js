//mongoose
const mongoose = require('mongoose')
mongoose.connect('mongodb://localhost:27017/blog', { useNewUrlParser: true })
    //defining models
const BlogPostSchema = new Schema({
    title: String,
    body: String
});
//collection
const BlogPost = mongoose.model('BlogPost', BlogPostSchema)
module.exports = BlogPost