express = require 'express'
DataContoller = require('./controllers/data')
bodyParser = require('body-parser');

app = express();

app.engine 'mustache', require 'mustache-express4'
app.set 'view engine', 'mustache'
app.set 'views',__dirname+'/views/'
app.set 'partials', __dirname+'/views/partials'
app.use '/static', express.static("#{__dirname}/static")
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/new-entry', DataContoller.new)
app.post('/save', DataContoller.save)
app.get('/list', DataContoller.list)
 

app.listen(5000, -> console.log "App started")