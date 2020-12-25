---
layout: post
title: Set Environment for Web Developer EP.2
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/set-env-for-web-developer/mautic_developer_mautician-720x340.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

ต่อจาก <a href="http://wp.curve.in.th/set-env-for-web-developer"> EP.1 </a> ในบทความนี้จะพูดถึง Frontend Task โดยใช้ Gulp 
<!--more-->

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1cq0ZEXWF6Qeo5k7hW3oWmKN6NYI0Mtt-" column=1 %}

แทนที่เราจะต้องลงโปรแกรมต่างๆ เพื่อให้เครื่องคอมสุดที่รักของเราสามารถรัน Web ได้ /me ก็ได้แนะนำให้ทุกคนเปลี่ยนมาทำงานบน VMs ใน [EP.1](http://wp.curve.in.th/set-env-for-web-developer) ไปแล้ว ซึ่งมีเครื่องมืออย่าง Vagrant มาช่วยเราจัดการความวุ่นวายบน VMs

แต่ แต่ แต่ ปัญหามันไม่ได้จบแค่นี้

เพราะปัจจุบันจะพบว่า web ไม่ใช้แค่ static content อีกต่อไป

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1rFwKJ5p92PIDMwGz9vDZBKEFDp8qiiC6" column=1 %}

เรามาอยู่ในจุดที่ทุกคนต้องการเวปที่มีความ dynamic
* กดตรงนั้น จะมี popup ขึ้นมา
* กดตรงนี้ จะต้องซ่อนเมนู
* ถ้าเน็ตหลุดจะทำ offline mode ได้
* มีคนทักมา จะต้องมี noti เด้งขึ้นมา
* สามารถกดแชร์ลงเฟสบุ๊คได้
* ผู้ใช้เพิ่มเนื้อหาของตัวเองได้
* และ ต้องเปิดได้ในทุกๆขนาดหน้าจอ
* บลาๆ

บางเวปไซท์สามารถแสดงผลเป็น 3D [Ex](http://www.dock.cz/en/about) 

หรืออาจจะทำเป็นเรื่องราว [Ex](http://www.cabletv.com/the-walking-dead) 

หรือไม่ก็สามารถ interact กับผู้ใช้ได้ [Ex](http://www.guillaumejuvenet.com/#project) 

<span class="tag-en">#โลกหมุนไปไวจนฉันตามไม่ทันแล้วพี่บัวลอย</span>

ซึ่งเวปเหล่านี้ก็จะกลายเป็นงานที่ Web developer อย่างเราๆต้องทำ และนั้นหมายถึงการต้องใช้ภาษาเดิมๆ อย่าง javascript, css และ html ที่ไม่ได้ออกแบบมาให้สามารถทำได้ขนาดนี้ ถึงจะสามารถทำได้จริงๆ แต่ก็ต้องใช้โค้ดที่ยาก ซับซ้อนและวุ่นวาย

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1-gcDdGHtKdCuwJqWhhKQJqc6nk2pTPuB" column=1 %}

ดังนั้นการเขียนเวปจึงเริ่มเปลี่ยนไป เราเริ่มต้องภาษาใหม่ๆ เครื่องมือใหม่ๆเอามาทดแทนเอาไปทดแทนของเดิมที่มีอยู่แล้ว เช่น ES6, JSX, Typescript, Plug(ชื่อเดิมว่า Jade), Sass, Elm, Flow และอีกมากมาย

{% include aligner.html images="https://drive.google.com/uc?export=view&id=13yTj_TBzfvLxJySerJV4O5bnrtVbUz-_" column=1 %}

ซึ่งแต่ละเครื่องมือก็เข้ามาแก้ปัญหาที่แตกต่างกันออกไป เช่น

* **ES6** เป็นการมาตรฐานโค้ดแบบใหม่ของ Javascript ทำให้เราสามารถจัดการ OOP ได้ง่ายขึ้น, สามารถต่อสู้กับการฟังก์ชัน Asynchronous ได้ง่ายขึ้น และ จุดเพิ่มเติมอีกมากมาย
* **JSX** รวมการสร้าง HTML มาอยู่บน Javascipt ทำให้เราสามารถจัดการทั้ง Model-View-Controller ได้โดยใช้แค่ .js ไม่กี่ไฟล์
* **Typescript** เพิ่ม variable type ให้กับ Javascript ทำให้เราสามารถตรวจสอบความผิดปกติของโค้ดได้ดีขึ้น ไม่ต้องรอให้ไปอยู่บนหน้าเวป
* **Plug** เปลี่ยน html ทำให้เราไม่จำเป็นต้องมี tag เปิด-ปิด อีกต่อไป โค้ด html ก็จะง่ายขึ้นมากมาย
* **Sass** ทำให้สามารถประกาศตัวแปรได้ใน css หรือ จะประกาศเป็น function ก็ได้เหมือนกัน

และอื่นๆอีกเยอะแยะ


ไม่เพียงแค่นั้นเครื่องมือเหล่านี้ก็มาพร้อมกับ concept การเขียนโค้ดแบบใหม่ๆให้เราใช้ อย่าง flux architure, 2-way binding, reactive programming, singlepage application, ...

แต่การเครื่องมือใหม่ๆเหล่านี้ไม่สามารถใช้ได้ใน browser ปัจจุบัน แปลว่าทุกครั้งที่เราต้่องการให้โค้ดเหล่านี้แสดงผล เราต้องทำการ compile/transpile ให้มันอยู่ในรูปแบบเดิมๆ javascript, css และ html แบบเดิมๆ

และแน่นอนว่า สิ่งที่เราต้องเขียน ไม่ได้มีแค่ js ง่ายๆแค่ไฟล์เดียว อย่างโปรเจคปัจจุบัน /me เขียนไปแล้วกว่า 50 ไฟล์ และก็ต้องเป็นหน้าที่เราที่ต้อง merge ไฟล์ทั้งหมดมารวมกัน

นอกจากนี้แล้ว เพื่อการเป็น "**developer ที่ดี**" <span class="tag-en">#ทำตัวหนา</span> เราอาจจะต้องเขียนเทสเคส, รันเทส, ลดขนาดรูป, ย่อขนาด js และ รีเฟรชบราวเซอร์

สรุปรายการที่ /me ต้องทำหลังจากแก้โค้ด 1 ครั้ง

* compile
* merge
* test
* minify js/css
* compress image
* reload browser

{% include aligner.html images="https://drive.google.com/uc?export=view&id=142syKqt55hO3jhY9fAa7D6oXyMGMuP9F" column=1 %}

<div class="blockquote">It’s 2016. No one transpiles JS/CSS/HTML directly anymore.</div>

เหตุนี้จึงเป็นที่มาของเครื่องมือที่ชื่อว่า Gulp //ความจริงมี Grant อีกตัว แต่ไม่เคยใช้ 555

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1p0R-uRZRTPKqaNgMKh5ztKxnvM1DCqKb" column=1 %}
Gulp เป็น task runner ซึ่งทำหน้าที่คอยสอดส่องไฟล์ต่างๆ และทำงานบางอย่างเมื่อเกิดการเปลี่ยนแปลงในไฟล์ที่เราต้องการ

เดิมทีแล้ว Gulp เป็นแค่ node module เล็กๆ ถ้าเราต้องการจะทำอะไร ก็ลง gulp plugin ปลั๊กเข้าไป

ทำให้ Gulp มีความยืดหยุ่น และ หลากหลาย และ โครงสร้างของ Gulp ก็ง่ายมากๆ เพราะมันใช้รูปแบบ pipline หรือ streaming โดยจะรับ input เข้ามา แล้วพ่น output ต่อๆไปเรื่อยๆ ต้องการทำอะไร ก็ส่งต่อๆกันไป เหมือน "\|" ใน ubuntu

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1USphTIbyiB3LoZy1HFwPTTbAj5mzLO-I" column=1 %}

และการเริ่มใช้ Gulp ก็แค่ เริ่มต้นจากการหา gulp plugin ที่เราต้องการ อาจจะเป็น gulp-sass, gulp-minify-css, gulp-uglify, gulp-typescript และอิีกมากมาย เอาเป็นว่า น่าจะมีทุกอย่างที่ต้องการ

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1A-dMVjAIDW6RrQumF-BgmrHpTJcLaRPG" column=1 %}

หลัังจากนั้น ก็นิยาม task, watch และ default

โดย task คืองานที่ต้องการให้ gulp ทำ, watch คือ การกำหนดให้ gulp จับตาดูไฟล์ที่กำหนดไว้ เมื่อมีการเปลี่ยนแปลงก็จะให้ทำ task ที่เราต้องการ และ default คือ task ที่จะเร่ิมทำทุกครั้งที่รัน gulp

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1mZTTa2YCd3LwrwdfqisaWdhd0dnZVt_S" column=1 %}

และสุดท้าย ก็ `gulp` ซะ

{% include aligner.html images="https://drive.google.com/uc?export=view&id=18mjUktLYQsjM-6l3iprK0mr9ABPR7XTd" column=1 %}

แค่นี้ ก็ไม่ต้องไปคิดเรื่อง compile หรือ reload browser อีกต่อไป <span class="tag-en">#ชีวิตดี๊ดี</span>

และทั้งหมดนี้ ก็คือสรุปหัวข้อบรรยาย "**Set Environment for Web Developer**" โดย /me ยังไงก็ขอขอบคุณที่อ่านมาถึงจุดนี้ เย้ๆๆ แล้วมาแบ่งปันความรู้กันอีกนะ

<div class="blockquote">อย่าเอาคำว่า "ไม่มีเวลา" มาเป็นข้ออ้างที่จะหยุดเรียนรู้ เทคโนโลยีพัฒนาไปทุกวัน เราไม่สามารถบังคับให้คนอื่นก้าวช้าๆรอเราได้ เราต้องพัฒนาตัวเองแล้วพาตัวเองให้ทันคนอื่นๆ</div>
