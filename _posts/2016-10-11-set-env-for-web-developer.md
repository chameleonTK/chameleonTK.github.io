---
layout: post
title: Set Environment for Web Developer EP.1
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/set-env-for-web-developer/mautic_developer_mautician-720x340.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR
[11/10/2016] /me ไปพูดให้น้องๆ CPE ที่ภาควิชาวิศวกรรมศาสตร์ฟัง ถึงความสำคัญของการเซตอัพ Develop Environment ซึ่ง Ep.1 พูดถึง server env. โดยเน้นไปที่ Vagrant เพื่อจัดการ VMs
<!--more-->

{% include aligner.html images="https://lh3.googleusercontent.com/d/1tU4FpEiTc4LRwsmGbIC7AyDz8W81iEyv" column=1 %}

วันนี้(11/10/2016) ได้โอกาสจาก อาจารย์มะนาว และ อาจารย์สุภาพร ให้เกียรติกลับมหาลัยไปพบรรยายเทคโนโลยีใหม่ๆ ตามโครงการปันความรู้จากพี่สู่น้อง ซึ่งเป็นเรื่องที่น่าตื่นเต้นมาก ซึ่งหัวข้อที่ไปพูดในวันนี้ คือ

# "Set Environment for Web Developer"

แต่เผื่อน้องๆหลายคน หรือ web developer ท่านอื่นๆอาจจะสนใจ เลยถือโอกาสเอาเนื้อหาที่พูดในวันนี้ มาเขียนเป็นบทความซะเลย หลังจากห่างหายจากการเขียนบทความเกี่ยวกับ Coding ไปนานนนนน~

# Why?

ในการเขียนเวปไซท์หนึ่งชิ้นนั้น หลายๆคนมักพูดกันว่า ยากนะ! เพราะต้องเขียนถึง 3 ภาษา คือ Client side script, Server side script และ UI ซึ่งนั้นเป็นความวุ่นวายที่คนเขียนเวปทุกคนต้องเจอ แต่ก่อนจะเจอโค้ดเหล่านั้น เรากลับต้องมาเผชิญหน้ากับการทำหน้าที่เป็น System Admin ที่ต้องจัดการลงโปรแกรมต่างๆ เพื่อให้เซิฟเวอร์ หรือ เครื่องคอมของเราแสดงผลเวปขึ้นมาได้ซะก่่อน

ซึ่งการจัดการโปรแกรมเหล่านั้น มันไม่ง่ายเลย แน่นอนว่ามีคนสอนเยอะแยะในอินเตอร์เน็ต อย่าง Document จาก [Mozilla How do I set up a basic working environment?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Set_up_a_basic_working_environment) ซึ่งนี้เป็นแค่วิธีการเซตอัพแบบ Basic เท่านั้น <span class="tag-en">#ย้ำอีกครั้ง</span> แค่นี้ก็ได้บทความยาวๆแล้ว 1 บทความ หากต้องการอะไรเพิ่มเติมก็ต้องเจอกับเจอกับ command line อีกหลายบรรทัดแน่นอน

และการเซตอัพในแต่ละ OS ก็ต้องทำต่างกันไป และในแต่ละครั้งก็ใช้ว่าจะได้ผลลัพย์ออกมาถูกต้อง หลายครั้งมักจะปัญหาไม่ว่าจะเป็น

* ลง Apache ไม่ได้ ทำไงดี?
* ลง PHP แล้ว แต่มันไม่รันไฟล์ .php
* Framework Laravel 5.0 รันบน PHP 7 ไม่ได้ แก้ยังไงดี
* ไม่รู้ enable mod_rewrite ยังไง
* ลง mod mysql ไม่ได้
* mod mongodb ใช้กับ IIS ไม่ได้
* Access denied
* ... และอีกมากมาย

<div class="blockquote">

บางทีก็คิดนะฉันเป็น Web Developer หรือ System Admin?
</div>

แต่หลายคนก็บอกว่า ทำไมไม่ลง XAMPP, WAMPP, LAMPP หละ ไม่เห็นจะต้องวุ่นวายเลย?
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ie79EJXXQJi2aQJT1-p6bGqqUuEU6Iml" column=1 %}

ใช่ครับ มันเป็น package เหล่านั้นทำให้ชีวิต /me ดีขึ้นมากในระยะหนึ่งเลยทีเดียว แต่ความเริงร่ามันอยู่ได้ไม่นานหรอกครับ เพราะเมื่ออยู่ๆ /me พบว่า โปรเจคที่จะทำต้อง downgrade PHP ใน XAMPP ที่อยู่ในเครื่อง รอยยิ้มที่เคยมีมันค่อยๆหายไปกับความวุ่นวายที่เกิดขึ้น และ โลกของความเป็นจริงมันไม่ใช่แค่นี้นะซิครับ

