---
layout: post
title: "Programming with Nothing : Recursion"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/feats/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

หลังจากเรามีเครื่องมือหลายๆชิ้นไม่ว่าจะเป็น ตัวเลข, การบวกลบคูณ, ค่าความจริง และการเปรียบเทียบ ที่ /me พยายามสร้างมันขึ้นมาจากฟังก์ชั่นเล็กๆหลายๆแบบ และเครื่องมือสุดท้ายสำหรับการสร้าง modulo ก็คือ <b>"Recursion"</b>
<!--more-->

# Recursion

กลับมาดูฟังก์ชั่น isPrime(n) กันอีกครั้ง

```js
const isPrime = (p)=>{
   for i in range(TWO,p):
        IF(IS_ZERO(p%i))( return "Not Prime")(null)
    return p
}
```

ดูเหมือนว่า ส่วนประกอบสำคัญสำหรับการทำ isPrime(n) ตัวนึงที่หายไป คือ ตัวดำเนินการที่เรียกว่า "modulo" หรือการหารเอาเศษ ซึ่งเป็นตัวดำเนินการที่สำคัญสำหรับการเช็คคุณสมบัติของการเป็น prime number

และสำหรับบทนี้ หลังจากเรามีเครื่องมือหลายๆชิ้นไม่ว่าจะเป็น ตัวเลข, การบวกลบคูณ, ค่าความจริง และการเปรียบเทียบ ที่ /me พยายามสร้างมันขึ้นมาจากฟังก์ชั่นเล็กๆหลายๆแบบ และเราเครื่องมือสุดท้ายสำหรับการสร้าง modulo ก็คือ **"Recursion"**

# Modulo

กลับมาที่ ฟังก์ชั่น Modulo อีกครั้ง
m%n หรือ m mod n หมายถึง เศษที่เกิดจากการหาร m ด้วย n โดย เศษที่ว่านั้นต้องมีค่าอยู่ในช่วง 0 ถึง n-1 และสามารถหา m%n ได้โดยการลบ m ด้วย n ไปเรื่อยๆ(การลบไปเรื่อยๆมันก็คือการหารนั้นแหละ) จนกว่า m จะมีค่าน้อยกว่า n

สามารถเขียนฟังก์ชั่นนี้ในรูปทั่วๆไปได้ว่า

```js
function MODULO(m, n) {
    if (n<=m) {
        return MODULO(m-n, n)
    } else {
        return m
    }
}
```

