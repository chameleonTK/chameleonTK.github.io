---
layout: post
title: "Programming with Nothing : Arithmetic operators"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/img/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

ตรากตรำกับการสร้าง Numbers มาแล้วใน Ep.1 คร่าวนี้ต้องมาเผชิญการการดำเนินการต่างๆ ไม่ว่าจะเป็น บวก, ลบ, คูณ และหาร
<!--more-->

# Arithmetic operators

หลังจากที่เรานิยามตัวเลขโดยใช้ functions กันแล้ว สิ่งต่อมาที่หนีไม่พ้น ก็คือการนิยามการดำเนินการพื้นฐานต่างๆ ทั้ง บวก, ลบ, คูณ และ หาร และสิ่งที่จำเป็นสำหรับการดำเนินการทั้งหมด ก็คือ operators 2 ตัว incrementing และ decrementing

## Incrementing

เป็นฟังก์ชั่นง่ายๆที่เทียบเท่ากับการบวกหนึ่ง หรือ ++ นั้นเอง บางครั้งอาจจะเรียกแทนด้วย "Successor function"

```js
function INCREMENT (n) {
    return function(newProc, x){
        newProc(n(newProc, x));
    }
}
```

เฮ้ ดูสิ่งที่ /me สร้างขึ้นมาซิ มันคืออะไร?

จำกันได้รึปล่าวว่า ตัวเลขคือฟังก์ชั่นหน้าตาแบบนี้

```js
function N (proc, x) {
    return proc(proc(proc(... x ...)))
} 
```

มันคือการเรียก proc ซ้ำๆไปเรื่อยๆ ทั้งหมด N ครั้ง ดังนั้นเมื่อเราพยายามใส่ N(newProc,x) เป็น arg ก็เสมือนเป็นการเปลี่ยน proc ทั้งหมดเป็น newProc

```js
proc(proc(proc(... x ...))) (newProc, x) => newProc(newProc(newProc(... x ...)))
```

และ INCREMENT function ของเราก็เรียก newProc ซ้อนไปอีกชั้นทำให้สิ่งที่ return กลับมา กลายเป็นตัวเลขใหม่ที่มีค่าเพิ่มขึ้น 1 นั้นเอง

บางคนอาจจะคิดว่า แล้วทำไมเราไม่เขียนแบบนี้หละ? ง่ายกว่ากันตั้งเยอะ

```js
function INCREMENT(n) {
    return proc(n)
}
``` 

แต่ แต่ แต่ โค้ดนี้เป็นโค้ดที่อาจจะใช้ได้ และอาจจะใช้ไม่ได้พร้อมๆกัน เพราะเมื่อกลับไปดูโค้ดแล้วเกิดคำถามว่าตัวแปร proc มาจากไหน? แน่นอนว่าต้องมาจากการใช้ตัวแปรอะไรซักอย่างแน่นอน มันจึงไม่ใช่การใช้แค่ฟังก์ชั่นอย่างที่ /me ตั้งใจ

นอกจากนี้ เราจะทราบได้อย่างไรว่า proc ที่อยู่ใน n กับ proc ที่เราเพิ่มเข้าไป มันคือ proc ตัวเดียวกัน?

ต่อมา /me ขอลดรูป INCREMENT ให้อยู่ใน arrow function

```js
const INCREMENT = (n)=>((p)=>(x)=>p(n(p)(x)));
```

หลังจากที่เราได้ INCREMENT แล้วเจ้าสิ่งนี้จะกลายเป็นเครื่องมือในการสร้าง operators ตัวต่อๆไปนั้นก็ต่อ ADD, MULTIPLY และ POWER

{% include aligner.html images="programming-with-nothing/count-numbers-on-hand-suitqais-diaries-6.jpg" column=1 %}

เป็นเรื่องง่ายสำหรับทุกๆคน ที่บอกว่า 4 + 3 = 7 เพราะความคุ้นเคย และการฝึกฝนมาหลายสิบปี

จำได้รึปล่าวว่าตอนเราเด็กๆ เราบวกตัวเลขกันยังไง? นับนิ้ว?

ความทรงจำวัยเด็ก บอกเราว่า 4 + 3 = 4 + 1 + 1 + 1 หรือ
"การดำเนิน INCREMENT ซ้ำๆกัน 3 ครั้ง กระทำบนตัวเลข 4"

