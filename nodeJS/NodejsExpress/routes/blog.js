var express = require('express');
var router = express.Router();
const monk = require('monk');
const { body, validationResult} = require('express-validator');

const url = 'localhost:27017/nodeBasic';
const db = monk(url);

router.get('/',function(req, res, next) {
    res.render('blog');
});
router.get('/add',function(req, res, next) {
    res.render('addblog');
});
router.post('/add',[
body("name","กรุณาป้อมชื่อบทความ").not().isEmpty(), 
body("description","กรุณาใส่เนื้อหาบทความ").not().isEmpty(), 
body("author","กรุณาระบุชื่อผู้แต่ง").not().isEmpty(), 
],
function(req, res, next) {
    const result = validationResult(req);
    var error = result.errors;
    if (!result.isEmpty()) {
      res.render('addblog',{errors:error});
    } else {
        var ct = db.get('blogs');
        ct.insert({
            name:req.body.name,
            description:req.body.description,
            author:req.body.author
        },function(err){
            if(err){
                res.send(err);
            }else{
                req.flash("error","บันทึกข้อมูลเรียบร้อยแล้ว");
                res.location('/blog/add');
                res.redirect('/blog/add');
            }
        });
    }
});


module.exports = router;