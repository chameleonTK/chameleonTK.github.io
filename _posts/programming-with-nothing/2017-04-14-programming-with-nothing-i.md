---
layout: post
title: "Programming with Nothing : Introduction"
tags: [Archive, Code Code and Code, Programming With Nothing]
thumbnail: "assets/feats/programming-with-nothing/iStock_000031670186Small.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

การเขียนโปรแกรม เป็นทั้งเรื่องของศาสตร์และศิลป์ เพราะการแก้ไขปัญหาหนึ่งๆนั้น ไม่ได้มีแค่แนวทางเดียว บางแนวทางก็ง่ายมากมาย บางวิธีก็ซับซ้อนจนไม่สามารถเข้าใจได้ 

แต่ จริงๆแล้ว แค่เพียงภาษาโปรแกรมนั้นสามารถสร้าง function ได้ ก็เพียงพอที่จะสามารถแก้ไขทุกๆปัญหาที่แก้ได้ด้วย Computer ดังนั้นการแก้ปัญหาด้วย functions ก็เป็นอีกหนึ่งวิธีที่น่าสนใจ

<!--more-->

การเขียนโปรแกรม เป็นทั้งเรื่องของศาสตร์และศิลป์ เพราะการแก้ไขปัญหาหนึ่งๆนั้น ไม่ได้มีแค่แนวทางเดียว บางแนวทางก็ง่ายมากมาย บางวิธีก็ซับซ้อนจนไม่สามารถเข้าใจได้ แต่แน่นอนว่าแต่ละวิธีการก็ย่อมมีข้อดีข้อเด่นของตัวมันเอง