เริ่มเห็นรูปแบบอะไรบ้างอย่างแฮะ?
4 + 6 = 4 + 1 + 1 + 1 + 1+ 1 + 1 หรือ
"การดำเนิน INCREMENT ซ้ำๆกัน 6 ครั้ง กระทำบนตัวเลข 4"
4 + 20 = 4 + 1 + 1 + 1 + 1 + 1 + 1 + ... + 1 หรือ
"การดำเนิน INCREMENT ซ้ำๆกัน 20 ครั้ง กระทำบนตัวเลข 4"
...
etc.

ย้อนกลับไปที่ นิยามของตัวเลขกันอีกครั้ง

<div class="blockquote">ตัวเลข N คือ ฟังก์ชั่นที่ดำเนิน proc N ครั้งบนตัวแปร x</div>

ดังนั้น เมื่อเรา apply หลักการเดียวกันนี้ เราจะสามารถกล่างในมุมมองคล้ายๆกันได้ว่า

<div class="blockquote">การบวก n ใส่ตัวแปร m คือ ฟังก์ชั่นที่ดำเนิน INCREMENT n ครั้งบนตัวแปร m</div>

หรือ
```js
const ADD = (n)=>(m)=>(n(INCREMENT)(m));
```

และด้วยเหตุผลเดียวกันนี้ เราสามารถอัพเดต ADD ไปเป็น MULTIPLY และ POWER ได้
MULTIPLY = ฟังก์ชั่นที่ดำเนิน (ADD m) n ครั้งบนตัวเลข 0
POWER = ฟังก์ชั่นที่ดำเนิน (MULTIPLY m) n ครั้งบนตัวเลข 1

```js
const INCREMENT = (n)=>((p)=>(x)=>p(n(p)(x)));
const ADD = (n)=>(m)=>(n(INCREMENT)(m));
const MULTIPLY = (n)=>(m)=>(n(ADD(m))(ZERO));
const POWER = (n)=>(m)=>(m(MULTIPLY(n))(ONE));
```

## Decrementing

หลังจากที่เรารู้ความสามารถของ Incrementing แล้ว มันก็ไม่เป็นเรื่องยากที่จะจิตนาการว่า ถ้าเราสามารถ Decrementing ได้เราจะสามารถสร้าง SUBTRACT, DIVIDE, MODULO หรือ กระทั่งการทำ SQUARE_ROOT ก็เป็นไปได้ (แต่ไม่เขียนนะ มันยากเกินไป LOL)

แต่ดูเหมือนว่าการสร้างฟังก์ชั่น DECREMENT เป็นเรื่องที่ยากกว่าที่คิดเพราะว่า
* เราไม่ทราบ proc ที่อยู่ภายในตัวแปร n
* ถ้า DECREMENT(ZERO) จะเกิดอะไรขึ้น? เพราะว่า ระบบที่เราสร้างนี้มันไม่มี -1 นะ

ดังนั้น อย่างแรกของการนิยาม DECREMENT หรือ predecessor function ก็คือการเขียนในรูปคณิตศาสตร์ที่รัดกุม และนั้นก็คือ


$$ DECREMENT(n)=\begin{cases}0 & if n = 0\\n-1 & otherwise\end{cases} $$


ตามรูปแบบคณิตศาสตร์ ก็นำมาเขียนเป็น function ได้ดังนี้

```js
const DECREMENT = function (n) {
    return function(p){
        return function(x){
            return n(function(g){
                return function(h) {
                    return h(g(p))
                }
            })(function(y){
                return x;
            })(function(y){
                return y;
            })
        }
    }
}
```

หรือ เขียนเป็น arrow functions
```js
const DECREMENT = (n)=>(p)=>(x)=>n((g)=>(h)=>h(g(p)))((y)=>x)((y)=>y);
```

เฮือกกก Orz มันคืออะไรเนี๊ยะ ที่เห็นว่ามันยาก ไม่ต้องตกใจ เพราะมันยากจริงๆนั้นแหละ (/me อ่านอยู่ 3 hr. ตอนนี้ยังงงๆ RIP)

มาลองพิจารณาที่ละขั้นตอนๆ แยะส่วนประกอบ แล้ว จัดรูปมันให้อยู่ในรูปฟังก์ชั่นหลายตัวแปร จะได้ว่า

```js
const X = (y=>x);                // x is argument in DECREMENT
const I = (y=>y);                // identity function

const DECREMENT = function (n) {
    return function(proc,x){
        return n(function(g){
            return function(h) {
                return h(g(proc))
            }
        }, X)(I)
    }
}
```

เพื่อให้มันง่ายขึ้น กำหนด
X คือ ฟังก์ชั่นที่รับอะไรก็ตาม จะ return x; และ
I คือ ฟังก์ชั่นที่รับอะไรก็ตาม จะ return ตัวที่รับมา;

