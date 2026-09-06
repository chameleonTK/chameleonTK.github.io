---
layout: post
title: "ทำความเข้าใจ Hopfield Network"
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/understanding-hopfield-network.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

> **_คำเตือน_**_เนื้อหาในบทความนี้เต็มไปด้วยศัพท์แสงทางวิชาการ โปรดใช้วิจารณญาณก่อนเสพ_

<!--more-->

> _“for foundational discoveries and inventions that enable machine learning with artificial neural networks”_
>
>
> _แด่การค้นพบและรังสรรค์อันเป็นรากฐานที่ริเริ่มความเป็นไปได้ของ Machine Learning ด้วย Artificial Neural Network — Physics Nobel Prize, 2024_

บล๊อคนี้ขอติดกระแส Physics Nobel 2024 ที่พึ่งให้รางวัลในช่วง(หลาย?)สัปดาห์ที่ผ่านมา //ไม่รู้จะยังทันอยู่รึปล่าว

เนื่องจากส่วนตัวเรียนมาในสาย AI และในฐานะที่รางวัลโนเบลปีนี้มอบให้แก่ Profs สองท่านผู้บุกเบิกในสายที่เรียน (John Hopfield และ Geoffrey Hinton) เลยขอเป็นพื้นที่เล็กๆเฉลิมฉลองให้กับทุกๆท่านที่อยู่ในสายงานเดียวกัน 🎉🎉🎉 โดยการมาอธิบายกันในเชิงลึกๆกันไปเลยว่า ผลงานที่ได้โนเบลปีนี้ ไม่ว่าจะเป็น Hopfield Network และ Boltzmann Machine มันคืออะไรกันแน่? เพื่อมาเข้าใจว่าทำไมโนเบลถึงให้รางวัลกับอาจารย์ทั้งสองท่านนี้ แต่ว่าในบล๊อคนี้ จะเริ่มจากแค่ Hopfield Network กันก่อน

## What is Hopfield Network?

Hopfield Network เป็นโมเดลที่นำเสนอโดย John Hopfield ในปี 1982 ในเปเปอร์ที่ชื่อว่า _“_[_Neural networks and physical systems with emergent collective computational abilities_](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/)_”_

เพื่อศึกษาความสามารถที่เป็น collective property หรือ ความสามารถที่อยู่ๆก็โผล่ขึ้นมาเองจากระบบที่เกิดจากองค์ประกอบย่อยๆเล็กๆที่เรียบง่ายหลายๆอันมารวมๆกัน — _“Computational properties of use of biological organisms […]_ _can emerge as collective properties of systems having a large number of simple equivalent components”_

ฟังแล้วอาจจะดูงงๆ แต่จริงๆแล้วระบบแบบนี้มีอยู่ทั่วๆไปรอบตัวเรา เช่น

หลายๆคนคงเคยเรียนมาในวิชาฟิสิกต์ ในการโมเดลอนุภาคของอากาศรอบๆตัวเราเป็นจุดเล็กๆที่วิ่งไปมาๆ ซึ่งเจ้าอนุภาคเล็กๆเหล่านี้เมื่อมีจำนวนมากๆมารวมกันทำให้เกิดสิ่งใหม่ที่เรียกว่า ความดัน Pressure

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ytkOGXr-R5fGqdKXRsmM8KTjqxF08L96" column=1 %}

<p><a href="https://www.britannica.com/science/ideal-gas">https://www.britannica.com/science/ideal-gas</a></p>
</div>

หรือใกลตัวขึ้นมาหน่อย ในร่างกายของทุกๆคน ประกอบไปด้วยเซลล์เล็กๆเต็มไปหมด เซลล์เล็กๆเหล่านี้ไม่สามารถย่อยอาหารได้ด้วยตัวของมันเอง ไม่สามารถยกน้ำหนักหลายๆสิบกิโลได้ แต่เมื่อพวกมันมามัดรวมกันเป็นกระเพาะ หรือ มัดกล้ามเนื้อ ความสามารถใหม่จึงเกิดขึ้น

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Z3wgqvUHscVtTp2XU7qS1lWmhAsTp21Q" column=1 %}

<p><a href="https://hal.science/tel-01246844/">https://hal.science/tel-01246844/</a></p>
</div>

//พาอ้อมกันมาซะไกลเลย

