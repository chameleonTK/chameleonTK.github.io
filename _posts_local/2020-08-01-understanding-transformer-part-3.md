---
layout: post
title: "ทำความเข้าใจ Transformer [Part III]"
tags: [Archive, Code Code and Code]
thumbnail: "assets/img/understanding-transformer-part-3/image-01.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

> **_คำเตือน_**_เนื้อหาในบทความนี้เต็มไปด้วยศัพท์แสงทางวิชาการ โปรดใช้วิจารณญาณก่อนเสพ_

<!--more-->

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-01.png" column=1 %}

<p>credit: <a href="https://deepfrench.gitlab.io/deep-learning-project/">https://deepfrench.gitlab.io/deep-learning-project/</a></p>
</div>

ในที่สุดก็มาถึงส่วนสุดท้ายกับการเดินทางเพื่องัดแงะ แกะ ของเล่นใหม่ ที่เรียกว่า Transformer

ในบทความนี้ ผู้เขียนจะเน้นไปที่รายละเอียดปลีกย่อยที่ยังไม่ได้พูดถึงใน 2 บทความก่อนหน้า ซึ่งประกอบด้วยเทคนิคการเทรน Transformer, การทำ prediction และส่วนสุดท้าย Visualisation เพื่อทำความเข้าใจสิ่งที่เกิดขึ้นภายใน Self-attention head

สำหรับใครที่ยังไม่ได้ตามอ่าน 2 บทความ ก่อนหน้านี้ สามารถจิ้มได้ที่ลิงค์ตรงนี้ได้เลยครับ [Part I](/understanding-transformer-part-1/) และ [Part II](/understanding-transformer-part-2/)ได้เลยครับ

## Training the Transformer

### Traning Data

อะไรคือสิ่งที่สำคัญที่สุดในการทำ Machine learning? คำตอบ ก็คือ **ข้อมูล** ถ้าไม่มีข้อมูลก็ไม่สามารถสอนโมเดลได้ สำหรับ Transformer ข้อมูลที่เราต้องใช้เพื่อเทรนโมเดล คือ parallel corpus หรือ ข้อมูลประโยคที่มีประโยคเดียวกันแต่หลายภาษา ตามตัวอย่างด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-02.png" column=1 %}

<p>ตัวอย่าง parallel corpus ภาษาไทย-อังกฤษ; <a href="http://www.arts.chula.ac.th/~ling/ParaConc/">http://www.arts.chula.ac.th/~ling/ParaConc/</a></p>
</div>

โดยในเปเปอร์ จะพบว่า Transformer ถูกเทรนด้วย parallel corpus 2 ก้อน จาก WMT 2014

*   ข้อมูลก้อนแรก เป็นข้อมูลประโยคภาษาอังกฤษ-เยอรมัน มีข้อมูลประมาณ 4.5 ล้านคู่ประโยค (ใช้ขนาดของ BPE vocab = 37000 tokens)
*   ข้อมูลก้อนที่ 2 เป็นข้อมูลประโยคภาษาอังกฤษ-ฝรั่งเศษ มีข้อมูลประมาณ 36ล้านคู่ประโยค (ใช้ขนาดของ BPE vocab = 32000 tokens)

— _เทียบกับภาษาไทย ซึ่งข้อมูลแต่ละก้อนมีไม่ถึง 1 ล้านคู่ประโยค พูดแล้วก็เศร้า แต่ก็ต้องดิ้นรนกันต่อไป_

### Batching

เทคนิคนึงที่ใช้กันเป็นมาตรฐานในการเทรนโมเดล deep learning คือ เทคนิคการใช้ **_mini batch_**หรือก็คือ แทนที่จะป้อนข้อมูลทั้งก้อนไปสอนโมเดล เราจะหั่นข้อมูลเป็นชิ้นเล็กๆ เรียกว่า **_batch_**

เมื่อไรก็ตามที่โมเดลประมวลผลทุกๆประโยคใน batch แล้ว โมเดลก็จะอัพเดต 1 ครั้ง และ หลังจากอัพเดตครบทุก mini batch แล้ว จะเรียกว่าจบ 1 epoch

เหตุผลหลักที่ต้องใช้ mini-batch มาจากข้อจำกัดของหน่วยความจำในหน่วยประมวลผล (โดยปกติแล้ว เราจะใช้ GPU) โดยเราจะสามารถใช้ประสิทธิภาพของหน่วยประมวลผลได้สูงสุดเมื่อใส่ข้อมูลไปพอดีๆกับหน่วยความจำที่มี เพราะทุกๆข้อมูลในหน่วยความจำสามารถถูกส่งไปคำนวนพร้อมๆกัน โดยไม่ต้องดึงข้อมูลจาก disk หลายๆรอบ ดังนั้นการเลือกขนาด batch ที่ไม่พอดี จะทำให้ต้องใช้เวลามากขึ้นในการเทรนโมเดล —_ปัจจุบัน บ. ใหญ่ๆ อย่าง google, microsoft, nvdia ต่างแข่งกันเทรนโมเดลโดยใช้แค่ batch เดียว โดยเอา GPU หลายๆก้อนมาต่อกัน ส่วนเราๆ ทำได้แต่มอง แล้วก้มหน้าก้มตาทำ mini-batch ต่อไป_