จากความเดิมตอนที่แล้ว ตัวเลข N คือการดำเนินการเรียก proc N ครั้ง บนตัวแปร x ทำนองเดียวกัน เราสามารถ apply นิยามได้ดังนี้ กับสิ่งที่อยู่ภายใน DECREMENT จะได้ว่า [แทน n ลงในโค้ด]

```js
function(){
    var proc = function(g){
        return function(h) {
            return h(g(p))
        }
    }

    var x = X;
    return proc(proc(proc(... (x) ...)));
}(I)
```

**พิจารณาที่ n = ZERO;**

เพราะไม่มี proc ดังนั้น ภายใน DECREMENT ลดรูปเหลือแค่ X(I)

```js
>> DECREMENT(ZERO)
=> (...)=> { return X(I) };
=> (...)=> { return x };
=> ZERO
//ผ่านไป 1 กรณี
```

**พิจารณาที่ n > ZERO;**

เมื่อทดสอบรันดูแล้ว จะเห็นว่า g(p) ที่อยู่ภายใน proc จะให้ค่า x แค่ครั้งแรกครั้งเดียว หลังจากนั้นเราจะได้ p(p(p(...))) ซ้อนกันไปเรื่อยๆ หรือพูดได้ว่า p รันซ้อนกันทั้งหมด n-1 ชั้น นั้นเอง

และนอกจากนี้ ในชั้นสุดท้าย จะได้ h(...) ซึ่งเมื่อโดน apply ด้วย (I) ก็จะโดนปลด h(...) => ...

```js
>> proc(x)
=> function(h) {
    return h(x)
}

>> proc(proc(x))
=> function(h) {
    return h(p(x))
}

>> proc(proc(proc(x))) 
=> function(h) {
    return h(p(p(x)))
}

>> h(p(p(p(p(...)))))(I) = 
=> p(p(p(p(...))))
```

ดังนั้น

```js
>> DECREMENT(N)
=> (...)=> { return p(p(p(...))) }; //n-1 nested
=> N-1
```

ฉลองงงงงงง~ เราทำได้ เราทำได้ ชิตังเม โป้ง //ผิด
* ความจริงแล้ว เราสามารถ implement predecessor function ได้อีกหลายวิธี ซึ่งอาจจะง่ายกว่า โดยใช้ If

หลังจากลำบากตรากตรำกับการสร้าง decrementing function ถึงเวลาที่เราจะเจอกับ SUBTRACT, DIVIDE และ MODULO แต่ในข่าวดีก็มีข่าวร้ายว่า จากเครื่องมือที่เรามีตอนนี้ เราสามารถสร้างได้เพียง SUBTRACT //กรรม

```js
const SUBTRACT = (n)=>(m)=>(n(DECREMENT)(m));
```

ทั้งนี้ ข้อระวังในการใช้ SUBTRACT คือ

```js
>> SUBTRACT(THREE)(ONE);
=> TWO

>> SUBTRACT(ONE)(THREE);
=> ZERO
```

กรรม สิ่งที่ /me ทำมาทั้งหมด คืออะไร?

ไม่ต้องเสียใจ Operation ที่เราได้ ถึงแม้ว่ามันจะไม่ใช่ SUBTRACT อย่างสมบูรณ์ (เพราะเงื่อนไขจากฟังก์ชั่น DECREMENT

ทำให้ทุกครั้งที่ได้ค่าน้อยกว่า ZERO มันจะ return ZERO แทน) แต่ก็สามารถเอาไปใช้กับ isPrime(n) ได้อย่างไม่ต้องกังวล

สำหรับ ตัวดำเนินการแบบนี้ เรียกอีกชื่อว่า [Monus](https://en.wikipedia.org/wiki/Monus)

เพราะ /me บอกแล้วว่า ตอนนี้เราออกแบบระบบสำหรับ Natural numbers เท่านั้น จึงถือว่าไม่น่ากังวลเท่าไรนัก

และสำหรับ DIVIDE และ MODULO คงต้องผลัดไปในตอนต่อๆไป จนกว่าเราจะมีเครื่องมือมากพอ

สำหรับตอนนี้ ก็จบลงเพียงแค่นี้

และบทต่อไป จะได้เจอกับ data type อีกอันที่เป็นไม้เบื่อไม่เมากับโปรแกรมเมอร์มาช้านาน Booleans

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

ขอบคุณ คำอธิบาย Predecessor เพิ่มเติมจาก
[Lambda calculus predecessor function reduction steps](http://stackoverflow.com/questions/8790249/lambda-calculus-predecessor-function-reduction-steps)