โลกของความเป็นจริง มันเป็นยังไงเหรอ?

ก็เป็นโลกที่เราควบคุมทุกอย่างไม่ได้ครับ เพราะเมื่อเราต้องรับทำเวปไซท์ให้ลูกค้า สิ่งที่ตามมาคือ เราต้องอัพโค้ดของเราบนเครื่องที่เขามี ถ้าโชคดีเราสามารถเปลี่ยน service ต่างๆได้ก็ดี แต่หลายครั้งที่ /me พบว่าลูกค้ามี PHP อยู่แล้วบ้าง, ลง web server อยู่แล้วบ้าง, ห้ามไม่ให้ลงนู้นบ้าง, อัพเดตตรงนี้ไม่ได้บ้าง มากมาย~ ซึ่งนั้นหมายถึงโค้ดของเราที่อาจจะรันไม่ได้ในเครื่องของลูกค้า <span class="tag-en">#เหมือนโดนทิ้งไว้กลางทาง</span>

หลายครั้ง /me เลยต้องกลับมาที่การ set up แบบเดิมๆ ค่อยๆลงโปรแกรมทีละอย่าง ทีละอย่าง บางอันก็ต้อง upgrade, บางอันต้อง downgrade แค่คิดว่าต้องทำแบบนี้ 2-3 ครั้ง ก็อ้วกได้แล้ว เพราะมันมีปัญหามากมายเหลือเกิน ประมาณได้ว่า ลง 10 ครั้ง ก็คงจะมีปัญหาใหม่ๆให้แก้ได้ทุกครั้ง ยิ่งคนที่ไม่มีประสบการณ์ ยิ่งเป็นเรื่องยากในการแก้ปัญหาเหล่านี้ เพราะมันไม่มีคู่มือตายตัวว่า เราจะได้เจอปัญหาอะไรบ้าง?

{% include aligner.html images="https://lh3.googleusercontent.com/d/1ZMdZ41BwCK063-bIiWXENXBRwW9bMrAb" column=1 %}

และนอกจากเราควบคุมอะไรไม่ได้แล้ว เรายังโดนควบคุมอีกด้วย เพราะแต่ละงานล้วนมีกำหนดเวลาที่เขาต้องการ นั้นหมายความว่า เราจะเริงร่าค่อยๆแก้ไปทีละปัญหาๆไปเรื่อยเวลาที่ใช้พัฒนาเวปที่ต้องการก็จะยิ่งน้อยลง
{% include aligner.html images="https://lh3.googleusercontent.com/d/19184VJ_gS2S2yR7kpDvThZSLTt-Yg4wW" column=1 %}

นี้ยังไม่นับรวม เวลาที่ต้องไปศึกษา framework ที่ต้องใช้, bussiness logic ของลูกค้า, ออกแบบ software architechture, migration data

ยังไม่เริ่ม dev เราก็หมดเวลาไปกับเรื่องพวกนี้หมดแล้ว

# How to deal with it?

แน่นอนว่า ปัญหานี้ไม่ใช้ปัญหาที่เราคนเดียวเท่านั้นที่เจอ คนอื่นๆก็เจอปัญหาเหมือนๆกัน จึงทำให้เกิด Tools มากมายมาช่วยแก้ปัญหา ซึ่ง Tools ที่ /me ใช้ คือ Vagrant

โดยอาศัยหลักการว่า "ถ้า set up enviroment มันยากนัก ก็สร้าง VMs ที่เป็นแบบที่ต้องการซะเลยซิ" หรือ ศัพย์เท่ห์ๆ คือ "Virtualization Technology" ซึ่ง Vagrant ก็เป็นหนึ่งในเครื่องมือประเภทนี้

# How it works?

