---
layout: post
title: "ทำความเข้าใจ Transformer [Part II]"
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/understanding-transformer.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

> **คำเตือน** เนื้อหาในบทความนี้เต็มไปด้วยศัพท์แสงทางวิชาการ โปรดใช้วิจารณญาณก่อนเสพ

<!--more-->

ในที่สุดก็มาถึง บทความที่ 2 ของซีรีย์ “ทำความเข้าใจ Transformer” สำหรับใครที่ยังไม่ได้อ่านส่วนแรก กดไปที่ <a href="/understanding-transformer-part-1/" target="_blank" rel="noopener noreferrer">ลิงค์นี้</a> ได้เลย

ในส่วนนี้ ซึ่งอาจจะเป็นส่วนที่ยาวที่สุดในซีรีย์ ผู้เขียนตั้งใจเขียนขึ้นเพื่อแยกแจกแจงองค์ประกอบต่างๆใน Transformer

อย่างที่รู้กันไปแล้วว่า หลักการสำคัญของ Transformer นั้น คือ Self-Attention แต่ในทางปฏิบัติ มันก็ยังมีองค์ประกอบย่อยๆ อีกจำนวนมาก เพื่อบีบเค้นขีดจำกัดของการเรียนรู้ให้ได้ประสิทธิภาพสูงสุด

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1P4g75tmc0VUxhEnvSArXOwIBAu75cMms" column=1 %}

<p>credit: <a href="https://deepfrench.gitlab.io/deep-learning-project/">https://deepfrench.gitlab.io/deep-learning-project/</a></p>
</div>

# Transformer Architecture

อย่างที่อธิบายไปในบทก่อนหน้านี้ว่า Transformer ออกแบบมาอยู่ในรูปแบบที่เรียกว่า Encoder-Decoder Architecture เพื่อใช้ในการแปลภาษา

ภาพด้านบน เป็น Architecture คร่าวๆ ทั้งหมดภายใน Transformer ยอมรับตรงๆว่า ดูผ่านๆก็น่ากลัวแล้ว เพราะดูเหมือนว่า มันเต็มไปด้วยองค์ประกอบอะไรไม่รู้เยอะแยะไปหมด แต่ต่อจากนี้เป็นต้นไป เราจะค่อยๆ งัดแงะ ชิ้นส่วนเหล่านี้ออกมาที่ละจุด เพื่อมาดูกันว่า มันทำงานยังไง? และทำไมถึงต้องมีชิ้นส่วนเหล่านี้ในโมเดล?

## Input Embedding

Input Embedding ถือส่วนแรกก่อนเข้าสู่ตัวโมเดลจริงๆ เรียกได้ว่าเป็นหน้าด่านของโมเดล เป็นชั้นที่ทำหน้าที่ แปลงคำ หรือ ตัวอักษร ไปเป็นเวกเตอร์ของตัวเลข เพราะว่า Neural Network ไม่สามารถจัดการกับสิ่งอื่นที่นอกเหนือจากตัวเลขได้ ดังนั้นคำทุกคำ จะต้องถูกเปลี่ยนไปเป็นตัวเลข ก่อนเข้าไปสู่ขั้นตอนต่อไป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1gaG21vTba9iWp_K87gowFbBoD5rWygYd" column=1 %}

<p>ทั้ง Encoder และ Decoder ต่างก็มี Input Embedding เป็นของตัวเอง</p>
</div>

### **_Byte-pair Embedding_**

Byte-pair Embedding หรือ BPE เป็นเทคนิคแรกที่ Transformer ใช้ เพื่อเตรียม vocabulary ก่อนที่จะสร้าง lookup table ที่จะใช้ในการบันทึกว่า คำแต่ละคำจะเปลี่ยนเป็น vector อะไร

โดย ปัญหาของ Embedding แบบดั้งเดิม คือ การใช้คำ(word)เป็นหน่วยย่อยที่สุดของประโยต นั้นคือ 1 คำจะแทนด้วน 1 vector ดังนั้นจึงจำเป็นจะต้องลิสต์ของคำศัพท์ทั้งหมดที่คิดว่าจะเจอ และ แน่นอนว่า ยิ่งมีจำนวนศัพท์มาก ก็ยิ่งเปลืองพื้นที่ความจำ เพราะต้องสร้าง lookup table ขนาดใหญ่ แลกเปลี่ยนกับความแม่นยำของโมเดลที่(ควรจะ)เพิ่มมากขึ้น

