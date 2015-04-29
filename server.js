var express  = require('express');
var app = express();
app.use(express.static(__dirname));
console.log("Visualizing the world on port 8000");
app.listen(process.env.PORT || 8000);