บทความหนึ่ง ซึ่งเป็นแรงบันดาลใจในการเขียนบทความนี้ คือ [Programming with Nothing](https://codon.com/programming-with-nothing) ของ [@tomstuart](http://twitter.com/tomstuart) ซึ่งเล่าว่า จริงๆแล้ว แค่เพียงภาษาโปรแกรมนั้นสามารถสร้าง function ได้ ก็เพียงพอที่จะสามารถแก้ไขทุกๆปัญหาที่แก้ได้ด้วย Computer ดังนั้นการแก้ปัญหาด้วย functions ก็เป็นอีกหนึ่งวิธีที่น่าสนใจ

{% include aligner.html images="https://lh3.googleusercontent.com/d/1rU59-3vStf17MBQfSB4koCwn3KOjkL5u" column=1 %}

/me อยากลองเขียนโค้ดโดยใช้แค่ฟังก์ชั่นขึ้นมาจริงๆด้วยภาษา javascript [ต้นฉบับเขาเขียนด้วย Ruby ฮะ] โดยในบทความนี้อาจจะมีเนื้อหาหลายส่วนไม่เหมือนกับต้นฉบับ มีการลดทอนและเพิ่มเติมส่วนที่ /me สนใจ แต่ยังคงใช้รูปแบบเหมือนกับที่ [@tomstuart](http://twitter.com/tomstuart) เสนอเอาไว้ คือ หลังจากนี้ไป เราจะลืมการใช้ Library, Modules, NPM, Classes, Objects หรือ แม้กระทั้ง Arrays, Strings, Numbers และ Booleans

สิ่งที่เหลืออยู่ เพียง 2 อย่างก็คือ
* Creating Functions
* Calling Functions
Aiming high

เดิมทีเป้าหมายเดิมฉบับ Original คือ ความพยายามเพื่อเขียน FizzBuzz program

<div class="blockquote">Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.</div>

ซึ่งเป็นโค้ดคลาสสิก สำหรับสัมภาษณ์งานโปรแกรมเมอร์ในยุค 200x ซึ่ง /me ไม่อินกับเจ้าโปรแกรมนี้เท่าไรนัก ในบทความนี้จึงขอเปลี่ยนเป็นโค้ดคลาสสิกอีกอันที่ /me จำได้ว่าเป็น challange แรกที่ทำให้ /me เข้าสู่วงการคอมพิวเตอร์

<div class="blockquote">IsPrime(n): Find whether a given number is prime or not?</div>

หรือ เขียนเป็น pseudo-code ง่ายๆ แบบนี้
```python
def isPrime(p):

    for i in range(2,p):
        if p%i==0:
            return "Not Prime"
    return p
```

ซึ่งแน่นอนว่า สิ่งที่ /me ต้องเขียนก็คือ การใช้แค่ function เพื่อแทนที่โค้ดทั้งหมดไม่ว่าจะเป็น for loop, range, if condition และรวมไปถึง string representation

# Thinking procs

ก่อนที่เราจะเริ่มเขียน isPrime(p) ตอนนี้จะขอใช้เวลา 2-3 นาทีเพื่อปรับความเข้าใจสำหรับคำว่า **"function"** และรายละเอียดเล็กๆน้อยๆที่น่าสนใจของเจ้าฟังก์ชั่นเหล่านี้

### Function is Black box.

{% include aligner.html images="https://lh3.googleusercontent.com/d/17hov9k-ww2r96UN4YfP_hCSavsT3p8oL" column=1 %}


นิยามง่ายๆของคำว่า ฟังค์ชั่น คงหนีไม่พ้นคำว่า "กล่องดำที่เราไม่จำเป็นต้องรู้กระบวนการภายในกล่อง" การสร้างฟังก์ชั่น ก็คือ การสร้างกล่องเครื่องมืออันหนึ่งซึ่งรับ input เข้าไปผ่านกระบวนการอะไรสักอย่างที่เราไม่จำเป็นต้องรู้ แล้วสามารถพ่น output ออกมาได้ สมมติ

```js
function (m, n) {
    return m+n
} (10, 20)
```

เมื่อ /me ใส่ค่า 10 และ 20 เป็น input เข้าไปในฟังก์ชั่น อะไรซักอย่าง สิ่งที่เกิดขึ้น คือ ฟังก์ชั่นทำการคำนวนแล้วให้คำตอบออกมา ฟังก์ชั่นที่ให้คำตอบเหมือนกัน ถึงแม้ว่ากระบวนการภายในต่างกัน ก็ยังถือเป็นฟังก์ชั่นเดียวกัน

ดังนั้น ไม่ว่าจะเป็นโค้ดนี้

```js
function (m, n) {
    var carry = m & n;
    var result = m ^ n;
    while(carry != 0)
    {
        var shiftedcarry = carry << 1;
        carry = result & shiftedcarry;
        result ^= shiftedcarry;
    }
    return result
} (10, 20)
```

หรือ

```js
function (m, n) {
    var carry = m & n;
    var result = m ^ n;
    while(carry != 0)
    {
        var shiftedcarry = carry << 1;
        carry = result & shiftedcarry;
        result ^= shiftedcarry;
    }
    return result
} (10, 20)
```

หรือ โค้ดนี้

```js
function (a, b) {
    if(b == 0)
        return a;
    return adder3( a ^ b, (a & b) << 1);
}
```

ก็คือ black box กล่องเดียวกันที่เรามักตั้งชื่อมันว่า adder

### Same Input, Same Output

ทุกครั้งที่เราใส่ input เดิมลงไปในฟังก์ชั่น เดิม ก็จำเป็นต้องได้ค่าเหมือนเดิม ซึ่งนี้เป็นส่วนหนึ่งของแนวคิดที่เรียกว่า [Stateless programming](https://www.quora.com/What-is-stateless-programming-and-what-are-some-examples) ทำให้ไม่ว่ากล่องดำอันนี้จะอยู่ที่ไหนก็ตาม มันก็คงพฤติกรรมเดิม และเราสามารถคาดเดาพฤติกรรมของมันได้

### No need for multiple arguments

เมื่อมีฟังก์ชั่นแล้ว สิ่งที่ขาดไปไม่ได้ คือ arguments หรือ ตัวแปรต่างๆสำหรับสำหรับการคำนวน แต่ทั้งนี้มีเทคนิคหนึ่ง ที่เรียกว่า [Currying](https://en.wikipedia.org/wiki/Currying) ซึ่งสามารถจัดรูปใหม่ สำหรับทุกๆฟังก์ชั่นที่รับหลายตัวแปร ให้กลายเป็นแค่ฟังก์ชั่น 1 ตัวแปร(nested single-argument function) //ว้าวววว

จากตัวอย่างเดิม จะสามารถจัดรูปแบบเป็น

```js
function (m) {
    return function(n){
        return m+n
    }
} (10) (20)
```

เมื่อฟังก์ชั่นที่อยู่ชั้นนอกรับค่าตัวแปร m แล้วสิ่งที่มันทำแตกต่างจากเดิม คือ การคืนค่าฟังก์ชั่นอีกตัวซึ่งรอรับตัวแปร n เพื่อคำนวน เมื่อใส่ argument ครบแล้วมันถึงจะเริ่มการคำนวน

# Javascript functions

แต่ละภาษา ต่างมีวิธีการเขียนฟังก์ชั่น หรือ บางภาษาโปรแกรม อย่าง ruby เรียกฟังก์ชั่นแทนด้วย procedure และมีวิธีประกาศฟังก์ชั่นได้หลายวิธี สำหรับภาษา javascript ก็มีวิธีการประกาศฟังก์ชั่นหลายรูปแบบไม่แพ้ภาษาอื่นๆ

```js
function A(){};             // function declaration
var B = function(){};       // function expression
var C = (function(){});     // function expression with grouping operators
var D = function foo(){};   // named function expression
var E = (function(){        // IIFE that returns a function
  return function(){}
})();

var F = new Function();     // Function constructor
var G = new function(){};   // special case: object constructor
var H = x => x * 2;         // ES6 arrow function
```

แต่อย่างไรก็ตามทุกๆรูปแบบ ใช้ calling function เหมือนกัน คือ การใส่ (x) ด้านหลัง function

```js
(x => x * 2) (20);
```

ทั้งนี้ ในบทความนี้จะเลือกใช้ arrow function เป็นรูปแบบหลักของการใช้ประกาศฟังก์ชั่นต่างๆ :)

อย่างไรก็ตาม /me คิดว่าบทความนี้ คงเป็นอีกบทความที่น่าจะยาวๆมากๆ จึงคิดว่า ควรจะแบ่งออกเป็นหลายๆตอน //เพื่อจะอู้เขียนบ้างไม่เขียนบ้าง สำหรับตอนที่ 1 ก็คงจบลงเพียงเท่านี้

แล้วมาเจอกันในตอนต่อไปว่า เราจะแทนเจ้าฟังก์ชั่นพวกนี้เป็นตัวเลขได้ยังไง แล้วมันจะสามารถดำเนินการบวก, ลบ, คูณ, หารกันได้ยังไง?
//ขอบคุณครับที่อ่านจนจบ
