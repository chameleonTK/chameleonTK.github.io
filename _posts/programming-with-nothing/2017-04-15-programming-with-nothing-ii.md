---
layout: post
title: "Programming with Nothing : Numbers"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/feats/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

เป็นไปได้ไหมที่สร้างตัวเลขขึ้นมาโดยใช้แค่ความสามารถของฟังก์ชั่น? แล้วตัวเลขมันคืออะไรกันแน่? 
<!--more-->

# Numbers

<div class="blockquote">
Numbers is the most fundemantal thing for human being.
</div>

เพราะตัวเลขคือจุดเริ่มต้นของการคำนวน ดังนั้นปัญหาแรกของเรา คือ เป็นไปได้ไหมที่สร้างตัวเลขขึ้นมาโดยใช้แค่ความสามารถของฟังก์ชั่น?

ดังนั้น ก่อนที่ /me จะเริ่มต้นสร้างสิ่งที่เรียกว่า "ตัวเลข" เรามาทำความเข้าใจความหมายของสิ่งที่เรากำลังจะสร้างขึ้นมาก่อน

# What is number?

{% include aligner.html images="https://lh3.googleusercontent.com/d/18p3E5OzInFyzWnAvxbIn5LY03FL-zZl2" column=1 %}

มันเป็นเรื่องยากในการนิยามคำว่า "ตัวเลข" บางคนบอกว่า "ตัวเลขคือสิ่งที่ใช้อธิบายจำนวนของสิ่งของ" แต่ดูเหมือนว่า คำนิยามนี้สร้างคำถามที่ย้อนให้เกิดคำถามต่อไปอีกว่า "จำนวนคืออะไร?" ดูเหมือนว่ามันแค่เป็นการเล่นคำเพื่ออธิบายคำว่า "ตัวเลข" เท่านั้นเอง คล้ายกับการนิยามคำในพจนานุกรม "ขาว คือ สีที่ตรงข้ามกับดำ, ดำ คือ สีที่ตรงข้ามกับขาว"?

เมื่อพูดถึงตัวเลขแล้ว ตัวเลขมีหลายประเภท สำหรับตัวเลขที่เราใช้ในโค้ดนี้ คือ Natural numbers หรือ จำนวนนับ(Counting numbers) ซึ่งเป็นกลุ่มตัวเลขประเภทแรกๆที่เกิดขึ้นในอารยธรรมมนุษย์เพื่อใช้ในการนับสิ่งของต่างๆ หนึ่ง, สอง, สาม, ...

"การนับ" จึงเป็นคีย์สำคัญในการนิยามจำนวน ลองจินตนาการว่า ถ้าเรามีถุงใส่แอ๊ปเปิ้ลและส้ม อยู่จำนวนหนึ่ง ถ้าทุกครั้งที่เราหยิบแอ๊ปเปิ้ลออกจากถุง เราจะต้องหยิบส้มออกจากถุงด้วยเหมือนกัน เราสามารถดำเนินการแบบนี้ไปได้เรื่อยๆจนกว่าแอ๊ปเปิ้ล หรือส้ม อันใดอันหนึ่งหมดจากถุง

ในกรณีที่ ถ้าทั้งแอ๊ปเปิ้ล และส้ม หมดพร้อมๆกัน ทำให้เรารู้ว่าทั้งสองมีจำนวนเท่ากัน หรือ ถ้ามีส่ิงใดเหลืออยู่ก็แปลได้ว่า สิ่งนั้นมีมากกว่าอีกสิ่งหนึ่ง แน่นอนว่า เราสามารถเปลี่ยนของภายในถุงเป็นอะไรก็ตาม มันก็ยังคงมีคุณสมบัตินี้เหมือนๆกัน ด้วยคุณสมบัตินี้ นำไปสู่ความสามารถในการเปรียบเทียบจำนวน

และเรายังสามารถนิยามตัวเลข โดยใช้กระบวนการคล้ายๆกันนี้ได้ว่า "ตัวเลข คือ การทำซ้ำการดำเนินการอะไรซักอย่างไปเรื่อยๆ เทียบกับสิ่งของมาตรฐานที่เรากำหนดไว้" โดยตัวเลขแต่ละตัว คือ การดำเนินการเรียกฟังก์ชั่นซ้อนๆกัน
* เลข 1 แทนด้วย การดำเนินการ 1 ครั้ง
* เลข 2 แทนด้วย การดำเนินการ 2 ครั้ง
* เลข 3 แทนด้วย การดำเนินการ 3 ครั้ง
...

และแน่นอนว่า เลข 0 แทนด้วยการไม่ดำเนินการอะไรเลย

ด้วยนิยามนี้ /me สามารถนำมาใช้ในการสร้าง number โดยใช้ function ที่เรียกซ้อนๆกัน ได้ดังนี้

/me นิยาม ตัวเลข 1 โดยการสร้างฟังก์ชั่นที่รับ 2 ตัวแปร โดยตัวแปรแรก คือ การดำเนินการอะไรซักอย่าง เช่น การหยิบของออกจากถุง, การทำลาย หรือ การมาร์กเส้น 1 เส้นไว้บนกระดาน และอีกตัวแรก คือ สิ่งที่เราจะดำเนินการด้วย ในที่นี้ อาจจะเป็นส้ม, แอ๊ปเปิ้ล หรือ ก้อนหิน

