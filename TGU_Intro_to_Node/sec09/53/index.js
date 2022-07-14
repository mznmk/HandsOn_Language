var fs = require("fs");
var path = require("path");

// fs.readFile(path.join(__dirname, "sample.txt"), "utf8", (err, data) => {
//   if (err) {
//     console.log(err.message);
//     return;
//   }

//   fs.writeFile(path.join(__dirname, "sample-copy.txt"), data, "utf8", (err) => {
//     if (err) {
//       console.log(err.message);
//       return;
//     }
//     console.log("OK");
//   });
// });

var util = require("util");
var readFile = util.promisify(fs.readFile);
var writeFile = util.promisify(fs.writeFile);

// readFile(path.join(__dirname, "sample.txt"), "utf8")
//   .then((data) => {
//      return writeFile(path.join(__dirname, "sample-copy.txt"), data, "utf8");
//   })
//   .then(() => {
//     console.log("OK");
//   })
//   .catch((err) => {
//     console.log(err.message);
//   });

(async function () {
  try {
    var data = await readFile(path.join(__dirname, "sample.txt"), "utf8");
    await writeFile(path.join(__dirname, "sample-copy.txt"), data, "utf8");
    console.log("OK");
  } catch (err) {
    console.log(err.message);
  }
})();