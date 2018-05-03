var express     = require("express");
var app         = express();
var fs          = require("fs");
var bodyParser  = require("body-parser");
var pug         = require("pug");

var urlencodedParser = bodyParser.urlencoded({ extended: false });
var userFile = __dirname + "/data/users.json";

app.set('view engine', 'pug');
app.set('views', './views');

app.get('/', function (req, res) {
	res.send("hello world");
});

app.get("/index.html", function (req, res) {
	res.render('index', {
		title: 'Main Page'
	});
});

app.get("/listUsers", function (req, res) {
	var locals = {
		title: 'PUG !!!!'
	};
	// var fn = pug.compileFile('users.pug');

	fs.readFile(userFile, function (err, data) {
		locals.users = JSON.parse(data)
		// var html = fn(locals);
		res.render('users', locals);
	});
});

app.post('/addUser', urlencodedParser, function (req, res) {
	// "name" : "mahesh",
	//   "password" : "password1",
	//   "profession" : "teacher",
	//   "id": 1
	console.log(req.body);
	var user = req.body;
	fs.readFile(userFile, function (err, data) {
		var users = JSON.parse(data);
		var newID = Object.keys(users).length + 1;
		user.id = newID
		users["user" + newID] = user;
		console.log(users);
		fs.writeFile(userFile, JSON.stringify(users, null, 4), function (err) {
			if (err) {
				console.log(err);
			}
		});
	});

});

// TODO: delete route with ID.
app.post('/deleteUser', urlencodedParser, function (req, res) {
	console.log(req.body);
	var id = req.body.id;
	fs.readFile(userFile, function (err, data) {
		var users = JSON.parse(data);
		if (id) {
			delete users["user" + id];
			res.end(JSON.stringify(users, null, 4));
		} else {
			console.log("No id found");
		}
		// delete users["user" + id];

	});
});

app.get("/get/:id", function (req, res) {
	fs.readFile(userFile, function (err, data) {
		var users = JSON.parse(data);
		var user = users["user" + req.params.id];
		console.log(user);
		res.end(JSON.stringify(user));
	});
});

app.post('/post_handler', urlencodedParser, function (req, res) {
	console.log(req.body);
});

app.get('/css/*', function (req, res) {
	var cssFile = __dirname + '/styles/' + req.path.substr(5);
	fs.readFile(cssFile, function (err, data) {
		if (err) {
			return console.log('Error Reading ' + cssFile);
		} else {
			res.end(data);
		}
	});
});

var server = app.listen(8081, function () {
	var host = server.address().address
	var port = server.address().port

	console.log("Example app listening at http://%s:%s", host, port);
});
