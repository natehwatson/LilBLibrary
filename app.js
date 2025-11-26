const express = require('express');
const app = express();
const port = 3000

const path = require('path')
const handlebars = require('express-handlebars');

//use handlebars engine
app.set('view engine', 'hbs');
// set views folder to src/views
app.set('views', path.join(__dirname, 'src', 'views'));
// define where layouts are
app.engine('hbs', handlebars.engine({
    layoutsDir: path.join(app.get('views'), 'layouts'),
    partialsDir: path.join(app.get('views'), 'partials'),
    extname: 'hbs',
    //defaultLayout: 'filename',
}));

handlebars.registerPartials

//serve static files
app.use(express.static(path.join(__dirname, 'public')));

// root path
app.get('/', function(req, res) {
    // serves body main.handlebars to container index.handlebars
    res.render('main', {layout : 'index', content: '>'});
});

app.listen(3000, () => {
    console.log(`listening on port ${port}`)
});