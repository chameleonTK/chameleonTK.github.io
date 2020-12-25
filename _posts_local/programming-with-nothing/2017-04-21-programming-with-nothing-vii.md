---
layout: post
title: "Programming with Nothing : List"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/img/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

หลังจาก /me ผจญภัยในการสร้างเครื่องมือมาแล้วกว่าครึ่ง เรากลับมาพบกับความจริงที่ว่า psudo-code ที่เราร่างไว้นี้ มันไม่น่าจะสามารถสร้างเป็น function ที่ใช้เฉพาะ functions ได้จริงๆ แต่เราก็ยังมีทางออก ซึ่งต้องใช้ความช่วยเหลือจากเพื่อนยากที่ชื่อว่า  List
<!--more-->

เพราะว่าอะไร?

```js
const isPrime = (p)=>{
   for i in range(TWO,p):
        IF(IS_ZERO(MODULO(p)(i)))( return "Not Prime")(null)
    return p
}
```

สิ่งหนึ่งที่เป็นปัญหาสำคัญที่สุดในตอนนี้ คือ คำสั่ง for เนื่องจากการใช้ for ในแบบนี้ แอบมีสิ่งที่เราไม่พึงปราถนาเกิดขึ้น และมันก็คือ ตัวแปร และ assignment semantics เพราะเราจำเป็นต้องมีตัวแปร i เป็น counter ในการนับจำนวนรอบ

นอกจากนี้แล้ว psudo-code นี้ก็ดูแปลกประหลาดเกินไปสำหรับการสร้างเป็น function with functions

/me จึงจำใจสร้างมันขึ้นมาใหม่ โดยการใช้เครื่องมือตัวใหม่ ไฉไลกว่าเดิม

# List

List เป็น data structure ที่ทำให้ /me สามารถสร้างข้อมูลที่มีความสัมพันธ์ต่อๆกัน นอกจาก List แล้วยังต้องมี function ที่จำเป็นในการเข้าถึง List ไม่ว่าจะเป็น `isEmpty()`, `first()`,`range()`, `map()`, `reduce()` ซึ่งเจ้า function เหล่านี้เป็นกุณแจที่สามารถช่วยให้เราสร้าง loop ขึ้นมาได้อีกด้วย

ด้วยความรู้พวกนี้ เราสามารถเขียน psudo-code v2 ขึ้นมาใหม่ดังนี้

```js
//range is not valid in javascript
function range(start, target){
  if (target < start) {
    return [];
  } else {
    return Array.apply(0, Array(target-start))
      .map(function (element, index) { 
        return index + start;  
    });  
  }
} 

function isPrime(n){
  return range(2, n).reduce(function(acc, val){
    if (n%val==0){
      return "NOT Prime";
    } else {
      return acc
    }
  }, n+"")
}

// Test
range(2,100).forEach(function(n){
  if (isPrime(n)){
    console.log(n);
  }
})
```

แน่นอนว่าโค้ดนี้ สามารถเอาไปรันได้จริงๆ ใน native javascript

และเมื่อเปลี่ยน psudo-code ใหม่ ทำให้เราจำเป็นต้องสร้างฟังก์ชั่นอีก 2 ตัว คือ `range()` และ `reduce()` และทั้งคู่ต่างเป็น function ที่มาคู่กับการใช้ List

## กลับมาที่หัวข้อ "List" อีกครั้ง

วิธีที่ง่ายที่สุดที่ /me สามารถสร้าง List ขึ้นมาได้นั้น คือ การใช้ Pairs หรือ คู่ลำดับ ซึ่งเจ้าคู่ลำดับนี้นอกจากสามารถใช้ในการสร้าง List แล้ว ยังสามารถนำไปใช้ในการสร้าง Tree หรือ data type ประเภทอื่นๆอีกมากมาย (โดยเฉพาะคนที่คุ้นเคยกับการใช้ cons ใน Lips)

ซึ่งโครงสร้างแบบนี้สามารถแทนได้ด้วยฟังก์ชั่นดังนี้

