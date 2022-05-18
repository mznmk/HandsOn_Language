var http = require('http');

var data = "Hello World";
var url = "http://localhost:3000";
var options = {
  method: "POST",
  headers: {
   "Content-Type": "application/x-www-form-urlencoded",
   "Content_Length": Buffer.byteLength(data)
  }
}
var req = http.request(url, options, (res) => {
  res.pipe(process.stdout);
});
req.on("error", (err) => {
  console.log(err.message);
});
req.end(data);