var express  = require('express');
var app = express();
app.use(express.static(__dirname));
app.get("/", function(req,res){
    res.send("hello");
});
console.log("Visualizing the world on port 8000");
app.listen(process.env.port || 8000);
