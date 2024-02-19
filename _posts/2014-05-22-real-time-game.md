---
layout: post
title: RealTime multiplayer game with Node.js
feature-img: "assets/feats/real-time-game/Mosteroids.png"
thumbnail: "assets/feats/real-time-game/Mosteroids.png"
tags: [Archive, Code Code and Code]
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(165,42,42)

---


# Realtime Multiplayer Game with #Node.js
ก่อนอื่น ต้องทำความเข้าใจ node.js กันก่อน

node.js เสมือนเป็นภาษา javascript ที่ เพิ่มเติมด้วย asynchronous i/o library for file, socket and HTTP communication ซึ่งทำให้ node.js มีความสามารถเพียงพอที่จะทำให้ตัวเองเป็น web server
<!--more-->


<div style="font-size: 1.5em; font-weight: bold;">แต่</div>
ด้วยเหตุผลว่า javascript run single-threaded นั้นคือ ในครั้งหนึ่งๆ จะมีเพียงคำสั่งเดียวเท่านั้นที่จะสามารถรันได้ ดังนั้นจึงไม่สามารถจองให้คนใดคนหนึ่งได้ หากทำเช่นนั้น คนอื่นจะต้องรอ ซึ่งทำให้ ระบบโดยรวม ช้าลงมาก แต่เพื่อแก้ปัญหานี้ nodeJs จึงเกิดเป็น non blocking IO model , Continuation Passing Style and Event Loop กลายเป็นว่า เร็วฟุดๆ หากเรา implement ได้อย่างถูกวิธี

