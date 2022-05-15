var path = require("path");

var filepath = "/projects/sec09/50/index.html";
console.log(path.dirname(filepath));
console.log(path.basename(filepath));
console.log(path.extname(filepath));

console.log(path.join("/projects/sec09/50/", "index.html"));

console.log(path.normalize("/projects/sec09/50/lib/../index.html"));