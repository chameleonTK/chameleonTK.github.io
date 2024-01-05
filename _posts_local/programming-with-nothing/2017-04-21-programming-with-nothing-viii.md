---
layout: post
title: "Programming with Nothing : String"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/img/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR
EP.8 บทนี้ ถือเป็นบทสุดท้ายที่จะยุ่งเกี่ยวกับ Code และเป็นปลายทางของการสร้าง isPrime(n)

<!--more-->



ใน [EP.7](https://chameleontk.github.io/programming-with-nothing-vii) เราได้สร้าง isPrime(n) ที่ทำงานได้อย่างถูกต้องเรียบร้อยแล้ว และสิ่งสุดท้ายในการเขียน isPrime(n) ก็คือ การแสดงผล เพื่อทำให้คนอื่นเข้าใจคำตอบง่ายขึ้น ซึ่งต้องอาศัย data type ชนิดสุดท้าย
String

หากเป็นคนที่เคยผ่านการเขียนโปรแกรมด้วยภาษา C คงจะเข้าใจเป็นอย่างดีว่า string ที่เรากำลังพูดถึงกันอยู่ตอนนี้ ความจริงแล้วไม่มีอะไรซับซ้อนเลย

ความจริงที่น่าตกใจ คือ

<div class="blockquote">string = array of characters = array of specified numbers</div>

ทั้งนี้เพราะว่า แม้กระทั่งใน computers ทั่วๆไป ก็ไม่มีข้อมูลตัวอักษร ทั้งหมดที่เราเก็บลงในคอมพิวเตอร์ต่างเป็นตัวเลข สิ่งที่เราเห็นเป็นแค่ ข้อตกลง ที่คอมทุกเครื่องใช้ร่วมกัน และเรียก "ข้อตกลง" นี้ว่า [Encoding](http://en.wikipedia.org/wiki/Character_encoding) และข้อตกลงที่ว่านี้ คือ ข้อตกลงที่ว่าด้วยการแทนตัวอักษรด้วยตัวเลข ไม่ว่าจะเป็นตัวอักษรใดก็ตาม หากต้องการเก็บลงคอมพิวเตอร์ ทุกอย่างจะโดนแปลงเป็นตัวเลข ด้วยข้อตกลงที่กำหนด

ดังนั้น ไม่ว่าจะอยู่ที่ไหนก็ตาม แค่เพียงแค่ใช้ตัวเลขเดียวกัน ในข้อตกลงเดียวกัน ทุกคนก็สามารถสื่อสารกันได้อย่างเข้าใจ และข้อตกลงที่เข้าใจง่าย และโด่งดังมากๆ ก็หนีไม่พ้น [ASCII](http://en.wikipedia.org/wiki/ASCII) ที่สร้างขึ้นในปี 1960 แต่ยังคงมีใช้กันถึงปัจจุบัน (ถึงแม้ว่าจะค่อยๆโดนแทนที่ด้วย [Unicode](https://en.wikipedia.org/wiki/Unicode))

ซึ่งเจ้า ASCII บอกว่า
```js
>> 'A' == 65
>> 'B' == 66
>> 'C' == 67
>> ...
>> 'Z' == 90
```

ดังนั้น /me สามารถสร้างคำว่า "PRIME" แทนด้วย List ของตัวเลขดังนี้

```js
>> "PRIME" == [80, 82, 73, 77, 69]
```

แต่อย่างไรก็ตาม /me ไม่จำเป็นจะต้องใช้ standard encoding เพราะว่า /me ต้องสร้าง decoder เพื่อแปลงตัวเลขไปเป็นตัวอักษรด้วยตัวเองอยู่แล้ว

เพื่อออกแบบมาตรฐานของตัวเอง /me จะกำหนดเพียงตัวอักษรทั้งหมดที่ต้องใช้ ซึ่งมีเพียง "0123456789NOT PRIME" ทั้งหมด 19 ตัวอักษรแทนด้วยตัวเลข 0 ถึง 18

ดังนั้น "NOT PRIME" = [11, 12, 13, ..., 18] สามารถแทนด้วย

```js
const NOT_PRIME=RANGE(ADD(TEN)(ONE), DECREMENT(ADD(TEN)(TEN)))
```

และ 2 ฟังก์ชั่นสุดท้าย ที่จำเป็นสำหรับการใช้ string คือ

* TO_DIGIT(N) ฟังก์ชั่ันสำหรับการแปลง number ไปเป็น string

```js
// original version
const TO_DIGITS = function(n){
    if (n<10){
        return [n];
    } 

    var k = TO_DIGITS(Math.floor(n/10))
    k.push(n%10)
    return k
}


const TO_DIGITS = Z(f=>N=>PUSH(IF(LESS_THAN(N)(TEN))(EMPTY)(x=>f(DIVIDE(N)(TEN))(x)))(MODULO(N)(TEN)));
```

และ

* to_string(N) สำหรับการแปลง functional string ไปเป็น native string

```js
function to_char(c) {
  return '0123456789NOT PRIME'.slice(to_integer(c), to_integer(c)+1)
}

function to_string(str) {
  return to_array(str).map(s=>to_char(s)).join("")
}
```

ประกอบทุกส่วนเข้าด้วยกัน

```js
const isPrime = (N)=>{
    return FOLD(RANGE(TWO)(N))(TO_DIGITS(N))(acc=>n=>{
        return IF(IS_ZERO(MODULO(N)(n)))(NOT_PRIME)(acc)
    })
}

to_array(MAP(RANGE(TWO)(HUNDRED))(n=>isPrime(n)))
.forEach((b,i)=>{
    console.log(to_string(b));
})
```

Victory !!

ในที่สุดเราก็มาถึง checkpoint จุดสุดท้าย จุดที่เราร่วมกันสร้าง isPrime(n) ตั้งแต่ต้นโดยไม่ใช้ data structure อื่นนอกจาก functions

```js
const isPrime = (N)=>{
    return FOLD(RANGE(TWO)(N))(TO_DIGITS(N))(acc=>n=>{
        return IF(IS_ZERO(MODULO(N)(n)))(NOT_PRIME)(acc)
    })
}
```

และตามที่ได้สัญญาเอาไว้ว่า เราจะแปลงทั้งหมดเป็นฟังก์ชั่น เราจะไม่หลงเหลือความเป็นตัวแปรอีกต่อไป

```js
const isPrime = (N)=>((f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))
(f=>l=>x=>g=>(b=>b)((p=>p(x=>y=>x))(l))(x)(y=> g(f((l=>(p=>p(x=>y=>y))
((p=>p(x=>y=>y))(l)))(l))(x)(g))((l=>(p=>p(x=>y=>x))((p=>p(x=>y=>y))
(l)))(l))(y))))((f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))(f=>m=>n=>(b=>b)
((m=>n=>(c=>a=>b=>c(b)(a))((n=>n(x=>(x=>y=>y))((x=>y=>x)))
((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(n)(m))))
(m)(n))(x=>(l=>x=>(x=>y=>f=>f(x)(y))((x=>y=>y))((x=>y=>f=>f(x)(y))(x)(l)))
(f((n=>(p=>x=>p(n(p)(x))))(m))(n))(m)(x))((x=>y=>f=>f(x)(y))((x=>y=>x))
((x=>y=>x))))((p=>x=>p(p(x))))(N))(((f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))
(f=>N=>(l=>x=>(f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))(f=>l=>x=>g=>(b=>b)
((p=>p(x=>y=>x))(l))(x)(y=> g(f((l=>(p=>p(x=>y=>y))((p=>p(x=>y=>y))(l)))
(l))(x)(g))((l=>(p=>p(x=>y=>x))((p=>p(x=>y=>y))(l)))(l))(y)))(l)((l=>x=>
(x=>y=>f=>f(x)(y))((x=>y=>y))((x=>y=>f=>f(x)(y))(x)(l)))((x=>y=>f=>f(x)(y))
((x=>y=>x))((x=>y=>x)))(x))((l=>x=>(x=>y=>f=>f(x)(y))((x=>y=>y))((x=>y=>f=>f(x)(y))
(x)(l)))))((b=>b)((m=>n=>(c=>a=>b=>c(b)(a))((n=>n(x=>(x=>y=>y))((x=>y=>x)))
((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(n)(m))))(N)
(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(m))((p=>x=>x))))
((p=>x=>p(p(x))))((p=>x=>p(p(p(p(p(x))))))))))((x=>y=>f=>f(x)(y))((x=>y=>x))
((x=>y=>x)))(x=>f(((f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))(f=>m=>n=>(b=>b)
((m=>n=>(n=>n(x=>(x=>y=>y))((x=>y=>x)))((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))
(y=>x)(y=>y)))(n)))(m)(n)))(n)(m))(x=>(n=>(p=>x=>p(n(p)(x))))
(f((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(m)(n))(n))(x))
((p=>x=>x))))(N)(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(m))((p=>x=>x))))
((p=>x=>p(p(x))))((p=>x=>p(p(p(p(p(x))))))))))(x)))(((f=>(x=>f(y=>x(x)(y)))
(x=>f(y=>x(x)(y))))(f=>m=>n=>(b=>b)((m=>n=>(n=>n(x=>(x=>y=>y))((x=>y=>x)))
((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(m)(n)))(n)(m))
(x=>f((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(m)(n))(n)(x))
(m)))(N)(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(m))((p=>x=>x))))
((p=>x=>p(p(x))))((p=>x=>p(p(p(p(p(x))))))))))))(N))(acc=>n=>(b=>b)((n=>n(x=>(x=>y=>y))
((x=>y=>x)))(((f=>(x=>f(y=>x(x)(y)))(x=>f(y=>x(x)(y))))(f=>m=>n=>(b=>b)
((m=>n=>(n=>n(x=>(x=>y=>y))((x=>y=>x)))((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))
(y=>x)(y=>y)))(n)))(m)(n)))(n)(m))(x=>f((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))
(y=>x)(y=>y)))(n)))(m)(n))(n)(x))(m)))(N)(n)))((f=>(x=>f(y=>x(x)(y)))
(x=>f(y=>x(x)(y))))(f=>m=>n=>(b=>b)((m=>n=>(c=>a=>b=>c(b)(a))((n=>n(x=>(x=>y=>y))
((x=>y=>x)))((n=>m=>(m((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y)))(n)))(n)(m))))
(m)(n))(x=>(l=>x=>(x=>y=>f=>f(x)(y))((x=>y=>y))((x=>y=>f=>f(x)(y))(x)(l)))
(f((n=>(p=>x=>p(n(p)(x))))(m))(n))(m)(x))((x=>y=>f=>f(x)(y))((x=>y=>x))((x=>y=>x))))
(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(m))((p=>x=>x))))((p=>x=>p(p(x))))
    ((p=>x=>p(p(p(p(p(x)))))))))((n=>p=>x=>n(g=>h=>h(g(p)))(y=>x)(y=>y))
((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))
(m)))(m))((p=>x=>x))))((p=>x=>p(p(x))))((p=>x=>p(p(p(p(p(x)))))))))
(((n=>m=>(n((n=>m=>(n((n=>(p=>x=>p(n(p)(x)))))(m)))(m))((p=>x=>x))))
((p=>x=>p(p(x))))((p=>x=>p(p(p(p(p(x))))))))))))(acc))
```

<span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span> <span class="tag-en">#หนิมันภาษาอะไรเนี๊ยะ</span>

ก็หวังว่า ถ้ามีคนอ่านมาจนถึงตอนนี้ ก็คงได้อะไรไปไม่บ้างก็น้อย และขอจบบล๊อคซีรีย์ Programming with Nothing อย่างไม่เป็นทางการเพียงแค่นี้ เพราะ จริงๆมีตอนต่อไป เป็นบทสรุปว่า ทำไมเราถึงสามารถใช้ functions สร้างได้ขนาดนี้ แนวคิดนี้เดิมทีแล้วเป็นของใคร?

ไว้เจอกันใหม่นะฮะ

<div class="blockquote">
I cannot teach anybody anything. I can only make them think
― Socrates</div>

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