> #### What Makes Node.js Faster?
>   * [How the single threaded non blocking IO model works in Node.js](https://stackoverflow.com/questions/14795145/how-the-single-threaded-non-blocking-io-model-works-in-node-js)
>   * [What Makes Node.js Faster Than Java?](https://strongloop.com/strongblog/node-js-is-faster-than-java/)

เพื่อความตื่นเต้น ลองมาดู ตัวอย่างหนึ่งของ multiplayer web: [MMOsteroids](http://demos.seblee.me/MMOsteroids.html)

* TOC
{:toc}


## Get started
ในตัวอย่างนี้ เราจะแบ่ง code เป็น 2 ส่วน
* Server : จะเป็นตัวกลางในการสื่อการกับ client อื่นๆ
* Client : แสดงผลเกมส์

## Requirements

> #### Node.js
>   apt-get install nodejs

> #### NPM
>   apt-get install npm

> #### Socket.io
>   cd to/your/project
> 
>   npm install socket.io


##  Step 1. Setting up Server file

เริ่มด้วย การ setting node.js server ของเรา 
* สร้าง  server.js ซึ่งจะต้องทำการ include libery util และ socket.io 
* สร้างตัวแปรต่างๆที่จำเป็นต้องใช้ 
* สร้าง init function ซึ่งจะเป็น function ในการกำหนด ค่าต่างๆของ server และ เป็น bootstrap ของ server 
* จากนั้นเริ่ม implement ใน init function ทำการตั้งค่า port ที่จะเป็นช่องทางในการติดต่อและวิธีการเชื่อมต่อของ socket 
* และสุดท้ายคือ สั่งรัน init function

```js
// server.js
var util = require("util"), io = require("socket.io");
var socket,players;
function init() {
    players = [];
 
    /* setting socket.io ใช้ในการส่งข้อมูล*/
    socket = io.listen(8000);  /* setting port */  
    socket.configure(function() {
        socket.set("transports", ["websocket"]); 
        socket.set("log level", 2);
    });
};
 
init();  /* start our server */
```

ทดสอบโดยลองรันคำสั่ง

```bash
node server.js
```

หากทำการลงครบถ้วน สมบูรณ์ จะได้
```bash
info – socket.io started
```

## Step 2. Set Event Handlers for Socket.io
จากที่ทราบมาแล้วว่า node.js เป็น event-loop นั้นทำให้การ programming สำหรับ node.js จะต่างออกไปจากปกติ เรียกว่า **Event-driven programming** จะเป็นการกำหนดว่า เมื่อแต่ละ event เกิดขึ้น เราจะต้องตอบสนองยังไง? ซึ่ง main loop ของ node.js จะเป็นส่วนดักจับ event ต่างๆที่เกิดขึ้น [listens for events] เมื่อ event เกิดขึ้นจึงเรียก function ที่เรากำหนดไว้ เรียก function เหล่านี้ว่า **callback function**

* สร้าง function setEventHandlers เพื่อกำหนด callback ให้กับ event ต่างๆ 
* event แรก ที่กำหนดคือ เมื่อ มีการ connect มาที่ socket.io ซึ่งมันจะทำการสร้างตัวแปร client ขึ้นมา ซึ่งจะเป็นตัวที่ใช้ติดต่อกับ browser ของผู้เล่นแต่ละคน หลังจาก socket.io สร้างตัวแปร client ขึ้นมาแล้ว จะทำการเรียก callback `function onSocketConnection` พร้อมส่งตัวแปร client เป็น argument 
* ใน onSocketConnection จะต้องทำการตั้งค่า event 3 อย่างให้กับตัวแปร client

1. บอก client ว่า มีผู้เล่นตายไปแล้ว
2. บอก client ว่า มีผู้เล่นใหม่
3. บอก client ว่า มีผู้เล่นย้ายตำแหน่ง

```js
// server.js
function init() {
    /* ..... code จาก #1 ..... */
    setEventHandlers();
};
var setEventHandlers = function() {
    socket.sockets.on("connection", onSocketConnection);
};

function onSocketConnection(client) {
    util.log("New player has connected: "+client.id);
    client.on("disconnect", onClientDisconnect);
    client.on("new player", onNewPlayer);
    client.on("move player", onMovePlayer);
};

function onClientDisconnect() {
    util.log("Player has disconnected: "+this.id);
};

function onNewPlayer(data) {
   /* implement later*/
};

function onMovePlayer(data) {
   /* implement later*/
};

```

## Step 3. Create Player class on server
เราสามารถใช้ client ที่ socket.io สร้างมาแล้ว แต่ แต่ แต่ … แต่ละ browser [tab] จะเข้าถึงตัวแปร client ของตัวเองได้อย่างเดียว <span class="tag-en"><span class="tag-en">#กำ</span></span> จึงสร้าง Player class ขึ้นมาเอง เพื่อใช้แทน client อื่นๆ เอาไว้สื่อสารกัน โดยกำหนดให้ Player แต่ละ instance จะต้องผูก ด้วย id กับ client หนึ่งเสมอ!!

* สร้าง  Player.js และ setter-getter function ตามด้านล่างเบยยยย~

```js
// Player.js
var Player = function(startX, startY) {
    var x = startX,
        y = startY,
        id;
    
    var getX = function() {
        return x;
    };
 
    var getY = function() {
        return y;
    };
 
    var setX = function(newX) {
        x = newX;
    };
 
    var setY = function(newY) {
        y = newY;
    };
 
    return {
        getX: getX,
        getY: getY,
        setX: setX,
        setY: setY,
        id: id
    }
};
 
/* export เพื่อให้ file อื่นสามารถใช้ได้ */
exports.Player = Player;
 
```

## Step 4. Implement “onNewPlayer” event
หลังจากเราสร้าง Player class ก็ต้องกลับมาผูกแต่ละ Player กับตัวแปร client ซึ่งสามารถทำได้ขณะที่เกิด event **new player** มาที่ server เนืองจาก browser ส่งมา ซึ่งจะส่งมาหลังจาก connection กับ server เรียบร้อยแล้ว

* include class Player 
* สร้าง Player instance ใน function onNewPlayer 
* ส่งไปบอก browser ของเครื่องอื่นๆ ว่ามี new player 
* ส่งไปบอก browser ของเครื่องตัวเองให้สร้าง player คนอื่นๆที่มีอยู่แล้ว 
* เก็บ Player instance เข้า players

```js
// server.js
/* ... code ก่อนๆ ... */
var Player = require("./Player").Player;
 
function onNewPlayer(data) {
    var newPlayer = new Player(data.x, data.y);
    newPlayer.id = this.id;
    this.broadcast.emit("new player", { id: newPlayer.id, 
                                         x: newPlayer.getX(), 
                                         y: newPlayer.getY() }); 
    var i, existingPlayer;
    for (i = 0; i < players.length; i++) {
        existingPlayer = players[i];
        this.emit("new player", {id: existingPlayer.id, 
                                  x: existingPlayer.getX(), 
                                  y: existingPlayer.getY()});
    };
    players.push(newPlayer);
};
 
```

## Step 5. Let’s be a Client
ทั้งหมดที่ผ่านมา คือการเตรียม server ซึ่งจะใช้เป็นตัวช่วยในการติดต่อกันระหว่างผู้เล่น ต่อมาเราจึงหันมา implement ฝั่ง client บ้าง แต่เราจะข้ามรายละเอียดของวิธีการสร้าง แต่เราจะมาทำให้มันเป็น multiplayer กัลลลลล ลล ล ล ~

* download single player game [[DWL](https://www.dropbox.com/s/okxrlq7nln38r8g/game-demo.rar)] 
* unzip ออกมาจะเห็น copy ให้อยู่ที่เดียวกับ server.js และ Player.js 
* ลอง open **index.html** จะเห็น จุดดำๆ วิ่งไปมาได้ โดยใช้ปุ่มลูกศร เหมือนรูปด้านล่าง


<div style="text-align: center;border: 1px solid #c7c7c7;margin-bottom: 20px;">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Vr-T42wGPVCEYcp4rVzQbEyEKXpLj2Q3" column=1 %}
</div>

ก่อนจะเริ่ม Implement จะมาแนะนำไฟล์ต่างๆให้รู้จักกันก่อน

* `index.html` : เป็นหน้าที่เริ่มต้นรันเกมส์
* `js/game.js` : เป็น js ควบคุมการดำเนินไปของเกมส์ เช่น รับ input , แสดงผลลัพย์ต่างๆ
* `js/Player.js` : class ตัวแทนของผู้เล่นคนอื่นๆ

เริ่มต้นด้วย include socket.io ให้กับ ฝั่งผู้เล่น โดยแก้ไข `index.html`

```html
<!-- index.html -->
<span style="color: slategray"> &lt;!-- other --&gt; </span>
&lt;canvas id="gameCanvas"&gt;&lt;/canvas&gt;

<span style="color:rgb(253, 215, 14)">
&lt;!-- add this line --&gt;
&lt;script src="http://localhost:8000/socket.io/socket.io.js"&gt;
&lt;/script&gt;
&lt;!-- add this line --&gt;
</span>
&lt;script src="js/requestAnimationFrame.js"&gt;&lt;/script&gt;
&lt;script src="js/Keys.js"&gt;&lt;/script&gt;
<span  style="color: slategray"> &lt;!-- other --&gt; </span>
 
```

ต่อมา เราจะมาแก้ไขไฟล์ game.js เพื่อให้รองรับ #multiplayer โดย 
* สร้างตัวแปร socket เพื่อใช้ในการติดต่อกับ server และตัวแปร remotePlayers เพื่อเก็บ Player instance ของผู้เล่นคนอื่นๆ 
* ติดต่อกับ server 
* สร้าง callback สำหรับ event ที่จะเกิดขึ้นเช่นเดียวกับ server แต่เป็นมุมมองของผู้เล่น

```js
// js/game.js
function init() {
    /*  other code */
    /*  ............ */
 
    /*  add this */
    // socket connect
    socket = io.connect("http://localhost", {port: 8000, transports: ["websocket"]});
 
    // Initial remote players
    remotePlayers = [];
    setEventHandlers();
};
 
var setEventHandlers = function() {
   /*  other code */
   /*  ............ */
 
    /* add this*/
    socket.on("connect", onSocketConnected);
    socket.on("disconnect", onSocketDisconnect);
    socket.on("new player", onNewPlayer);
    socket.on("move player", onMovePlayer);
    socket.on("remove player", onRemovePlayer);
};
 
function onSocketConnected() {
    console.log("Connected to socket server");
};
 
function onSocketDisconnect() {
    console.log("Disconnected from socket server");
};
 
function onNewPlayer(data) {
    console.log("New player connected: "+data.id);
};
 
function onMovePlayer(data) {
    /* implement later */
};
 
function onRemovePlayer(data) {
   /* implement later*/
};
 
```

หากพยายามจนมาถึงขั้นนี้ เช็คควสามถูกต้องโดยพิมพ์ `node server.js` เพื่อ รัน server

หาเป็นไปอย่างถูกต้องแล้ว จะเห็นข้อความในกล่องด้านล่าง ใน javascript console
[[ หาใช้ chrome กด ctrl+shift+J ]]

```
Connected to socket server
```

ปล.ทั้งหมดนี้แค่เพื่อ connect กับ server คงหวังว่าจะเห็น multiplayer แล้วซินะ <span class="tag-en"><span class="tag-en">#ยังไม่เสร็จขอรับ</span></span>

## Step 6. Display another Player
หลังจาก connection เรียบร้อยแล้ว ต่อไปคือการแสดงผลผู้เล่นคนอื่นๆในฝั่ง client นั้นหมายความว่าเราต้องทำการแก้ไขไฟล์ public/js/Player.js

* ใส่ส่วนของตัวแปร id ลงไปเพื่อใช่ระบุตัวตนของผู้เล่น 
* สร้าง getter-setter function เหมือนในส่วน server

```js
// js/Player.js
var Player = function(startX, startY) {
  /* other code*/
  /* ............*/
 
  var id;
 
  // Getters and setters function
  var getX = function() {
    return x;
  };
 
  var getY = function() {
    return y;
  };
 
  var setX = function(newX) {
    x = newX;
  };
 
  var setY = function(newY) {
    y = newY;
  };
 
  /* edit this */
  return {
    getX: getX,
    getY: getY,
    setX: setX,
    setY: setY,
    update: update,
    draw: draw
  }
 
};

```

แต่แค่นี้ยังไม่พอสำหรับการแสดงผลผู้เล่น สิ่งต่อไปคือ กลับไปแก้ไขไฟล์ game.js 
* ส่งข้อมูลใน browser ของเครื่องตัวเอง ไปให้ผู้เล่นอื่นแสดง 
* รับข้อมูลจาก broeser ของเครื่องผู้เล่นอื่น 
* วาด

```js
// js/game.js
/* ............*/
/* other code */
function onSocketConnected() {
  console.log("Connected to socket server");
 
  //ส่งข้อมูลในเครื่องเราไปให้ผู้เล่นอื่น
  socket.emit("new player", {x: localPlayer.getX(), y: localPlayer.getY()});
};
 
function onNewPlayer(data) {
  console.log("New player connected: "+data.id);
 
  // Initialise the new player
  var newPlayer = new Player(data.x, data.y);
  newPlayer.id = data.id;
 
  remotePlayers.push(newPlayer);
};
 
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  localPlayer.draw(ctx);
 
  /* edit this */
  // Draw the remote players
  for (ver i = 0; i < remotePlayers.length; i++) {
    remotePlayers[i].draw(ctx);
  };
  /* edit this */
};
 
/*other code*/
```

## Step 7. Update it!!
ใกล้ถึงความจริงแล้ว หากลองรันตอนนี้จะเห็นว่า ทุกครั้ง refresh จะเกิดจุดใหม่ โดยของเก่าไม่หายไป และที่สำคัญคือ จุดอื่นๆไม่เลื่อน เพราะยังไม่ทำการส่ง **update** นั้นเอง

แต่แน่นอนว่าครั้งนี้จะเป็นการแก้ไขทั้ง ฝั่งผู้ใช้ และ ฝั่งเซิฟเวอร์

#### ฝั่งผู้ใช้
* สร้าง function playerById เพื่อ ใช้ในการหาผู้ใช้คนอื่น จาก Id 
* ลบผุ้เล่นคนอื่นเมื่อเกิด event remove player แต่ไม่จำเป็นต้องส่งไปบอกฝั่งเซิฟเวอร์ขณะ disconnect !! 
* ส่งข้อมูลตำแหน่งปัจจุบันไปยังเซิฟเวอร์ 
* เปลี่ยนตำแหน่งของจุด เมื่อเกิด event move player

```js
// js/game.js
/*..........*/
/* other code*/
 
/* add this */
function playerById(id) {
  for (ver i = 0; i &lt; remotePlayers.length; i++) {
    if (remotePlayers[i].id == id)
      return remotePlayers[i];
  };
 
  return false;
};
 
// Remove player
function onRemovePlayer(data) {
  var removePlayer = playerById(data.id);
  if (!removePlayer) {
    console.log("Player not found: "+data.id);
    return;
  };
 
  remotePlayers.splice(remotePlayers.indexOf(removePlayer), 1);
};
 
 
// Move player
function onMovePlayer(data) {
  var movePlayer = playerById(data.id);
  if (!movePlayer) {
    console.log("Player not found: "+data.id);
    return;
  };
 
  movePlayer.setX(data.x);
  movePlayer.setY(data.y);
};
 
/* edit this*/
function update() {
  if (localPlayer.update(keys)) {
    // ส่งข้อมูลไปบอก server 
    socket.emit("move player", {x: localPlayer.getX(), y: localPlayer.getY()});
  };
};
 
```

#### ฝั่งเซิฟเวอร์
สำหรับฝั่งเซิฟเวอร์ จะมีการแก้ไขที่ไม่ต่างกัน นั้นคือ 
* สร้าง function playerById 
* ลบผุ้เล่นคนอื่นเมื่อเกิด disconnect และส่งต่อให้ผู้เล่นคืนอื่นด้วย evnet remove player 
* สุดท้าย คือ หากข้อมูลจากผู้เล่นคนใดมีการเปลี่ยนแปลงจะทำการส่งข้อมูลต่อไปให้ผู้เล่นคนอื่นๆ
* **เสร็จสมบูรณ์***

```js
// server.js
/* other code*/
 
/* add this*/
function playerById(id) {
  var i;
  for (i = 0; i &lt; players.length; i++) {
    if (players[i].id == id)
      return players[i];
  };
 
  return false;
};
 
function onClientDisconnect() {
  util.log("Player has disconnected: "+this.id);
 
  var removePlayer = playerById(this.id);
  if (!removePlayer) {
    util.log("Player not found: "+this.id);
    return;
  };
 
  players.splice(players.indexOf(removePlayer), 1);
  this.broadcast.emit("remove player", {id: this.id});
};
 
 
function onMovePlayer(data) {
  var movePlayer = playerById(this.id);
  if (!movePlayer) {
    util.log("Player not found: "+this.id);
    return;
  };
 
  movePlayer.setX(data.x);
  movePlayer.setY(data.y);
 
  this.broadcast.emit("move player", {id: movePlayer.id, x: movePlayer.getX(), y: movePlayer.getY()});
};
 
```

{% include aligner.html images="https://lh3.googleusercontent.com/d/1kp7Ees62FoGJZhlqPfn4oAyasR13uoTb" column=1 %}


[ดูโค้ดฉบับเต็ม](https://github.com/robhawkes/mozilla-festival)

## เครดิต
* [CREATING A REAL-TIME MULTIPLAYER GAME WITH WEBSOCKETS AND NODE.JS](http://rawkes.com/articles/creating-a-real-time-multiplayer-game-with-websockets-and-node.html)