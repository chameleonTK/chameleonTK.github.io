---
layout: post
title: "Programming with Nothing : Predicates & Comparison Operators"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/feats/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

บันไดขั้นต่อไป เพื่อพา /me สร้าง isPrime(n): Predicates 
<!--more-->

# Predicates

หลังจากพูดถึง Booleans ไปแล้ว สิ่งต่อมา ก็คือสิ่งที่เรียกว่า **"Predicates"** จะพูดว่ามันคืออะไรก็ค่อนข้างยาก ดูเหมือนว่าคำนี้ใช้ในหลายๆความหมายและหลายๆสาขาวิชา /me เองก็สับสนอยู่เหมือนกัน

แต่ในที่นี้ **Predicates** หมายถึง ของ 2 อย่าง คือ

* Boolean-valued function : ฟังก์ชั่นที่ return boolean
* Characteristic function : ฟังก์ชั่นที่อธิบายความสัมพันธ์หรือลักษณะเฉพาะบางอย่างของสิ่งที่เราสนใจ

ตัวอย่างที่สำคัญ และเป็นฟังก์ชั่นที่จำเป็นสำหรับ isPrime() ก็คือ IS_ZERO(n) ซึ่งมีหน้าที่เช็คว่าตัวเลข n เท่ากับ 0 หรือไม่

```js
def IS_ZERO(n)
   if n == 0
      true
   else
      false
   end
end
```

`IS_ZERO(n)` ถือเป็นสะพานชิ้นสำคัญที่เชื่อมความสัมพันธ์ของ numbers ไปเป็น boolean แน่นอนว่า ทุกคนสามารถ implement IS_ZERO ได้อย่างง่ายได้ในภาษาโปรแกรมมิ่งทั่วๆไป แต่สำหรับเงื่อนไขที่ใช้เฉพาะ functions เราสามารถเขียนมันขึ้นมาได้อย่างไร?

ก่อนอื่น คือการพิจารณาตัวเลขที่เราสร้างขึ้นมากันอีกครั้ง

```js
const ZERO  = (p)=>(x)=>x;
const ONE   = (p)=>(x)=>p(x);
const TWO   = (p)=>(x)=>p(p(x));
const THREE = (p)=>(x)=>p(p(p(x)));
```

จะเห็นว่า ZERO เป็นเพียงตัวเลขเดียวที่ไม่เรียก function p และ /me สามารถใช้คุณสมบัตินี้ในการสร้าง IS_ZERO โดยกำหนดให้ p เป็นฟังก์ชั่นที่จะ return FALSE เสมอ เมื่อไรก็ตามที่ตัวเลขนั้นไม่ใช่ ZERO มันจะให้ค่าเป็น FALSE และในทางกลับกัน เราสามารถกำหนดให้ x มีค่าเป็น TRUE เมื่อ ZERO ทำการ return x เท่ากับว่า มันเป็นการ return TRUE ด้วยเช่นกัน

```js
const IS_ZERO = function(n){
    return n((x)=>FALSE)(TRUE);
}

// Arrow function
const IS_ZERO = (n)=> n((x)=>FALSE)(TRUE);
```

ลองทดสอบอีกครั้ง

```js
>> to_boolean(IS_ZERO[ZERO])
=> true

>> to_boolean(IS_ZERO[THREE])
=> false
```

ลองเอา IS_ZERO ไปใช้ใน isPrime(n)

```js
const isPrime = (p)=>{
   for i in range(TWO,p):
        IF(IS_ZERO(p%i))( return "Not Prime")(null)
    return p
}
```

หลังจากได้ส่วนประกอบสำคัญอย่าง IS_ZERO(n) มาแล้ว

บันไดขั้นต่อมา คือ เครื่องหมายเปรียบเทียบ(Comparison Operators) มากกว่า, น้อยกว่า, มากกว่าเท่ากับ และน้อยกว่าเท่ากับ

ความจริงแล้ว การเปรียบเทียบก็เสมอการหยิบแอ๊ปเปิ้ลและส้มออกจากถุงพร้อมๆกัน ใครโดนหยิบจนเหลือถุงเปล่าก่อนก็เป็นฝ่ายพ่ายแพ้และถือว่ามีจำนวนน้อยกว่าไปโดยปริยาย

หรือพูดเป็นสมการคณิตศาสตร์ได้ว่า m <= n ก็ต่อเมื่อ m - n <= 0

ดังนั้นการสร้าง LESS_THAN_OR_EQUAL(m, n) ก็หนีไม่พ้นการใช้ SUBTRACT และการเทียบเท่ากับ ZERO แต่โลกที่เราสร้างขึ้นนี้ไม่มีสิ่งที่เรียกว่า **จำนวนลบ** ดังนั้น การเทียบน้อยกว่า ZERO จึงไม่มีความหมายใดๆ (ทุกตัวเลขที่ต่ำกว่า 0 จะได้ค่าเท่ากับ 0)

เราจึงสามารถสร้าง LESS_THAN_OR_EQUAL(m, n) ได้ดังนี้

```js
const LESS_THAN_OR_EQUAL = (m)=>(n)=>IS_ZERO(SUBTRACT(m)(n))
```

และเมื่อ /me พบว่า not LESS_THAN_OR_EQUAL คือ GREATER_THAN
```js
const GREATER_THAN = (m)=>(n)=>NOT(IS_ZERO(SUBTRACT(m)(n)))
```

สิ่งที่น่าคิดต่อมาคือ แล้ว "น้อยกว่าเฉยๆ" และ "มากกว่าเท่ากับ" จะสร้างขึ้นมายังไง? แต่ /me ยังไม่อับจนหนทาง เรายังมีคุณสมบัติสุดท้าย

คุณสมบัติสลับด้าน เมื่อ x < y แล้ว y > x

โดยทั่วไปแล้วเรามักใช้สมการแก้ไขปัญหา สำหรับสมการ ไม่ว่าเราสลับด้านมันยังไง มันก็ยังคงได้สิ่งเดียวกัน แต่สำหรับอสมการ เรากลับได้สิ่งที่แตกต่างจากเดิม และนี้คือหนึ่งในคุณสมบัติเฉพาะของอสมการ และทำให้ /me เอามาใช้ในการสร้าง LESS_THAN(m, n) และ GREATER_THAN_OR_EQUAL(m, n) ดังนี้

```js
const LESS_THAN = (m)=>(n)=>IS_ZERO(SUBTRACT(n)(m))
const GREATER_THAN_OR_EQUAL = (m)=>(n)=>NOT(IS_ZERO(SUBTRACT(n)(m)))
//เผื่อไม่สังเกต มันมีการสลับตัวแปรจากของเดิม
```

จบไปอีกหนึ่งตอน

ถึงแม้ว่าเรายังไม่เข้าใกล้เป้าหมาย isPrime(n) ของเราเลย แต่มันก็เป็นการวางรากฐานที่มั่นคง หลังจากนี้ เราจะสามารถลุยไปได้อย่างรวดเร็ว

สำหรับตอนหน้า /me จะพาไปเขียนฟังก์ชั่นที่เรายังค้างกันอยู่ DIVIDE และ MODULO ซึ่งต้องใช้สิ่งที่เราสร้างมาทั้งหมดไม่ว่าจะเป็น SUBTRACT, LESS_THAN_OR_EQUAL และ เครื่องมือชิ้นใหม่ที่เรียกว่า Y combinator และการทำ recursion

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

แต่สามารถ ดูโค้ดส่วนต่างๆได้ที่ [Github](https://github.com/chameleonTK/programming-with-nothing-js) จะทยอย push ตามบล๊อคที่ทยอยเขียน