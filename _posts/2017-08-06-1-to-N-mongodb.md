---
layout: post
title: 1-N Relations with MongoDB
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/1-to-N-mongodb/20150225relationaldatabase.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(83 171 222)
---

## TL;DR
หลังจากที่รู้จัก MongoDB กันไปแล้ว ก็เข้ามาสู่คำถาม  "ฉันจะเก็บข้อมูลลงใน MongoDB ยังไง?"

<!--more-->

{% include aligner.html images="https://lh3.googleusercontent.com/d/1nFcTLCqJIh4VdDPXnzHTNTbKz34svmR_" column=1 %}

อาทิตย์ที่แล้ว /me เขียนแนะนำ MongoDB ไปเป็นที่เรียบร้อยแล้ว ใน [MongoDB is comming](https://chameleontk.github.io/mongo) พูดไปจนถึงข้อดี/ข้อเสีย และตัวอย่างงานที่เหมาะ/ไม่เหมาะกับเจ้า MongoDB

สำหรับตอนนี้เป็นบทต่อเนื่องหลังจากที่รู้จัก MongoDB กันไปแล้ว ก็เข้ามาสู่คำถามสำคัญยิ่งขึ้น

# Table of content
* TOC
{:toc}

# How do I model my database on MongoDB?
ความแตกต่างสำคัญสำหรับการออกแบบโครงสร้างข้อมูลใน MySQL และ MongoDB คือ flattened ของข้อมูล

สำหรับข้อมูลใน Relational DB อย่างใน MySQL เราสามารถออกแบบให้มีความสัมพันธ์ระหว่างตารางได้อย่างซับซ้อน

{% include aligner.html images="https://lh3.googleusercontent.com/d/1vm4oJetnPnC1hIArVoDvhhpZo7S5u4q-" column=1 %}

ในทางกลับกัน สำหรับ MongoDB มักออกแบบให้แต่ละข้อมูลมีความสัมพันธ์กันแบบแบนๆ ไม่ซับซ้อน หรือเรียกว่า "flattened" ดังนั้นการออกแบบโครงสร้างข้อมูลใน MongoDB จึงต้องมีมุมมองที่แตกต่างจากการคิดแบบ Relational DB

# It is not relational thinking

เมื่อพูดถึงข้อมูล รูปแบบที่ขาดไม่ได้คือ ข้อมูลประเภท 1-N (ข้อมูล A 1 ก้อนมีความสัมพันธ์กับข้อมูล B หลายๆก้อน)

หากมองแบบ MySQL สิ่งแรกที่ DB admin ถาม มักจะเป็น

<div class="blockquote">How are your data related to each other?</div>

"ข้อมูลพวกนี้สัมพันธ์กันอย่างไร?" เมื่อเห็นความสัมพันธ์แล้ว DB admin ทุกคนก็คงจะสามารถคิดได้ทันทีว่าต้องใช้ primary key/foriegn key แบบไหน เชื่องโยงกับประเภทของความสัมพันธ์แบบใด

แต่สำหรับ MongoDB ซึ่งไม่มีรูปแบบตายตัวในการออกแบบ ไม่มี join ไม่มี trigger ไม่มี transactional การคิดแบบ Document Oriented จึงเริ่มจากคำถามต่างออกไป

<div class="blockquote">what is the cardinality of the relationship?</div>

"มีปริมาณข้อมูลที่สัมพันธ์กันเยอะแค่ไหน?" ซึ่งคำตอบต้องการ คือ

* one-to-few
* one-to-many
* one-to-squillions

สำหรับ MongoDB ถึงแม้ว่า จะเป็น 1-N relationship เหมือนกัน แต่ไม่ได้หมายความว่าจะต้องออกแบบเหมือนกัน

# Embedding with 1-to-few

ความสัมพันธ์ user/address ผู้ใช้ 1 คน มีข้อมูลที่อยู่ได้หลายที่ หรือ user/bank_account ผู้ใช้ 1 คน มีข้อมูลบัญชีธนาคารได้หลายบัญชี ตัวอย่างพวกนี้เป็นตัวอย่างความสัมพันธ์แบบ "one-to-few" ข้อมูล 1 ชิ้น มีความสัมพันธ์กับข้อมูลอีกประเภทแค่เพียงไม่กี่ชิ้น การออกแบบที่เหมาะสำหรับข้อมูลในลักษณะนี้ คือ Embedding หรือ การฝังข้อมูลไปในก้อนหลักเลย เช่น

```
db.user.findOne()
````

```js
{
    name: "Pakawat Nakwijit", 
    first_name: "Pakawat",
    last_name: "Nakwijit",
    addresses : [
        { street: "Sukumvit", city: "Bangkok", country: "Thailand" },
        { street: "Thepkasattri", city: "Phuket", country: "Thailand" }
    ]
}
```

Embedding เป็นวิธีที่ง่ายที่สุดสำหรับการเก็บข้อมูลที่สัมพันธ์กัน เพราะ Document Oriented Database เปิดให้สามารถบันทึกข้อมูลที่มีโครงสร้างแบบไหนก็ได้ แม้กระทั้ง Array หรือ Dictionary

จุดเด่นที่สำคัญที่สุด ไม่ใช่แค่ง่าย แต่มันทำให้เราสามารถดึงข้อมูลที่เกี่ยวข้องต่างๆได้โดยใช้ 1 query แลกมาด้วยข้อเสียที่สำคัญ คือ ไม่สามารถเข้าถึงข้อมูลทั้งสองด้านแบบ stand-alone entities ได้

ดังนั้น หากจำเป็นต้องมีการแสดงรายการบัญชีของลูกค้าทั้งหมด หรือ แสดงที่อยู่ของลูกค้าทุกคน การใช้ Embedding จะไม่ใช่ทางออกที่ดี ถึงแม้ว่าจะเป็น "one-to-few" ก็ตาม

<div class="blockquote">Just because you can embed a document, doesn’t mean you should embed a document.</div>

"ข้อมูลเท่าไรจึงจะไม่ใช่ few" แน่นอนว่ามันไม่มีนิยามตายตัว แต่การพยายามดื้อใช้ Embedding กับปริมาณข้อมูลมากๆ จะเป็นส่วนสำคัญที่ทำให้ DB ล่มได้ง่ายๆ เพราะขนาดข้อมูลในแต่ละ document มีผลกระทบสำคัญมากๆกับ write performance และ data fragmentation ใน MongoDB

PS: Documents in MongoDB must be smaller than [the maximum BSON document size](https://docs.mongodb.com/manual/reference/limits/#BSON-Document-Size).

# 1-to-many and child-referencing

สำหรับข้อมูลที่มีจำนวนมากขึ้น แทนที่จะฝังข้อมูลไปตรงๆ เราสามารถเลือกบันทึกเฉพาะ ObjectIDs เพื่ออ้างอิง เรียกวิธีการแบบนี้ว่า "Child-referencing" ตัวอย่างง่ายๆที่ชัดเจน เช่น

ความสัมพันธ์ user-task ผู้ใช้ 1 คน มีข้อมูลงานที่ต้องรับผิดชอบหลายงาน และแน่นอนว่า มันไม่จำกัดแค่ 1-2 ชิ้น บางคนอาจจะมีได้มากขึ้น 100+ ชิ้น

```
db.user.findOne()
````

```js
{
  
    _id: ObjectID('ImTK'),  
    name: "Pakawat Nakwijit",  
    first_name: "Pakawat",  
    last_name: "Nakwijit",  
    tasks : [
        ObjectID('A001'),
        ObjectID('A002'),
        ObjectID('A005'),
    ]  
}
```


```
db.tasks.find()
````

```js
[  
      { _id: ObjectID('A001'), name: "Task1"},
      { _id: ObjectID('A002'), name: "Task2"},
      { _id: ObjectID('A003'), name: "Task3"},
      { _id: ObjectID('A004'), name: "Task4"},
      { _id: ObjectID('A005'), name: "Task5"},
]
```

รูปแบบลักษณะนี้ แยกข้อมูลทั้ง 2 ประเภทออกจากกันทำให้เราสามารถดึงข้อมูลทั้งคู่ได้อย่างอิสระต่อกัน ก้าวข้ามข้อเสียที่เกิดขึ้นใน Embedding แต่ก็มาพร้อมกับข้อเสียสำคัญ คือ

เราจำเป็นต้อง query มากกว่า 1 ครั้งเพื่อดึงข้อมูลที่ต้องการทั้งหมด หาต้องการข้อมูลที่มีความซับซ้อน ยิ่งจำเป็นต้องสร้าง **application-level join** เมื่อเชื่อมโยงข้อมูลจากทั้ง 2 collections เข้าด้วยกัน

แต่ข้อดีอีกข้อที่ไม่ได้พูดถึง คือ รูปแบบนี้ เป็นรูปแบบที่ง่ายที่สุดสำหรับการสร้าง N-to-N schema โดยไม่ใช่ join

```
db.tasks.find()
````

```js
[  
      { _id: ObjectID('A001'), name: "Task1", "responsibility_by": [ObjectID('ImTK'), ObjectID('KpTH')]},
      { _id: ObjectID('A002'), name: "Task2", "responsibility_by": [ObjectID('KpTH')]},
      { _id: ObjectID('A003'), name: "Task3", "responsibility_by": []},
      { _id: ObjectID('A004'), name: "Task4", "responsibility_by": [ObjectID('KpTH')]},
      { _id: ObjectID('A005'), name: "Task5", "responsibility_by": [ObjectID('ImTK')]},
]
```

# Parent-referencing over squillion records

เมื่อข้อมูลมีมากขึ้น ขนาดของ array ก็ใหญ่ขึ้น แน่นอนว่า ไม่สามารถใช้วิธีที่การเดิมๆได้อีกต่อไป วิธีการสุดท้ายที่สามารถทำได้ อ้างอิงทุกอย่างโดยใช้ key เฉกเช่นเดียวกับ Relational DB

ตัวอย่างข้อมูลประเภทนี้ คือ logging system ซึ่งแน่นอนว่าต้องมีปริมาณที่เพิ่มขึ้นเรื่อยๆ ไม่มีขีดจำกัดที่แน่นอน

```
db.user.findOne()
````

```js
{  
    _id: ObjectID('ImTK'),
    name: "Pakawat Nakwijit"
}
```

```
db.logs.find()
````

```js
[
    { time: ISODate("2014-03-28T09:42:41.382Z"), message: "login", user: ObjectID('ImTK')},
    { time: ISODate("2014-03-28T09:41:12.435Z"), message: "login", user: ObjectID('KpTH')},
    { time: ISODate("2014-03-28T09:40:09.214Z"), message: "loout", user: ObjectID('ImTK')},
    { time: ISODate("2014-03-28T09:40:48.423Z"), message: "login", user: ObjectID('ImTK')},
]
```



# Conclusion

เมื่อพิจารณาที่จะเก็บข้อมูลลงใน MongoDB จำเป็นต้องเปลี่ยนมุมมองการออกแบบไปจากเดิม เริ่มต้นดูข้อมูลแล้วตั้งคำถาม 2 ข้อ

* What is the cardinality of the relationship: is it one-to-few; one-to-many; or one-to-squillions?
* Will the entities on the “N” side of the One-to-N ever need to stand alone?

หรือ

* มีข้อมูลที่สัมพันธ์เยอะแค่ไหน?
* จำเป็นต้องดึงข้อมูลทั้ง 2 อิสระต่อกันหรือไม่?

แล้วนำคำตอบพวกนี้มาเลือกรูปแบบที่ต้องการ Embedding, Child-referencing และ Parent-referencing

สำหรับใครที่ไม่คุ้นเคยกับข้อมูล /me ขอสรุป โดยใช้ Rules of Thumb จาก [6 Rules of Thumb for MongoDB Schema Design](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1) ดังนี้

1. เลือก Embedding เสมอ ยกเว้นจะมีเหตุผลที่คิดว่าไม่เหมาะสม
2. ถ้าต้องการเข้าถึงข้อมูลโดยตรง (อิสระกับข้อมูลอื่น) เป็นเหตุผลที่เหมาะสมที่จะไม่เลือกใช้ Embedding
3. ข้อมูลที่อยู่ใน array ต้องมีขนาดจำกัด (ใน Embedding และ Child-referencing) ถ้ามีมากกว่า 100 ชิ้น ให้หยุดคิดที่จะใช้ Embedding และ ถ้ามากกว่า 1,000 เลือกใช้ Parent-referencing เถอะ
4. Application-level joins ไม่น่ากลัว ถ้าทำ index และเลือกวิธี query อย่างถูกต้อง การ join แบบนี้ก็สามารถมีประสิทธิภาพทัดเทียมกับ server-side joins ใน Relational DBs.

นี้เป็นแค่ Basic Design ยังมีเทคนิคที่น่าสนใจอีก 2 ตัว คือ Two-way referencing และ Denormalization ที่จะมาช่วยเค่นประสิทธิภาพให้กับ MongoDB และ Rules of Thumb ข้อที่ 5 และ 6

ติดตามอ่านต่อได้ที่ [Two-way referencing & Denormalization Concept](https://chameleontk.github.io/1-to-N-mongodb#)

# Credit/Reference

[Why You Should Never Use MongoDB](http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/)

[6 Rules of Thumb for MongoDB Schema Design](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1)

[Thinking in Documents](http://embed.vidyard.com/share/mz2CPEZZHErlqxUmGHAhCg)