ผลพวงจาก [EP5](https://chameleontk.github.io/programming-with-nothing-v) ทำให้ /me มีเครื่องมือที่เรียกว่า LESS_THAN_OR_EQUAL(n, m) สำหรับเงื่อนไขใน function MODULO

นั้นแปลว่า เราสามารถสร้าง MODULO(m)(n) ได้ดังนี้

```js
//human-readable version
const MODULO = (m)=>(n)=>{
    return IF(LESS_THAN_OR_EQUAL(n)(m))(
            MODULO(SUBTRACT(m)(n))(n)
    )(m)
};


const MODULO = (m)=>(n)=>IF(LESS_THAN_OR_EQUAL(n)(m))(MODULO(SUBTRACT(m)(n))(n))(m);
```

ดูเหมือนว่า เราพร้อมที่จะใช้การ MODULO(m)(n) แล้ว

```js
>> to_integer(MODULO(TWO)(THREE));
=> ...
=> ...
=> RangeError: Maximum call stack size exceeded
```

เอ๋ๆๆๆ ยังไงๆ

ดูเหมือนว่าฟังก์ชั่นที่เราสร้างขึ้นมามันใช้การไม่ได้ แต่แน่นอนว่าสิ่งที่เราทำเป็นสิ่งที่ถูกต้อง แต่ทำไมมันใช้การไม่ได้??

ลองเปิดย้อนกลับไปที่หัวข้อ Evaluation Order ใน EP4 อีกครั้ง

เพราะว่า javascript มีลำดับการคำนวนเป็น Application order หรือเป็นแบบ strict function ทุกๆครั้งที่ call function เจ้า javascript จะทำการ evaluate arguments ทั้งหมดก่อน แล้วจึงค่อย evaluate function's body

ดังนั้นเมื่อกลับไปที่ MODULO(m)(n) อีกครั้ง จะเห็นว่า เราใส่ MODULO(...)(n) เป็น argument หนึ่งของ IF(b) ทำให้ทุกๆครั้งที่เรียก MODULO(m)(n) เจ้าตัว javascript จะพยายามเรียกตัวเองซ้ำขึ้นมาอีกครั้ง แล้วทำแบบนี้ไปเรื่อยๆจนทำให้ Stack overflow

เพื่อที่จะแก้ไขปัญหาที่เกิดขึ้น /me จำเป็นต้องหยุดการคำนวนภายใน IF ก่อนที่มันจะเรียกตัวเองอีกครั้ง และสามารถทำได้โดยการสร้างฟังก์ชั่นอย่างมีชั้นเชิงซ้อนไปอีกชั้น เพื่อไม่ให้ IF คำนวนสิ่งที่อยู่ภายใน

สิ่งที่ได้คือ
 
```js
//human-readable version
const MODULO = (m)=>(n)=>{
    return IF(LESS_THAN_OR_EQUAL(n)(m))(
        (x)=>{
            return MODULO(SUBTRACT(m)(n))(n)(x)
        }
    )(m)
};

const MODULO = (m)=>(n)=>IF(LESS_THAN_OR_EQUAL(n)(m))((x)=>MODULO(SUBTRACT(m)(n))(n)(x))(m);
```

เจ้า (x) => {...(x)} ทำให้ IF สามารถ evaluate arguments ได้โดยไม่ทำให้เกิด stack overflow เพราะจังหวะที่มันกำลัง evaluate arguments นั้น มันเจาะลึกลงไปได้เพียงแค่เปลือกนอกของ MODULO(...)(n) เท่านั้นเอง

```js
>> to_integer(MODULO(TWO)(THREE));
=> 2

>> to_integer(MODULO(THREE)(TWO));
=> 1
```

เย้ มันทำงานได้อย่างถูกต้อง แต่ปัญหาต่อมา กลับมาอยู่ที่ปรัชญาการสร้าง isPrime(n)

เพราะ /me สร้าง MODULO ขึ้นโดยการใช้ MODULO ซ้ำอีกครั้ง ถึงแม้ว่าจะดูไม่แตกต่างจาก const อื่นๆที่เราสร้างกันมาตั้งแต่ต้น แต่ความจริงแล้ว มันแอบมีการอ้างสิ่งที่เรียกว่า **ตัวแปร และ assignment semantics** เพราะว่าเราไม่สามารถ replace คำว่า "MODULO" ด้วยค่าที่อยู่ฝั่งซ้ายของ const MODULO = ... โดยไม่มีตัวแปร MODULO

ซึ่งแน่นอนว่ามันขัดกับแนวคิดที่เราสร้างมาตั้งแต่ต้น

แต่ /me สามารถแก้ไขปัญหานี้ได้ โดยเครื่องมือที่เรียกว่า

# Y combinator
[Y combinator](http://en.wikipedia.org/wiki/Fixed-point_combinator) เป็นชิ้นส่วนสำคัญที่ใช้แก้ปัญหานี้โดยเฉพาะ ทำให้เราสามารถสร้าง a recursive function ได้โดยใช้สิ่งนี้

```js
//human-readable version
const Y = (m)=>{
    return (x)=>{
        return f(x(x))
    }((x)=>{
        return f(x(x))
    })
};

const Y = f=>(x=>f(x(x)))(x=>f(x(x)))
```

แค่ดูก็น่าจะรู้ได้ไม่ยากว่า Y combinator ไม่ใช้สิ่งที่อธิบายได้แบบง่ายๆ และ /me จะไม่พยายามอธิบายมัน ถึงแม้ว่าจะเป็น human-readable version ก็ยังอ่านไม่รู้เรื่องเลยทีเดียว (ถ้าว่างจะหาเวลาเขียนอีกที)

แต่น่าเสียดายที่เรากลับไปเจอปัญหาเดียวครั้งก่อนอีกครั้งแต่สามารถแก้ได้โดยใช้ (x)=>{...(x)} และทำให้ Y combinator เปลี่ยนไปเป็น Z combinator (สำหรับ strict languages)

```js
//human-readable version
const Z = (m)=>{
    return ((x)=>{
        return f((y)=>x(x)(y))
    })((x)=>{
        return f((y)=>x(x)(y))
    })
};


const Z = f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y)))
```

ท้ายที่สุด /me จะใช้ Z combinator กับ MODULO ฉบับดั้งเดิม ได้ดังนี้

```js
//human-readable version
const MODULO = Z(                                   // call Z combinator
    f=> {                                           // add f as a new argument
        return m=>n=> {                                   
            return IF(LESS_THAN_OR_EQUAL(n)(m))                        
            (x=>f(SUBTRACT(m)(n))(n)(x))            // use f instead of MODULO
            (m)
        }
    }
)

const MODULO = Z(f=>m=>n=>IF(LESS_THAN_OR_EQUAL(n)(m))(x=>f(SUBTRACT(m)(n))(n)(x))(m))
```

ทดสอบดูอีกครั้ง

```js
>> to_integer(MODULO(TWO)(THREE));
=> 2

>> to_integer(MODULO(THREE)(TWO));
=> 1
```

สุดท้ายก็เอามาประกอบเข้ากับ isPrime(n)

```js
const isPrime = (p)=>{
   for i in range(TWO,p):
        IF(IS_ZERO(MODULO(p)(i)))( return "Not Prime")(null)
    return p
}
```

สุดท้ายก่อนที่จะจบตอน /me จำเป็นต้องตามหาเครื่องมืออีกตัวที่หายไป

# Divide

การหาร กับ การหารเหลือเศษ เป็นเครื่องมือที่มีความคล้ายคลึงกันมาก ทั้งนี้เนื่องจากทั้งคู่ ต่างโดนนิยามมาพร้อมๆกัน สำหรับการหารนั้นสามารถสร้างจากการ recursion ได้เช่นเดียวกับการหารเหลือเศษ เพราะว่า จริงๆแล้ว
a/b = 1 + ((a-b)/b) โดยที่ ถ้า a < b แล้ว a/b = 0

สามารถเขียนฟังก์ชั่นนี้ในรูปทั่วๆไปได้ว่า

```js
function DIVIDE(m, n) {
    if (n<=m) {
        return INCREMENT(DIVIDE(m-n, n))
    } else {
        return ZERO
    }
}
```

ทั้งนี้ด้วยความรู้เรื่อง Z combinator ที่สั่งสมมาจะได้ว่า
```js
//human-readable version
const DIVIDE = Z(                                   // call Z combinator
    f=> {                                           // add f as a new argument
        return m=>n=> {                                   
            return IF(LESS_THAN_OR_EQUAL(n)(m))                        
            (x=>INCREMENT(f(SUBTRACT(m)(n))(n))(x))            
            (ZERO)
        }
    }
)


const DIVIDE = Z(f=>m=>n=>IF(LESS_THAN_OR_EQUAL(n)(m))(x=>INCREMENT(f(SUBTRACT(m)(n))(n))(x))(ZERO))
```

เย้ๆๆ

จบแล้วสำหรับ recursion ซึ่งเป็นจุดสำคัญที่ทำให้เราสามารถสร้าง modulo และ divide ได้อย่างง่ายดาย(เหรอ?)

สำหรับตอนต่อไป คือจุดเปลี่ยนสำคัญในการสร้าง isPrime(n) เมื่อ /me ต้องผจญกับการสร้าง list และฟังก์ชั่นต่างๆที่จำเป็นสำหรับการใช้ list

## อ่านตอนอื่นๆได้ที่
* [EP1: Introduction](https://chameleontk.github.io/programming-with-nothing-i)
* [EP2: Numbers](https://chameleontk.github.io/programming-with-nothing-ii)
* [EP3: Arithmetic operators](https://chameleontk.github.io/programming-with-nothing-ii)
* [EP4: Booleans](https://chameleontk.github.io/programming-with-nothing-iv)
* [EP5: Predicates & Comparison Operators](https://chameleontk.github.io/programming-with-nothing-v)
* [EP6: Recursion](https://chameleontk.github.io/programming-with-nothing-vi)
* [EP7: List](https://chameleontk.github.io/programming-with-nothing-vii)
* [EP8: String](https://chameleontk.github.io/programming-with-nothing-viii)
* [EP9: Epilogue](https://chameleontk.github.io/programming-with-nothing-ix) * ยังไม่เขียน

ต้นฉบับ [Programming with Nothing](https://codon.com/programming-with-nothing)

แต่สามารถ ดูโค้ดส่วนต่างๆได้ที่ [Github](https://github.com/chameleonTK/programming-with-nothing-js) จะทยอย push ตามบล๊อคที่ทยอยเขียน