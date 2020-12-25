---
layout: post
title: "Programming with Nothing : Booleans"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/img/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

คำถามลอยไปลอยมา หลังจาก /me สามารถแทนค่าความจริงด้วย functions ได้แล้ว ข้อมูลอีกชนิดที่ยังเหลืออยู่คือ booleans หรือ ค่าความจริง True/False  จะสามารถแทนด้วย funcitons ได้ยังไง? และตอนนี้คือคำตอบ

<!--more-->
# Booleans

/me จะแทนค่าความจริงด้วยฟังก์ชั่นได้ยังไง? คำถามลอยไปลอยมา

หนึ่งในคำตอบที่น่าสนใจ เกิดจากความจริงอย่างหนึ่ง คือ ค่าความจริง ไม่ว่าจะ จริง(True) หรือ เท็จ(False) มักใช้พร้อมๆ Conditional Statements ซึ่งโดยทั่วไปแล้ว มันคือ **"ถ้า...เป็นจริง ฉันจะทำ... ถ้าไม่ฉันจะทำ..."**

ดูเหมือนว่าพฤติกรรมของ Booleans คือ เงื่อนไขสำหรับเลือก actions อันใดอันหนึ่ง จาก 2 เหตุการณ์ ดังนั้นเราสามารถใช้พฤติกรรมลักษณะนี้ในการสร้าง Booleans ด้วยฟังก์ชั่นที่รับตัวแปร 2 ตัว แล้วเลือกตัวใดตัวหนึ่งออกไป ดังนี้

```js
function TRUE (x, y) {
    return x;
}

function FALSE (x, y) {
    return y;
} 
```

TRUE เป็นฟังก์ชั่นที่ return ตัวแปรแรกเสมอ และ FALSE เป็นฟังก์ชั่นที่ return ตัวแปรที่สองเสมอ เมื่อเปลี่ยนเป็น arrow functions จะได้ดังนี้

```js
const TRUE = (x)=>(y)=>x;
const FALSE = (x)=>(y)=>y;
```

ทำนองเดียวกับกับตัวเลข /me จำเป็นต้องสร้าง to_boolean เพื่อใช้ในเปลี่ยนฟังก์ชั่นค่าความจริงพวกนี้ไปเป็น native javascript

```js
function to_boolean(b) {
    return b(true)(false)
}
```

ตรวจสอบอีกที

```js
>> to_boolean(TRUE)
=> true

>> to_boolean(FALSE)
=> false
```

<span class="tag-en">#ง่ายกว่างี้มีอีกไหม</span>? <span class="tag-en">#ง่ายกว่างี้มีอีกไหม</span>? <span class="tag-en">#ง่ายกว่างี้มีอีกไหม</span>? <span class="tag-en">#ง่ายกว่างี้มีอีกไหม</span>? <span class="tag-en">#ง่ายกว่างี้มีอีกไหม</span>?

เมื่อได้ Booleans แล้ว เครื่องมือต่อมาที่ขาดไม่ได้คือ IF "ถ้า....ถ้าใช้ แล้ว....ถ้าไม่ แล้ว....." และแน่นอนว่า จากรูปแบบของ Booleans แล้ว /me สามารถนำมาสร้าง IF ได้อย่างง่ายดาย

```js
function IF(cond, x, y) {
    return cond(x)(y)
}
```

แต่ความจริงแล้ว IF เป็นแค่ [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) ที่ช่วยอำนวยความสะดวกในการอ่านโค้ดและเขียนโค้ดเท่านั้นเอง เพราะว่าเราสามารถใช้ Booleans แทน IF ได้เลยทันที เพราะทั้งคู่ใช้ concept เหมือนกัน

```js
>> IF(TRUE)("A")("B")
=> "A"

>> TRUE("A")("B")
=> "A"

>> IF(FALSE)("A")("B")
=> "B"

>> FALSE("A")("B")
=> "B"
```

