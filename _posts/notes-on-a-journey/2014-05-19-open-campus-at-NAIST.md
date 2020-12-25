---
layout: post
title: Open Campus @ NAIST
feature-img: "assets/feats/open-campus-at-NAIST/naist3.jpg"
thumbnail: "assets/feats/open-campus-at-NAIST/naist3.jpg"
tags: [Archive]
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(165,42,42)

---


<span class="tag-en">#17/5/2014</span> กิจกรรม Open Campus เปิดมหาลัยเพื่อแสดงผลงาน ซึ่งเยอะมากๆๆ ที่ NAIST แน่นอนว่าเกือบทั้งหมดเป็น ภาษาญี่ปุ่น <span class="tag-en"><span class="tag-en">#กำ</span></span>

<!--more-->

หลังจากพยายาม ต่อสู้ กับ อุปสรรคทางภาษา !@#$%^&(คนญี่ปุ่นพูดอังกฤษได้น้อยมา แต่โชคดีที่ฝั่ง information science มีชาวต่างชาติอยู่เยอะ ก็เลยสบายหน่อย) ก็ได้เจอ research เจ๋งๆ เยอะฟุดๆ คงเล่าได้ไม่ครบ ผิดบ้างถูกบ้าง~

### Geographically Aggregatable  with IPv6 [IP lab]
ซึ่งเค้าคิดกันว่า ipv6 มันยาววววมากกกก~ เค้าจึงสนใจ ลองดีไซน์รูปแบบที่สามารถ "ระบุพิกัด" ของเราได้เพียงแต่เราต่อ internet ถามว่า มันมีประโยชน์จริงๆรึปล่าว ในเหตุการณ์ฉุกเฉิน อาจจะหลงทาง เกิดเหตุอุบัติภัย เหตุการณ์ที่ต้องขอความช่วยเหลือ การแจ้งพิกัดเป็นเรื่องสำคัญ ซึ่งถ้าเราใช่ระบบนี้จริงๆ หมายความว่า <b>แค่คุณต่อ internet ก็สามารถแจ้งที่อยู่เราได้แล้ว <span class="tag-en">#winwin</span></b>

. 
.
.
ปล. แต่ถ้าเราเล่นเน็ตปกติ ก็ไม่ต้องใช้ระบบนี้นะ ไม่งั้นคงน่ากลัวแย่ we are stoker!!

