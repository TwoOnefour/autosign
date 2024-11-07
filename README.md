# What's this
A program that will automatically sign up.

main_moniter.py is the main python file that responses for the main logics to sign up.

timeset.py is a crontab support python file, used to flush the crontab recording, to make sure everyone who access my miniprogram and fill the form can be included in crontab.

testapp1.js is a Nodejs script, creating a server process to receive the information from miniprogram and put them into mysql database.

Due to politics and rules, required by university, students should report their health situation every single day.

I think that is meaningless, unhelpful, troublesome.

Convenience should be make in order to study. First prime should be scholor, not rules.

So I make this in my first year in university, when I have been arrived at the university for two months.That is in Nov. 2020.

# How to use it

Just running the python script on your Linux server by 

<code>python ./main_moniter.py username password name area </code>

Crontab is useful.

<code>crontab -e</code>

<code>4 10 * * * python ./main_moniter.py username password name area </code>

You can also access my miniprogram named "测试获取code" in Wechat.Search it by name in Wechat, and you can see it.

![IMG_5216](https://user-images.githubusercontent.com/77989499/224929404-d1fe2716-c884-45de-9c9a-792dee1c6771.PNG)

Fill the form with your username, password, nickname, sign timing and area. My server will help you sign up in your setting time.

# 这是什么
这是一个武理自动打卡健康填报的程序，其中
main_moniter.py是python主程序，用来负责主要打卡逻辑

timeset.py是linux上设置crontab的python程序，由于我的服务器连接了小程序，可以定期运行timeset.py，负责将新加入的自动打卡人从数据库中提取，并放入crontab中自动打卡

testapp1.js是nodejs写的一个服务器端，用于接收处理小程序前端传输的数据和信息
# 如何使用
## 直接使用
<code>python ./main_moniter.py username password name area </code>

## linux上使用crontab实现自动化
<code>crontab -e</code>
<code>4 10 * * * python ./main_moniter.py username password name area </code>

:wq保存

# 闲话
由于学校政策，需要学生每日打卡

我不觉得每天打卡是一个有意义的事情

我是来学校学习知识的，不是来循规蹈矩的

所以我在进学校以后一直想做一个自动打卡的程序

最初的版本在进学校后第二个月写了出来,后来经过了大概四次版本更新，我总结一下

最初的版本是只用cookie来打卡，那个cookie是永久的，只要获取了那个cookie，直接post相应的api，就能实现签到，这是最简单的版本

第二个版本是设置了cookie的有效期，但是以前的cookie并没有失效

我在给别人新增加的时候发现cookie会失效，于是写了第二个版本，这个版本开始需要解绑与微信的绑定，从api模拟登录-填报-解绑三个过程，这个版本也是很简单的

使用获取到的没有绑定的cookie，然后登录，使用登录后cookie实现后面的逻辑就可以

直到第三个版本，时间很长，大概在2021到2022年学年，这个版本学校应该在更新数据库，数据非常乱，cookie能够返回很多学生的信息，这时候我的做法是暴力循环，直到填报成功

第四个版本，最魔鬼的版本，时间在2022年3月26日前后，更新以后，接口信息加密，绑定了微信的openId，我一直苦于没有思路，之后硬碰了一个星期五天左右，终于写出来了

当时因为openId没有做验证，只要随机生成一个没有绑定的openId，就可以绕过微信那边的验证，然后信息的加密使用了base64编码，很容易就解码了，于是第四个版本我在4月的时候做了出来，之前不想做
是因为要打法环全成就，打了一周多一点

![image](https://user-images.githubusercontent.com/77989499/224934550-516e1e56-bd19-47ae-868f-e7acc603975d.png)

这是我当时配套写的微信小程序，可以看到时间在四月七号前后 

再然后就一直稳定使用到疫情解放，不用健康打卡了，本项目也没有了意义，算是留个纪念


# TODO
- 后端接口校验
- 数据库套redis，redis可以存用户的code
- 消息队列可以削峰
- 后端接口加密，例如使用jwt
- 数据多了可以分表分库，甚至分多个mysql实例