เมื่อเปลี่ยนเป็นโค้ด จะได้แบบนี้

```js
function one(proc, x) {
    return proc(x)
} 
```

และทำนองเดียวกัน /me สามารถนิยาม 2, 3, ... ดังนี้

```js
function two(proc, x) {
    return proc(proc(x))
} 

function three(proc, x) {
    return proc(proc(proc(x)))
} 
```

และ ด้วยรูปแบบเดียวกันนี้ /me สามารถนิยามตัวเลข 0 (แต่มันไม่ใช่ counting numbers หนิ) โดยวิธีการเดิม แต่เราจะไม่ให้มันดำเนินการใดๆ

```js
function zero(proc, x) {
    return x
} 
```

เมื่อเราเปลี่ยนโค้ดทั้งหมดให้อยู่ในรูปแบบของ arrow function จะสามารถลดรูปเป็น

```js
const ZERO  = (p,x) => x;
const ONE   = (p,x) => p(x);
const TWO   = (p,x) => p(p(x));
const THREE = (p,x) => p(p(p(x)));
```

** ถึงเงื่อนไขของสำหรับโค้ดนี้ คือ โค้ดที่ใช้เฉพาะฟังก์ชั่น อาจจะมีคนแย้งว่า โค้ดที่เห็นตอนนี้มันมีการสร้างตัวแปรตัวหนะ <span class="tag-en">#ไม่เหมือนที่คุยกันไว้หนิหน่า</span>

แต่ แต่ เพื่อให้ทุกคนสามารถเข้าใจง่ายขึ้น /me จึงขอใช้ const ซึ่งเป็นการประกาศตัวแปรที่ไม่สามารถเปลี่ยนแปลงค่าภายในได้ แปลว่ามันจะมีค่าแบบนี้ไปตลอดกาล และเมื่อทุกอย่างครบสมบูรณ์ เราจะย้อนกลับ crtl+replace ทุกๆตัวแปรด้วยฟังก์ชั่นที่สร้างขึ้น <span class="tag-en">#เราจะขอทำตามสัญญาขอเวลาอีกไม่นาน</span>

# What is that number?

สุดท้าย ก่อนที่จะข้ามไปสู่ส่วนถัดไป /me ลองมาทายดูว่าตัวเลขนี้คือเลขอะไร

```js
const X = (p,x) => p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(p(x)))))))))))))))))))))))))));
```

มันค่อนข้างยาก และน่าเบื่อกว่าที่คิด คิดดูซิว่าถ้าเป็นเลข 3 หลัก คงต้องนับกันวุ่นวาย ดังนั้น /me จึงอยากแนะนำฟังก์ชั่น to_integer(n) เพื่อเปลี่ยนตัวเลขแบบฟังก์ชั่นไปเป็นตัวเลขธรรมดาแบบที่ทุกคนคุ้นเคย ถึงแม้ว่ามันจะไม่เกี่ยวกับโค้ดส่วนที่ /me ต้องการ แต่มันจะช่วยให้ /me เช็คค่าต่างๆได้ง่ายขึ้นบน console ปกติ โดยไม่ต้องมี console ใหม่ที่รองรับตัวเลขที่เรานิยามขึ้น

```js
function to_integer(n) {
    return n((x)=>x+1,0)
}
```

จากนิยามตัวเลขที่เรากำหนดไว้ว่ามันคือ การดำเนินการอะไรซักอย่างซ้ำๆกันหลายๆครั้ง ดังนั้นถ้ากำหนดให้การดำเนินการนั้น คือ การบวกหนึ่งใน native javascript เข้าไปยังเลข 0 สิ่งที่เราจะได้ คือ ตัวเลขแบบเดิมที่เราคุ้นเคย yeepeee

```js
>> to_integer(ZERO)
=> 0

>> to_integer(THREE)
=> 3
```

เห้ยยยย แทนค่าตัวเลขของเราลงใน psudo-code ที่ /me ร่างไว้

```python
def isPrime(p):
    for i in range(TWO,p):
        if p%i==0:
            return "Not Prime"
    return p
```

แป๋ววว ดูเหมือนว่า โปรแกรมนี้ยังคงไม่สามารถรันได้แน่นอน! เพราะยังมี for loop, %, range(), ... และ อีกมากมายรอการ implement และหวังว่าเมื่อ /me สร้างทุกอย่างเสร็จสมสูรณ์ เราจะได้พบกับ New Era of isPrime(p)

PS. ดูโค้ดส่วนต่างๆได้ที่ [Github](https://github.com/chameleonTK/programming-with-nothing-js) จะทยอย push ตามบล๊อคที่ทยอยเขียน

จบไปอีกหนึ่งตอน

ตอนนี้ /me เล่าถึง numbers และการนิยามตัวเลข โดยใช้ฟังก์ชั่น สำหรับตอนต่อไป /me จะพาแนะนำการดำเนินการต่างๆบนจำนวนนับ เพราะ /me เลือกที่สร้างจำนวนขึ้นมาด้วยตัวเอง จึงจำเป็นต้องสร้าง Arithmetic operations: บวก ลบ คูณ หาร ด้วยตัวเองเช่นกัน
