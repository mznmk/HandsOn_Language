setTimeout(() => {
  console.log("setTimeout()");
}, 1000);

console.log("global");

var end = (new Date()).getTime() + 5000;
while ((new Date()).getTime() < end) {
}