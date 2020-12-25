---
layout: post
title: What different between Object, Instance and Class
tags: [Archive, Code Code and Code]
thumbnail: "assets/img/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(165,42,42)

---


มันเป็นเรื่องยากมากที่จะบอกความแตกต่าง หากไม่เคยลองมา implement เอง

<!--more-->

# [O]bject [O]riented [P]rogramming

The basic concept of OOP : Class >> Object >> Instance.

### Class
is Blueprint / Template ซึ่งจะระบุถึง #stages (field), #behavior (method) และ #constructor อะไรบ้าง? ซึ่งบางภาษาอาจจะมี class variable หรือ static method ซึ่งจะเป็นตัวแปลที่อยู่กับคลาส อาจจะใช้นับจำนวน instance หรือระบุเอกลักษ์บางอย่างของ class ซึ่งทุกๆ instance เหมือนกันหมด

### Object
is a Copy of the class ซึ่งจะถูกสร้างขึ้นใน memory เมื่อทำการ new ขึ้นมา เสมือนการนำ blueprint ไปสร้างมาเป็น วัตถุจริงๆ

### Instance
is a Reference variable ซึ่งจะอ้างอิงไปถึง address ของ Object ใน memory 


<div class="blockquote">
A blueprint for a house design is like a class description. All the houses built from that blueprint are objects of that class. A given house is an instance. -- Joe Snyder[1]
</div>

## Example


<div style="padding:10px; border: 1px solid grey; margin-bottom:20px">
From <span style="color:red;font-weight: bold;">Class A </span> has  
<span style="color:#0FECE3;font-weight: bold;">Object1</span> , <span style="color:#0E6986;font-weight: bold;">Object2</span> and <span style="color:#2807AF;font-weight: bold;">Object3</span>
</div>

<span style="color:#0FECE3;font-weight: bold;">Object1</span>จะมีค่าทุกอย่างเหมือน <span style="color:#0E6986;font-weight: bold;">Object2</span>  และ <span style="color:#2807AF;font-weight: bold;">Object3</span> แต่อยู่คนละที่ใน Memory



<div style="padding:10px; border: 1px solid grey; margin-bottom:20px">
From <span style="color:#0FECE3;font-weight: bold;">Object1 </span> has
<span style="color:#0F0CE0;font-weight: bold;">obj1_Instance1</span> <span style="color:#0E0980;font-weight: bold;">obj1_Instace2</span> and <span style="color:#2807A0;font-weight: bold;">obj1_Instance3</span>
</div>


ทุกๆ instance มีค่าเหมือนกัน ชี้ที่เดียวกันใน Memory หากมีการเปลี่ยนแปลงที่ <span style="color:#0FECE3;font-weight: bold;">Object1 </span> ก็จะเปลี่ยนเหมือนกันทุกตัว

## Declaration Type of Instance

```js
Person john; john = new Person();
```

เราอาจจะอธิบายโค้ดนี้ด้วยการบอกว่า "สร้าง john เป็นตัวแปร type Person แล้ว สร้าง object แล้วให้ john เป็น instance ชี้ไปยัง address ของ object ที่สร้างขึ้น"

แต่จริงๆแล้วก่อนสร้าง instance ตัวแปร john ก็ไม่ต่างจากตัวแปร type Animal, World หรือ ชื่อของ Class อื่นๆ เพราะว่า สุดท้ายแล้วมันก็แค่ pointer ชี้ไปยัง address ของ object แต่อย่างไรก็ตาม การประกาศ type เป็นการช่วยในการจัดการข้อมูล ซึ่งเป็นหน้าที่หนึ่งที่ complier ช่วยทำให้ เช่น จะเกิด error หากเราพยายาม assign address ของ class Animal ไปใส่ใน instance type Table.



<div class="blockquote">
If you want to become a good developer, its important to understand that no computer environment ever works based on philosophic ideals.
</div>




## Credit
* [1] [Difference between object and instance](https://stackoverflow.com/questions/3323330/difference-between-object-and-instance)
* [Class vs Object vs Instance](https://alfredjava.wordpress.com/2008/07/08/class-vs-object-vs-instance)

Lastest edit: 2020-12-18