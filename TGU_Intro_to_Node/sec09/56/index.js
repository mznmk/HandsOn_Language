var path = require("path");
var fs = require("fs");

// var writer = fs.createWriteStream(path.join(__dirname, "created.txt"), "utf8");
// writer.end("Hello World !");

var reader = fs.createReadStream(path.join(__dirname, "sample.txt"), "utf8");
var writer = fs.createWriteStream(path.join(__dirname, "sample-copy.txt"), "utf8");
reader.pipe(writer);
reader.resume();
