const express = require('express');
const app = express();

app.get('/',(req,res) => {
    res.send("hello world");
});

app.get('/about',(req,res)=>{
    res.send("About");
});

app.get('/users/:id',(req,res)=>{
    const { id } = req.params;

    res.send(`<h1>${id}</h1>`)
});


app.listen(3000);