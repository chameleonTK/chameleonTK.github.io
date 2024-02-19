---
layout: post
title: Digital Ocean 1st Time
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/digitalocean/digitalocean-square-logo.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR
/me เป็น Developer ที่ทำนู้นทำนี้ บางครั้งก็ลองใช้ Ruby บ้าง Python บ้าง แต่สุดท้ายสิ่งที่ทำก็ไม่ได้เอามาให้คนอื่นใช้งาน เพราะไม่มี server สำหรับ deploy เลยถือโอกาสจิ้มๆ สร้าง VPS ใน Digital Ocean มาเป็น server ของตัวเองซะเลย
<!--more-->

{% include aligner.html images="https://lh3.googleusercontent.com/d/1U9zeL_vPg56v0GhicvYjZ0XxAXqdp1uG" column=1 %}

ห่างหายไปนาน จริงๆก็แอบว่างนะ แต่อากาศร้อนๆแบบนี้ ใครจะมานั่งเขียนบล๊อคยาวๆไหว ประเทศไทยตอนนี้ก็ 41 องศาไปเรียบร้อบแล้ว <span class="tag-en">#ฉันยังอยู่ประเทศไทยนะไม่ใช่ดวงอาทิตย์</span> แต่ด้วยความที่ Draft ไว้เพียบ เลยต้องมาค่อยๆเครียร์

วันก่อนครับ <span class="tag-en">#ไม่เล่นมุกละ</span> ประมาณช่วงศุกร์ที่ผ่านมา [17/4/2015] อยู่ๆก็ตัดสินใจเช่า VPS มาเป็นของตัวเอง ส่วนเหตุผลก็คือ <span class="tag-en">#ตังค์เหลือ</span> <span class="tag-en">#หลอกๆ</span> ความจริงคือ เซงที่โฮสที่เช่าอยู่ ไม่ยอมอัพเดตอะไรให้เลย แต่ก็ไม่ใช่ความผิดของโฮสหรอกนะ เค้าไม่สามารถอัพเดตได้อยู่แล้ว เพราะมันต้องอัพเดตทั้งระบบ แล้วเวปของบางคนอาจจะพังได้ <span class="tag-en">#คงจะมีคนเงิบมากมาย</span> เลยมาลงเอยที่ VPS ของตัวเอง

{% include aligner.html images="https://lh3.googleusercontent.com/d/1V1vFAxRszIWOjfG77p7A4hUrS-Li6dpi" column=1 %}

# VPS คืออะไร ??

