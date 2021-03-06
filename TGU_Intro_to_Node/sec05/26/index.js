// setTimeout(() => {
// 	console.log("setTimeout()");
//   }, 100);
  setTimeout(() => {
	console.log("setTimeout()");
  }, 0);
  
  setImmediate(() => {
	console.log("setImmediate()");
  });
  
  process.nextTick(() => {
	console.log("process.nextTick()");
  });
  
  Promise.resolve().then(() => {
	console.log("Promise.resolve().then()");
  });
  