{% include aligner.html images="https://lh3.googleusercontent.com/d/1P-eU_T67pOamvV3aWbvRNZ8JL-G9ZXLs" column=1 %}
1. /me สร้าง Vagrantfile เพื่อกำหนดข้อมูลสำคัญของ VM ไม่ว่าจะเป็น OS, networking, memory, processing core
2. Vagrant จะเอา Vagrantfile นั้นไปสั่งให้ provider ทำหน้าที่สร้าง VMs ขึ้นมาจริงๆ ซึ่ง provider อาจจะเป็น VMWare หรือ Virtualbox ก็ได้
3. หลังจากมี VMs แล้ว Vagrant ก็จะสั่งให้ provisioning tool ทำการลง service/module/library ที่เราต้องการ (เดี๋ยวจะมีพูดถึงอีกรอบ)
4. /me ก็ ssh เข้าไปทำงานได้ทันที ถ้าไม่ชอบ ssh เข้าไปก็ทำการสร้าง Sync folder ทำให้เราสามารถแก้โค้ดที่อยู่ใน VMs ผ่านเครื่องของเรา

จากที่เล่ามา จะพบว่าความจริงแล้ว Vagrant ทำหน้าที่เป็นแค่ virtual machine manager สามารถช่วยเราสร้าง,แก้ไข,กำหนด IP และอื่นๆบน VMs แบบง่ายๆ โดยไม่จำเป็นต้องพึ่ง System Admin //SysAdminจะตกงานรึปล่าวเนี๊ยะ

แต่ สิ่งที่ทำให้ Vagrant แตกต่างและมีคนใช้เยอะแยะ ไม่ได้มีแค่นี้ ฟีเจอร์ที่น่าสนใจของ Vagrant อีก 3 ข้อ

## 1. Setting VM-specific settings using Text-based format

นั้นหมายความว่า เราสามารถเซตทุกๆอย่างเกี่ยวกับ vm ได้ โดยใช้แค่ text editor แล้วยังสามารถอัพโหลด config ให้คนในทีมใช้กันได้ง่ายๆ โดยไม่ต้องอัพโหลด ISO ขนาด x GB

{% include aligner.html images="https://lh3.googleusercontent.com/d/1iyodcxJjo3O2sbOspn4BOj6t6PUdPNtm" column=1 %}

## 2. Enable to run provisioning software like Puppet or Chef or just pain shell script

การ provisioning นี้ คือการเป็นส่วนที่ใช้ในการกำหนดว่า VMs ที่เราต้องการจะต้องมี Service/Plugin/Library อะไรบ้าง, กำหนด permission, config ทุกสิ่งทุกอย่างที่ต้องการ

ซึ่งสามารถเขียนเองด้วย BASH เหมือนที่เราใช้ใน Terminal หรือ อาจจะใช้เครื่องมือที่ทำหน้าที่นี้โดยเฉพาะอย่าง Puppet หรือ Chef ก็ทำได้เหมือนกัน
//ส่วนตัวไม่เคยใช้ Puppet และ Chef เลย ใช้เฉพาะ BASH ล้วนๆ แต่ /me พบว่ามีคนใจดีรวบรวม BASH สำหรับลงโปรแกรมต่างๆไว้ ใครสนใจลองดูได้ที่ Vaprobash

{% include aligner.html images="https://lh3.googleusercontent.com/d/1dCp2ULjyCZ_hkdqfcpgzflk3W9crbUfY" column=1 %}

## 3. Importing pre-made images (called "boxes")

อย่างที่เล่าไปแล้วว่า Vagrant เปิดให้เราสามารถกำหนดโปรแกรมที่ต้องการ และ เซตอัพต่างๆได้ แต่มือใหม่หลายคน มักเจอปัญหาว่า "ผมก็ยังไม่รู้ว่าเลยว่าต้องลงโปรแกรมอะไรบ้าง?" และงานบางงานที่ต้องมีการ set up enviroment ยากมากๆ เช่น hadoop หรือ elastic search ถ้าจะต้องมาศึกษาเอง อาจจะใช้เวลา 3-4 วัน หรืออาจจะลากยาวไปเป็นอาทิตย์เลย

แล้ว

แต่จริงๆแล้วก็มีคนอื่นอีกตั้งหลายคนที่ต้องการคล้ายๆกับเรา แล้ว set up สิ่งเหล่านั้นไว้แล้ว เราเรียกมันว่า "boxes" ทำให้เราสามารถลงระบบอะไรก็ได้ที่เราต้องการ เพียงแค่โหลด box นั้นๆลงมา แล้วสั่ง `vagrant up` ก็สามารถใช้งานได้ทันที

ถ้าใครสนใจ สามารถเข้าไปหา boxes ที่เราต้องการได้ที่ http://vagrantbox.es หรือ ไม่ก็ลอง google ตาม github ก็มีเหมือนกัน

สำหรับ Framework ที่ดังๆ ก็มักจะมี box เป็นของตัวเอง เช่น