```js
const PAIR = x=>y=>f=>f(x)(y);
const LEFT = p=>p(x=>y=>x)
const RIGHT = p=>p(x=>y=>y)
```

จิตนาการว่า Pair คือ คู่ลำดับ <x, y>

โดยที่ PAIR เป็นฟังก์ชั่นรับ 2 ซึ่งตัวแปรแรกเป็น ของที่อยู่ทางซ้าย และ ของที่อยู่ทางขวา แล้ว return เป็นฟังก์ชั่นที่รอดำเนินการอะไรสักอย่างกับของทั้ง 2 ชิ้น

```js
>> PAIR(ONE)(THREE)
=> (f)=>f(ONE)(THREE)
```

โดยที่ LEFT, RIGHT คือ ฟังก์ชั่นรับคู่ลำดับแล้วดำเนินการ เลือกของชิ้นแรก(ทางซ้าย) และ เลือกของชิ้นที่ 2 (ทางขวา) ตามลำดับ ดังนั้นเราจะสามารถเข้าถึงค่าของ PAIR ได้โดยการใช้ฟังก์ชั่นทั้ง 2 นี้

สำหรับการสร้าง List ด้วย pair นั้น เราสามารถสร้างได้หลากหลายรูปแบบ และรูปแบบที่ง่ายที่สุด ก็คือ "linked list" โดยการสร้างแต่ละ PAIR เก็บ value และอีกด้านชี้ไปยัง PAIR คู่ถัดๆไป ตามรูป

{% include aligner.html images="programming-with-nothing/Guy_Steele_parallel_programing_lisp_cons-2.png" column=1 %}

//ตัวอย่าง linked list และแถมตัวอย่างสำหรับคนที่อยากจะสร้าง tree

ถึงแม้ว่าจะต้องการให้เป็นไปตามรูป แต่สำหรับการ implement จริงๆเราต้องการรูปแบบที่ซับซ้อนกว่านั้น เพราะมันขาด pointer NULL ที่เป็น pointer ตัวสุดท้าย ชี้ไปยังพื้นที่ว่างเปล่า ซึ่งจำเป็นสำหรับการสร้าง list ว่าง

โครงสร้างหนึ่งที่สามารถนำมาใช้แทน linked list จาก PAIR เรียกว่า **"Two pairs as a list node"** โดย เราจะใช้ PAIR 2 ชั้น สำหรับ ทุกๆ node ดังนี้

```js
>> NODE => <first, <second.first,="" second.second="">>

</first,>
```

โดย
* first เป็น flag บอกสถาณะ isEmpty ของ list
* second.first เป็น head (ของที่อยู่ทางซ้าย)
* second.second เป็น tail (ของที่อยู่ทางขวา)

โดยเริ่มต้น แทน NULL หรือ EMPTY ด้วย
const EMPTY = PAIR(TRUE)(TRUE)

ฟังก์ชั่นพื้นฐานที่เหลือในการสร้าง linked list ดังนี้

```js
const EMPTY = PAIR(TRUE)(TRUE)
const IS_EMPTY  = LEFT

const UNSHIFT = l=>x=>PAIR(FALSE)(PAIR(x)(l))
const FIRST = l=>LEFT(RIGHT(l))
const REST = l=>RIGHT(RIGHT(l))
```

โดยแต่ละฟังก์ชั่นสามารถเข้าใจได้ไม่ยาก เมื่อพิจารณาจากโครงสร้าง list ดังนี้

```js
>> EMPTY
=> <true, true="">

>> UNSHIFT(EMPTY, ONE)
=> <false, <one,="" empty="">>

>> UNSHIFT(UNSHIFT(EMPTY, ONE), TWO)
=> <false, <two,="" unshift(empty,="" one)="">>
=> <false, <two,="" <false,="" <one,="" empty="">>>>

</false,></false,></false,></true,>
```

เพื่อความสะดวก /me จะสร้าง to_array สำหรับดึงทุกๆ items ออกมาจาก list และแปลงเป็น native array