แต่สิ่งที่น่าสนใจ คือ วิธีการแบ่ง mini batch ของ Transformer ซึ่งโดยปกติแล้ว ข้อมูลจะถูกแบ่งตามจำนวนข้อมูล

ตัวอย่าง ถ้าให้ 1 mini-batch กำหนดให้มี 2 ประโยค

> แมวสีดำของฉันกำลังเดินไปกินข้าวแสนอร่อยที่วางไว้ที่หน้าบ้าน
>
> คุณย่าชอบตะโกน เมี๊ยวเมี๊ยวเมี๊ยว เพื่อเรียกน้องแมวให้มากินข้าว
>
>  ****************************************************
>
> เสือคือแมวตัวโต
>
> แมวชอบปลาทู

ปัญหาที่เห็นได้ชัดเจน คือ ประโยคแต่ละอันยาวไม่เท่ากัน ดังนั้น การแบ่งตามจำนวนประโยค จะทำให้แต่ละ batch มีขนาดไม่เท่ากันจริงๆ ผู้สร้าง Transformer จึงเลือกที่จะแบ่ง mini-batch ตามจำนวนคำ (tokens) แทน

ตัวอย่าง ถ้าให้ 1 mini batch มีประมาณ 35 คำ

> แมวสีดำของฉันกำลังเดินไปกินข้าวแสนอร่อยที่วางไว้ที่หน้าบ้าน
>
> แมวชอบปลาทู
>
>  ****************************************************
>
> คุณย่าชอบตะโกน เมี๊ยวเมี๊ยวเมี๊ยว เพื่อเรียกน้องแมวให้มากินข้าว
>
> เสือคือแมวตัวโต
>
>  ****************************************************

Note: โมเดล Transformer ในเปเปอร์ ผู้สร้างเลือกที่จะเทรนด้วย mini-batch ที่มีขนาดประมาณ 50000 คำต่อ mini-batch (แบ่งเป็นภาษาเป้าหมาย 25000 คำ และ ภาษาเริ่มต้น 25000 คำ)

### Optimizer

นี้คือส่วนสำคัญอันดับต่อมา สำหรับผู้อ่านที่ไม่เข้าใจว่า optimizer คืออะไร? ก่อนอื่นต้องเข้าใจก่อนว่า ในแต่ละโมเดล จริงๆแล้วมันเป็นแค่กล่องดำที่ประกอบไปด้วยตัวแปรต่างๆ โดยตัวแปรพวกนี้จะถูกเอาไปใช้ในการคำนวน เพื่อให้ได้คำตอบที่ต้องการ ซึ่งการเทรนโมเดล จริงๆแล้วก็คือ**การปรับค่าตัวแปร** (tuning parameters) ในกล่องดำที่ว่านี้เพื่อให้ได้คำตอบที่สอดคล้องกับข้อมูลตัวอย่างที่เราใส่ไป

ปัญหา คือ ปรับยังไงให้ได้ค่าตัวแปรที่ดีที่สุดออกมา? และนี้แหละคือหน้าที่ของ optimizer

ไอเดีย optimizer แบบง่ายๆ อาจจะเป็นแค่สุ่มอัพเดตค่าตัวแปรแต่ละตัวไปเรื่อยๆ สิ่งที่เกิดขึ้นคือ ถ้าเราเทรนนานมากพอ เราอาจจะเจอตัวแปรที่ดีพอตามที่เราต้องการ แต่ปัญหาต่อมา คือ ต้องเทรนนานเท่าไร ถึงจะเจอสิ่งที่เราต้องการ? และในความเป็นจริงโมเดลอย่าง Transformer มีจำนวนตัวแปรอยู่หลายล้านตัว จึงแทบจะเป็นไปไม่ได้เลยที่จะสุ่มๆแล้วจะเจอสิ่งที่ใช้

เพื่อหาตัวแปรที่ดีที่สุด(หรือใกล้เคียง)ให้ได้**เร็วที่สุด** สิ่งที่จำเป็น คือ ใช้ optimizer ที่มีประสิทธิภาพ (อย่างน้อยก็ต้องดีกว่าแค่สุ่มไปเรื่อยๆ) มี optimizer หลายตัวที่สามารถนำมาใช้ได้ เช่น SGD, Adagrad, RMSProp, Adam หรือ NAG

โดยสิ่งที่ Transformer เลือกใช้ คือ Adam optimizer โดยตั้งค่า β1=0.9, β2=0.98 and ϵ=0.000000001 — _ทั้ง 3 ค่านี้ เป็นการตัวแปรที่ต้องกำหนดก่อนให้ adam optimizer ทำงาน_

สิ่งที่เจ๋งของ Adam คือ การเป็น adaptive learning rate นั้นคือ ตัวแปรแต่ละตัวไม่จำเป็นต้องอัพเดตค่าด้วยอัตราที่เท่ากัน (it uses parameter-wise learning rates) และยังสามารถใช้ผลลัพธ์จากการอัพเดตครั้งก่อนมาใช้ในการอัพเดตครั้งต่อๆไปด้วย (feedback from the training process)

