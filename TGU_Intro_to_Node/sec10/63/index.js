const { URL } = require("url");

const url = new URL("https://www.google.com");
console.log(url.protocol);
console.log(url.host);
