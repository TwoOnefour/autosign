var fs = require("fs");
var https = require('https');
var http = require('http');
var querystring = require('querystring');
var util = require('util');
var mysql  = require('mysql');
const url = require('url');
var express  = require('express');
const qs = require("querystring");
const request = require("request");
var app = express();
var exec = require('child_process').exec;
global.userinfo={
    openid:'',
    session_key:''
}
const httpsOption = {
    key : fs.readFileSync(""),
    cert: fs.readFileSync("")
}
//证书




var getopenId = function(js_code){
    var options = {

    host: 'api.weixin.qq.com',

    port: 80,

    path: '/sns/jscode2session?appid=&secret='+js_code+'=JSCODE&grant_type=authorization_code',

    method: 'GET',

    headers:{


        }

    }
    var getreq = https.request(options, function(res) {

        console.log("statusCode: ", res.statusCode);

        console.log("headers: ", res.headers);

        var data='';

        res.on('data', function(chunk){

            data += chunk;

        });

        res.on('end', function(){

            console.log("\n--->>\nresult:",data)

        });
    return data
    })

    return getreq;

}
//定义getopenId获得openId

app.post('/login', function(req, res) {

    var post = '';
    req.on('data', function (chunk) {
        post += chunk;
    })
    req.on('end', function () {
        global.res4=res

        post = JSON.parse(post.toString(''));
        global.post1={
            name:post.Name,
            sn:post.sn,
            idCard:post.idCard,
            area:post.area,
            time:post.time
        }
        var cmdStr = 'python main_moniter.py "'+post.Name+'" "'+post.sn+'" "'+post.idCard+'" "'+ post.area+'"';
        if(global.userinfo.openid!=''){
        var workerProcess=exec(cmdStr,function(err,stdout,stderr){
    if(err) {
        console.log('error:'+stderr);
        global.res4.end(stderr)
    }

        });
        workerProcess.stdout.on('data', function (stdout) {
                global.code=stdout.replace(/\r\n/g,"")
                global.code=global.code.replace(/\n/g,"");
                global.code=global.code.replace(/\s/g,"");
            console.log('stdout:',global.code,)
            {


        if(global.code=='code1'){
            console.log(global.code)
            global.res4.end('请去原填报小程序解绑')
        }
        else if(global.code=='code2'){
            console.log(global.code)
            global.res4.end('账号或密码有误')
        }
        else if(global.code=='code3'){
            global.res4.end('账号错误')
        }
        else{



            if(global.code=='code4'){
                console.log(global.code)
                        console.log(global.post1)
        //数据库添加
        var connection = mysql.createConnection({
            host     : 'localhost',
            user     : 'root',
            password : '',
            port: '3306',
            database: 'mydb2'
        })
        var addSql = 'INSERT INTO information(sn,idCard,area,time,name,openId) VALUES(?,?,?,?,?,?)';
        var addSqlParams = [global.post1.sn, global.post1.idCard, global.post1.area, global.post1.time, global.post1.name, global.userinfo.openid];
        connection.connect();
        connection.query(addSql, addSqlParams, function (err, result) {
            if (err) {
                if (err.code == 'ER_DUP_ENTRY') {
                    global.res4.end('已经绑定啦，请勿重复绑定')
                }
                console.log(err.message)
            }
            if (result != undefined) {
                global.res4.end('成功绑定，记得去原来的小程序解绑噢')
            }

            console.log('--------------------------INSERT----------------------------');
            //console.log('INSERT ID:',result.insertId);
            console.log('INSERT ID:', result);
            console.log('-----------------------------------------------------------------\n\n');
        });
            }


        connection.end();


        }
              }
        });

        workerProcess.stderr.on('data', function (data) {
            console.log('stderr: ' + data);
        });
        }
        else{
            global.res4.end('获得openid失败')
        }

    });
})

app.post('/getcode', function(req, res){
    var post = '';
  req.on('data', function(chunk){
        post += chunk;
})





    req.on('end', function () {
        post = JSON.parse(post.toString(''));
        global.res1=res
        console.log(post)
        var query = {
            appid: '',
            secret: '',
            js_code: post.code,
            grant_type: 'authorization_code',
        }
        var content = qs.stringify(query)


        var url='https://api.weixin.qq.com/sns/jscode2session?'+content
        const myFirstPromise = new Promise((resolve, reject) => {
            request(url, function (err, response, body) {

                body = JSON.parse(body.toString(''))
                global.userinfo.session_key = body.session_key
                global.userinfo.openid = body.openid
                console.log(global.userinfo)
                global.res1.write('成功登录')
                if(!!global.userinfo.openid){
                    res1.end()
                }

            })
        })





    })


});

app.post('/cencelbind', function(req, res){
    var post = '';
  req.on('data', function(chunk){
        post += chunk;
})





    req.on('end', function () {
        post = JSON.parse(post.toString(''));
        console.log('测试',global.userinfo.openid)
        var delSql = 'DELETE FROM information where openId="'+global.userinfo.openid+'"';
        global.res2=res
                var connection = mysql.createConnection({
            host     : 'localhost',
            user     : 'root',
            password : '',
            port: '3306',
            database: 'mydb2'
        })
        connection.connect();
        connection.query(delSql,function (err, result) {

            if(err){
                console.log(err.message)
                global.res2.end(err.message);

            }
            else if(result.affectedRows==' 1 '){
                global.res2.end('解绑自动填报成功')
                console.log('--------------------------DELETE----------------------------');
                console.log('DELETE affectedRows',result.affectedRows);
                console.log('-----------------------------------------------------------------\n\n');
            }
            else if(result.affectedRows==' 0 '){
                global.res2.end('已经解绑了，请勿重复点击')
            }
        })
        connection.end();

});





});
app.get('/', function(req, res){
    res.writeHead(200,{'Content-Type':"text/html"});
    fs.readFile(__dirname + "/index.html", "utf-8", function (error, data){undefined

    if(error)

        res.end("read html file error.");

    else

        res.end(data.toString());

});
})
https.createServer(httpsOption, app).listen(62000);
