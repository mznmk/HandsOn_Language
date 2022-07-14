const CustomReader = require("./customreader");
const CustomWriter = require("./customwriter");
var reader = new CustomReader();
var writer = new CustomWriter();

reader.pipe(writer);
reader.resume();