โดย John Hopfield นำเสนอว่า _ความทรงจำ (Memory)_ จริงๆแล้วอาจจะเป็น collective property ที่เกิดจากการทำงานของเซลล์ประสาทในสมองทำงานร่วมกันก็เป็นไปได้ โดยแสดงให้เห็นว่า โมเดลคอมพิวเตอร์ง่ายๆที่จำลองมาจากการทำงานของเซลล์สมองหลายๆกันสามารถสอนให้จำข้อมูลบางอย่างได้นะ ซึ่งไอ้เจ้าโมเดลคอมพิวเตอร์ง่ายๆ ที่ว่า คือ Hopfield Network ที่ได้รางวัลนั้นเอง

## What is memory?

ถ้าถามใครหลายๆคนว่า หน่วยความทรงจำคืออะไร?? สิ่งที่เป็นภาพจำคงต้องอยู่ในภาพนี้ ไม่มากก็น้อย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/10kci8GNtBZaeMWrBLjQwC9USNoFo1wWa" column=1 %}
</div>

ซึ่งโดยเนื้อแท้แล้ว สิ่งที่ Memory เหล่านี้ทำ คือ การทำตัวเป็นตารางจดรายการต่างๆไว้ว่า แต่ละตำแหน่ง (Address) จะเก็บข้อมูล (Content) อะไรไว้บ้าง หากอุปกรณ์ไหน อยากได้ข้อมูล ณ ตำแหน่งไหน อุปกรณ์เหล่านี้ก็จะไปค้นๆในตารางที่ทำไว้ แล้วก็ดึงข้อมูล ณ ตำแหน่งนั้นออกไปให้

คล้ายๆกับการทำงานของไปรษณีย์ แต่ละบ้านจะมีบ้านเลขที่อยู่ (Address) ของตัวเอง การส่งหรือรับของ (Content) ไปที่บ้านไหนทำได้โดยการส่งของ หรือ รับของ จากที่อยู่นั้นๆ _//แปลว่า จริงๆแล้ว ไปรษณีย์ มีพฤติกรรม คล้ายๆหน่วยความจำขนาดใหญ่อันนึงเช่นกันนะ_

ดังนั้น โดยคอนเซปแล้ว **หน่วยความจำ** คือ สิ่งบางอย่างที่สามารถดึงข้อมูลที่ต้องการ (Content) จากข้อมูลที่เรารู้บางส่วน (Address) — _“A general content-addressable memory would be capable of retrieving this entire memory item on the basis of sufficient partial information”_

แต่ดูเหมือนว่า หน่วยความจำในคอมพิวเตอร์ที่เราเห็นๆกัน จะต่างจากสิ่งที่พบเจอในธรรมชาติ เพราะ ดูเหมือนว่าธรรมชาติไม่มีตารางสำหรับเชื่อมโยงในแบบที่พูดไป แต่ธรรมชาติมีกฎบางอย่างที่จะนำทางให้ระบบประพฤติในแบบของมัน

สำหรับคนที่ใส่แว่น บางคนอาจจะรู้จัก Nitinol หรือ Memory wire เป็นตัวอย่างหนึ่งของ Memory ในธรรมชาติ โดยเจ้า Nitinol มันคือเส้นโลหะที่มีความสามารถในการคืนตัวให้อยู่ในรูปทรงเดิมของมันได้ หรือก็คือ มันมีความทรงจำบางอย่างซ้อนอยู่ใน Physical Property ของลวดเส้นนี้ ทำให้มันสามารถย้อนกลับไปยังรูปแบบที่กำหนดไว้ได้ _//ฟังแล้วเหมือนหุ่นยนต์เริ่มมีความจำ อีกไม่นานจะครองโลก_😂😂

โดยสิ่งที่ John Hopfield ทำ คือ

1.   นำเสนอวิธีการออกแบบ Network ที่มี Energy Landscape บางอย่าง โดยมีจุดต่ำสุด (Local Minima) แทน Memory Content ที่ต้องการ — _Storage Step_
2.   นำเสนอกฎง่ายๆบางอย่างที่ทำให้ Network เปลี่ยนแปลงไปยังรูปแบบเดียวกับ Memory Content ที่จำเอาไว้— _Retrieval Step_

ดังนั้น เราจะบอกได้ว่า Network มีความจำ ก็ต่อเมื่อ Network สามารถเปลี่ยนแปลงสถานะของตัวเองไปอยู่ในรูปแบบเดียวกับ Memory Content ได้อย่างถูกต้องได้ (หลังจากที่ Network ถูกสอนให้เก็บข้อมูล Memory Content ไปแล้ว)