ก่อนอื่นก็ต้องมารู้จัก Cloud Computing กันก่อนดีกว่า หลายๆคนอาจจะเคยได้ยินมาบ้างแล้ว เพราะตอนนี้มันกำลังเป็นหัวข้อ Top Hit ของคนด้านคอมพิวเตอร์เลยก็ว่าได้ มาถึงคำถามว่า มันคืออะไร? [ในความเข้าใจของ #me] Cloud system คือ กองของคอมพิวเตอร์หลายๆตัว(Resource pooling)มาเชื่อมต่อกันให้เป็นระบบเดียวกับ โดยมีความสามารถเอาคอมพิวเตอร์ (เรียกมันว่า Compute node) มาต่อเพิ่มได้เรื่อยๆ โดยจะแบ่งให้คนอื่นสามารถแบ่งไปใช้ได้ตามที่ต้องการ(On-demand self-service) โดยผ่านระบบอินเตอร์เน็ต(Broad network access) <span class="tag-en">#มีรายละเอียดอีกแต่ขอข้ามไป</span>

ส่วน VPS (Virtual Private Server) เป็นบริการหนึ่งของ Cloud ในรูปแบบ PaaS <span class="tag-en">#ไม่ต้องไปสนใจ</span> โดยจะอนุญาตให้ผู้ใช้สร้าง VM หรือ เครื่องคอมพิวเตอร์จำลอง ขึ้นมาใน Cloud เสมือนเครื่องเซิฟเวอร์จริงๆ ซึ่งจะช่วยทำให้เราไม่จำเป็นต้องไปดูแล Hardware อย่าง HDD, RAM, CPU ด้วยตัวเอง ปล่อยให้ผู้เชี่ยวชาญกว่าดูแลให้ ส่วน #Developer อย่างพวกเราก็มานั่งหน้าคอม เขียนโปรแกรม <span class="tag-en">#ที่จะครองโลก</span> ต่อไป

สรุป คือ ถ้าอยากได้ Server ของตัวเอง โดยไม่ต้องไป <span class="tag-en">#ซื้อเอง</span> <span class="tag-en">#ประกอบเอง</span> <span class="tag-en">#ต่อเน็ตเอง</span> <span class="tag-en">#ดูแลเอง</span> แนะนำว่าให้หา VPS มาซักอันเถอะครับ

{% include aligner.html images="https://lh3.googleusercontent.com/d/1yk7E0Sjlh6X6fOQJwz7v28Lm7i9-TRr6" column=1 %}


# ทำไมต้องมาเลือก Digital Ocean

<span class="tag-en">#เพื่อนแนะนำ</span> อันนี้สำคัญเลย จริงๆก็แอบหาเหมือนกันว่า มีแบบที่เป็นของคนไทยรึปล่าว ส่วนใหญ่มันไม่ค่อยน่าเชื่อถือเท่าไร บางที่ก็โคตรจะแพง <span class="tag-en">#ฉันมาเช่า</span>VPSไม่ใช่มาให้ปล้น และ อีกเหตุผลคือ Digital Ocean รับประกันว่า มันง่ายสัสๆๆ "Deploy an SSD cloud server in 55 seconds" <span class="tag-en">#ง่ายจริง</span> แถมไม่ค่อยแพงด้วย เริ่มต้นที่ 5$ <span class="tag-en">#ฉันจะได้ค่านายหน้าปะ</span>

# เมื่อต้องมาสร้างจริงๆ

ตอนแรกนึกว่า สร้าง VPS ซักอันจะยาก พอเห็นแล้ว ง่ายกว่าที่คิดแฮะ <span class="tag-en">#ง่ายโคตร</span>

{% include aligner.html images="https://lh3.googleusercontent.com/d/1mrN2l16WrH5x7jWGnxdY0ds676ifkdw-" column=1 %}


ที่เสียเวลาที่สุด ไม่ใช่ ตอนสร้าง VPS แต่เป็น ตอนผูกบัญชีเข้ากับ Paypal ต่างหาก เพราะเดบิตธนาคารกรุงเทพ ไม่สามารถจ่ายตังค์กับ Digital Ocean ได้ แต่ถ้าใครใช้ บัตรเครดิต ก็คงไม่มีปัญหาอะไร

{% include aligner.html images="https://lh3.googleusercontent.com/d/16vb8CXMky_fu8KS2-b-rc-xr3WGjFfXq" column=1 %}


ด้านบนเป็นภาพตอนเลือกแพคเกต ซึ่งจะไม่สามารถปรับ Disk, RAM, Bandwidth ได้ตามใจชอบ มันมาให้แล้วเป็นแพคเกตๆ แต่เราสามารถเลือกได้ว่าจะลง OS อะไร? แถมถ้าใครคิดว่าไม่อยากเซตอัพระบบเอง มันก็มีระบบที่เซตอัพมาแล้วให้ด้วย

สำหรับ แพคเกตที่ให้เลือก ถ้าใครอยากแค่ลองอะไรแปลกๆเฉยๆ ก็ใช้แค่ 5$ ก็น่าจะเพียงพอนะ

หลังจากสร้าง VPS เสร็จแล้ว [Digital Ocean จะเรียกแต่ละ VPS ของเรา ว่า #Droplet ] ก็มาลอง SSH กัน ซึ่งถ้าใครใช้ Window ก็สามารถใช้ #putty แต่สำหรับสาวก Linux/Unix ก็สามารถใช้ #terminal ได้เลย

ก่อนจะเริ่ม SSH ทุกครั้งที่เราสร้าง Droplet (VPS) อย่าลืมไปเอา root password กันได้ใน Email ที่ใช้สมัครเอาไว้ หรือ ถ้าใครว่าง ก็สามารถเซต public key ไว้ ซึ่งจะทำให้ ครั้งต่อไปจะไม่ต้องใส่ password กันหลายๆรอบ

ถ้าจะ SSH ก็ใส่เพียง IP ที่เราได้ โดย เริ่มต้น เราจะต้องใช้ User: root ไปก่อนถ้าใครอยากได้ชื่ออื่นก็ไปทำเอาเองละกัน ก็จะได้หน้าตาแบบนี้ <span class="tag-en">#เต็มไปด้วยเซ็นเซอร์</span> แค่นี้ก็เหมือนกันว่า มีเครื่องคอมเครื่องนึงมาเล่นกันแล้ว <span class="tag-en">#ฉลอง</span> <span class="tag-en">#แต่มันยังไม่จบ</span>

{% include aligner.html images="https://lh3.googleusercontent.com/d/122KqpaUsgqfLA2t6uHmgCwy8mGnLa5HS" column=1 %}

** ถ้าได้มาลอง จะรู้ว่าตอน SSH แอบกระตุ๊กเล็กๆ เพราะว่า เครื่องหลักอยู่ไกลถึงอเมริกา ไม่รู้ว่าจะมีขยายสาขามาตั้งที่เอเชียเมื่อไร <span class="tag-en">#รอกันต่อไป</span>

# เตรียมเครื่องให้พร้อมเขียนเวป [Set up LAMPP]

ด้วยความที่อยากลองเป็น Linux Admin เองซักครั้ง <span class="tag-en">#ปกติทำได้ก็แค่ในเครื่องตัวเอง</span> ก็เลยตั้งใจลงเป็น Ubuntu 14.04 เพียงอย่างเดียว ความเงิบอย่างแรก คือ <span class="tag-en">#ไม่รู้จะเริ่มยังไงดี</span> ด้วยความที่ปกติใช้ Ubuntu อยู่แล้ว ก็เลยไม่ต้องปรับตัวอะไรมาก แต่สำหรับคนที่ไม่เคย ก็ลองไปอ่าน Document ซึ่ง Digital Ocean เขียนไว้เยอะพอสมควรเลยทีเดียว แถมยังละเอียดมากอีกด้วย

สำหรับ #me อย่างแรกนึกออกว่าจะต้องลงก็คือ LAMPP = Linux + Apace + MySQL + PHP + phpmyadmin เพราะว่าเป็นเครื่องมือที่ง่ายที่สุดสำหรับเขียนเวปไซท์ มาเริ่มกันเลยดีกว่า

## Install Apache
Apache เป็น Opensource Web Server ที่ไว้สำหรับรองรับ request ที่ส่งมาที่ server

```bash
sudo apt-get update
sudo apt-get install apache2
```

สำหรับถ้าต้องการสั่งปิดการทำงานของ Apache

```bash
sudo service apache2 stop
```

** สามารถเปลี่ยน stop เป็น start/restart ได้

## Install MySQL
MySQL เป็น Database management system ที่นิยมใช้มาก

```bash
sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql
```

*** ระหว่างลง <span class="tag-en">#อย่า</span>enter รัวๆ เพราะจะมีให้ใส่ root password สำหรับ MySQL ด้วย

จากนั้นก็ต้อง activate MySQL โดย

```bash
sudo mysql_install_db
```

สุดท้ายก็คือ รัน MySQL set up script

```bash
sudo /usr/bin/mysql_secure_installation
```

## Install PHP
PHP เป็นภาษาสำหรับเขียนเวปไซท์ที่ใช้เยอะเป็นอันดับต้นๆ และมี Document ให้ศึกษาเยอะแยะ

```bash
sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt
```

หลังจาก install จะต้องทำการเซตอัพให้รู้จัก index.php โดยเปิดไฟล์ "/etc/apache2/mods-enabled/dir.conf"

จากนั้นเพิ่ม index.php ลงไป
>    DirectoryIndex index.php index.html index.cgi index.pl index.php index.xhtml index.htm

# Install phpmyadmin

phpmyadmin เป็น web interface ที่สามารถทำให้เข้าถึงดาต้าเบสได้ง่ายๆผ่านเวป ไม่จำเป็นต้องใช้ commandline

```bash
sudo apt-get install phpmyadmin
sudo php5enmod mcrypt
sudo service apache2 restart
```

สุดท้าย...

ถ้าทั้งหมดเป็นไปอย่างถูกต้อง เราก็จะสามารถเข้าดู Website ผ่าน IP ของ VPS

*** root directory จะอยู่ที่ /var/www/html

{% include aligner.html images="https://lh3.googleusercontent.com/d/1Ryt9ObVHrfRwweysuy9d687ubnlGhADV" column=1 %}

<span class="tag-en">#เยี่ยมจริงๆ</span> <span class="tag-en">#เยี่ยมจริงๆ</span> <span class="tag-en">#เยี่ยมจริงๆ</span> แต่อย่าลืมนะว่า VPS ก็เสมือนคอมพิวเตอร์ของเรา มันติดไวรัส หรือ โดนแฮ๊กได้ ซึ่งปกติ Hosting จะเป็นคนดูแลเรื่องนี้ให้เรา แต่ตอนนี้ เราต้องมาดูแลเองละ <span class="tag-en">#ฉันก็แอบกลัวโดนแฮ๊กอยู่เหมือนกัน</span>

## เพิ่มเติม1 

ถ้าอยากให้แต่ละ user มี website root directory ของตัวเอง

```bash
sudo a2enmod userdir
sudo service apache2 restart
```

แค่นี้ แต่ละ user ก็จะสามารถเข้าสร้าง page ของตัวเอง ได้ที่ /home/<username>/public_html ชมเวปผ่าน http://your.host.name/~username

## เพิ่มเติม2
เมื่อ PHP ไม่รัน script ที่อยู่ใน public_html 

ให้เปิดไฟล์ /etc/apache2/mods-enabled/php5.conf จากนั้นแก้ เพิ่ม # ตามตัวอย่าง
 #php_admin_value  engine Off

จากนั้น ก็ restart web server

```bash
sudo service apache2 restart
```

## เพิ่มเติม3 ตั้งค่า Servername

ข้ามไปก่อน ยอม ดึกละ ขี้เกียจเขียน

# Credit

* [How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu)
* [How to give Public_html to each user?](http://askubuntu.com/questions/263286/how-to-give-public-html-to-each-user)
* [Ubuntu Tips: Apache does not execute PHP files](http://matthewwittering.com/blog/ubuntu-tips/apache-not-running-php-files.html)
* [where in Apache2 do you set the Servername directive globally?](http://unix.stackexchange.com/questions/155150/where-in-apache2-do-you-set-the-servername-directive-globally)