* [Homestead](https://github.com/laravel/homestead) for Laravel
* [VVV](https://github.com/Varying-Vagrant-Vagrants/VVV) for Wordpress
* [vagrant-elk-box](https://github.com/comperiosearch/vagrant-elk-box) for Elasticsearch


# สรุป Vagrant ช่วยให้ชีวิตดีขึ้น ยังไง?

### Focus on doing what you do best

เพราะว่า /me เป็นแค่ Web developer ตัวเล็กๆคนหนึ่งที่มีความเชี่ยวชาญเฉพาะด้าน. Vagrant ทำให้เราไม่จำเป็นต้องไปยุ่งยากกับการเซตอัพ service นั้น, ลง library นู้นนี้ และยิ่งไม่ต้องปวดหัวกับการ update version เพราะเรื่องเหล่านี้ สามารถปัดไปให้เจ้า Vagrant รับผิดชอบ

### Development = Production

เมื่อเราใช้ Vagrant จะทำให้เราสามารถกำหนดสภาพแวลล้อมต่างๆให้ตรงกับเซิฟเวอร์ของลูกค้าได้ นั้นหมายถึง มันจะไม่มีทางเกิด "works on my machine bugs" หรืออาการ "พี่ๆมันรันในเครื่องผมได้นะ ไม่รู้ทำไมรันในเซิฟเวอร์ไม่ได้"

### Same environment for all member in your team

สำหรับงานที่ต้องทำกันหลายๆคน Vagrant จะทำให้ทุกๆคนพัฒนาโปรแกรมได้ในสภาพวะเดียวกัน ซึ่งทำให้ง่ายเมื่อถึงเวลาที่ต้องเอาโค้ดมารวมกัน และยังสามารถให้ Tester หรือ QPM ลงระบบแล้ว จิ้มๆ หรือ เขียนโปรแกรมทดสอบได้ โดยรับประกันว่า มันจะได้ผลเหมือนกันกับที่เราโปรแกรม


### และเรื่องสุดท้าย

นอกจาก Vagrant แล้วยังมีอีกหลาย Technology ที่แก้ปัญหานี้ได้เหมือนๆกัน ซึ่ง Tools นึงที่ดังพอๆกัน คือ Docker ซึ่งใช้ Container Technology

แต่ Docker ไม่ได้สร้าง VMs แต่มันแค่สร้างกำแพง(คำเปรียบเทียบ)ขึ้นมาใน OS ของเรา ทำให้เราสามารถลง set up อะไรก็ตามภายในกำแพงนี้ได้ โดยไม่กระทบกับสิ่งที่อยู่ภายนอก และสามารถห่อสิ่งที่เรา set up ไว้ย้ายไปที่อื่นได้ และเพราะมันไม่ได้สร้าง VMs ทำให้ enviroment ที่สร้างโดย Docker (เรียกว่า Container) ทำงานได้เร็วมาก ไม่เปลือง RAM
{% include aligner.html images="https://lh3.googleusercontent.com/d/19FdONh73j_DhTmrxhuqydyskRFeRtS-J" column=1 %}

แต่ ข้อเสียสำคัญของ Docker คือ มันรันได้เฉพาะ Ubuntu ได้อย่างเดียว ถ้าจะลงบน OS อื่นๆ ก็ต้องสร้าง VM Ubuntu ขึ้นมาอีกที ซึ่งกลายเป็นปัญหาที่ยุ่งยากพอสมควรในการใช้งาน แต่เร็วๆ /me ได้ข่าวว่า Docker เวอร์ชั่นล่าสุด 1.12 สามารถรัน native บน OS X, window 10 ได้แล้ว ไม่รู้จะ work แค่ไหน ถ้าใครไม่ชอบ vagrant ก็ไปลองกันได้

นี้ก็ร่ายมาซะยาวเลย สำหรับส่วนแรกก็ขอเบรคไว้เพียงแค่นี้

สำหรับคนที่สนใจ สามารติดตาม [EP.2](https://chameleontk.github.io/set-env-for-web-developer-2) ได้ ซึ่งจะเป็นเรื่องเกี่ยวกับ Gulp และ การจัดการ dependency

## กราบขอขอบคุณ
* [Why should I use Vagrant instead of just VirtualBox?](http://superuser.com/questions/584100/why-should-i-use-vagrant-instead-of-just-virtualbox)
* [Vagrant: What, Why, and How](https://code.tutsplus.com/tutorials/vagrant-what-why-and-how--net-26500)
* [What Is Vagrant and Why Should I Care?](https://24ways.org/2014/what-is-vagrant-and-why-should-i-care/)