_//ไม่ต้องตกใจ เริ่มมีศัพท์แสงเพิ่มขึ้นมาละ เดี๋ยวจะทยอยอธิบายไปทีละข้อๆ_

## Hopfield Network Architecture

ก่อนอื่น เริ่มจากการดูโครงสร้างของ Hopfield Network กันก่อน

Hopfield Network เป็นโมเดลที่ออกแบบมาจาก inspiration จากการศึกษาพฤติกรรมของเซลล์สมอง และ โมเดลฟิสิกต์ อย่าง [Ising model](https://en.wikipedia.org/wiki/Ising_model) (ซึ่งเป็นแบบจำลองใช้ในการอธิบายพฤติกรรมทางฟิสิกต์ของแม่เหล็ก //_ที่ซึ่งนี่ก็ไม่เชี่ยวชาญเหมือนกัน_)

โดย Hopfield Network ประกอบไปด้วย Neuron หลายๆตัว โดยแต่ละตัวสามารถมี stage ได้ หนึ่งใน 2 แบบ คือ เป็น -1 หรือ 1 สามารถเปลี่ยนไปมาๆได้ (binary threshold unit) แทน stage ของ neuron ตัวที่ i ด้วย si

และในแต่ละ neuron จะมีเส้นเชื่อมโยงไปยังตัวอื่นทุกๆตัว (fully connected) โดยเส้นเชื่อมโยงระหว่าง neuron ตัวที่ _i_ และ _j_ จะมี weight wij กำกับ คล้ายๆกับค่าความสนิทระหว่าง _i_ และ _j_ ยิ่ง wij มาก แปลว่า _i_ และ _j_ สนิทกัน แปลว่า เมื่อไรก็ตามที่ _i_ มีการเปลี่ยน stage แปลว่า _j_ จะมีแนวโน้มที่จะเปลี่ยนตาม

สามารถวาดโครงสร้างของ Hopfield Network ตามรูปภาพด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1rkKo89WcYXcfEyf33YzIrBaJX8I6Icnc" column=1 %}

<p><a href="https://arxiv.org/abs/1102.4240">https://arxiv.org/abs/1102.4240</a></p>
</div>

### Enegy Function

นิยามต่อมา คือ Enegy Function ซึ่งเป็นตัวแทนความเสถียรของโมเดล เป็นคอนเซป เดียวกันกับที่ใช้ในฟิสิกส์ นั้นคือ Enegy แทนพลังงานของอนุภาค ซึ่งอนุภาคต่างๆต้องการจะเปลี่ยนแปลงตัวเองให้อยู่ในสถานะที่มีพลังงานน้อยที่สุด (ให้อารมณ์แบบอยู่แบบชิวๆ ไม่มีอะไรมาวุ่นวาย)

โดย Enegy Function ของ Hopfield Network นิยามโดยใช้ความเป็นอันหนึ่งอันเดียวของทั้ง network โดยมีเป้าหมาย คือ อยากให้ neuron ที่สนิทๆกัน (มี weight ระหว่างกันมากๆ) มี stage เดียวกัน และ ให้ neuron ที่เกลียดกัน (มี weight ระหว่างกันน้อยๆ หรือ เป็นลบมากๆ) มี stage ต่างกัน จะได้สมการว่า

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/13AHnLmwSf-y9i2Np6jfPtXJGQU2WUcyu" column=1 %}
</div>

โดยมี si และ sj ของ stage ของ neuron ตัวที่ _i_ และ _j_ และ wij คือ weight ระหว่าง _i_ และ _j_

จะเห็นว่า E มีเครื่องหมายลบอยู่ด้านหน้า เพื่อบอกว่า เราต้องการให้ระบบมี Enegy น้อยๆ หรือก็ คือ

ถ้า network มีความเป็นอันหนึ่งอันเดียวมากๆ

=> ได้ผลรวมค่า wij มากๆ

=> ได้ energy น้อยๆ

สำหรับบางคน อาจจะเห็นสมการที่ต่างกันในเอกสารอื่นๆ เช่น

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1w8kLqex682ExDmw1dJzPyQgvN3MFZ3Pv" column=1 %}
</div>

อันนี้เกิดจากการเพิ่มให้ neuron แต่ละตัวมีค่า bias เพิ่มขึ้นมาอีก 1 ค่า เพื่อคุมการทำงานของ threshold ซึ่งจะมีอธิบายในหัวข้อต่อๆไป

ในกรณีบล๊อคนี้ จะกำหนดให้ bi = 0 ทั้งหมด เพื่อให้ง่าย _//และเพราะคนเขียน ขก._

สิ่งที่เกิดขึ้น คือ Enegy Function ที่ได้ เป็น function ของ **stage** ของ neurons ใน network และ **weights** ระหว่างการแต่ละ neurons ถ้า plot ให้สถานะต่างๆของระบบเป็นจุด 1 จุดบนระนาบ x-y และให้ ค่า Energy เป็นความสูงที่จุด x-y นั้นๆ จะได้สิ่งที่เรียกว่า Energy Landscape ตามรูปด้านล่าง

_//ถ้าคนที่เรียน ML มา จะคุ้นเคยใน term Loss Function/Loss Landscape_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1wtcJN8WVoUj6d7UH2-G8vRX0UXw5nPfY" column=1 %}

<p><a href="https://arxiv.org/abs/1712.09913">https://arxiv.org/abs/1712.09913</a></p>
</div>

โดย จะเห็นว่าเจ้า Energy Function ที่ว่า ขึ้นอยู่กับ 2 สิ่ง คือ stages และ weights ดังนั้น เราน่าจะสามารถแทน 2 สิ่งนี้กับ content และ address ในการทำงานแบบหน่วยความจำได้

โดยให้ address ผูกกับ weights นั้นคือ เราต้องการเปลี่ยนแปลง weights เพื่อดัดตัว Energy Landscape ให้อยู่ใน**_รูปแบบที่ต้องการบางอย่าง_**ที่สามารถควบคุมพฤติกรรมของ network ได้ และ ผูก content กับ stages ของ neurons นั้นคือ เมื่อ network เปลี่ยนแปลงๆไปเรื่อยตาม**_กฎบางอย่าง_**จนหยุดแล้ว จะแทน stage ที่ network สุดท้าย ที่ไม่เปลี่ยนแปลงแล้ว เป็น content ที่ network จำไว้

ซึ่งรูปแบบนี้ เป็นรูปแบบเดียวกันกับที่นัก neuroscientist คาดว่า น่าจะเป็นรูปแบบที่สมองใช้ในการเก็บความทรงจำ; ความทรงจำ == ความแรงของการเชื่อมต่อระหว่างเซลล์ประสาทในสมอง — _the strength of connections between neurons; [_[_เพิ่มเติม_](https://en.wikipedia.org/wiki/Long-term_potentiation)_]_

## **Storage Step**

จากหัวข้อก่อนหน้า เพื่อให้ Network สามารถจำอะไรบางอย่าง สิ่งที่เราต้องการ คือ

_“เปลี่ยนแปลง weights เพื่อดัดตัว Energy Landscape ให้อยู่ในรูปแบบที่ต้องการบางอย่าง”_

คำถามต่อมา คือ “_รูปแบบที่ต้องการบางอย่าง_” คืออะไร?

ในกรณีนี้ _รูปแบบที่ต้องการ_ คือ [Energy Landscape ที่ weights นั้นๆ] จะต้องมี local minima ที่จุดๆที่ stage = Content

สิ่งที่เราสามารถทำได้ คือ ทดลองค่า weights ไปเรื่อยๆ แต่ในทางปฎิบัติ มันเป็นไปไม่ได้ที่จะลองๆเรื่อยๆแล้วจะการันตีว่า จะเจอ weights ที่ทำให้ Energy Landscape เป็นไปตามที่ต้องการ

โดย John Hopfield เสนอว่า จริงๆแล้ว เราสามารถการันตีได้ โดยใช้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1vhfOYD4DTbRv8f3VCnE0LiHNMrrcoWR6" column=1 %}
</div>

ซึ่งเมื่อแทนลงใน Energy function จะได้ว่า

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1cyR96CQwqeyjEVbnJ9CDeg53Al3QBeEz" column=1 %}
</div>

จะเห็นว่า term ด้านขวา เป็น term กำลัง 2 ซึ่งการันตีว่า จะมีค่าเป็น + เสมอ แปลว่า ถ้าการเปลี่ยนแปลง si ที่จุดอื่นรอบๆ จะต้องให้ E ที่มากกว่า (ลบน้อยกว่า) หรือ เท่ากันเท่านั้น (ให้นึกถึงภาพกราฟพาราโบล่า)

ซึ่งแนวคิดแบบนี้ เป็นวิธีการเดียวกันกับ Hebbian learning rule โดย Donald Hebb ที่นำเสนอในปี 1949 เพื่ออธิบายพฤติกรรมของ synapses ในสมอง _//ซึ่งเป็นเรื่องที่นี่ไม่เชี่ยวชาญ ขอข้ามๆไปละกัน_

> Neurons that fire together wire together — Donald Hebb

### ลองดูตัวอย่าง

สมมติให้มี Hopfield Network ขนาด 256 neurons และ weights ทั้งหมด 256x256 = 65,536 เส้น

โดยจัด neurons ให้อยู่ในตารางขนาด 16x16 แปลว่า จะได้ neurons ตามรูป โดยแทน **ช่องสีขาว** เมื่อ stage ของ neuron ตำแหน่งนั้นๆ เท่ากับ 1 และ

แทน **ช่องสีดำ**เมื่อ stage ของ neuron ตำแหน่งนั้นๆ เท่ากับ -1

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1HynVX9Srg-9rGmUAoQjrMpfjAa2q8RmD" column=1 %}
</div>

ถ้าให้ Memory Content หน้าตาแบบนี้ ซึ่งแทนได้ด้วย vector ขนาด 16x16 หรือ ถ้าเปลี่ยนเป็น 1-dimension จะได้ vector ขนาด 1x256 = [1,1,1,…,-1,-1,1,1,…] ซึ่ง data vector ที่ได้สามารถนำไปเข้าสมการ wij = si * sj โดย si หรือค่าของ vector ที่ตำแหน่ง i

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1AAgHV_LuBGQMFwAKaNrjdxA6oVmv4pYG" column=1 %}
</div>

ในกรณีที่ยกมาให้ อาจจะดูยากเกินไป ถ้าให้ดูตัวอย่างที่ง่ายกว่าเดิม อย่าง

Memory Content = [1,1,-1,-1] จะได้ว่า

Weights = [[1,1,-1,-1], [1, 1, -1, -1], [-1, -1, 1, 1], [-1, -1, 1, 1]]

//แค่นี้ เราก็ได้ wights ที่พร้อมสำหรับการดึงข้อมูลแล้ว

### แต่ แต่ แต่ จะทำอย่างไร ถ้าต้องการให้ Network จำหลายๆอย่าง?

แน่นอนว่า เราสามารถทำได้ง่ายๆ โดย การซ้อนๆ Energy function ของแต่ละ Content เข้าด้วยกันตรงๆได้เลย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/12gQNo8fKabtQwjA1zmgKpmrWGYJEU9Cw" column=1 %}
</div>

โดย c แทน content แบบต่างๆที่ต้องการให้จำ และ si at c แทน ข้อมูลช่องที่ i ของ content c

ซึ่งจะทำให้เกิด Energy Landscape อันใหม่ที่มี Local Minima หลายๆจุด* ตาม Content ที่ต้องการ

_//*แน่นอนว่า ไม่เสมอไป อ่านต่อเพิ่มเติมที่ Storage Limit ด้านล่าง_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1zCj6wZHzvnVV89qsmaxiE-JQ0cKfYr3t" column=1 %}

<p>รูปนี้ ไม่ใช่ Enegry Landscape ที่ถูกต้องนะ เป็นแค่การเปรียบเปรย</p>
</div>

## Retrival Step

ในอีกด้าน หลังจากเตรียม weights พร้อมแล้ว ส่วนสุดท้ายที่เราต้องการ คือ

_“วิธีในการเปลี่ยนแปลง stage ของ network ไปเรื่อยตาม_**_กฎบางอย่าง_**_ให้ไปหยุดที่ Local Minima”_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1iXcB-9OXBdR9fHZ4-0XUZnip95ff_njK" column=1 %}

<p>ไปกดเล่นได้ที่ <a href="https://chameleontk.github.io/code-challanges/week7_hopfield_network/index.html">https://chameleontk.github.io/code-challanges/week7_hopfield_network/index.html</a></p>
</div>

โดย John Hopfield เสนอว่า Hopfield Network สามารถ converge ไปยัง local minima ได้เสมอ โดยใช้กฎง่ายๆ โดยการสุ่มเลือก neuron **ทีละ 1 ตัว (asynchronously)** และ อัพเดต stage โดยใช้สมการดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1riChCm5WEFRx5JAUF_PSj6jlCPAEVy5z" column=1 %}
</div>

หรือก็คือ ให้พิจารณา neuron ที่อยู่รอบๆ

ถ้าหากน้ำหนักของฝ่ายที่เป็น + มากกว่า ก็ให้เลือกเปลี่ยน stage เป็น 1

ถ้าหากน้ำหนักของฝ่ายที่เป็น - มากกว่า ก็ให้เลือกเปลี่ยน stage เป็น -1

เพียงแค่นี้เอง เรียบง่าย แต่ทรงพลัง

โดย John Hopfield ได้พิสูจน์ต่อว่า update rule ดังกล่าว จะการันตีว่า Network จะมีพฤติกรรม 1 ใน 3 แบบดังนี้ [[เพิ่มเติม](https://www.inference.org.uk/itprnn/book.pdf)]

1.   Network จะลู่เข้าสู่ local minima จุดใดจุดหนึ่งบน Energy Lanscape
2.   Network จะติดหล่มแล้ววนๆ oscillation อยู่ระหว่าง 2 stages
3.   Network จะมีพฤติกรรมแบบแปลกๆ (chaotic behaviour) ที่ไม่สามารถทำนายได้

โดยเนื่องจาก Hopfield Network มีลักษณะของ weights แบบ symmetric หรือ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/10HNIjuUzsndpjrVXVQrc89a7ufYoyOlY" column=1 %}
</div>

ซึ่ง John Hopfield ได้พิสูจน์ต่อว่า เพราะ หาก weights เป็น symmetric แล้วทำให้ network มีพฤติกรรมจาก update rule เป็นแค่แบบที่ 1 หรือ 2 เท่านั้น

และถ้าเราอัพเดตแบบ asynchronous หรือ อัพเดต neuron แค่ทีละตัวๆ ไม่ได้อัพเดตพร้อมกันทีเดียวทั้ง network จะการันตีได้ว่า network จะลู่เข้า local minima เสมอ — โดย Hopfield ให้ความเห็นว่า แนวคิดการอัพเดตแบบ asynchronous น่าจะใกล้เคียงกับการทำงานในธรรมชาติมากกว่าด้วย

หรือ พูดอีกแง่ การการันตีว่า Hopfield Network จะลู่เข้าหา local minima มาจากคุณสมบัติ 2 อย่าง คือ symestric weights และ asynchronous updates

จากทั้งหมดที่กล่าวมา จะเห็นว่า ความสามารถของ memory สามารถเกิดขึ้นได้จากการทำงานร่วมกันของ simple neurons ที่ทำงานร่วมกับ a simple update rule

## Storage Limit

ปัญหานึงที่น่าสนใจ คือ Hopfield Network สามารถจำได้มากแค่ไหน??

จากการ Analyse ของ John Hopfield พบว่า จำนวนข้อมูลที่ Hopfield Network สามารถเก็บข้อมูลได้ จำกัดอยู่ที่แค่ค่าๆนึง หลักจากนั้น Hopfield Network จะลู่เข้าสู่ stage แปลกๆที่ไม่ใช่ Content ที่ต้องการอีกต่อไป

ส่วนนึงเกิดในลักษณะของ spurious local minima เมื่อ local minima สองจุดที่อยู่ใกล้ๆกันมากๆ จนรวมกันเป็น local minima ใหม่ซึ่งไม่ได้เชื่อมโยงกับข้อมูลอันใดเลย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ITjz8dlSOTgrdpGuEy1wJk6vLoUSGeMF" column=1 %}

<p><a href="https://www.cs.toronto.edu/~hinton/coursera/lecture11/lec11.pdf">https://www.cs.toronto.edu/~hinton/coursera/lecture11/lec11.pdf</a></p>
</div>

โดย capacity limit ที่ John Hopfield พบอยู่ที่ ราวๆ 0.15N โดย N คือ จำนวน neuron ใน network แปลว่า ถ้าใช้ network ที่มีขนาด 256 neurons จะเก็บข้อมูลได้ประมาณ 38.4 หรือ 38 รูปเท่านั้นเอง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/17-VyF5Du401nPPJZBZKsLKA4KNBBE6EC" column=1 %}

<p>เมื่อใส่ข้อมูลไปหลายๆรูป สุดท้ายแล้ว Network จะไม่สามารถลู่เข้าไปที่ local minima ที่ต้องการอีกต่อไป</p>
</div>

แปลว่า ถ้าเราใช้ network เป็น storage แปลว่า ซึ่งแต่ละรูป เราต้องใช้ N neuron units นั้นคือ ทั้ง network เราสามารถเก็บข้อมูลได้ จำนวน 0.15N*N bits

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1HnIVxao4SO--3uFCU630A1TvMoZgjj5U" column=1 %}
</div>

แต่กลับกัน ถ้าต้องเก็บข้อมูลของ network ซึ่งมีจำนวน weights = N*N และ weight แต่ละตัวมีค่าได้ตั้งแต่ -M ถึง M โดย M แทนจำนวน memory ที่ต้องการเก็บบน network แปลว่า เราต้องใช้ memory ขนาดจำนวน

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1BFVwFixpAv5h7mwfC9Mk_TcsnHnpLqvE" column=1 %}
</div>

เทียบกันระหว่าง จำนวน bits ที่จำได้ (0.15N*N) และ จำนวน bits ที่ต้องใช้ในการเก็บข้อมูลของ network หรือ N*Nlog(2M+1)

แปลว่า ไม่ว่ายังไงก็ตาม Hopfield Network ก็ไม่มีทางคุ้มค่า เพราะในระยะยาว N*Nlog(2M+1) ให้ค่ามากกว่า 0.15N*N ไปเรื่อยๆ

นอกจากนี้แล้ว หากข้อมูลที่ใส่ไปใน network มีความ correlate กัน (รูปหน้าตาคล้ายๆกัน) จะยิ่งทำให้ Storage limit น้อยยิ่งกว่าเดิมอีก — _correlated between patterns further decrease storage capacity_

_//อ่าววววว แล้วเราจะศึกษาไปทำไมกันนะ??_

## Impacts from Hopfield Network

แน่นอนว่า Hopfield Network ไม่ใช่โมเดลที่ดีที่สุดในการเก็บข้อมูล แต่มันเป็นโมเดลแรกๆที่แสดงให้เราเห็นว่า การทำงานร่วมกันของ simple component ทำให้เกิด emergent property ที่น่าประหลาดใจได้

นอกจากนี้ Hopfield Network ยังเป็นจุดเริ่มต้นทำให้เข้าใจ(หนึ่งในความเป็นไปได้ของ)การทำงานของสมอง เอาแรงบรรดาลใจจาก field อย่าง Physics และ Neuroscience ไปในงานเชิง computational

แรงบรรดาลใจนี้ ต่อยอดไปเป็น Boltzmann Machine, VAE, GAN ไปจนถึง Modern Architecture อย่าง Transformer ที่เป็นพื้นฐานของ ChatGPT ที่กำลังจะครองโลกในอีกไม่กี่ปี 🤣🤣

สำหรับใครที่อยากศึกษา Modern Hopfield Network ซึ่งมี Storage Capacity มากกว่าเดิม + convergence rate ดีกว่าเดิม สามารถเริ่มต้นได้จากอีกเปเปอร์ ซึ่งนำเสนอโดย John Hopfield เช่นกัน อย่าง [Dense Associative Memory for Pattern Recognition](https://arxiv.org/abs/1606.01164)

สำหรับใครที่อยากเล่น Hopefield Network สามารถดู implementation แบบง่ายๆได้ตามลิงค์ด้านล่าง

## Credit

บทความนี้ ต้องขอขอบคุณ

*   [Neural networks and physical systems with emergent collective computational abilities](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/) เปเปอร์ต้นฉบับ ที่มาของรางวัลโนเบลอันทรงเกียรติอันนี้ //สารภาพว่า อ่านแล้วก็ไม่ได้เข้าใจทั้งหมด 🤯🤯🤯
*   สำหรับผู้เริ่มต้น อยากแนะนำให้ฟังคลิปนี้มากๆ เขาสรุปได้เข้าใจง่ายมากๆ [How are memories stored in neural networks?](https://www.youtube.com/watch?v=piF6D6CQxUw)
*   และสุดท้ายขอขอบคุณ คอร์ส [Neural Networks for Machine Learning](https://www.youtube.com/watch?v=cbeTc-Urqak&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9) จาก Prof. Geoffrey Hinton เป็นอีก resource ที่ย่อยง่าย

ทั้งนี้ขอขอบคุณผู้อ่านทุกๆคนที่ตามอ่านมาจนถึงตรงนี้ กราบ กราบ กราบ :)
