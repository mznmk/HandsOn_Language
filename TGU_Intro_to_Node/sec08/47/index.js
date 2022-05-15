var EventEmitter = require("events");
var ee = new EventEmitter();

ee.on("event", () => {
	console.log("event 1st");
	console.log("event 2nd");
	console.log("event 3rd");
});
ee.emit("event");