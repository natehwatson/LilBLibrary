const express = require('express');
const app = express();
const port = 3000

const path = require('path')
const handlebars = require('express-handlebars');
const db = require('./src/config/connectToDB.js');
const searchController = require('./src/controllers/searchController.js');

//use handlebars engine
app.set('view engine', 'hbs');
// set views folder to src/views
app.set('views', path.join(__dirname, 'src', 'views'));
// define where layouts are
app.engine('hbs', handlebars.engine({
    layoutsDir: path.join(app.get('views'), 'layouts'),
    partialsDir: path.join(app.get('views'), 'partials'),
    extname: 'hbs',
    defaultLayout: false,
}));


//serve static files
app.use(express.static(path.join(__dirname, 'public')));

// root path
app.get('/', function(req, res) {
    // serves body main.handlebars to container index.handlebars
    res.render('main', {layout : 'index', content: '>'});
});

app.get('/search', searchController.searchSongsByTitle);

app.get('/api/search', searchController.searchSongsByTitleAPI);

app.listen(3000, () => {
    console.log(`listening on port ${port}`)
});