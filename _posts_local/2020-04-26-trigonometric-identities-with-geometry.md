---
layout: post
title: "พิสูจน์สูตรตรีโกณ ด้วย เรขาคณิต"
tags: [Archive, Mathematics]
thumbnail: "assets/img/trigonometric-identities-with-geometry/image-01.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

ย้อนกลับไปสมัยตอนเรียน ม.ปลาย เชื่อว่า หลายๆคนคงได้พบเจอกับมหากาพย์การท่องสูตรตรีโกณมิติไปไม่มากก็น้อย หน้ากระดาษ A4 ที่เต็มไปด้วยสูตรอะไรก็ไม่รู้ยุบยับไปหมด ความทรงจำสุดสยองที่ไม่อยากย้อนกลับไปนึกถึงมัน

<!--more-->

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-01.jpg" column=1 %}

<p><a href="https://www.quora.com/What-are-all-the-trigonometric-formulas">https://www.quora.com/What-are-all-the-trigonometric-formulas</a></p>
</div>

ใครจะไปคิดว่า เราสามารถใช้เรขาคณิตง่ายๆในการพิสูจน์สูตรด้านบนได้! บางทีนี้คือเสน่ห์ของคณิตศาสตร์ หลายๆอย่างที่แตกต่างกันแต่กลับมีความสัมธันธ์กันได้อย่างสวยงาม

> Truth is ever to be found in the simplicity, and not in the multiplicity and confusion of things. — Issac Newton

## Start with Basic Knowledge

ก่อนจะเริ่มลงรายละเอียด ขอปูพื้นฐานให้กับหลายๆคนที่คงลืมเนื้อหาพวกนี้ไปแล้ว สิ่งแรกที่ต้องรู้ก่อนจะเริ่ม คือ ฟังก์ชั่นตรีโกณ ไม่ว่าจะเป็น sin A, cos A หรือ tan A นิยามมาจาก สัดส่วนของสามเหลี่ยมมุมฉากที่มีมุมๆนึง เป็นมุม A ตามรูปด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-02.png" column=1 %}
</div>

ถ้าเรากำหนดให้ด้านตรงข้ามมุมฉาก มีความยาว R แล้ว ความยาวด้านที่อยู่ชิดกับมุม A และด้านที่อยู่ตรงข้ามมุม A จะมีขนาด **Rcos A**และ **Rsin A** ตามลำดับ

ย้อนกลับไปสมัยเรียน วิธีการแบบนี้ จะเจอบ่อยๆในวิชาฟิสิกซ์ หลายๆคนคงจะคุ้นๆกับเสียงท่านอาจารย์แว่วๆมาไกลๆว่า “ใกล้มุมเป็น cos ไกลมุมเป็น sin”

ซึ่งเราจะใช้แค่หลักการนี้ กับ พื้นฐานเรขาคณิต มาตะลุยพิสูจน์สูตรตรีโกณต่างๆกันในวันนี้

## Let’s do Trigonometring

เป้าหมายของวันนี้ คือ พิสูจน์ 4 สูตร ได้แก่ **sin A+B, cos A+b, sin A-B** และ **cos A-B**

สิ่งแรกที่ต้องทำคือ วาดรูปสามเหลี่ยม แต่เพราะเป้าหมายแรกของเรา คือ หา **A+B** จึงต้องเอาสามเหลี่ยม ที่มีมุม **A** และ **B**มาซ้อนกัน ตามรูปด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-03.png" column=1 %}
</div>

การหา มุมที่มีขนาดเท่ากับ **A+B** ก็ไม่ได้ยาก เพราะจากพื้นฐานเรขาคณิต เราจะพอรู้มาว่า มุมทแยงเส้นขนาน (เส้นแนวนอน 2 เส้นในรูป) มีค่าเท่ากัน นั้นทำให้คือ มุมแทยงในรูป มีขนาดเท่ากับ **A+B** ซึ่งเป็นมุมเป้าหมายที่เราตามหา

นอกจากนี้ เรายังรู้ว่า มี มุม B แอบซ่อนอยู่อีกที่ ตามรูป ซึ่งเกิดจาก 2 คุณสมบัติที่ว่า

*   สามเหลี่ยมมีมุมรวมกัน เท่ากับ 180 องศา
*   มุมที่รวมกันได้เส้นตรง จะต้องรวมกันได้ 180 องศา

_(ใบ้มาแล้ว ที่เหลือลองคิดต่อเป็นการบ้านว่า มันเท่ากับ B จริงๆรึปล่าว?)_

สิ่งที่น่าตื่นเต้นที่กำลังจะเกิดขึ้น เมื่อลองเติมค่าตรีโกณต่างๆจาก Basic Knowledge ที่พูดไปแล้ว

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-04.png" column=1 %}
</div>

_ใกล้มุมเป็น cos ไกลมุมเป็น sin … ใกล้มุมเป็น cos ไกลมุมเป็น sin …_

จะได้ว่า ฐานของสามเหลี่ยมสีแดง เท่ากับ **cos A** ซึ่งพอย้ายต่อลงมาที่ ฐานของสามเหลี่ยมสีฟ้า ก็คือการคูณเข้าไปอีก **cos B**ผลลัพย์ คือ **cos A cose B**

ทำนองเดียวกัน สำหรับด้านต่างๆทั้งหมด