ใน word embedding แรกเริ่ม อย่าง word2vec มีลิสต์ของคำศัพท์มากถึง 3,000,000 คำ [[more]](https://towardsdatascience.com/comparing-transformer-tokenizers-686307856955) แต่กระนั้น ก็ยังมีคำอีกจำนวนมากที่ยังเป็น unknown word เพราะว่าไม่ได้อยู่ใน สามล้านคำที่ลิสต์เอาไว้ บางคนให้เหตุผลว่า ศัพท์ที่เหล่านั้นแทบจะไม่ได้เจอในบริบททั่วๆไป ดังนั้นไม่ต้องใส่ใจกับมันมากก็ได้ แต่ในบริบทเฉพาะทางอย่าง เอกสารวิชาการ เอกสารแพทย์ หรือ หนังสือนิยายซึ่งมีการสร้างคำเฉพาะตัว เช่น Harry Potter หรือ The Lord of the ring เทคนิคเหล่านี้ จะไม่สามารถทำงานได้เลย เพราะคำที่เจอจำนวนมากจะโดนเปลี่ยนให้เป็น unknown word

เพื่อควบคุมจำนวนของคำศัพท์ (vocab) ที่จะใช้ และ จัดการกับ out-of-vocab words (OOV) หรือ คำที่โมเดลไม่เคยเจอมาก่อนตอนเทรน Transformer เลือกใช้ เทคนิคที่ชื่อว่า **_Byte-pair Embedding_** หรือ **_BPE_** [[more]](https://arxiv.org/abs/1508.07909) ซึ่งเป็นเทคนิคที่มีต้นกำเนิดมาจากเทคนิคการบีบอัดข้อมูล (lossless data compression algorithm) โดยเทคนิคนี้จะพยายามสร้างลิสต์ของข้อมูลจากการคิดว่า ทำยังไงที่จะใช้พื้นที่เก็บ (storage) ได้อย่างมีประสิทธิภาพมากที่สุด โดยเริ่มจากลิสต์ตัวอักษรทั้งหมดที่ใช้ในภาษานั้นๆ เช่น ในกรณีภาษาอังกฤษ

```python
init_vocab = ["a", "b", "c", ..., "z"]
```

ซึ่งจะได้ lookup table ขนาดเพียงแค่ 26xN โดย N คือ ขนาดของ word vector

และจะเห็นว่า lookup table แค่นี้ เพียงพอสำหรับ เปลี่ยนคำใดๆ ให้เป็นเวกเตอร์ ของตัวเลข (ในที่นี้คือ จะได้ vector หลายๆอัน หรือก็คือ matrix) ซึ่งเป็นการการันตีว่า ทุกคำสามารถเปลี่ยนเป็น word vector ได้โดยใช้ lookup table นี้

**อย่างคำว่า “kitten”**

```python
=> "kitten"

=> ["k", "i", "t", "t", "e", "n"]

=> [

 [0.1, -0.1, -0.2, 0.3], #for k

 [0.3, 0.1, -0.2, -0.3], #for i

 [-1.1, -0.1, 1.4, 0.3], #for t

 [-1.1, -0.1, 1.4, 0.3], #for t

 [0.2, 0.1, -0.6, -2.3], #for e

 [-0.1, 0.1, -2.2, 0.9], #for n

]
```

//ปล. ตัวเลขที่ใส่มาเป็นแค่เลขสุ่มๆเท่านั้น


แต่เพียงแค่นั้น อาจจะซับซ้อนน้อยเกินไป เพราะว่า ปกติแล้วเมื่อเอาตัวอักษรมารวมกันแล้ว subword ที่ได้ มักได้หน้าที่ใหม่ที่แตกต่างจากเดิม เช่น d- ที่เป็นแค่ตัวอักษรธรรมดา เมื่อเปลี่ยนเป็น prefix de- จะได้ความหมายในเชิงปลดอะไรสักอย่างออกไป เช่น de-compose, de-code

การใช้ vocab แค่นี้ ทำให้เป็นเรื่องยากที่โมเดลจะเรียนรู้หน้าที่ทั้งหมดที่เป็นไปได้ของแต่ละตัวอักษร

ดังนั้นขั้นตอนต่อมา BPE จะไล่นับว่าคู่ของตัวอักษรอะไร เป็นคู่ที่เจอเยอะที่สุด แล้วใส่คู่ตัวอักษรนั้น เป็น vocab ใหม่ เช่น ถ้า “en” เป็นตัวอักษร ที่เจอมากที่สุด คำอย่าง “kitten” จะถูกเปลี่ยนไปเป็น [“k”, “i”, “t”, “t”, “**en**”] เป็นต้น

BPE จะทำแบบนี้ไปเรื่อยๆ จนว่าจะได้ ขนาดของ vocab เท่ากับที่ต้องการ

```python
final_vocab = ["a", "b", "c", ..., "z", "th", "the", "er", ...]
```

คำที่มีพบบ่อยๆ อย่าง “the”, “have” และ prefix-suffix ที่สำคัญๆ อย่าง “-tion”, “-ity” ก็จะถูกใส่ไปเป็นหนึ่งใน vocab ของ BPE

สิ่งที่ได้ คือ ศัพท์แต่ละคำในประโยคจะโดนย่อยแล้ว แทนที่ด้วย subwords เช่น

> “In ancient times cats were worshipped as gods”
>
> => “In an-cient time-s cat-s were wor-ship-ped as god-s”

คำศัพท์ที่มีไม่ค่อยพบกันบ่อยๆ อย่าง “Grimalkin” จากเดิมที่อาจจะถูกทิ้งให้เป็น unknown word แต่ใน BPE คำนี้ก็จะโดนแทนด้วย subword อย่า “Gri-mal-kin”

วิธีการนี้มีประโยชน์อย่างมากกับภาษาที่มีลักษณะเป็น Agglutinative language หรือ ภาษาที่สามารถเอาคำมาต่อๆกันได้เยอะๆ อย่าง ภาษาญี่ปุ่น ที่มักมีปัญหา OOV เพราะว่า คำในภาษาสามารถนำมาต่อๆกันเพื่อสร้างคำใหม่ได้

นอกจากแก้ปัญหา out-of-vocab ของศัพท์หายาก (rare words) แล้ว BPE ยังสามารถควบคุมจำนวน subwords ที่จะใช้อีกด้วย

ยิง-นัด-เดียว-ได้-นก-สอง-ตัว

หลังจากเปลี่ยน words เป็น subwords แล้ว ก็เข้าสู่ Embedding ของจริง หรือก็คือ loopup table ซึ่งเป็นตารางอย่างง่าย บันทึกว่า subword นี้ๆ จะเปลี่ยนเป็นเวกเตอร์อะไร

ในช่วงเริ่มต้น loopup table นี้จะเป็นแค่ตารางกับตัวเลบสุ่มๆ เมื่อมี subword เข้ามา มันก็จะถูกเปลี่ยนเป็นเวกเตอร์ที่มีตัวเลขแบบสุ่มๆ แต่ในระหว่างการเทรน โมเดลจะค่อยๆปรับตัวเลขเหล่านี้ทีละเล็กทีละน้อย ท้ายที่สุดแล้ว subwords จะถูกแทนที่ด้วยเวกเตอร์ที่สามารถเข้ารหัสบริบทบางอย่างตามความเหมาะสมกับปัญหาและข้อมูลที่ป้อนให้กับโมเดล

ที่น่าสนใจคือ หลายๆครั้งจะพบว่า word vector ที่ได้ มักเข้ารหัสบริบทที่ให้ความหมายในระดับคำ เช่น คำที่มีความหมายใกล้เคียงกัน (word similarity) หรือ คำที่มักใช้ด้วยกัน(collocation) ให้เป็น vector ที่อยู่ใกล้ๆกัน

> แต่อย่างไรก็ตาม ผู้เขียนขอใช้หน่วยย่อยของประโยคเป็น word เหมือนเดิม เพื่อให้ง่ายสำหรับเข้าใจส่วนต่อๆไป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1qmqEUbHpftxduSU61pblCpIlfSab6_c3" column=1 %}

<p>ตัวอย่างการกระจายตัวของ Word Embedding ที่ได้จาก Word2Vec จากบทความ <a href="https://towardsdatascience.com/understanding-feature-engineering-part-4-deep-learning-methods-for-text-data-96c44370bbfa"><em>Understanding Feature Engineering (Part 4) — Deep Learning Methods for Text Data — Towards Data Science</em></a></p>
</div>

### **_Positional Embedding_**

เนื่องด้วยว่า Transformer ตัดการทำ recurrent (จาก RNNs) และ convolute (จาก CNNs) ออกไป ปัญหาที่เกิดขึ้นคือ ในขณะที่กำลังประมวลผลคำใดคำหนึ่งอยู่ โมเดลไม่มีสิ่งที่จะช่วยในการระบุตำแหน่งของคำปัจจุบัน ว่าตอนนี้กำลังประมวลผลคำที่เท่าไรในประโยค คำไหนอยู่ด้านหน้า คำไหนอยู่ด้านหลัง นักวิจัยที่ออกแบบ Transformer จึงมีความเห็นว่า เรามีความจำเป็นที่จะต้องเพิ่ม Positional Embedding เข้าไป เพื่อช่วยให้โมเดลสามารถรับรู้ตำแหน่งของคำที่กำลังพิจารณาอยู่

โดย Transformer เลือกใช้ ค่า sin/cos ในการแทน position ต่างๆ ตามสมการด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/11Li_2g1c06HyBHXJ1SrmXIOI-F6vrSvb" column=1 %}

<p>From: <a href="https://arxiv.org/pdf/1706.03762.pdf">Attention Is All You Need</a></p>
</div>

หรือ ก็คือ แต่ละตำแหน่งในประโยคจะถูกแทนที่ด้วยเวกเตอร์อันนึง โดยค่าของแต่ละช่อง เป็นค่า sin/cos function ในความถี่ต่างๆ มาผสมๆกัน เช่น

> PE(5) = [ sin(5), cos(5), sin(5*1.0136), cos(5*1.0136), …]

โดยคุณสมบัติหนึ่งของ positional embedding แบบนี้ คือ PE ณ ตำแหน่ง p+k ใดๆ สามารถเขียนให้อยู่ในรูปแบบความสัมพันธ์เชิงเส้นกับ PR ณ ตำแหน่ง p ได้ [[more]](https://timodenk.com/blog/linear-relationships-in-the-transformers-positional-encoding/)

> PE(p+k) = a * PE(p) + b

หรือก็คือ ถ้าโมเดลจะสามารถเรียนรู้คุณสมบัตินี้ด้วยตัวเอง โมเดลจะรู้ทั้ง absolute และ relative position ระหว่างคำ หรือก็คือ มันจะสามารถเทียบได้ว่า คำที่ดูอยู่นี้ คือ คำที่อยู่ตอนต้นของประโยค หรือ เป็นคำที่อยู่ก่อนหน้าคำนั้นนู้นนี้

ท้ายที่สุดแล้ว หลังจาก Transformer ได้รับ word embedding และ positional embedding ของแต่ละคำมาแล้ว embedding ทั้งคู่ จะโดนเอามาบวกกัน แล้วส่งต่อไปยัง layer ที่อยู่ถัดๆไป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1zl6j_r8VZSu_lz75FKW4JwI1-unohEN3" column=1 %}

<p>สิ่งที่เกิดขึ้นใน Input Embedding เพื่อเปลี่ยนตัวอักษรเป็นเวกเตอร์ตัวเลข</p>
</div>

**Note:**

1.   _Transformer เซตขนาดของทั้ง word embedding และ positional embedding เป็น เวกเตอร์ขนาด 512x1_
2.   _Word embedding จริงๆแล้ว จะโดนเอาไปหารด้วย sqrt(512) หรือ ประมาณ 22.63 ก่อนที่จะไปรวมกับ Positional embedding ซึ่งจะมีอธิบายเหตุผลใน component ที่อยู่ถัดๆไป_
3.   _สังเกตุว่า ตอนนี้ และจากนี้เป็นต้นไป ทุกๆ หน่วยย่อยใน Transformer จะมีข้อมูลออกขนาด 512 units เท่าๆกัน แทนด้วย d_model ทั้งนี้ก็เพื่อทำให้แต่ละหน่วยสามารถเอามาต่อกันเป็นชั้นๆได้เรื่อยๆ_
4.   _ในขั้นตอนการสร้างลิสต์ของ subwords ด้วย BPE โมเดลใช้ข้อมูลจาก corpus ที่มีคำจากทั้ง 2 ภาษา คือ ภาษาที่เราจะแปล และ ภาษาเป้าหมาย ไปพร้อมๆกัน เพราะมีงานวิจัยสนับสนุนว่า ทำแบบนี้มันดีกว่า [[more](https://github.com/rsennrich/subword-nmt)] ดังนั้น Transformer จึงมี lookup table แค่ชุดเดียว เพราะ มันมีทั้ง vocab ของทั้งภาษา และสามารถใช้ร่วมกันได้ทั้งใน Encoder/Decoder_

## Position-wise Feed-Forward Networks

ก่อนที่จะทำความรู้จักกับ self-attention มาทำความรู้จัก **_Feed-Forward Networks_** กันก่อน สำหรับคนที่ไม่มีพื้นฐานมาก่อน Neural Network ออกแบบมาเพื่อเลียนแบบการทำงานของเซลล์ประสาทในสมอง โดยจะส่งข้อมูลกันเป็นทอดๆ หรือ ทำงานเป็นชั้นๆ

จาก Universal approximation theorem อธิบายว่า ในจำนวน neural units เท่าๆกัน โมเดลที่มีหลายๆ layers สามารถเรียนรู้รูปแบบที่ซับซ้อนได้ดีกว่าการใช้โมเดลที่มีแค่ไม่กี่ชั้น

สิ่งที่เกิดขึ้นคือ ในชั้นแรกๆ มันจะเริ่มเรียนรู้สิ่งที่ง่ายๆ อย่าง เส้นแนวนอน เส้นขอบ แล้วค่อยๆนำสิ่งเหล่านั้นมาประกอบเป็น รูปทรง ไปจนกลายเป็นรูปร่างของวัตถุ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ahyW8WkUaFy8Jd9KF3e_Mlbn_wuquwDR" column=1 %}

<p>From <a href="https://str.llnl.gov/june-2016/chen">https://str.llnl.gov/june-2016/chen</a></p>
</div>

นี้จึงเป็นเหตุผลว่า ทำไมต้องใช้ deep learning หรือ neural network ที่มีหลายๆ layers เพื่อทำงานที่มันซับซ้อนๆ

ด้วยเหตุผลเดียวกันนี้ ใน Transformer จึงจะประกอบไปด้วย Neural layer ซ้อนๆกันหลายๆ layers ซึ่งเรียกชั้นเหล่านี้ว่า **_Position-wise Feed-Forward Networks_** หรือ FFN

โดย สิ่งที่เป็นเหตุผลว่าทำไมเรียก เจ้าสิ่งนี้ว่าเป็น _Position-wise_ ก็เพราะว่า Transformer จะใช้ Networks อันเดียวกันกับทุกๆคำในประโยค คล้ายๆกับ RNNs หรือก็คือ ในตอนคำนวน แต่ละคำจะโดนคูณด้วย Weight Matix เดียวกันทั้งหมด ซึ่งจะลดจำนวน parameters ที่โมเดลต้องเรียนรู้ไปได้มาก พร้อมๆกันกับควบคุมไม่ให้โมเดลยึดติดไปกับตำแหน่งใดตำแหน่งหนึ่งของคำแค่ตำแหน่งเดียว

โดย FFN หนึ่งหน่วยจะประกอบไปด้วย 1 hidden layer with 2048 units และ อีก 1 output layer with 512 units ตามรูปด้านล่าง โดยใช้ ReLU เป็น Activation function ในแต่ละ hidden unit

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1g7KpiD8l30T-uZgdEHNK7jvBYkPK4L-y" column=1 %}

<p>แถบสีแดง คือ ข้อมูลนำเข้า และ ผลลัพท์จาก FFN</p>
</div>

จากที่เล่ามา จะเห็นได้ว่า FFN ทำหน้าที่สำคัญในการสะกัดข้อมูลออกจากข้อมูลนำเข้า ซึ่งท้ายที่สุดแล้วข้อมูลที่ได้นี้ จะเป็นคำตอบที่เราต้องการ

ทั้งนี้ FFN เป็นเพียงแค่องค์ประกอบเล็กๆอันนึงในหน่วยย่อยของทั้งใน Encoder และ Decoder

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1jMzXlP4_jGdsmtWkeVmnQlG-Jqof1j2W" column=1 %}

<p>ภาคต่อหลังจากคำถูกเปลี่ยนไปเป็น vector: มันก็จะเข้าไปใน Encoder ผ่านหน่วยย่อยๆอีกหลายๆชั้น โดย ในแต่ละหน่วยย่อย จะประกอบไปด้วย FFN หนึ่งอัน + Self-Attention อีกหนึ่งอัน</p>
</div>

## Self-Attention in Detail

มาถึงจุดที่สำคัญที่สุดใน Transformer นั้นก็คือ กระบวนการ self-attention ความจริงแล้ว ก่อนที่ word vector จะโดนประมวลผลใน FFN มันต้องผ่านด่านที่ชื่อว่า Seft-Attention layer นี้ก่อน

### **_Scaled Dot-Product Attention_**

ปกติแล้ว แค่เพียง FFN หลายๆชั้น ก็สามารถแก้ไขปัญหาหลายๆปัญหาได้ดีในระดับที่น่าพึงพอใจ แต่ในปัญหาที่ซับซ้อน อย่าง Machine Translation ใช้เพียงแค่ FFN นั้นไม่เพียงพอ อย่างที่อธิบายไปแล้วในบทความ<a href="/understanding-transformer-part-1/" target="_blank" rel="noopener noreferrer">ก่อนหน้านี้</a>

> [การใช้แค่ FFN อย่างเดียว]คล้ายๆกับการเรียนอะไรสักอย่างด้วยตัวเอง โดยไม่มีใครแนะแนวทางให้ กว่าจะสามารถเข้าใจ ก็จะต้องใช้เวลาเรียนรู้นานกว่าปกติ หรือ บางครั้งอาจจะมืดแปดด้าน จบลงด้วยการปิดหนังสือ แล้วกลับไปนอน

สิ่งที่ Attention layer ทำ คือ แทนที่จะเรียนรู้ข้อมูลทุกอย่างที่อยู่ตรงหน้า มันจะเลือกว่า ข้อมูลของคำไหนบ้าง ที่มีแนวโน้มว่าจะเกี่ยวข้องกับคำที่กำลังประมวลผลอยู่ตอนนี้? หรือ คำไหนจะเป็นประโยชน์ในการแปลคำๆนี้ บ้าง?

โดยใช้หลักการคล้ายๆกับระบบ retrieval systems

ถ้าลองพิจารณา Youtube เป็นกรณีตัวอย่าง เวลาที่เราต้องการค้นหาวิดีโอบางอย่าง สิ่งที่เกิดขึ้นคือ

1.   เราพิมพ์ keywords ลงในช่องค้นหา ในทีนี้จะเรียก keywords นี้ว่า **Query**
2.   จากนั้น Youtube จะเอา query ที่ได้รับไปเปรียบเทียบกับ **Key** ของแต่ละวิดีโอ ซึ่งอาจจะเป็น video title หรือ description หรือ อาจจะเป็น เนื้อหาที่อยู่ในวิดีโอ
3.   จากนั้น Youtube ก็จะเลือก videos ที่ใกล้เคียงกับที่เราต้องการมากที่สุดออกมาให้ ข้อมูลที่ได้นี้ จะเรียกว่า **Value**

ด้วยเทคนิคเดียวกัน แต่ละ word vector จะถูกแปลงออกมาเป็น เวกเตอร์ 3 ชิ้น คือ key, value, และ query

จากนั้น สำหรับแต่ละ word จะใช้ query ของตัวเอง ไปเทียบกับ key ของ word อื่นๆในประโยค โดยในการใช้ dot product _(ใช้เชิงคณิตศาสตร์ ยิ่งเวกเตอร์ที่มีทิศทางใกล้ๆกันจะยิ่งมีค่า dot product มาก มันจึงนิยมใช้ในการเปรียบเทียบความเหมือนกันระหว่าง vector)_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ThaeAIVxE4O6LU9UIX5lkB0Z1SA3iZtR" column=1 %}
</div>

หรือ สามารเขียนให้อยู่ในรูป matrix ได้ว่า

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/18a56pDebkyDM1DhlV-mPg7rY3wHDrRBO" column=1 %}
</div>

สิ่งที่ได้ เป็นตัวแทนคะแนนความสัมพันธ์ระหว่าง word w กับ คำอื่นๆในประโยคเดียวกัน หรือก็คือ สัมพันธ์ภายในประโยคตัวเอง เป็นเหตุผลว่า ทำไมถึงเรียกว่า **_“Self”_**-attention ซึ่งในที่นี้ ขอเรียกค่านี้ว่า relavence score

กลับมาที่ในกรณีระบบ retrieval ของ Youtube หลังจากได้ relavence score แล้ว ระบบก็จะทำการเรียงลำดับตามคะแนนที่ได้ แล้วส่งออกมาเป็น ข้อมูลชิ้นเดียวที่ดีที่สุด หรือ ก็คือ video ที่มี relavence score สูงที่สุด

แต่ใน Transformer สิ่งที่เราต้องการ ไม่ได้เป็นแค่ข้อมูลก้อนใดก้อนหนึ่ง แต่เป็นภาพรวมว่า ข้อมูลชิ้นไหนน่าสนใจบ้าง ผมลัพท์ที่ได้ จึงเปลี่ยนไปเป็น ผลรวมของข้อมูลหลายๆก้อนโดยรวมกันในสัดส่วนที่ขึ้นอยู่กับ relevance score ที่คำนวนไปแล้ว (proportional retrieval)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1M592j5-0NIhG01hNn7ovCCOqDHsJXS7d" column=1 %}

<p>ตัวอย่างการคำนวน Attention เวอร์ชั่นอย่างง่าย (no scaling and softmax)</p>
</div>

ตามรูป ถ้า relevance score ระหว่าง query(แมว) และ key(แมว), key(กิน), key(ปลาทู) คือ 10, 4, 6 ตามลำดับ ผลลัพท์ที่ได้ คือ

> normalised relevance score = [10, 4, 6]/(10+4+6) = [0.5, 0.2, 0.3]
>
>
> self-attention(แมว) = 0.5value(แมว) + 0.2value(กิน) + 0.3value(ปลาทู)

ซึ่ง Transformer ทำในสิ่งที่คล้ายๆกันนี้ คือ นำ relevance score ไปเข้า **softmax function** เพื่อเปลี่ยนเป็นเวกเตอร์ความน่าจะเป็น หรือ probability vector แล้วนำไปคูณกับค่า values (เป็นลิสต์ของ value ของทุกๆคำในประโยค) จากนั้น เอาผลลัพย์ที่ได้มารวมกันเป็นเวกเตอร์

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ZF6Pwu4XKsvxADnp7Ymvl8VxTUTfp6Cp" column=1 %}
</div>

**Why Softmax?**

หลายคนคงสงสัยว่า ทำไมต้องใช้ softmax ซึ่งดูซับซ้อน ทั้งๆที่เราสามารถเปลี่ยน relavence score เป็น probability vector ได้โดยแค่ หารด้วยผลรวม (standard normalization) เหมือนในตัวอย่าง [10, 4, 6] _=>_[0.5, 0.2, 0.3]

เพราะว่า โดยทั่วไปแล้ว ค่าที่ได้จาก Neural Network มักอยู่ในรูปแบบของ logit หรือ log ของ value บางอย่าง (ปกติคือ log likelyhood)ดังนั้นการเอาค่า log มาหารด้วยผลรวมของค่า log จึงดูจะผิดและมีความหมายที่ไม่ถูกต้องสักเท่าไร เพื่อให้มีความหมายที่ถูกต้อง จึงต้องนำค่าทุกตัวไปใส่ exponential function ก่อน แล้ว ถึงจะหารด้วยผลรวม และนั้นก็คือ softmax function [[more]](http://medium.com/data-science-bootcamp/understand-the-softmax-function-in-minutes-f3a59641e86d)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1wTjqgDOECjDEARXnFqw9IsBUXiVFgb9u" column=1 %}

<p>สมการการคำนวน Attention เวอร์ชั่นอย่างง่าย (no scaling)</p>
</div>

และองค์ประกอบสุดท้าย ใน self-attention ที่ต้องพูดถึง คือ Scale ผู้เขียนเปเปอร์อธิบายไว้อย่างน่าสนใจว่า ขนาดของ query (q) และ key (k) มีผลต่อขนาดของผลลัพย์ กล่าวคือ ยิ่ง q เป็นเวกเตอร์ขนาดใหญ่ (q และ k จะต้องมีขนาดเท่ากัน เพื่อจะได้ dot product ได้) จะให้ค่า dot product ที่เป็นไปได้กว้างมากขึ้น เช่น

ถ้า q เป็นเวคเตอร์ที่มีขนาด 100 ช่อง (กำหนดให้แต่ละช่องมีค่าเป็น 0–1 มี ค่าเฉลี่ยของทุกช่อง= 0, ค่าเบี่ยงเบน =1) แล้ว q⋅k อาจจะมีค่าได้ตั้งแต่ 0–100

ถ้า q เป็นเวคเตอร์ที่มีขนาด 1000 ช่อง ค่า q⋅k อาจจะมีค่าได้ตั้งแต่ 0–1000

นั้นคือ ถ้า q ที่มีขนาด d ช่อง จะทำให้มี ค่าแปรปรวนของข้อมูล (variance) มากเท่ากับ d และยิ่ง variance มาก ก็ยิ่งทำให้ค่าที่ได้ softmax แกว่งไปเป็นค่า extream มาก (อันนึง 0.99999 ที่เหลือเป็น 0.00001 แทนที่จะเป็น 0.5, 0.2, 0.7 ) และ ค่าที่เป็น extream พวกนี้ ก็จะมีผลทำให้

*   ในกระบวนการ Self-attention แทนที่จะเป็น proportional retrieval มันก็จะเกือบจะกลายเป็น best-match retrieval หรือ เลือกเอาแค่อันเดียวที่ดีที่สุด ซึ่งเป็นผลลัพย์ที่ไม่เหมาะ เพราะว่า โดยทั่วไปแล้ว คำหนึ่งคำไม่ได้สัมพันธ์กับคำอื่นแค่คำเดียว
*   โมเดลจะเรียนรู้ได้ช้าลง เปรียบเหมือนคนที่มั่นใจในตัวเองมากๆ บอกว่า คำตอบคือ A แน่ๆ 99.99999% ถึงแม้ว่าเป็นคำตอบที่ผิด แต่มันก็แค่ลดความมั่นไปได้แค่นิดเดียว ต้องเจอคำตอบที่ผิดหลายๆรอบ ถึงจะสามารถเปลี่ยนความมั่นใจนั้นได้ หรือก็คือ ปัญหา gradient vanishing

เพื่อแก้ไขปัญหานี้ ก่อนที่จะเข้า softmax เจ้า Transformer จะเอาค่า relevence score มาหารด้วย sqrt(ขนาดของเวกเตอร์ k) เพื่อสเกลให้มันมีความแปรปรวนลดลง (reduce variance) และนี้เป็นเหตุผลเดียวกันในการหาร word vector ใน embedding layer ด้วย sqrt(512)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1kwEkYBG3113trcsXt6rT3HrPl-ESqCsl" column=1 %}

<p>สมการการคำนวน Attention เวอร์ชั่นเต็ม</p>
</div>

### How to get those Query, Key and Value?

คำถามถัดมา คือ แล้วจะหา query, key และ value ได้ยังไง?

คำตอบ คือ ใช้ linear transform หรือ พูดให้ง่ายๆ คือ เอาเวกเตอร์ของคำแต่ละคำ มาคูณด้วยเมทริกซ์อะไรสักอย่าง (จริงๆแล้ว คูณ ด้วย 3 matrix แทนด้วย Wq, Wk และ Wv)

ซึ่งค่าในเจ้าเมทริกซ์ทั้งสามตัวนี้ ถือเป็น parameters ของ Transformer ซึ่งจะอัพเดตไปเรื่อยๆ ในขณะที่ป้อนข้อมูลให้โมเดลเรียนรู้ คล้ายๆกับการสร้าง lookup table ใน input embedding layer

## Multi-head Attention

เพิ่มเติมจาก Self-Attention เนื่องจากว่า คำๆหนึ่งในประโยค ไม่ได้มีแค่ความสัมพันธ์เดียว เช่น

> Bobby takes his cats to the park because they love climbing trees.
>
> บ๊อบบี้พาแมวของเขาไปสวนสาธารณะ เพราะว่า พวกมันชอบปีนต้นไม้

สังเกตุว่า cats มีความสัมพันธ์กับ Bobby+takes ในฐานะกรรมของประโยค และก็ยังมีความสัมพันธ์กับ love + climbing ในฐานะที่เป็นประธาน

ในเชิงความหมาย climbing trees มีความสัมพันธ์กับ cats เพราะว่าเป็นสิ่งที่พวกนางชอบ แต่ก็ยังมีความหมายโดยนัยว่า the park ต้องมี trees เพื่อให้พวกนางปีน

ดังนั้น แค่ 1 attention head ซึ่งสามารถเรียนรู้ได้แค่ความสัมพันธ์รูปแบบเดียว ไม่พอในการเรียนรู้ภาพรวมของทั้งประโยค ซึ่งแก้ด้วยวิธีง่ายๆ คือ ทำ attention หลายๆรอบ โดยแต่ละรอบใช้ Wq, Wk และ Wv คนละตัวกัน แล้วค่อยนำมารวมกัน

วิธีการนี้ จะทำให้โมเดลสามารถเรียนรู้ความสัมพันธ์ได้หลายๆมุมมองไปพร้อมๆกัน (_capture various different aspects of the input_)

สุดท้าย เพื่อรวมผลลัพธ์จากทุกๆ attention head เข้าด้วยกัน เราจะทำการเอาผลลัพธ์ทั้งหมดมาต่อกัน (concatination)เป็น matrix ขนาดใหญ่ๆ แล้วคูณด้วยเมทริกซ์ Wo หรือ output matrix ซึ่งจะมิกซ์ผลลัพธ์ที่ได้ แล้วย่อมันให้เหลือเท่ากับขนาด 512 ก่อนที่จะส่งต่อไปยังส่วนถัดไป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/19c8i20kjB1UbkHYavasVEJBh_r6EKr00" column=1 %}

<p>ตัวอย่างสิ่งที่เกิดขึ้นใน Multi-head attention unit</p>
</div>

โดยใน implementation ของ Transformer ใช้ 8 attention head โดยมีเวกเตอร์ q, k, v ขนาด 64 ช่อง จากการทดลองสร้างโมเดลหลายๆแบบในเปเปอร์ พบว่า จำนวน attention head ค่อนข้างมีผลต่อโมเดลมาก คือ ถ้ามีน้อยเกินไป ข้อมูลที่ได้อาจจะไม่เพียงพอที่จะตอบโจทย์ที่เราต้องการ แต่ถ้ามันมีมากเกินไป ก็อาจจะทำให้โมเดลสับสน ประเด็นนี้ยังถือเป็นหนึ่งในประเด็นฮิตที่ต้องการงานวิจัยเพิ่มเติม

## **3 Types of attention**

กลับมาที่ attention layer อีกครั้ง ถ้าสังเกตจากรูปภาพด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Dsl4onjDvg7vAZ0ANJRl5wysgmNKZIg3" column=1 %}
</div>

จะพบว่า จริงๆแล้วใน Transformer มีการใช้ attention layer ทั้งหมด 3 ครั้ง คือ ใน Encoder, Decoder และ ในจุดที่รวมกันระหว่าง Encoder และ Decoder ถ้าพิจารณาละเอียดๆ จะพบว่า ทั้ง 3 ครั้ง มีการปรับการคำนวนเล็กน้อย เพื่อให้เหมาะสมกับจุดนั้นๆ ดังนี้

### **1. Encoder Self-Attention**

เป็น attention ที่อยู่ใน Encoder ส่วนนี้จะเหมือนกับที่อธิบายไปแล้วทั้งหมด กล่าวคือ relevance score จะถูกคำนวนในกับทุกๆคำที่อยู่ในประโยคเดียวกัน

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1OVpxBdV4psjZlXnknE97n9r5wtKkYW1O" column=1 %}
</div>

### **2. Masked Decoder Self-Attention**

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1CIXEZRz0C5hii322ySVJ3q87GAPv4KJf" column=1 %}
</div>

ใน attention layer แบบนี้ จะอยู่ในส่วนของ Decoder ซึ่งจะคำนวน relevance score กับเฉพาะคำที่อยู่ก่อนหน้ามันเท่านั้น เพราะว่า ในขณะที่โมเดลนี้ถูกนำไปใช้งานจริงๆ Transformer จะพ่นผลลัพย์มาเป็นทีละคำๆ ดังนั้นในมุมมองของ Decoder สิ่งที่มันรู้ ขณะที่กำลังจะแปลคำหนึ่งๆ คือ ประโยคต้นทาง และ คำที่เราแปลมาแล้วก่อนหน้าเท่านั้น เช่น การจะแปลประโยคด้านล่าง

> “ปลาทูน่าเป็นอาหารที่ดีสำหรับแมว”

ข้อมูลเริ่มต้นจะมีแค่ ประโยคต้นทาง เมื่อผ่านการแปล คำแรกที่ได้ คือ Tuna

แปลคำที่ 2: ข้อมูลที่มี คือ ประโยคต้นทาง + [Tuna] อาจจะได้คำว่า is

แปลคำที่ 3: ข้อมูลที่มี คือ ประโยคต้นทาง + [Tuna, is] อาจจะได้คำว่า good

แปลคำที่ 4: ข้อมูลที่มี คือ ประโยคต้นทาง + [Tuna, is, good] อาจจะได้คำว่า for

…

จนได้ประโยคสุดท้าย คือ Tuna is good for cats

เพื่อจำลองสถาณการณ์ให้ใกล้เคียงที่สุด ใน Decoder จะทำการ Mask หรือ ปรับ relevance score ของคำหลังจากคำปัจจุบันให้มีค่าเท่ากับ -inf แล้วจึงเข้า softmax เพื่อจะให้โมเดลไม่สนใจคำที่อยู่ถัดๆไป

นอกจากนี้ ถ้าเราไม่ทำ mask สิ่งที่เกิดขึ้นคือ โมเดลอาจจะทำการโกง เพราะว่า มันสามารถดูเฉลยได้เลยว่า คำต่อไปที่มันต้อง predict คืออะไร ดังนั้นสิ่งที่ได้จึงกลายเป็นแค่ ก๊อปปี้ ไม่เรียกว่า การเรียนรู้

### **3. Encoder-Decoder Attention**

รูปแบบสุดท้ายนี้ จะอยู่ในช่วงรอยต่อระหว่าง Encoder-Decoder เพื่อรวมข้อมูลจากทั้งสองโมเดลเข้าด้วยกัน โดยให้ ข้อมูลจาก Encoder เป็น keys แล้ว Decoder เป็น query

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1z497U4y4ieqH0lxqhwQZcdJ-wj_oWq3w" column=1 %}
</div>

เป็นแบบนี้เพราะว่า ในการแปลประโยคหนึ่งไปเป็นอีกภาษา โดยปกติแล้ว การจะเติมคำแต่ละคำแหน่งของประโยคปลายทาง เราจะมองไปที่ประโยคต้นทางแล้วหาคำที่ความหมายเหมือนกันมาเติม เช่น

> “ฉันให้แมวของฉันกินปลาย่างทุกวัน”

สมมติว่า ตอนนี้ได้คำแปลมาแล้ว 3 คำคือ [I, give, my]

ต่อไป สิ่งที่เราอยาก query น่าจะเป็นประมาณว่า _หาคำที่อยู่เป็นคำนามสามารถเป็นกรรมของ give ได้_ ซึ่งในที่นี้โมเดลก็จะให้ค่า attention อยู่ที่คำว่า แมว เป็นต้น

หรือก็คือ โมเดลก็จะไปหามาว่า คำไหนใน encoder น่าจะเป็นแบบที่เราต้องการ

**_คำเตือน_**_ในความเป็นจริง สิ่งที่เกิดขึ้นอาจจะไม่ได้อยู่ในรูปแบบความสัมพันธ์แบบที่อธิบายไป ที่อธิบายแบบนี้ก็เพื่อทำให้เห็นภาพเฉยๆ_

สิ่งที่เกิดขึ้นในเชิงปฎิบัติ คือ แค่ Attention + FFN layers ก็ยังไม่เพียงพอ

ใน 1 หน่วยย่อยของ Transformer หรือ เรียกว่า sublayer ยังประกอบไปด้วยเทคนิคเล็กๆอีก 3 อัน คือ

## **Layer Normalization**

Normalization เริ่มเข้ามาเป็นมาตรฐานในการเทรน Deep Learning งานวิจัยหลายๆชิ้นเห็นตรงกันว่า มันช่วยให้โมเดลเรียนรู้ได้ไวขึ้นมาก แต่โดยปกติแล้ว หลายๆโมเดล มักเลือกใช้ Batch Normalization มากกว่า Layer Normalization ส่วนหนึ่งเพราะว่า Layer Normalization ถูกออกแบบมาให้ใช้งานกับ RNNs หรือ โมเดลที่เทรนด้วยข้อมูลที่มีขนาดไม่เท่ากัน (ในกรณีของ Transformer ซึ่งเทรนด้วยประโยค และแต่ละประโยคอาจจะไม่จำนวนคำไม่เท่ากัน)

โดยหลักการทั่วไปของ Normalization layer ประกอบไปด้วย 4 ขั้นตอน

1.   คำนวนค่าเฉลี่ย (mean)
2.   คำนวนค่าความแปรปรวน (variance)
3.   ปรับค่าเป็นค่ามาตรฐาน (nomalize)
4.   ปรับด้วยค่าสเกลและชิพ (scale and shift)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1i1FMazg6LiCVoaT3O68EpiodRiAr9c9b" column=1 %}

<p>สมการทั้ง 4 สำหรับการทำ normalisation โดยปกติแล้ว eplison เป็นค่าคงที่ เพื่อไม่ให้เกิดการหารด้วย 0 และ ตัวแปร gramma และ beta ในขั้นตอนสุดท้าย เป็น ตัวแปรที่โมเดลจะต้องปรับด้วยตัวเอง ขณะที่สอนมัน (trainable parameters)</p>
</div>

หลักการทั่วไปแล้ว ทั้ง Batch Normalization กับ Layer Normalization ทำคล้ายๆกัน โดยความแตกต่าง เพียงหนึ่งเดียว คือ Batch Norm จะคำนวนค่าเฉลี่ย/ค่าความแปรปรวน จาก ผลลัพท์หลังจากคำนวนข้อมูลใน mini-Batch หนึ่งอัน(ปกติแล้ว ด้วยความจำกัดของหน่วยความจำที่ใช้การได้ ตอนเทรน เราจะค่อยๆใส่ข้อมูลทีละน้อยๆ เป็นก้อนเล็กๆ เรียกว่า mini-batch)

แต่กลับกัน Layer Normalization คำนวนค่าเฉลี่ย/ค่าความแปรปรวนของ parameters ใน Layer หรือก็คือ parameters ทุกๆตัวในชั้นเดียวกัน จะโดนปรับให้มีค่าเฉลี่ยเป็น 0 และ variance เป็น 1 ในทุกๆรอบการเทรน

เช่นใน FFN ที่มี 3 hidden units และมีค่าที่ก่อนทำการ nomalize ดังนี้

```python
# val[idx] = [h1, h2, h3]

# แทน ค่าสำหรับ hidden unit ตัวที่ 1, 2, 3 ในข้อมูลก้อนที่ idx val[1] = [2, 2, 3]

val[2] = [2, 8, 4]

val[3] = [2, 5, 2]

val[4] = [0, 3, 1]

BatchNorm["mean"]

= [(2+2+2+0)/4, (2+8+5+3)/4, (3+4+2+1)/4]

= [1.50, 4.50, 2.50]

LayerNorm["mean"]

= [(2+2+3)/3, (2+8+4)/3, (2+5+2)/3, (0+3+1)/3]

= [2.33, 4.67, 3.00, 1.33]

```

สังเกตุว่า BatchNorm จะทำ normalise หลังจากคำนวนครบ 1 mini-batch และจะอัพเดต parameters แต่ละตัวด้วย mean และ variance ที่แตกต่างกัน แต่ว่าใน Layer จะคำนวนทุกๆรอบที่มีข้อมูลนำเข้า แต่จะอัพเดต parameters แต่ละตัวด้วย mean และ variance ตัวเดียวกันเป็นรอบๆไป

### **Why normalization?**

คำอธิบายสาเหตุที่ทำให้โมเดลเรียนรู้ได้เร็วขึ้น คือ Normalization ช่วยแก้ไขปัญหาที่เรียกว่า **covariate shift**

ผู้เขียนขอหยิบคำอธิบายที่ Andrew Ng ใช้อธิบายในคอร์ส Machine Learning ดังนี้ [[more]](https://www.youtube.com/watch?v=nUUqwaxLnWs)

ลองจินตนาการว่า สมมติเรากำลังสอนให้โมเดลเรียนรู้ในการแยกรูปภาพแมวกับหมา แต่ว่ารูปแมวที่เราสอนทั้งหมดเป็นรูปแมวดำ สิ่งที่เกิดขึ้นคือ โมเดลมีแนวโน้วที่จะทำงานได้ดีกับเฉพาะภาพแมวดำ ถ้าใส่รูปแมวส้มไป โมเดลอาจจะงงๆ แล้วบอกว่า มันมิใช่แมวที่มันรู้จัก เรียกปัญหานี้ว่า covariate shift หรือ ก็คือ ถ้าข้อมูลเดิมมีการเปลี่ยนแปลงไป โมเดลอาจจะทำงานได้ไม่ดี หรือ ไม่สามารถทำงานได้เลย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1QaCxHbtHzOcrwdLlDjIeRNorCtWAs8ty" column=1 %}
</div>

สิ่งเดียวกันนี้ นอกจากเกิดขึ้นกับ ข้อมูลที่เรานำเข้า เพื่อสอนโมเดล แล้วยังเกิดขึ้นภายในโมเดลด้วยเหมือนกัน กล่าวคือ ข้อมูลที่ออกมาจาก hidden layer แต่ละชั้น มีแนวโน้วที่จะเปลี่ยนแปลง แกว่งไปแกว่งมาก ทำให้โมเดลสับสน จนไม่สามารถเรียนรู้ได้ เหมือนเรากำลังสอนเด็กน้อยแต่เราสอนภาษาอังกฤษ-ภาษาไทย-ภาษาจีน สลับกันไปมา ถึงแม้ว่าเด็กน้อยจะเรียนรู้ได้ แต่ก็ต้องใช้เวลามากกว่าเด็กคนอื่นๆ

การ Nomalization ใน hidden layer จะช่วยให้เวกเตอร์ในแต่ละชั้น มีความแกว่งลดลง มีผลทำให้ hidden units สามารถเห็นภาพชัดขึ้นว่า ควรจะจัดการกับข้อมูลที่รับค่ามายังไง เพื่อให้ได้ผลลัพย์ที่ต้องการ

ในหนังสือ Deep Learning ของ Ian Goodfellow ยังอธิบายเพิ่มเติมว่า กระบวนการนี้เป็นการ decoupling หรือ ทำให้แต่ละ layer ไม่ขึ้นต่อกัน หรือ การเปลี่ยนแปลงที่ layer หนึ่ง จะมีผลกับ layer อื่นๆน้อยลง (เดิม การเปลี่ยนแปลงนิดๆหน่อยๆ ใน layer นึง มีผลกระทบกับ layer ที่อยู่ถัดๆไป) ซึ่งทำให้เพิ่มประสิทธิภาพในการเรียนรู้ของแต่ละ layer

อาจจะเปรียบเทียบได้ว่า เหมือนมีชั้นบางๆมาคั้นกลาง ทำให้ layer อื่นจะไม่มากวนใจอีกต่อไป …

## **Residual Connections**

เทคนิคนี้(น่าจะ)เป็นที่รู้จัก จากโมเดลที่ชื่อว่า ResNet ซึ่งเป็นโมเดลที่ชนะการแข่งขันที่ชื่อว่า ILSVRC ปี 2015 ในโจทย์ Image Classification จาก ImageNet

Residual connections คือ เทคนิคซึ่งออกแบบขึ้นเพื่อแก้ปัญหา gradient vanishing เพราะ ยิ่งโมเดลมีจำนวน layer มาก ข้อมูลไม่สามารถส่งย้อนกลับเพื่อปรับ parameter ในชั้นแรกๆ เหมือน เราตะโกนบอกว่า “คำตอบที่ให้มาผิดนะ” คนที่อยู่ใกล้ๆเรา ก็จะได้ยินเสียงชัดเจน เขาจึงสามารถปรับตัวเองให้ถูกต้องได้ แต่ คนที่อยู่ไกลๆ ได้ยินแค่เสียงอู้อี้ๆ ไม่รู้ว่าคำตอบที่เขาส่งไปถูกต้องรึปล่าว จึงไม่สามารถเกิดการเรียนรู้ที่ถูกต้อง

สิ่งที่ ResNet ทำคือ ในแต่ละ layer จะมีการสร้างทางพิเศษเชื่อมข้ามไปยัง layer ถัดๆไป เพื่อทำให้มันได้ยินคำตอบชัดเจนขึ้น (higher gradient) [[more](http://medium.com/@natthawatphongchit/%E0%B8%A1%E0%B8%B2%E0%B8%97%E0%B8%B3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81-resnet-%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%94%E0%B8%B5%E0%B8%81%E0%B8%A7%E0%B9%88%E0%B8%B2-aec3a8c10793)] ซึ่งในที่นี้ คือ เพิ่มเส้นเชื่อมต่อจาก layer ก่อนหน้าไป layer ถัดไป (skip connection) โดยข้อมูลที่ข้ามไปนี้จะไปบวกกับข้อมูลเป้าหมาย ตามรูป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1hvOKqfCeU8LYS34QElsmABmWsX7VdmHe" column=1 %}

<p>Figure from <a href="https://arxiv.org/abs/1512.03385">https://arxiv.org/abs/1512.03385</a></p>
</div>

โดย Transformer ใช้เทคนิคเดียวกันนี้ โดยผลลัพท์สุดท้ายของแต่ละ sublayer จะไม่ใช้แค่ ผลลัพธ์จาก FFN แต่เป็น FFN บวกกับข้อมูลที่รับเข้ามา เพื่อเร่งกระบวนการเรียนรู้ของโมเดล

## **Dropout**

ชิ้นส่วนสุดท้าย ที่ไม่พูดถึงไม่ได้ คือ Dropout layer

เป้าหมายของ Dropout คือ ขณะที่เทรนในแต่ละรอบ Dropout layer จะแอบไปสุ่มลบ hidden units บางตัวออกไป (เป็นจอมโจรแห่งวงการ deep learning) วิธีการนี้ เป็นการบังคับให้โมเดลต้องปรับตัวไม่ให้ขึ้นอยู่กับ hidden units แค่อันใดอันหนึ่งเพียงอันเดียว หรือ overfitting กับข้อมูลรูปแบบใดรูปแบบหนึ่งเกินไป เพราะ hidden units อันนั้นจะโดนลักพาตัวไปเมื่อไรก็ได้

ทั้งนี้ ใน Transformer เจ้า Dropout layer นี้ จะโดนเอาไปใส่ในทุกๆส่วนของโมเดล ตั้งแต่ Input embedding (ทั้ง Positional และ BPE embedding), FFN layer, Multi-head Attention layer และ ก่อน Residual unit เรียกได้ว่า Dropout ในทุกๆขั้นตอน จนมีคำพูดติดตลกว่า จริงๆแล้ว Transformer ใช้หลักการสำคัญคือ Dropout มากกว่าที่จะเป็น self-attention เพราะว่า มันมีจำนวน dropout layer มากกว่า attention layer เสียอีก

ซึ่งในที่นี้ Dropout layer ใน Transformer ถูกเซตให้ dropout rate = 0.1 เป็นค่าเริ่มต้น หรือก็คือ มันจะสุ่มลบ hidden units ประมาณ 10%

## Encoder & Decoder

สรุปภาพรวมของ Encoder และ Decoder

**Encoder** ประกอบไปด้วย

1.   Input Embedding ซึ่งจะเอา BPE subwords เปลี่ยนให้เป็น Word Embedding แล้วบวกกับ Positional Embedding สร้างเป็น word vector ของแต่ละ subword
2.   Word vector จะผ่านเข้าไปใน Encoder ซึ่งจะประกอบไปด้วย ชั้นของหน่วยย่อย ซ้อนกันเป็นชั้นๆ ทั้งหมด 6 ชั้น แทนด้วย Nx = 6
3.   หน่วยย่อยแต่ละชั้น ประกอบไปด้วย Multi-head attention layer, LayerNorm, FFT และ Dropout (แทนด้วยเส้นสีเทาๆ) ตามรูปด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1kIjieUI_jEDY_kylSqHlG0QW4VG-gpB6" column=1 %}
</div>

ส่วนใน **Decoder** จะประกอบไปด้วย

1.   Input Embedding เหมือนกับ Encoder (จริงๆแล้ว Encoder และ Decoder ใช้ lookup table อันเดียวกัน)
2.   หลังจาก word vector จะผ่านเข้าไปใน Decoder ซึ่งจะประกอบไปด้วย ชั้นของหน่วยย่อย ซ้อนกันเป็นชั้นๆ ทั้งหมด 6 ชั้น แทนด้วย Nx = 6 เหมือนกับ Encoder
3.   หน่วยย่อยแต่ละชั้น ประกอบไปด้วย Masked Attention layer, Encoder-decoder Attention layer, LayerNorm, FFT และ Dropout ตามรูปด้านล่าง สังเกตุว่า แอบมีเส้นสีแดงที่เป็น Output จาก Encoder โผล่เข้ามาด้วย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1CQs1aAC0nyREzykNxVzYyLIQQF5shSDF" column=1 %}
</div>

ในที่สุด เราก็งัดแงะมาจนถึงโค้งสุดท้ายของ Transformer

หลังจากเอา Encoder มาต่อกับ Decoder แล้ว ยังมี Linear Layer อีกชั้น เป็นขั้นตอนสุดท้าย โดย Linear Layer จะใช้ค่าเดียวกับ lookup table ใน Input Embedding ซึ่งเสมือนการแปลง ข้อมูลที่ได้กลับไปเป็น word vector อีกครั้ง

ผลลัพท์จาก Linear Layer จะโดนใส่ไปใน Softmax function เพื่อเปลี่ยนเป็น probability vector ที่มีขนาดเท่ากับจำนวน vocab ในระบบ

probability vector นี้จะถูกตีควาให้ออกมาเป็นคำตอบที่ได้จากการรันในแต่ละรอบ ซึ่งอาจจะใช้คำที่มี probability สูงที่สุด หรือ อาจจะสุ่มเลือกคำตามความน่าจะเป็นที่ได้จาก probability vector แต่ในเปเปอร์ใช้เทคนิคที่เรียกว่า Beam Search ซึ่งจะอธิบายในบทความตอนหน้า (ที่ไม่รู้ว่าจะเขียนเสร็จเมื่อไร)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1-eG9WNyn7lhRB9YHzjmgZW_vmUkNs8AW" column=1 %}
</div>

การเดินทางที่แสนยาวนานมาถึงจุดพักที่ 2 แล้ว

หากใครอ่านแล้ว งงๆ อยากรู้ความเป็นมาของ Transformer แนะนำให้ย้อนกลับไปอ่าน <a href="/understanding-transformer-part-1/" target="_blank" rel="noopener noreferrer">Part I</a> ซึ่งผู้เขียนได้เล่าที่มาที่ไปของ Transformer พร้อมทั้งอธิบายว่าทำไม CNNs และ RNNs แบบเดิมๆ ถึงไม่เพียงพอสำหรับ งานทางด้าน NLP

และ ในตอนต่อไป

<a href="/understanding-transformer-part-3/" target="_blank" rel="noopener noreferrer">Part III</a>  ผู้เขียนจะมาเปิดเผยเงื่อนงำเทคนิคการเทรนต่างๆ กว่าจะมาเป็น Transformer อย่างที่เราเห็นๆกัน

ฝากติดตามอ่านด้วยนะครับ :)

## Credit

ก่อนอื่นต้องขอขอบคุณ เปเปอร์ต้นฉบับ [Attention Is All You Need](https://arxiv.org/abs/1706.03762) สำหรับเนื้อหาทั้งหมดนี้ และก็ต้องขอขอบคุณแหละข้อมูลเพิ่มเติมทั้งหลาย

*   [All You Need Is Attention … แค่ใส่ใจกันเท่านั้นก็พอ](http://medium.com/@u41ppp/all-you-need-is-attention-%E0%B9%81%E0%B8%84%E0%B9%88%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B9%83%E0%B8%88%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%97%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%81%E0%B9%87%E0%B8%9E%E0%B8%AD-f473f112db12) บทความภาษาไทยดีๆ เป็น inspiration ของบทความนี้เลยก็ว่าได้
*   [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) แนะนำให้อ่านแล้วรันโค้ดตาม เพราะ บทความนี้ย่อยเปเปอร์ออกมาเป็นโค้ดได้ชัดเจนและเจ๋งมากๆ ทำให้เข้าใจภาพการทำงานจริงๆ ไม่ใช้แค่สมการ !@#$%
*   [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) อีกหนึ่งบทความจาก [Jay Alammar](http://jalammar.github.io/) ซึ่งอธิบาย Transformer ด้วยภาพ ทำให้ทั้งเข้าใจง่าย +เรียบง่าย ไปพร้อมๆกัน
*   [Attention? Attention!](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html) สุดท้าย เป็นบทความรวบรวมหัวข้อต่างๆที่น่าสนใจเกี่ยวกับ Attention

## สุดท้ายนี้

> 1. ผู้เขียนพยายามอย่างเต็มความสามารถ เพื่อที่จะย่อยออกมาเป็นเนื้อหาพอดีคำ แต่กระนั้น มันก็ยังเป็นข้อมูลก้อนโต ถ้ามีส่วนไหนยังมีความมึนๆ หรือ ต้องการให้อธิบายเพิ่มเติม สามารถคอมเม้นได้จ้า
>
>
> 2. ผู้เขียนพึ่งเริ่มศึกษางานวิจัยทางด้านนี้ ถ้ามีข้อมูลส่วนใดผิดพลาด กรุณาอย่าด่าแรง และ ขออภัยมา ณ ที่นี้ และเช่นเดียวกันกับข้อ 1) ยินดีรับฟังคอมเม้น เพื่อผู้เขียนจะได้นำไปปรัปปรุงในโอกาสถัดๆไป :)