เช่น ถ้าอัพเดตครั้งก่อน Adam เพิ่มค่าให้กับตัวแปร w1 ไป 3 หน่วย แล้วโมเดลทำงานได้ดีขึ้น ในครั้งต่อไป Adam ก็มีแนวโน้มที่จะพยายามอัพเดต w1 อีกครั้งแต่รอบนี้ อาจจะเพิ่ม 9 หน่วย ไปเลยทีเดียว เพราะว่าการเพิ่ม w1 มีแนวโน้มว่าจะทำให้โมเดลทำงานได้ดีมากขึ้น เป็นต้น

ด้วยเหตุนี้ Adam จึงเป็นตัวเลือกที่ดีมากๆในการเทรน Transformer

> ผู้เขียนตั้งใจว่า จะเขียนสรุปเกี่ยวกับ optimizer เพิ่มเติม ในบล๊อคต่อๆไป เผื่อมีคนสนใจ สามารถติดตามได้ :)

### Learning Rate Schedule

นอกจากใช้ Adam แล้ว Transformer ยังใช้ learning rate schedule เพื่อคุม learning rate หรือ อัตราเร็วในการอัพเดตตัวแปร อีกด้วย

เพราะว่า learning rate คือ สิ่งที่สำคัญมากๆในการเทรนโมเดล โดยมันจะเป็นสิ่งที่กำหนดว่า optimizer จะอัพเดตค่าตัวแปรมากน้อยเท่าไร? ยิ่งกำหนด learning rate มากๆ จะยิ่งทำให้ในแต่ละรอบ optimizer อัพเดตตัวแปรไปได้มาก ทำให้เรียนรู้ได้เร็วขึ้น แต่กลับกันก็จะเพิ่มความเสี่ยงที่จะข้ามค่าที่ดีที่สุดไปโดยบังเอิญ (miss the optimal parameters)

เทียบได้กับการอ่านหนังสือแบบไวๆ; มันช่วยลดเวลาได้มาก เราสามารถบอกได้ว่า หนังสือเล่มนี้ มีบทไหนที่น่าสนใจบ้าง แต่ปัญหา คือ ถ้าอ่านข้ามๆมากเกินไป เราอาจจะพลาดส่วนที่ดีที่สุดของหนังสือไปโดยที่ไม่ได้ตั้งใจ

และสิ่งที่น่าสนใจ คือ หลายๆงานวิจัยพบว่า learning rate ไม่ควรเป็นค่าคงที่ เพราะในแต่ละช่วงของการเทรนโมเดล โมเดลมีพฤติกรรมการเรียนรู้ไม่เหมือนกัน นั้นคือ ในช่วงแรก เป็นช่วง optimizer ต้องการค้นหาอย่างกว้างๆ เพื่อหาขอบเขตของค่าตัวแปรที่เหมาะสม เรียกช่วงนี้ว่า warmup steps สิ่งที่ Transformer ทำคือ ค่อยๆเพิ่ม learning rate เพื่อทำให้โมเดล skim ข้อมูลที่ได้รับ เรียนรู้ภาพรวมของปัญหาที่กำลังจะแก้