```js
function to_array(l){
    var arr = [];
    while(!to_boolean(IS_EMPTY(l))) {
        arr.push(FIRST(l))
        l = REST(l);
    }
    return arr
}
```

หลังจากมี List แล้วก็กลับมาที่เป้าหมายของเรา : RANGE()

## RANGE

นึกๆดูแล้วมันง่ายมากสำหรับที่จะสร้างฟังก์ชั่นนี้โดยวิธีแบบ native

```js
function range(m, n){
    var opt = []
    for(var i=m; i<n; i++) {
        opt.push(i)
    }

    return opt;
}
```

แต่ด้วยปัญหาเดิมๆ เราไม่สามารถใช้วิธีนี้ได้ เพราะว่า มันอาศัยการประกาศตัวแปร และแน่นอนว่ามันขัดกับปรัชญาหลักของบทความนี้ ดังนั้น อีกหนึ่งตัวเลือก คือ การสร้าง range โดยใช้ recursion

```js
function range(m, n){
    if (m<n) {
        return range(m+1, n).unshift(m)
    } else {
        return []
    }
}
```

และด้วยความชำนาญในการสร้าง recursive functions ที่ศึกษามาแล้วใน [EP.6](http://wp.curve.in.th/programming-with-nothing-vi) จะได้ว่า

```js
//human-readable version
const RANGE = Z(f=>{
    return m=>n=>{
        return IF(LESS_THAN(m)(n))
            (x=>UNSHIFT(f(INCREMENT(m))(n))(m)(x))
            (EMPTY)
    }
})

const RANGE = Z(f=>m=>n=>IF(LESS_THAN(m)(n))(x=>UNSHIFT(f(INCREMENT(m))(n))(m)(x))(EMPTY))
>> to_array(RANGE(TWO)(FIVE)).map(item=>to_integer(item))
=> [2, 3, 4]
```

กลับไปที่โค้ด isPrime(n) อีกครั้ง

```js
function isPrime(n){
  return RANGE(2)(n).reduce(function(acc, val){
    if (n%val==0){
      return "NOT Prime";
    } else {
      return acc
    }
  }, n+"")
}
```

## Reduce/Fold

ปราการสุดท้าย อีก 1 ฟังก์ชั่น ที่กำลังรอการ implement ก็คือ reduce หรือบางครั้ง เราเรียกมันว่า fold ซึ่งเป็นฟังก์ชั่นทำหน้าที่ merge แต่ละ item ใน list เขาด้วยกันเป็น 1 value เช่น

```js
// Example : concatinate array of chars

>>  ["R", "I", "M", "E"].reduce(function(acc, item){ 
...    return acc+item
... }, "P")

=> loop1: item = "R", acc = "P"
=> loop2: item = "I", acc = "PR"
=> loop3: item = "M", acc = "PRI" 
=> loop4: item = "E", acc = "PRIM"
=> loop5: return "PRIME"
```

โดยความแตกต่างเพียงอย่างเดียวระหว่าง recuce และ fold ก็คือ
* เราต้องกำหนด initial value ให้สำหรับ fold(lst)
* แต่เราไม่ต้องกำหนด initial value ให้ reduce(lst) โดยจะมี initial = lst[0] อัตโนมัติ

หรืออาจจะพูดได้ว่า fold เป็น general case ของ reduce เลยก็ว่าได้

Note: จริงๆแล้วใน recude ใน javascipt สามารถเป็นได้ทั้ง fold และ reduce

สามารถ implement fold ได้โดยใช้ recursive ได้ดังนี้

```js
// Fold right
function FOLD(list, acc, action) {
    if (list.length==0){
        return acc
    } else {
        var thisItem = list.pop();
        var remainList = list; //list.pop() change itself
        return action(FOLD(remainList, acc, action), thisItem)
    }
}

//Example
>> FOLD([1, 2, 3], 0, plus)
=> plus(FOLD([2, 3], 0, plus), 1)
=> plus(plus(FOLD([3], 0, plus), 2), 1)
=> plus(plus(plus(FOLD([], 0, plus), 3), 2), 1)
=> plus(plus(plus(0, 3), 2), 1)
=> plus(plus(3, 2), 1)
=> plus(5, 1)
=> 6
```

ทั้งนี้ ยังมีอีกวิธีในการสร้าง fold เรียกว่า Fold left

```js
// Fold left
function FOLD(list, acc, action) {
    if (list.length==0){
        return acc
    } else {
        var thisItem = list.pop();
        var remainList = list; //list.pop() change itself
        return FOLD(remainList, action(acc, thisItem), action);
    }
}

//Example
>> FOLD([1, 2, 3], 0, plus)
=> FOLD([2, 3], plus(0, 1), plus)
=> FOLD([3], plus(2, plus(0, 1)), plus)
=> FOLD([], plus(3, plus(2, plus(0, 1))), plus)
=> plus(3, plus(2, plus(0, 1)))
=> plus(3, plus(2, 1))
=> plus(3, 3)
=> 3
```

ไม่ว่าจะเป็น Fold left หรือ Fold right ทั้งคู่ต่างมีความสามารถเท่าเทียมกัน (ในที่นี้จะเลือกใช้ Fold right) และสามารถเปลี่ยนให้อยู่ในรูปฟังก์ชั่นได้ดังนี้

```js
const FOLD = Z(f=>{
    return l=>x=>g=>{
        return IF(IS_EMPTY(l))
            (x)
            (y=> g(f(REST(l))(x)(g))(FIRST(l))(y))
    }
})

>> to_integer(FOLD(RANGE(ONE)(FIVE))(ZERO)(PLUS))
=> 1+2+3+4
=> 10

>> to_integer(FOLD(RANGE(ONE)(FIVE))(ONE)(MULTIPLY))
=> 1*2*3*4
=> 24

จากนั้นก็ยังสามารถใช้ FOLD ไปสร้าง MAP ที่ทำหน้าที่ใช้การเปลี่ยนทุกๆ items ใน list ตามฟังก์ชั่น f ได้ดังนี้
//human-readable
const MAP = list=>f=>{
    return FOLD(list)(EMPTY)(acc=>item=>{
        return UNSHIFT(acc)(f(item))
    })
}

const MAP = l=>f=>FOLD(l)(EMPTY)(k=>i=>UNSHIFT(k)(f(i)))
>> r = RANGE(ONE)(FIVE);
>> f1 = a=>POWER(a)(TWO)
>> to_array(MAP(r)(f1)).map(i=>to_integer(i))
=> [2, 4, 8, 16 ]

>> f2 = a=>POWER(a)(TWO)
>> to_array(MAP(r)(f2)).map(i=>to_integer(i))
=> [1, 4, 9, 16]
```

เมื่อได้เครื่องมือทุกอย่างพร้อมแล้ว ลุยกันต่อใน isPrime(n) โดยการแทนทุกๆฟังก์ชั่นลงใน psudo-code จะได้ว่า

```js
const isPrime = (N)=>{
    return FOLD(RANGE(TWO)(N))(TRUE)(acc=>n=>{
        return IF(IS_ZERO(MODULO(N)(n)))(FALSE)(acc)
    })
}
```

ลองทดสอบอีกครั้ง กับ ทุกๆตัวเลขในช่วง 2-100

```js
const TEN = MULTIPLY(TWO)(FIVE)
const HUNDRED = MULTIPLY(TEN)(TEN)

>> to_array(MAP(RANGE(TWO)(HUNDRED))(n=>isPrime(n)))
... forEach((b,i)=>{
...    if (to_boolean(b)){
...        console.log(i+2);        /// print prime 
...    }
... })
=> 2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

เห้ยยยยย มันคืออะไรอะ? มันใช่ prime numbers รึปล่าวนะ? ใช่จริงๆด้วย

ฮูเร้ๆๆๆ เสร็จแล้วววววววววว our isPrime(n)

และบทต่อไป กับการปรับ output อีกเล็กๆน้อยๆ ให้อยู่ในรูป string แบบเกร๋ๆ

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