ด้วยเงื่อนไขที่เหมือนกันนี้ เรายังสามารถ [refactoring](https://en.wikipedia.org/wiki/Code_refactoring) IF ให้มีความง่ายมากขึ้น

```js
function IF(cond) {
    return cond
}

// Arrow functions 

const IF = (b)=>b;
```

เพราะว่า ทุกครั้งที่ IF(boolean)(ActionThen)(ActionElse) เทียบเท่ากับ boolean(ActionThen)(ActionElse) ดังนั้น IF(boolean) เทียบเท่ากับ boolean

<span class="tag-en">#ฮูเร้</span> <span class="tag-en">#ฮูเร้</span> <span class="tag-en">#ฮูเร้</span> <span class="tag-en">#ฮูเร้</span> <span class="tag-en">#ฮูเร้</span> <span class="tag-en">#ฮูเร้</span>

และนี้ ก็เป็นอีก checkpoint สำหรับ isPrime(p)

```js
const isPrime = (p)=>{
   for i in range(TWO,p):
        IF(p%i==0)( return "Not Prime")(null)
    return p
}
```

// โค้ดดูเปลี่ยนไปจากเดิมเยอะ เพราะว่า /me เปลี่ยนจาก psudo-code เป็น javascript ที่ควรจะเป็น แต่ดูเหมือนว่าก็ยังไม่เป็นรูปเป็นร่างเท่าที่ควร เฮ้ออออ~ <span class="tag-en">#สู้ต่อไปทาเคชิ</span>

หลังจากที่เราสร้าง TRUE, FALSE และ IF ได้แล้ว /me อยากจะแถมเครื่องมืออีกอย่างที่น่าสนใจ(แต่ isPrime ของเราไม่ต้องใช้มัน) และมันก็คือ

# Logic Operations

สำหรับโปรแกรมเมอร์บางคนอาจจะงงๆ เพราะมักคุ้นเคยกับ &&, \|\|, ! หรือ สำหรับสาวก python ก็จะใช้เป็นคำว่า and, or, not

เราสามารถ implement ได้ดังนี้

```js
const AND = (a)=>(b)=>a(b)(a);
const OR = (a)=>(b)=>a(a)(b);
const NOT = (c)=>(a)=>(b)=>c(b)(a); //Applicative Order
// const NOT = (p)=>p(FALSE)(TRUE);    //Normal Order
const XOR = (a)=>(b)=>a(NOT(b))(b);
```

สามารถอธิบายง่ายๆ โดยใช้หลักของ logic ทั่วไป

### พฤติกรรมของ AND

สร้างจากความจริง 2 ข้อคือ

```js
>> false && B 
=> false

>> true && B
=> B
```

เมื่อ a เป็น FALSE แล้วแปลว่า **"ไม่ว่ายังไงก็ตาม expression นี้ ก็เป็น false"** จึงเลือกให้ return a ซึ่งมีค่าเป็น FALSE

เมื่อ a เป็น TRUE แล้วก็เลือก return b

### พฤติกรรมของ OR

สร้างจากความจริง 2 ข้อคือ

```js
>> true || B 
=> true

>> false || B
=> B
```

- ทำนองเดียวกับ AND -

### พฤติกรรมของ XOR

สร้างจากสัจพจน์ a xor b => (a and not b) or (not a and b) ดังนั้น

ถ้า a เป็น TRUE แล้ว จะเหลือแค่ (a and not b) ดังนั้น เราจึง return (not b)

ถ้า a เป็น FALSE แล้ว จะเหลือแค่ (not a and b) ดังนั้น เราจึง return (b)

และ สุดท้าย logic NOT

สังเกตว่ามันมีการสร้าง 2 แบบ สำหรับ Application order และ Normal order แล้วทั้ง 2 คืออะไร?

แน่นอนว่าหลายคนอาจสงสัยว่า Application order และ Normal order ต่างกันยังไง? ทั้งๆที่ทั้ง 2 NOT มีพฤติกรรมเหมือนกันคือการกลับค่าความจริง TRUE => FALSE และ FALSE => TRUE

ทั้งสองความลำดับการให้ความสำคัญระหว่าง arguments และ caller function โดย
* Normal order เลือกที่จะรัน caller function ก่อนที่จะไปรันแต่ละ arguments
* Application order เลือกที่จะรัน arguments ทุกค่าให้หมดก่อน แล้วจึงรัน caller function

ตัวอย่างง่ายๆ เช่น

```js
// สมมติว่ามี functions เหล่านี้
// Normal order (Lazy evaluation)
>> double(average(2, 4))
=> plus (average(2, 4), average(2, 4))
=> plus (divide(plus(2, 4), 2), average(2, 4))
=> plus (divide(6, 2), average(2, 4))
=> plus (3, average(2, 4))
=> plus (3, divide(plus(2, 4), 2))
=> plus (3, divide(6, 2))
=> plus (3, 3)
=> 6

// Application order
>> false || B
>> double(average(2, 4))
=> double(divide(plus(2, 4), 2))
=> double(divide(6, 2))
=> double(3)
=> 6
```

ดูเหมือนว่า Application order เป็นสิ่งที่ดีกว่า เพราะว่า มันลดจำนวนครั้งในการรันคำสั่งได้มากกว่า แต่ในบางกรณี ก็ไม่ดีอย่างที่คิด เพราะว่า Application order ต้องรันทุกๆ arguments ก่อนซึ่งบางครั้งเราไม่จำเป็นขนาดนั้น เพราะเราอาจจะไม่จำเป็นต้องใช้มัน

```js
>> const IF = (cond, funcA, funcB)=> { 
...   if(cond) 
...     return A; 
...   return B
... }

// Normal order (Lazy evaluation)
>> IF(true, "hello", (1/0));
=> "hello"

// Application order
>> IF(true, "hello", (1/0));
=> IF(true, "hello", ERROR);
=> ERROR
```

แต่เราไม่มีสิทธิเลือกหรอกนะว่า จะใช้ Evaluation order แบบไหน เพราะว่าแต่ละภาษาเลือกมาให้เราใช้เรียบร้อยแล้ว และ javascript เลือก Application order นั้นเอง

กลับมาต่อกับเรื่อง NOT

### พฤติกรรมของ NOT

มีลักษณะต่างกับอันอื่น คือ มันจะสร้าง booleans ตัวใหม่มาแทนตัวเก่า ที่สลับ argumants กับตัวเดิม และนั้นก็คือ not

จบแล้วสำหรับ data type พื้นฐานอย่างค่าความจริง true, false และตัวดำเนินการทางลอจิก อย่าง AND, OR สุดท้ายก็เป็นหัวข้อที่เกินมาอย่างงงๆ Evaluation order

สำหรับตอนต่อไป /me จะพาไปเจอกับคำสั่งที่ขาดไม่ได้ นั้นก็คือคำสั่ง "เปรียบเทียบ"


## อ่านตอนอื่นๆได้ที่
* [EP1: Introduction](http://wp.curve.in.th/programming-with-nothing-i)
* [EP2: Numbers](http://wp.curve.in.th/programming-with-nothing-ii)
* [EP3: Arithmetic operators](http://wp.curve.in.th/programming-with-nothing-ii)
* [EP4: Booleans](http://wp.curve.in.th/programming-with-nothing-iv)
* [EP5: Predicates & Comparison Operators](http://wp.curve.in.th/programming-with-nothing-v)
* [EP6: Recursion](http://wp.curve.in.th/programming-with-nothing-vi)
* [EP7: List](http://wp.curve.in.th/programming-with-nothing-vii)
* [EP8: String](http://wp.curve.in.th/programming-with-nothing-viii)
* [EP9: Epilogue](http://wp.curve.in.th/programming-with-nothing-ix) * ยังไม่เขียน

ต้นฉบับ [Programming with Nothing](https://codon.com/programming-with-nothing)

> PS2.โค้ดบางส่วนในบทความ อาจจะรันไม่ได้จริงๆ เพราะ javascript ไม่ได้เปลี่ยน multiple argument function เป็น nested single-argument function อัตโนมัติ อย่างในภาษา Haskell หรือ Lips ดังนั้นฟังก์ชั่นหลายตัวแปร จะต้องแปลงให้อยู่ในรูปตัวแปรเดียวก่อน ถึงจะสามารถรันได้อย่างปกติ แต่อาจจะทำให้อ่านยากมากขึ้น /me จึงขออธิบายด้วย multiple argument function

แต่สามารถ ดูโค้ดส่วนต่างๆได้ที่ [Github](https://github.com/chameleonTK/programming-with-nothing-js) จะทยอย push ตามบล๊อคที่ทยอยเขียน

ขอบคุณ คำอธิบาย Evaluation Order เพิ่มเติมจาก
[CSE 505: Concepts of Programming Languages](https://courses.cs.washington.edu/courses/cse505/99au/)