[[paper]](https://iplab.naist.jp/publications/pdf/Okada_PITSaC2013.pdf)

### Reality-Based Human-Human Communication [IMD lab]

ปัญหาใหญ่หนึ่งของการ meeting กับคนหมู่มาก หรือ การพรีเซ้นอะไรซักอย่าง คือ เราไม่รู้เลยว่าผู้ฟัง เข้าใจหรือ ไม่เข้าใจอย่างไร ในขณะที่เราพูด งานนี้จึงนำระบบ <span class="tag-en">#AR</span> [Augmented Reality] มาใช้ โดยเริ่ม

* I. โดยระบุยืนยันตำแหน่งของเรา ระบบจำตรวจจับวัตถุบริเวณนั้น 
* II. หลังจากนั้นทุกคนในห้องจะสามารถเปิดแอพที่เค้าทำ เพื่อดู slide 
* III. หากไม่เข้าใจ ไม่เห็นด้วย มีข้อสงสัย ก็สามารถกดแสดงความคิดเห็นในแอพ 
* IV. แอพจะทำงานร่วมกับอีกหน้าจอที่อยู่ด้านหน้า ซึ่งจะจับภาพของผู้ฟัง และแสดงผลเป็น animation เหนือตัวเรา ซึ่งก็จะผู้พูดก็จะเห็นว่า ตอนนี้ทุกคนคิดเห็นอย่างไร หรือ มีคำถามรึป่าว บลาๆๆๆ

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1NGO-g2NqNA2Zk_rdb5-utuYJucYeAJku" column=1 %}

//ลืมถ่ายรูป ของจริงมา ระบบทั้งหมดเป็น real time ทั้งหมด เจ๋งฟุดๆๆ

[[paper]](http://imd.naist.jp/research/pdf/2010_igor.pdf)

### Why Novice Programmers Fall into a Pitfall?: Coding Pattern Analysis in Programming Exercise [SD lab]

programming เป็น วิชาหนึ่งที่หลายคนบอกว่า แม่งโคตรยาก ฟร๊ากๆๆๆๆ เพราะก็เหมือนการเรียนภาษาทั่วๆไป หากเราไม่เข้าใจภาษา ไม่เข้าใจไวยกรณ์ ไม่เข้าใจศัพย์ ก็ยากที่จะเข้าใจ ดังนั้นในห้องเรียน เราจะรู้ได้ยังไงว่า ใครยังไม่เข้าใจอะไร ใครต้องการความช่วยเหลือบ้าง ปัญหาหนึ่งคือ ไอ้พวกที่ไม่เข้าใจ แม่งไม่ยอมขอความช่วยเหลือ สุดท้ายแล้วก็ จบเห่ ดับอนาถ

จึงเกิดระบบนี้ขึ้น เป็นระบบติดตามความเข้าใจ โดยมีแนวคิดว่า ในแต่ละ excercise ที่มีผลลัพย์ที่แน่นอนไว้อยู่แล้ว หากนักเรียนแต่ละคนเข้าใจในหัวข้อที่เรียน ความเหมือนของโค้ดย่อมเข้าใจโค้ดเป้าหมายขึ้นเรื่อยๆ ดังนั้นหากมีนักเรียนคนใดที่ความเหมือนของโค้ด ฉีกออกนอกลู่นอกทาง จึงหมายถึงว่า นักเรียนคนนั้นต้องการคำแนะนำบางอย่างแน่นอน

แต่คงใช้ไม่ได้กับโจทย์ที่มีความหลากหลายของคำตอบสูง Orz แต่อย่างน้อยก็ดีสำหรับติดตามผู้เริ่มต้นใหม่ การมีคำแนะนำในเวลาที่ต้องการ เย้เย้เย้

[[paper]](http://sdlab.naist.jp/pman3/pman3.cgi?DOWNLOAD=66)

### Wide-area wireless power supply [Infonet lab]
\* translate by GOOGLE [original 広域ワイヤレス給電 ]




<div class="video-container">
    <iframe class="video" src="https://www.youtube.com/embed/diHCFyDdsSQ" frameborder="0" allowfullscreen></iframe>
</div>

คงสงสัยว่า ไอ้คลิปนี้มัน คือ อะไร ?? <span class="tag-en"><span class="tag-en">#เฉลย</span></span> มันเป็นระบบรางที่ชาร์ตไฟเข้าตัวรถไฟ ทำให้รถไฟวิ่งๆๆได้ โดยตัวรางและรถไฟ ไม่มีส่วนไหนเชื่อมกันเลย <span class="tag-en">#wireless</span> ฮะ สรุปมันคือ ระบบชาร์ตไฟ แบบไม่ต้องเสียบปลั๊กนั้นเอง เอ๊ๆๆ ปกติมันก็มีอยู่แล้วหนิ wireless charger [[What is This?]](http://www.techwhatwhy.com/how-wireless-charger-work) แต่ โดยปกติ การ charge แบบนี้ตัวอุปกรณ์มักต้องติดกับที่ชาร์ต ไม่งั้นชาร์ตไม่เข้า แต่ระบบนี้ แม้ว่าเรา move ก็ยังชาร์ตเข้าได้เรื่อยๆ ต่อไป ปัญหาแบตหมดก็จะหมดไป <span class="tag-en">#hope</span>

{% include aligner.html images="https://drive.google.com/uc?export=view&id=14hS41fSNajviPrMXOu5kvODlFvPFydJL" column=1 %}

ปล. ตอนนี้ยังเป็นแค่ <span class="tag-en">#demo</span> นะฮะ เพราะพลังงานสูญหายเยอะ 50%

[[paper]](http://agano.naist.jp/hp/research/research_template/network_system_WPT.pdf)