ต่อมา เป็นช่วง decay steps ซึ่งจะค่อยๆลด learning rate ลง เพื่อที่จะทำให้ optimizer ค่อยๆปรับค่าตัวแปรต่างๆแค่ทีละน้อย ทำให้สามารถเก็บรายละเอียดได้ดียิ่งขึ้น ส่งผลให้ได้ความแม่นยำที่สูงยิ่งขึ้น [[เพิ่มเติม](https://github.com/tensorflow/tensor2tensor/issues/280)]

ทั้งนี้ Transformer จึงกำหนดให้ warmup steps = 4000 steps แรก โดยจะเพิ่ม learning rate ด้วยอัตราคงที่ แล้วจึงตามมาด้วย decay steps ที่ให้ learning rate ลดลงเป็นกราฟ square root

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-03.png" column=1 %}

<p>กราฟแสดงค่า learning rate ที่ step ต่างๆ โดยกราฟแต่ละเส้น มาจากการปรับตัวแปร 2 ตัว คือ d_model และ warmup_steps [<a href="http://nlp.seas.harvard.edu/2018/04/03/attention.html#batches-and-masking">ref</a>]</p>
</div>

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-04.png" column=1 %}
</div>

_— ในเปเปอร์จริงๆแล้ว ไม่ได้อธิบายเหตุผลว่า ทำไมถึงใช้ learning rate schedule ทั้งหมดนี้ เป็นความเข้าใจของผู้เขียนเอง ถ้ามีข้อผิดพลาด ยินดีที่จะรับฟังความเห็นของผู้อ่านทุกคนครับ_

สุดท้ายนี้ หลายคนอาจจะสับสนว่า Adam และ Learning Rate Schedule ที่พูดมา มันจะไปซ้ำซ้อนกันรึปล่าว เพราะว่า Adam ก็เป็น adaptive learning rate ซึ่งหมายความว่า มันสามารถปรับ learning rate ของแต่ละตัวแปรได้ด้วยตัวเอง ทำไมต้องมีการกำหนดว่า ช่วงไหนเป็น warmup ช่วงไหน decay ?

สิ่งที่เกิดขึ้นกับ learning rate จะมีลักษณะคล้ายๆกับ กราฟราคาหุ้น นั้นคือ มันมีการขึ้นๆลงๆ (short-term) เพื่อปรับตัวเองให้เข้ากับสถาณการณ์ปัจจุบัน แต่โดยภาพรวม ก็จะมีอีกเทรนด์ในภาพรวม (long-term)

โดยการขึ้นๆลงๆแบบ short-term นี้ คือ การปรับของ Adam แต่ Learning Rate Schedule จะเป็นการปรับ learning rate ในภาพรวม [[เพิ่มเติม](https://stats.stackexchange.com/questions/286723/is-manually-tuning-learning-rate-during-training-redundant-with-optimization-met)]

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-05.png" column=1 %}

<p>กราฟราคาหุ้น [<a href="https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/">https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/</a>]</p>
</div>

### Regularization

Regularization เป็นส่วนประกอบสำคัญชิ้นสุดท้ายในการเทรนทุกๆโมเดลเลยก็ว่าได้ เนื่องจากว่า เราไม่ต้องการสอนให้โมเดลแก้ปัญหาเฉพาะในกรณีๆที่มันเคยเจอเพียงอย่างเดียว (overfitting) แต่เราต้องการโมเดลที่สามารถเข้าใจข้อมูลในภาพรวม (generalization) เหมือนกับสิ่งที่คุณครูสอนเด็กนักเรียน คุณครูต้องสอนให้นักเรียนสามารถแก้โจทย์ได้ แม้ว่าจะเปลี่ยนตัวเลขไปบ้าง หรือ มีการพลิกแพลงเล็กๆน้อยๆ ไม่ใช่แค่แก้โจทย์เฉพาะตามที่เขียนอธิบายบนกระดาน

โดยในเปเปอร์ อธิบายว่า Transformer มีการใช้เทคนิค regularization 3 อย่าง ประกอบไปด้วย: Residual, Dropout และ Label smoothing โดย 2 อันแรกได้อธิบายไปแล้วใน [Part II](/understanding-transformer-part-2/) ดังนั้นใน part นี้ จึงจะอธิบายเฉพาะในเทคนิคสุดท้าย

### Label Smoothing

ทำไมต้องใช้ label smoothing?

ถ้าย้อนกลับไปที่ Transformer Architecture จะพบว่า คำตอบของ Transformer คือ probability distribution ที่เป็นผลลัพท์ของ softmax layer โดยในการสอนว่า โมเดลแปลถูกต้องหรือไม่? probability distribution ที่ได้จะโดนเอาไปเทียบกับ คำตอบ ซึ่งอยู่ในรูปแบบของ one-hot encoding ซึ่งเป็นเวกเตอร์ที่มี 1 อยู่แค่ 1 ช่องและช่องที่เหลือมีค่าเป็น 0 เช่น

> ถ้าให้ ใน vocab ของเรามี แค่ 4 คำ คือ [“everyone”, “love”, “white”, “cats”]
>
>
> คำว่า “white” ในรูปแบบ one-hot encoding จะแทนด้วยเวกเตอร์ 4 ช่อง: [0, 0, 1, 0]
>
> คำว่า “cats” ในรูปแบบ one-hot encoding จะแทนด้วยเวกเตอร์ 4 ช่อง: [0, 0, 0, 1]

ปัญหา คือ เมื่อเอาเวกเตอร์แบบ one-hot encoding ไปสอนโมเดล มันจะบังคับให้โมเดลพ่นคำตอบที่อยู่ในรูปแบบใกล้เคียงกับ one-hot encoding มากที่สุด หรือ ก็คือ โมเดลจะให้ค่าความน่าจะเป็นมากๆ ให้กับแค่คำๆเดียว (over-confidence) — _ถ้าโมเดลยอมให้แบ่งความน่าจะเป็นไปหลายๆคำ ค่า Loss จะเพิ่มมากขึ้น ซึ่งเป็นผลลัพท์ที่โมเดลไม่ต้องการ_

สิ่งนี้ทำให้โมเดลไม่กล้าที่จะลองเปลี่ยนแปลงคำตอบตัวเองไปเป็นคำอื่น ไม่กล้าที่จะเรียนรู้ที่จะใช้คำที่ใหม่ๆ หรือ คำที่ต่างจากเดิม หรือ อีกนัยนึง คือ overfitting ซึ่งจะทำให้ไม่สามารถทำงานได้ในสถาณการณ์ที่ไม่เคยพบมาก่อน

Label smoothing จึงถูกออกแบบมาเพื่อแก้ปัญหานี้ ด้วยการพยายามกระจายความน่าจะเป็นของคำที่ได้ probability มากๆ ไปให้กับคำอื่น โดยแทนที่ คำตอบที่เป็น one-hot encoding ด้วย เวกเตอร์ที่มีค่ามากกว่าแค่ 0 และ 1 ตามสมการด้านล่าง

_y\_smoothing_ = (1 — e) * _y\_onehot_ + e / _K_
ตัวเลขในตำแหน่งที่เคยมีค่า=1 จะโดนลดค่ามาเท่ากับ e-e/K แต่จะไปเพิ่มให้กับค่าในตำแหน่งอื่นๆ e/K

โดย e คือ ปริมาณที่จะเกลี่ยให้กับค่าอื่นๆ และ K คือ ขนาดของเวกเตอร์ y

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-06.gif" column=1 %}
</div>

> ถ้าให้ ใน vocab ของเรามี แค่ 4 คำ เหมือนตัวอย่างแรก และให้ e=0.4
>
>
> คำว่า “white” จะถูกแทนด้วยเวกเตอร์ : [0.1, 0.1, 0.7, 0.1]
>
> คำว่า “cats” จะถูกแทนด้วยเวกเตอร์ : [0.1, 0.1, 0.1, 0.7]

และสุดท้ายก็เอาเวกเตอร์ใหม่ที่ได้นี้ไปคำนวน cross-entropy loss เหมือนการเทรนโมเดลอื่นๆ เมื่อใช้เวกเตอร์ใหม่นี้ในการเทรน โมเดลจะไม่ต้องพยายามเค้นคำตอบให้อยู่กับแค่คำใดคำหนึ่ง ช่วยให้โมเดลสามารถลองคำใหม่ๆได้โดยไม่กระทบกับ loss มาก [[เพิ่มเติม](https://leimao.github.io/blog/Label-Smoothing/)]

โดยสรุปแล้วการเทรน Transformer ก็จะเป็นไปตาม pseudocode ด้านล่าง

model **=** make_model(...)

training_data = load_data(...)

batches = mini_batching(training_data)opt = Adam(..)

scheduler = learningRateScheduler(optimizer, ...)**for** epoch **in** range(n_epoch):

 model.train()

 **for** i, batch **in** enumerate(batches):

 x, y = batch

 out **=** model.forward(x)

 loss **=** cross_entropy(out, labelsmoothing(y))

 loss.backward() # calculate gradient

 opt.step() # update model's weights model.eval()

sentence = model.predict(...)

## Getting Prediction

หลังจากได้โมเดลแล้ว คำถามที่สำคัญเป็นลำดับต่อมา คือ จะเรียกใช้โมเดลยังไง?

### Decoding methods

ก่อนอื่นต้องมาเข้าใจกันก่อนว่า Transformer เป็นโมเดลประเภท “Autoregressive approach” หรือก็คือ โมเดลที่พ่นคำแปลเป็นคำๆทีละคำๆ โดยในการแปลแต่ละคำ โมเดลจะใช้บริบทจากประโยคต้นทาง และ บริบทจากคำที่แปลมาแล้วก่อนหน้า มาใช้รวมกัน เพื่อคำนวนว่าคำต่อไปควรเป็นคำอะไร

โดยผลลัพท์ที่ได้จะพ่นคำแปลออกมาในรูปแบบของ probability distribution (จาก softmax layer)

ดังนั้นวิธีมาตรฐานในการใช้ Transformer ในการแปล คือ เลือกคำที่มีค่าความน่าจะเป็นสูงที่สุด จากนั้นเอาคำๆนั้นมาป้อนกลับมาให้กับโมเดล เพื่อเลือกคำต่อไป แล้วก็ทำซ้ำไปเรื่อยๆ จนกว่าจะเจอ EOS token ซึ่งหมายความว่า โมเดลตัดสินใจแล้วว่า จะจบประโยคที่ตรงนี้ (EOS = End Of Sentence)

วิธีที่ว่านี้เรียกว่า **Greedy search** ซึ่งเป็นวิธีที่เข้าใจง่าย แต่ปัญหาสำคัญที่มักพบ คือ บางครั้งการเลือกคำที่มี probability สูงๆตลอด ไม่ได้ทำให้ได้ประโยคที่มี overall probability ที่ดีที่สุด เช่น

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-07.png" column=1 %}

<p><a href="https://huggingface.co/blog/how-to-generate">https://huggingface.co/blog/how-to-generate</a></p>
</div>

ในตัวอย่าง ถึงแม้ว่า คำว่า “**dog**” มีค่าความน่าจะเป็น 0.4 ซึ่งน้อยกว่า “**nice**” ที่มีความน่าจะเป็นอยู่ที่ 0.5 แต่เมื่อดูองค์ประกอบรวมทั้งประโยค “the nice woman” มีความน่าจะเป็น overall probability = 0.5 x 0.4 = 0.20

แต่ถ้าเลือก “the dog has” จะได้ overall probability = 0.4 x 0.9 = 0.36 ซึ่งมากกว่า ประโยคที่ได้จาก greedy search

นอกจากนี้ การใช้ greedy search ในหลายๆงานมักพบว่า ประโยคที่ได้มักจะมีคำซ้ำๆ หรือ มีคำวนไปวนมาแค่ไม่กี่คำ ได้คำไม่หลากหลาย ทั้งนี้เพราะว่า คำที่มีค่าความน่าจะเป็นสูงๆมักจับกลุ่มกันเพียงแค่ไม่กี่คำ

ด้วยเหตุนี้ หลายๆโมเดลจึงเลือกที่จะใช้วิธีการอีกวิธีที่เรียกว่า **Beam search**เพื่อแก้ไขปัญหาที่อธิบายมาก่อนหน้านี้

โดย Beam search ทำงานคล้ายๆกับ Greedy search แต่แทนที่จะเลือกแค่คำที่มี probability สูงที่สุด แค่ 1 คำ; Beam search เลือก K คำที่ดีที่สุด จากนั้นก็คำนวน ทุกๆตัวเลือกที่เกิดจากทุกคำที่เลือกมา แล้วเลือกคำต่อมาที่ดีที่สุด K คำ จากนั้นก็ทำซ้ำไปเรื่อยๆ เช่นเดียวกับ Greedy search —_ปกติจะเรียกตัวเลือกแต่ละตัวว่า “beam”_

ตัวอย่าง ในกรณีนี้ เลือกให้ K=2 (เส้นทึบ และ เส้นประ)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-08.png" column=1 %}

<p><a href="https://huggingface.co/blog/how-to-generate">https://huggingface.co/blog/how-to-generate</a></p>
</div>

ในรอบแรก โมเดลจะเลือกเก็บไว้ทั้ง “nice” และ “dog” ต่อมาในรอบที่ 2 พิจารณาตัวเลือกทั้งหมด ดังนี้

*   **(“nice”, “woman”): P = 0.5 x 0.4 = 0.20**
*   (“nice”, “house”): P = 0.5 x 0.3 = 0.15
*   (“nice”, “guy”): P = 0.5 x 0.3 = 0.15
*   (“dog”, “and”): P = 0.4 x 0.05 = 0.02
*   (“dog”, “runs”): P = 0.4 x 0.05 = 0.02
*   **(“dog”, “has”): P = 0.4 x 0.9 = 0.36**

จากการคำนวน overall probability โมเดลจะเลือก “the dog has” และ “the nice woman” เป็นตัวเลือกในรอบต่อๆไป

ตัวแปร K หรือ จำนวน beam ที่ว่านี้ สามารถปรับเปลี่ยนได้ โดยเมื่อ K=1; Beam search จะมีพฤติกรรมเหมือนกับ Greedy search แต่กลับกัน เมื่อ K=จำนวนคำใน vocab ทั้งหมด; Beam search ก็จะมีพฤติกรรมเหมือนกับการ Brute force ซึ่งการันตีว่าจะได้ optimal overall probability แต่ยิ่ง K มากขึ้น Beam search จะช้าลง และต้องใช้หน่วยความจำมากขึ้น [[เพิ่มเติม](https://huggingface.co/blog/how-to-generate)] — ในเปเปอร์ใช้ K=4

### **Length Penalty**

ความยาวของประโยค เป็นอีกสิ่งหนึ่งที่มักเป็นปัญหา เพราะทั้ง Greedy search และ Beam search ต่างไม่ได้คำนึงถึงความยาวของประโยค ปกติแล้วเงื่อนไขการจบประโยคก็คือ EOS token

แต่ในเชิงปฏิบัติ EOS token ไม่ได้ออกมาตรงจังหวะตามที่ต้องการ บ่อยครั้งที่ EOS ไม่ออกมาเลย และทำให้ได้ประโยคที่ยาวเกินจริง

Transformer แก้ปัญหาด้วยการกำหนดจำนวนคำสูงสุดของประโยคที่แปล ไม่เกิน (จำนวนคำในประโยคต้นทาง+50) และให้มี early stop โดยเมื่อไรก็ตามที่พบว่า ถ้าเพิ่มคำต่อไป แล้วไม่สามารถทำให้ overall probability ดีขึ้น?? โมเดลก็จะหยุดเพียงเท่านี้

และสุดท้าย เพื่อให้ได้ประโยคที่ยาวพอเหมาะ Transformer เพิ่มตัวแปรอีกหนึ่งตัวในการคำนวน Beam search คือ length penalty ซึ่งมีหลักการว่า beam แต่ละอันจะโดนลงโทษด้วยค่า length penalty ตามจำนวนคำที่ได้จาก beam นั้นๆ ยิ่งเพิ่มคำไปใน beam จะยิ่งทำให้ overall probability ลดลงมากกว่าเดิม โดยค่า length penalty นี้สามารถคำนวนจากสมการด้านล่าง — ในเปเปอร์ให้ alpha = 0.6

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-09.gif" column=1 %}
</div>

_— ผู้แปลยังไม่ค่อยเข้าใจวิธีการคำนวน early stop และ length penalty นี้สักเท่าไร ถ้ามีความผิดพลาดยังไง สามารถแย้งได้เลยครับ :)_

### Model Average

เทคนิคสุดท้ายเพื่อเค้นประสิทธิภาพของ Transformer ที่พูดถึงในเปเปอร์ คือ การใช้โมเดลหลายๆตัวมาร่วมมือกัน โดย Transformer จะเอาผลลัพท์ที่ได้จากโมเดล 5 checkpoints สุดท้าย มาหาค่าเฉลี่ย เพื่อให้ได้ผลลัพท์สุดท้าย — _โดยในที่นี้ ขณะที่เทรนโมเดล โมเดลจะโดนบันทึกข้อมูลปัจจุบันๆ เป็น 1 checkpoint ทุกๆ 10 นาที_

การทำ model averaging เป็นอีกเทคนิคที่ใช้เพื่อลดความผิดพลาดที่เกิดจาก variance ของโมเดล ทั้งนี้เพราะว่า neural network เป็นโมเดลที่ขึ้นชื่อว่า low bias high variance กล่าวคือ มันสามารถแก้ปัญหาต่างๆได้ โดยไม่ต้องมีเงื่อนไขต่างๆมากำกับ (low bias) แต่ผลลัพย์ที่ได้จากโมเดลอาจจะมีได้หลากหลายแม้ว่าจะเทรนแตกต่างกันแค่นิดหน่อย (high variance)

โดยความผิดพลาดจาก variance นี้ มักอยู่ในรูปแบบที่ว่า โมเดล A แปลแย่ในประโยครูปแบบนึง โมเดล B แปลแย่ในประโยคอีกรูปแบบนึง เมื่อนำผลลัพท์จากทั้งโมเดล A และ B มาเฉลี่ย ความผิดพลาดของทั้งคู่ก็จะโดนเฉลี่ยไปด้วยเเหมือนกัน ทำให้ได้ผลลัพท์ในภาพรวมที่ดียิ่งขึ้น

## Results

จากคำอธิบายที่ผ่านมา ผู้เขียนมักจะอ้างว่า โมเดลแบบนี้ดี แบบนี้ไม่ดี คำถามคือ วัดผลยังไงว่าโมเดลไหนดีหรือไม่ดี?

จากหัวข้อ Decoding method จะเห็นว่า Transformer เลือกใช้ overall probability ในการตัดสินหาประโยคที่ดีที่สุด แต่ overall probability ที่ได้นั้นเป็นความน่าจะเป็นในมุมมองของโมเดล ไม่ใช่ความน่าจะเป็นจริงๆของประโยคนั้นๆ และในเชิงปฎิบัติ แทบจะเป็นไปไม่ได้เลยในการคำนวนหาความน่าจะเป็นจริงๆของประโยค (ความน่าจะเป็นที่จะเจอประโยค A เมื่ออ่านเอกสารทั้งหมดในภาษานั้นๆ) สิ่งนี้จึงไม่สามารถใช้ในการวัดผลได้

เพื่อวัดผลว่า โมเดลไหนเป็นโมเดลที่ดีที่สุด สำหรับปัญหาการแปลภาษา นักวิจัยมักวัดผลด้วยการใช้ BLEU score

โดยเจ้า BLEU score มีหลักการคร่าวๆ คล้ายกับการคำนวน precision โดยจะนับ n-gram ที่เจอในประโยคที่แปลและเจอจริงๆในประโยคอ้างอิง เทียบกับ n-gram ที่มีทั้งหมดในประโยคอ้างอิง

ทั้งนี้ BLEU score ยังเพิ่มอีก 1 ตัวแปร เรียกว่า Brevity Penalty โดย ยิ่งโมเดลกล้าที่จะตอบประโยคยาวๆ (แต่ต้องตอบถูกนะ) จะทำให้ได้ค่า BLEU มากขึ้น [[เพิ่มเติม](https://ariepratama.github.io/Introduction-to-BLEU-in-python/)1] [[เพิ่มเติม](https://www.youtube.com/watch?v=DejHQYAGb7Q)2]

พูดสรุป คือ BLEU ให้คะแนนทั้งในรูปแบบของความถูกต้องในระดับคำ ลำดับของคำ และความเหมาะสมของความยาวของประโยค

สิ่งที่น่าสนใจ คือ Transformer สามารถทำคะแนน BLEU ได้มากถึง 41.8 (เต็ม 100) ในการแปลภาษาอังกฤษไปเป็นภาษาฝรั่งเศษ แต่ใช้การประมวลผลลดลง 10-100 เท่า

และสิ่งที่น่าสังเกต คือ ความซับซ้อนในการแปลภาษาแต่ละภาษามีความแตกต่างกัน ค่อนข้างมาก จะเห็นว่า Transformer สามารถแปลภาษาอังกฤษไปเป็นภาษาฝรั่งเศษ ได้ดีกว่าแปลภาษาอังกฤษไปเป็นภาษาเยอรมันมาก ซึ่งอาจจะเป็นผลมาจาก โครงสร้างภาษา และปริมาณข้อมูล

เมื่อพิจารณาภาษาไทย ซึ่งมีข้อมูลน้อยกว่ามาก โครงสร้างภาษาซับซ้อนและแตกต่างจากภาษาอังกฤษค่อนข้างมาก นี้อาจจะเป็นอุปสรรคหลักในการสร้างโมเดลสำหรับแปลภาษาไทย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-10.png" column=1 %}
</div>

### Pre-trained Model

สำหรับใครที่สนใจ อยากจะลองเอาโมเดลที่คนอื่นเทรนมาแล้วไปลองเล่นๆ ลองดูตาม repo ด้านล่างได้เลยครับ

*   [OpenNMT](https://github.com/OpenNMT/OpenNMT-py)
*   [GluonNLP](https://github.com/dmlc/gluon-nlp/)

## Visualisation

สุดท้ายนี้ ผู้เขียนขอจบบล๊อคนี้ด้วย ภาพ visualisation ของ attention head ใน Transformer (จริงๆแล้ว ภาพนี้ เป็น attention head ของ BERT ซึ่งเป็นพัฒนาการขั้นกว่าของ transformer)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-11.gif" column=1 %}

<p><a href="https://github.com/jessevig/bertviz">https://github.com/jessevig/bertviz</a></p>
</div>

สิ่งที่น่าสนใจ คือ หากพิจารณา attention score โดยละเอียด จะพบว่า Transformer สามารถแก้ปัญหา coreference resolution หรือการหาคำทั้งหมดที่อ้างถึงสิ่ง ๆ เดียวกัน ได้อย่างถูกต้อง

เช่น ในกรณีของประโยค “**my cat**always takes a nap on the tree in my garden because **she** loves that tree”

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-12.png" column=1 %}
</div>

หรือ ตัวอย่างประโยคที่อ่านแล้วดูงงๆ อย่าง “Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo”

> สำหรับคนที่งงว่ามันแปลว่าอะไร ลองแยกทำความเข้าใจตามนี้
>
> [[[Buffalo buffalo] (that) [Buffalo buffalo buffalo]] buffalo [Buffalo buffalo]]

สังเกตว่า Transformer สามารถทำความเข้าใจได้ว่า buffalo คำที่ 5 เป็นกริยาของ subordinate clause ที่อยู่ที่ตำแหน่งคำที่ 3–5

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="understanding-transformer-part-3/image-13.png" column=1 %}
</div>

เทคนิค self-attention นี้ เป็นการเปิดประตูใหม่ๆ ทั้งในแง่ของความสามารถที่แม่นยำมากขึ้น และยังเปิดประตูในด้านการ interpretability เกิดเป็นแนวทางใหม่ๆเพื่อใช้ในการศึกษาการทำงานภายในโมเดล deep learning

ทั้งนี้ ปัญหาทาง NLP ยังไม่ถึงทางตัน งานวิจัยใหม่ๆผุดขึ้นมาแก้ปัญหาเดิมๆด้วยมุมมองใหม่ๆ โมเดลใหม่ๆ อย่าง BERT, GPT-2, Transformer-XL, RoBert etc ตบเท้าเข้ามาเรื่อยๆ เรายังไม่ถึงเวลาที่จะหยุดการเรียนรู้ ต้องสู้กันต่อไป เฮ้!!

สุดท้ายนี้ ขอขอบคุณทุกๆคนที่ตามอ่านมาจนถึงจุดนี้ และที่สำคัญ สำหรับใครที่พลาดตอนก่อนๆ สามารถตามอ่านได้ที่ [Part I](/understanding-transformer-part-1/) และ [Part II](/understanding-transformer-part-2/)ได้เลยครับ

## Credit

ต้องขอขอบคุณ เปเปอร์ต้นฉบับ [Attention Is All You Need](https://arxiv.org/abs/1706.03762) สำหรับเนื้อหาทั้งหมดนี้ และก็ต้องขอขอบคุณแหละข้อมูลเพิ่มเติมทั้งหลาย

*   [All You Need Is Attention … แค่ใส่ใจกันเท่านั้นก็พอ](http://medium.com/@u41ppp/all-you-need-is-attention-%E0%B9%81%E0%B8%84%E0%B9%88%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B9%83%E0%B8%88%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%97%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%81%E0%B9%87%E0%B8%9E%E0%B8%AD-f473f112db12) บทความภาษาไทยดีๆ เป็น inspiration ของบทความนี้เลยก็ว่าได้
*   [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) แนะนำให้อ่านแล้วรันโค้ดตาม เพราะ บทความนี้ย่อยเปเปอร์ออกมาเป็นโค้ดได้ชัดเจนและเจ๋งมากๆ ทำให้เข้าใจภาพการทำงานจริงๆ ไม่ใช้แค่สมการ !@#$%
*   [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) อีกหนึ่งบทความจาก [Jay Alammar](http://jalammar.github.io/) ซึ่งอธิบาย Transformer ด้วยภาพ ทำให้ทั้งเข้าใจง่าย +เรียบง่าย ไปพร้อมๆกัน
*   [Attention? Attention!](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html) สุดท้าย เป็นบทความรวบรวมหัวข้อต่างๆที่น่าสนใจเกี่ยวกับ Attention

## สุดท้ายนี้

> _1. ผู้เขียนพยายามอย่างเต็มความสามารถ เพื่อที่จะย่อยออกมาเป็นเนื้อหาพอดีคำ แต่กระนั้น มันก็ยังเป็นข้อมูลก้อนโต ถ้ามีส่วนไหนยังมีความมึนๆ หรือ ต้องการให้อธิบายเพิ่มเติม สามารถคอมเม้นได้จ้า_
>
>
> _2. ผู้เขียนพึ่งเริ่มศึกษางานวิจัยทางด้านนี้ ถ้ามีข้อมูลส่วนใดผิดพลาด กรุณาอย่าด่าแรง และ ขออภัยมา ณ ที่นี้ และเช่นเดียวกันกับข้อ 1) ยินดีรับฟังคอมเม้น เพื่อผู้เขียนจะได้นำไปปรัปปรุงในโอกาสถัดๆไป :)_