และด้วยว่า สี่เหลี่ยมในรูปเป็นสี่เหลี่ยมมุมฉาก มีด้านตรงข้ามยาวเท่ากัน

สิ่งที่ได้ คือ

> sin A+B = sin A cos B + cos A sin B
>
>
> cos A+B = cos A cos B - sin A sin B

พริบตาเดียว เราพึ่งพิสูจน์ 2 สูตรมุมบวกกัน โดยใช้แค่สามเหลี่ยมสองอัน กับ ความรู้อีกเล็กๆน้อยๆจาก เรขาคณิต

เราจะไม่หยุดเพียงเท่านี้ มาลองดัดแปลงเปลี่ยนมุมสักเล็กน้อย ตามรูปด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-05.png" column=1 %}
</div>

แต่คราวนี้ สิ่งที่โผล่ออกมา คือ มุม **A-B** ซึ่งเกิดจาก ทฤษฎีเรขาที่ว่า มุมแย้ง (มุม **A**)ของเส้นขนานมีขนาดเท่ากัน แต่มุมที่ว่า ส่วนหนึ่งเท่ากับ **B** ไปแล้ว ส่วนที่เหลือ จึงต้องเท่ากับ **A-B**

จากนั้นก็เติม ค่าตรีโกณ อีกครั้ง

_ใกล้มุมเป็น cos ไกลมุมเป็น sin … ใกล้มุมเป็น cos ไกลมุมเป็น sin …_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-06.png" column=1 %}
</div>

แถ่น แถ่น แทนแทนแทน แถ่น แท้นแท้น …

> sin A-B = sin A cos B - cos A sin B
>
>
> cos A-B = cos A cos B +sin A sin B

## แถมอีก 2 สูตร

ของแถมประจำวันนี้ คือ สูตร sin 2A และ cos 2A ซึ่งจริงๆแล้ว เราสามารถคิดได้จาก 4 สูตรด้านบนที่มีแล้ว เพราะ แค่แทน A=B

แต่ขอท้าทายเพิ่มอีกสักนิด คราวนี้ เราจะใช้วงกลมเข้ามาช่วย แล้วคำนวนมันด้วยเรขาคณิต

เริ่มจาก ความรู้จากเรขาคณิต: “มุมที่จุดศูนย์กลางของ**วงกลม**จะมีขนาด**เป็นสองเท่า**ของขนาดของ**มุมใน**ส่วนโค้งของ**วงกลม**ที่รองรับด้วยส่วนโค้งเดียวกัน”

นั้นคือ จากรูป วงกลม รัศมี 1 หน่วย มีจุด **O**เป็นจุดศูนย์กลาง จะได้ว่า มุมที่จุดศูนย์กลาง คือ **2A** และมุมในส่วนโค้ง คือ **A**ตามลำดับ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-07.png" column=1 %}
</div>

จากนั้น ลากเส้นเพิ่มเติมเล็กน้อย จะได้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-08.png" column=1 %}
</div>

ด้วยว่า OP และ OQ ต่างเป็น รัศมีของวงกลม แล้วใช้ **_ใกล้มุมเป็น cos ไกลมุมเป็น sin …_**1 ครั้ง เพื่อคำนวนความยาวเส้นตรงชิดมุม A ผลที่ได้ คือ เส้นตรง PQ จะมีขนาดเท่ากับ 2 cos A

ต่อมา ถ้าพิจารณา สามเหลี่ยมสีแดงตามรูป ตามหลักการ

> ใกล้มุมเป็น cos ไกลมุมเป็น sin …
>
>
> ใกล้มุมเป็น cos ไกลมุมเป็น sin …

เราจะได้ความยาวฐานของสามเหลี่ยมจะเท่ากับ

> = ความยาวเส้นตรงข้ามมุมฉาก x cos A
>
> = (2 cos A) cos A
>
> = 1+cos 2A

ย้ายข้างสมการ จะได้ว่า

> cos 2A = 1- 2 cos A cos A

และจากรูปเดิม แต่ **#เปลี่ยนมุมกลับปรับมุมมอง**เปลี่ยนมามองสามเหลี่ยมชิ้นใหญ่สีฟ้าตามรูป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="trigonometric-identities-with-geometry/image-09.png" column=1 %}
</div>

เพราะ OP และ OR เป็นรัศมีของวงกลม ดังนั้นเส้น PR จึงยาวเท่ากับ 2 หน่วย เมื่อพิจารณาจากมุม A แล้ว จะได้ว่า ด้านตรงข้ามมุม A = 2 sin A

> ใกล้มุมเป็น cos ไกลมุมเป็น sin …
>
>
> ใกล้มุมเป็น cos ไกลมุมเป็น sin …

สุดท้ายพิจารณามุม A เล็กๆในสามเหลี่ยมย่อยด้านใน จะได้ว่า

> = ความยาวด้านชิดมุม A ในสามเหลี่ยมย่อย
>
> = ความยาวเส้นตรงข้ามมุมฉาก x cos A
>
> = 2 sin A cos A

แต่ถ้ามองจากมุม **2A**จะได้ว่าด้านนั้นยาว =**sin 2A**หรือก็คือ

> sin 2A = 2 cos A sin A

## Q.E.D.

Quod Erat Demonstrandum หรือ ซึ่งต้องพิสูจน์
