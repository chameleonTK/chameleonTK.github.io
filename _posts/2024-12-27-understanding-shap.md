---
layout: post
title: "ทำความเข้าใจ SHAP"
tags: [Archive, Code Code and Code]
thumbnail: "assets/feats/understanding-shap/image-01.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

> บทความนี้เป็นการสนองความต้องการส่วนตัวที่ว่า อยากจะหาเวลาอ่านและทำความเข้าใจ SHAP จริงๆจังๆซักที หลังจากที่ใช้งานมันในงานวิจัยของตัวเองมานานหลายปี ในที่สุดเวลานั้นก็มาถึง

<!--more-->

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1b0hSa55GeffjlTgJf9jFqCt_cTRdVxAB" column=1 %}
</div>

## TL;DR

SHAP หรือ **SH**apley **A**dditive ex**P**lanations เป็นแนวคิดที่นำเสนอขึ้นมาโดย S.M. Lundberg & S-I. Lee (2017) ใน เปเปอร์ชื่อ [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) เพื่อเป็น metric ในการศึกษาการทำงานของ AI Model

> _หากใครต้องการอ่านรายละเอียดเพิ่มเติม กดลิงค์ไปอ่านเปเปอร์ต้นฉบับได้เลยนะฮะ_

## ทำไมต้องทำความรู้จัก SHAP

ในช่วงหลายปีที่ผ่านมา พูดได้เต็มปากว่า วงการ AI พัฒนาไปอย่างก้าวกระโดด กระโดดแล้วก้าวต่ออีกไปมาๆแบบ 10 ตลบ //ตามไม่ทันแล้วจ้านายจ๋า ช่วยหยุดพัฒนากันสัก 3 เดือนได้ไหม?

และการพัฒนาที่ว่า มักอยู่ในรูปแบบของการพัฒนาความแม่นยำของโมเดล พูดได้เลยว่า ตอนนี้เราอยู่ในยุคที่โมเดล AI แม่นจนน่ากลัว แต่ความแม่นยำที่ได้ มันไม่ได้มาพร้อมกับคำอธิบายว่า **“ทำไมโมเดลถึงตัดสินใจอย่างนั้น”** — a tension between accuracy and interpretability.

ปัญหานี้ จึงนำไปสู่การวิจัยเพื่ออธิบายการทำงานของโมเดล AI โดยเฉพาะโมเดล Deep Learning ต่างๆ ที่ยังไม่มีทฤษฎีใดๆที่สามารถอธิบายได้อย่างชัดเจน และ เกิดเป็นสาขาการวิจัยที่เรียกว่า e**X**plainable **AI**หรือ XAI

และ SHAP ก็เป็นเทคนิคหนึ่งใน XAI เพื่อศึกษาว่าฟีเจอร์แต่ละอันมีผลต่อพฤติกรรมของโมเดลอย่างไรบ้าง?

## From Shapley Value to SHAP

หลักการของ SHAP หยิบยืมพื้นฐานมาจาก สิ่งๆหนึ่งที่เรียกว่า Shapley Value ซึ่งเป็น[แนวคิดที่นำเสนอโดย L. Shapley](https://www.degruyter.com/document/doi/10.1515/9781400881970-018/html?lang=en&srsltid=AfmBOoqjBmu4DP8_ui3Rnnxbgco9D8Aml5dzoI64F_NuWiughwLMt3q3) เมื่อปี 1951 (และได้รับรางวัลโนเบลสาขาเศรษฐศาสตร์จากงานชิ้นนี้ด้วยเช่นกัน ในปี 2012 🙇🏻🙇🏻)

โดยเจ้า Shapley Value ที่ว่า เป็นสิ่งที่ถูกสร้างขึ้นในสาขา Game Theory เพื่อศึกษาเกมกลุ่มหนึ่งที่เรียกว่า “Cooperative Game” หรือ เกมที่ผู้เล่นทุกคนต้องร่วมมือกันเพื่อ**เป้าหมายร่วม**อะไรบางอย่าง

โดยคำถามที่ L. Shapley ตั้งใจศึกษา คือ เราจะบอกได้อย่างไรว่า _“ผู้เล่น (players) แต่ละคนมีส่วน (contributions) มากน้อยเท่าไรในผลลัพธ์ที่เกิดขึ้นในเกม นึงๆ (payout)”_

หรือเขียนในอีกมุมมองนึงได้ว่า _“ถ้าเราต้องการแบ่งรางวัลที่ได้จากเกมๆนึง ให้แก่ผู้เล่นทุกคนตามการมีส่วนร่วมของผู้เล่นคนนั้นๆ เราจะต้องแบ่งอย่างไรให้ยุติธรรมที่สุด”_

จากคำถามที่ได้มา จะพบ keywords สำคัญๆ ดังต่อไปนี้

1.   ผู้เล่น (players)
2.   การมีส่วนร่วม (contributions)
3.   ผลลัพธ์ที่เกิดขึ้น (payout)
4.   และ จุดที่สำคัญที่สุด คือ “แบ่งอย่างไรให้ยุติธรรมที่สุด” (fair distribution) ??

และ L. Shapley พบว่า Shapley Values ของแต่ละเกม คือ คำตอบ**หนึ่งเดียว**ของโจทย์ที่ว่านี้ หรือก็คือ Shapley Values คือ ตัวเลขสัดส่วนที่ “ยุติธรรมที่สุด” ในการแบ่งผลลัพธ์ (หรือ รางวัล) สำหรับผู้เล่นแต่ละคน

> หลายๆคนคงเริ่มจะหงุดหงิดกันละว่า “ยุติธรรมที่สุด” ที่ว่า มันคืออะไร ???

ก่อนที่จะพูดถึงนิยามของความยุติธรรมที่ว่า ขอเริ่มต้นจากการนิยามเกม และ ตัวแปรต่างๆที่จำเป็นกันก่อน

1.   นิยาม เซตของผู้เล่น (Players) ด้วย P = {1, 2, 3, … p} โดย |P| คือ จำนวนผู้เล่นทั้งหมดในเกม
2.   นิยาม กลุ่มย่อยๆของผู้เล่น (Coalition) ด้วย S ⊆ P
3.   นิยาม φ = {φ₁, φ₂, φ₃, …, φₚ} แทน ผลตอบแทนที่ควรจะแบ่งให้ ที่ผู้เล่นแต่ละคนในเกมนั้นๆ
4.   นิยาม รางวัล หรือ ผลลัพธ์ที่เกิดขึ้น (Payout) ด้วย value function: v(S) มีโดเมนเป็น Power Set ของ P และ เรนจ์ เป็น real number

พูดอีกแบบ คือ v(S) รับ coalition S เป็น input และ output เป็นตัวเลขๆนึงแทนรางวัลที่ได้จากเกมนั้นๆ ในกรณีที่ให้เฉพาะผู้เล่นใน S เป็นผู้มีส่วนร่วมในเกม (และ ผู้เล่นคนอื่นนั่งเฉยๆไม่ยุ่งกับเกม)

และ กำหนดให้ v(∅) = 0 ถ้าไม่มีผู้เล่นเล่นในเกมนั้นๆ ผลลัพธ์ที่ได้ต้องเท่ากับศูนย์

งานของ L. Shapley ได้นิยาม “ความยุติธรรม” ด้วยคุณสมบัติ 4 ข้อ ได้แก่

**#1. Efficiency:**ผลรวมของผลตอบแทน φᵢ ของผู้เล่นแต่ละคนได้รับ ต้องเท่ากับ รางวัลรวมทั้งหมดกรณีที่ผู้เล่นทุกคนร่วมมือกัน

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1yL3_Pf3L1-GDDsB8ESVZQNkBKex53wb6" column=1 %}
</div>

**#2. Symmetry:** ถ้าผู้เล่นสองคนใดๆ j, k ทำให้ได้ผลลัพธ์เหมือนกัน ในทุกๆ กลุ่มย่อย (Coalition) ที่ผู้เล่นนั้นๆลงไปเล่นด้วย ผลตอบแทนที่จะแบ่งให้ผู้เล่น j และ k ต้องเท่ากันเสมอ!

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Sihi8HATkgYvNh8xGD0-OKta34O4l8Mw" column=1 %}
</div>

**#3. Null effects/Dummy:**ผู้เล่นที่ไม่ทำให้ผลลัพธ์ของเกมเปลี่ยนแปลง ในทุกๆ กลุ่มย่อย (Coalition) ที่ผู้เล่นนั้นๆลงไปเล่นด้วย (พวกผู้เล่นที่ไร้ประโยชน์ 🤔) ผู้เล่นคนนั้นจะต้องไม่ได้รับผลตอบแทนใดๆ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1yJw7KAY0vzaU4dkrI2usYnS21IuPT_u2" column=1 %}
</div>

**#4. Linearity:**ถ้ามีเกม 2 เกมที่แตกต่างกัน ผลตอบแทนที่ผู้เล่นแต่ละคนได้จะต้องเท่ากับผลรวมของของตอบแทนที่ผู้เล่นคนนั้นๆได้ จากแต่ละเกมมารวมกัน

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1xzIt3PwCN5S5_EOkdl1snSWMA1I2pwtM" column=1 %}
</div>

_//ถ้าความยุติธรรม ความดี ความสุข ในโลกความเป็นจริง มันนิยามง่ายๆแบบนี้ก็คงจะดีแฮะ_

จากคุณสมบัติทั้งหมด 4 ข้อนี้ L. Shapley ได้พิสูจน์ว่า มีวิธีการแบ่งรางวัล**_แบบเดียวเท่านั้น_**ที่จะมีคุณสมบัติครบทั้ง 4 ข้อ (one and only one unique solution!!) และผลลัพธ์นั้น คือ Shapley Values ของเกมนั้นๆนั่นเอง

_//และแน่นอนว่า ถ้าใครไม่เห็นด้วยว่า คุณสมบัติ 4 ข้อนี้เป็นนิยามที่ดีสำหรับการแบ่งผลตอบแทนอย่างยุติธรรม แปลว่า Shapley Values น่าจะไม่ใช่คำตอบที่คุณตามหา_

โดยต่อมา [H.P. Young (1985)](https://link.springer.com/article/10.1007/BF01769885) และ [S.M. Lundberg & S-I. Lee (2017)](https://papers.nips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html) ได้พิสูจน์ว่า จริงๆแล้ว คุณสมบัติ 4 ข้อที่ว่ามา สามารถลดให้เลือกแค่ 2 ข้อ คือ Efficiency และ Monotonicity ก็พอแล้ว

**#5. Monotonicity:**สำหรับเกม 2 เกมที่แตกต่างกัน v₁ และ v₂ ถ้าผลลัพธ์จากการมีส่วนร่วมของผู้เล่นในเกม v₁ มากกว่าหรือเท่ากับ v₂ จะได้ว่า ผลตอบแทนของผู้เล่นคนนั้น v₁ ต้องมากกว่าหรือเท่ากับ v₂ เสมอ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ld9prF3joIx-002MNxmJeFEJPGcV7lw3" column=1 %}
</div>

_//คุณสมบัติสุดท้าย อาจจะทำให้งงๆและดูจะไม่จำเป็นในตอนนี้ อยากให้ดูผ่านๆ และจำไว้ว่า มันมีอยู่ ซึ่งจะมีผลต่อกับออกแบบ SHAP ที่จะกล่าวถึงในตอนท้ายๆ_

## Calculating Shapley Value

เพื่อหาวิธีการแบ่งผลตอบแทนที่ยุติธรรมตามคุณสมบัติทั้ง 4 ข้อ (หรือ 2 ข้อ) ที่ว่ามา

ผลตอบแทน หรือ Shapley Value จะต้องเป็นไปตามนิยามต่อไปนี้

> “The Shapley value is the average marginal contribution of a feature value across all possible coalitions”
>
>
> —[C. Molnar, (2024)](https://christophm.github.io/interpretable-ml-book/shapley.html)

หรือ ก็คือ ผลตอบแทน ของ ผู้เล่น i หรือ φᵢ ต้อง เท่ากับ

> ค่าเฉลี่ยของ (ผลต่างระหว่าง (ผลลัพธ์จากเกมที่ผู้เล่น i มีส่วนร่วม และเกมที่ผู้เล่น i ไม่มีส่วนร่วม) ในทุกๆกลุ่มย่อยที่เป็นไปได้)

อ่านแล้วดูซับซ้อนๆ แต่จริงๆแล้ว สามารถไม่ได้ซับซ้อนอย่างที่คิด หากพิจารณาจากสมการต่อไปนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Uyx-Eyt-D-ukv-OHcP5SzuzeWpJnHMiH" column=1 %}
</div>

เฮือกกก 😰😰😰 ดูเหมือนจะไม่ได้ช่วยซักเท่าไร งั้นลองเติมสี และทำความเข้าใจกันทีละส่วนๆ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1zAAdrehBv6SxoURFfgPxJMOZ5IaQfH8r" column=1 %}
</div>

ส่วนที่ 1 ขอเริ่มจากส่วนที่อยู่ด้านในที่สุด ซึ่งเป็นส่วนที่ง่ายที่สุดในสมการนี้(?) ซึ่งก็คือส่วนของสีแดง: **v(S ∪ {j})**หมายถึง _“ผลลัพธ์จากเกมที่ผู้เล่น i มีส่วนร่วม”_

ไปต่อยัง ส่วนที่ 2 ใกล้ๆกัน ส่วนของสีเขียว: **v(S)**หมายถึง _“ผลลัพธ์จากเกมที่ผู้เล่น i ไม่มีส่วนร่วม”_

ดังนั้นถ้าเราเอามารวมกัน จะได้ว่า **v(S ∪ {j})-****v(S)**คือ “ผลต่างระหว่าง (ผลลัพธ์จากเกมที่ผู้เล่น i มีส่วนร่วม และเกมที่ผู้เล่น i ไม่มีส่วนร่วม)”

ต่อมา ขอข้ามมาดูส่วนสีชมพู Sum of S ซึ่งหมายถึง “ในทุกๆกลุ่มย่อยที่ S ที่ไม่มีผู้เล่น j ”

และส่วนสุดท้ายและเป็นส่วนที่ดูยากที่สุด คือ ส่วนสีฟ้า แทน จำนวนของจำนวนกลุ่มย่อยที่ S ที่เป็นไปได้ ตามที่อ้างถึงในส่วนสีชมพูที่อธิบายไปก่อนหน้า โดยเมื่อเอาผลรวมที่ได้มาหารด้วยจำนวน จะทำให้เราได้ “ค่าเฉลี่ย” นั้นเอง

แต่ แต่ แต่ จำนวนกลุ่มย่อยจากในส่วนสีฟ้าที่ว่าไม่ใช่เป็นเพียงการนับแบบธรรมดานะซิ

_//ทำไมต้องทำให้ซับซ้อนด้วยนะ??_

เพื่อทำความเข้าใจเพิ่มเติม ต้องมาพิจารณาวิธีการตีความการนับที่ว่า โดยในบล๊อค นี้จะอธิบาย การตีความใน 2 รูปแบบ ได้แก่ Set Defition และ Order Definition โดยการตีความแต่ละแบบก็จะนำไปสู่การ implement เพื่อหาค่า Shapley values ในรูปแบบที่แตกต่างกัน

### **# Set Defition**

การตีความแบบนี้ จะมองส่วนสีฟ้า คือ **ค่าน้ำหนัก (weights)**

เนื่องจากกลุ่มย่อย S สามารถมีหลายๆขนาด ตั้งแต่ 0 ไปจนถึง |P|-1 แต่ กลุ่มย่อยในแต่ละขนาดมีจำนวนรูปแบบที่เป็นไปได้ต่างกัน เช่น กลุ่มย่อยที่มีขนาด = 0 หรือ ขนาด = |P|-1 จะมีได้เพียงรูปแบบเดียว แต่ กลุ่มย่อยขนาดอื่นสามารถมีจำนวนรูปแบบมากกว่า 1

ดังนั้นจึงกำหนด weights ขึ้นเพื่อทำให้กลุ่มย่อยแต่ละขนาดมีอิทธิพลต่อการคำนวนผลตอบแทนแบบเท่าๆกัน โดยจะแทน term ส่วนสีฟ้านี้ด้วย w₁, w₂, w₃, …, เป็น weights ที่เกิดจาก |S| = 1, 2, 3, …

**สำหรับคนที่ยังงง สามารถดูตัวอย่างดังต่อไปนี้**

> **ตัวอย่าง**

ถ้าให้ เซตของผู้เล่น P = {a, b, c, d, e}

ในการพิจารณา φₐ หรือ ผลตอบแทนของผู้เล่น a จะต้องพิจารณากลุ่มย่อย S ในทุกๆกรณี ซึ่งจะประกอบไปด้วย

_//กำหนดให้ S’ = เซตของผู้เล่นที่ไม่อยู่ใน S และไม่ใช่ผู้เล่นที่สนใจ ณ ขณะนั้น

// หรือ S’ = P — S — {a})_

กรณี |S| = 0 ซึ่งมี 1 กรณี คือ

S = ∅ และ S' = {b, c, d, e}

w0 = 0!(5–0–1)! / (5!) = (0! 4!) / 5! = 24/120

w0*1 = 24/120
กรณี |S| = 1 ซึ่งมี 4 กรณี คือ

S = {b} และ S' = {c, d, e}

S = {c} และ S' = {b, d, e}

S = {d} และ S' = {b, c, e}

S = {e} และ S' = {b, c, d}

w1 = 1!(5–1–1)! / (5!) = (1! 3!) / 5! = 6/120

w1*4 = 24/120

กรณี |S| = 2 ซึ่งมี 6 กรณี คือ

S = {b, c} และ S' = {d, e}

S = {b, d} และ S' = {c, e}

S = {b, e} และ S' = {c, d}

S = {c, d} และ S' = {b, e}

S = {c, e} และ S' = {b, d}

S = {d, e} และ S' = {b, c}

w2 = 2!(5–2–1)! / (5!) = (2! 2!) / 5! = 4/120

w2*6 = 24/120

กรณี |S| = 3 ซึ่งมี 4 กรณี คือ

S = {c, d, e} และ S' = {b}

S = {b, d, e} และ S' = {c}

S = {b, c, e} และ S' = {d}

S = {b, c, d} และ S' = {e}

w3 = 3!(5–3–1)! / (5!) = (3! 1!) / 5! = 6/120

w3*4 = 24/120

กรณี |S| = 4 ซึ่งมี 1 กรณี คือ

S = {b, c, d, e} และ S' = ∅

w4 = 4!(5–4–1)! / (5!) = (4! 0!) / 5! = 24/120

w4*1 = 24/120

จะเห็นว่า wᵢ * (จำนวนของกลุ่มย่อยที่มีขนาด i) เป็นค่าคงที่ = 1 / |P| เสมอ

หรือ ถ้าจะคำนวนย้อนกลับไป เพื่อหาค่า w จะได้ตรงกับ term สีฟ้าที่เห็นอยู่พอดิบพอดี

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Q2UzI4CHEDyECQoym80t_tQ5ER1YuPBf" column=1 %}
</div>

ถ้าเป็นไปตามการตีความแบบนี้ จะพูดได้ว่า Shapley Values คือ “ค่าเฉลี่ย**แบบถ่วงน้ำหนัก**” รูปแบบนึงนั้นเอง

**คำนวน Shapley Values**

ตามการนิยามแบบ Set Definition สามารถคำนวน Shapley Values ได้โดยใช้แนวทาง [Shapley regression values](https://onlinelibrary.wiley.com/doi/abs/10.1002/asmb.446) โดยใช้ pseducode ดังนี้

def ShapleyValue(p):

 phi = 0

 for S in getAllCombinations(P-{p}):

 payoutWithP = v(S+{p})

 payoutWithoutP = v(S)

 w = getWeight(len(S))

 phi += w*(payoutWithP - payoutWithoutP)

 return phi

**# Order Defitions:**

การตีความแบบนี้ จะมองส่วนสีฟ้า คือ **จำนวนลำดับ**ที่เป็นไปได้ในการสร้างกลุ่มย่อย S — all possible different _permutations_ in which the coalition can be formed.

นั้นคือ ขณะที่กำลังพิจารณา ผลตอบแทน ของ ผู้เล่น i หรือ φᵢ จะได้ว่า

ณ กลุ่มย่อย S ใดๆ เราจะสามารถแบ่งเซตของผู้เล่น P เป็น 3 กลุ่ม ดังนี้

P = S + {i} + S’ โดย |S’| = |P| - |S| - 1

นั้น คือ

**จำนวนลำดับทั้งหมดที่เป็นไปได้ในการสร้างให้มีกลุ่มย่อย S**=

(จำนวน permutation ของ S) *

(จำนวน permutation ของ {i}) *

(จำนวน permutation ของ |S’| )

= |S|! * 1! * (|P| — |S| — 1)!

เมื่อเฉลี่ยในทุกๆลำดับที่เป็นไปได้ทั้งหมด หรือ |P|! ก็จะได้ เท่ากับ term ส่วนสีฟ้าพอดิบพอดีอีกแล้ว!!

**สำหรับคนที่ยังงง สามารถดูตัวอย่างดังต่อไปนี้**

> **ตัวอย่าง**

ถ้าให้ เซตของผู้เล่น P = {a, b, c, d, e}

ในการพิจารณา φₐ หรือ ผลตอบแทนของผู้เล่น a แบบเดียวกับตัวอย่างก่อนหน้า

กรณี S = {b} และ S' = {c, d, e} จะได้ลำดับที่เป็นไปได้ทั้งหมด 6 ลำดับ ดังนี้

1. b > a > c > d > e

2. b > a > c > e > d

3. b > a > d > c > e

4. b > a > d > e > c

5. b > a > e > c > d

6. b > a > e > d > c
นั้นคือ weight ในขณะที่คำนวน S = {b} จะเท่ากับ (1!3!)/5! หรือ 6/120

ลองอีกตัวอย่าง

กรณี S = {b, c} และ S' = {d, e} จะได้ลำดับที่เป็นไปได้ทั้งหมด 4 ลำดับ ดังนี้

1. b > c > a > d > e

2. b > c > a > e > d

3. c > b > a > d > e

4. c > b > a > e > d

นั้นคือ weight ในขณะที่คำนวน S = {b, c} จะเท่ากับ (2!2!)/5! หรือ 4/120

ดูๆไปแล้ว ก็ไม่ต่างอะไรกับการคำนวนแบบ Set Definitions แต่ แต่ แต่ การตีความแบบนี้ สามารถนำมา visualise การคำนวนที่อยู่ในรูปแบบตารางได้ ตามตัวอย่างต่อไปนี้

> **ตัวอย่าง**

ถ้าให้ เซตของผู้เล่น P = {1, 2, 3} และ พิจารณา φ₁

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1CJLY_xxNG0NPYqWyDCxcA4K7EErf_miD" column=1 %}

<p>credit: <a href="https://www.youtube.com/watch?v=_TEjJn9nemM">https://www.youtube.com/watch?v=_TEjJn9nemM</a> by</p>
</div>

จะเห็นว่า เราสามารถคำนวน φ₁ สามารถทำได้ง่ายๆ โดยการหาค่าเฉลี่ยของ **ผลต่างของผลลัพท์** ในจังหวะที่ผู้เล่น 1 โดยเพิ่มเข้ามาในเกมจากทุกๆลำดับที่เป็นไปได้

ตัวอย่าง การพิจารณา φ₂

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1FLqApiiz1NZfRRISxz0r30g6GRBYU6qc" column=1 %}
</div>

ตัวอย่าง การพิจารณา φ₃

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1se87HOuuUec1eaHUp2YMXN0cRGCSc74V" column=1 %}
</div>

ด้วยแนวทางเดียวกันนี้ การตีความแบบ Order Definition สามารถเปลี่ยนนิยามของ Shapley Values ให้อยู่ในรูปแบบที่ง่ายขึ้น ได้ตามนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1cnC_Pc2LJjJBOAeQh6d6nq1Vwh-_EQcg" column=1 %}
</div>

โดยมี Π แทน ลำดับทั้งหมดที่เป็นไปได้ ซึ่ง |Π| = |P|! และ Sⱼ ที่ 𝜏 แทน เซตของผู้เล่นที่อยู่ก่อน j ในลำดับ 𝜏

> **ตัวอย่าง**

ถ้าให้ เซตของผู้เล่น P = {1, 2, 3} จะได้ว่า

Π = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
ถ้าให้ 𝜏 = (1, 2, 3) จะได้ว่า S₁ ที่ 𝜏 = ∅

ถ้าให้ 𝜏 = (1, 3, 2) จะได้ว่า S₁ ที่ 𝜏 = ∅

ถ้าให้ 𝜏 = (2, 1, 3) จะได้ว่า S₁ ที่ 𝜏 = {2}

ถ้าให้ 𝜏 = (2, 3, 1) จะได้ว่า S₁ ที่ 𝜏 = {2, 3}

ถ้าให้ 𝜏 = (3, 1, 2) จะได้ว่า S₁ ที่ 𝜏 = {3}

ถ้าให้ 𝜏 = (3, 2, 1) จะได้ว่า S₁ ที่ 𝜏 = {2, 3}

สิ่งหนึ่งที่น่าสนใจ คือ การนิยามแบบนี้ ลำดับของผู้เล่นแต่ละอัน จะมี weight เท่ากันทั้งหมด คือ 1/|P|! เนื่องจาก |Π| = |P|! ซึ่งทำให้การคำนวนยุ่งยากน้อยลง (รึปล่าว?)

**คำนวน Shapley Values**

ต่อยอดตามการตีความแบบ Order Definition สามารถคำนวน Shapley Values ได้โดยใช้แนวทาง [Shapley regression values](https://onlinelibrary.wiley.com/doi/abs/10.1002/asmb.446) โดยใช้ pseducode ดังนี้

def ShapleyValue(p):

 phi = 0

 permutations = getAllPermutations(P)

 for prm in permutations:

 S = getPlayersFromPermu(prm, p)

 payoutWithP = v(S+{p})

 payoutWithoutP = v(S)

 phi += (payoutWithP - payoutWithoutP)
phi /= len(permutations)

 return phi

พูดไปแล้วการตีความแบบ Order Definition ดูจะไม่ได้แตกต่าง หรือ พิเศษไปกว่าการตีความแบบ Set Definition

แต่ แต่ แต่ สิ่งหนึ่งที่ทำให้การนิยาม Shapley Values แบบหลัง น่าสนใจมากกว่าแบบแรก คือ นิยามแบบ Order Definition สามารถนำไปสู่วิธีการการประมาณค่า Shapley Values ที่เร็วกว่าแบบเดิมมากๆ โดยใช้ Monte Carlo Method

## Approximating Shapley Value

จากที่ผ่านๆมา สิ่งหนึ่งที่น่าสังเกต คือ วิธีการคำนวน Shapley Values ล้วนมี BigO อยู่ในระดับ O(|P|!) เป็นอย่างน้อย เนื่องจาก ขั้นต่ำๆแล้วต้องคำนวนผลลัพธ์จากทุกๆ combinations (ในการนิยามแบบ Set Definition) หรือ ทุกๆ permutations (ในการนิยามแบบ Order Definition)

แปลว่า ในความเป็นจริงๆ หากต้องการคำนวน Shapley Values สำหรับเกมที่มีผู้เล่น 10 คน อาจจะต้องการการคำนวนทั้งหมดราวๆ 3,628,800 รอบ ถ้าเพิ่มจำนวนผู้เล่นเป็น 20 คน อาจจะต้องการการคำนวนมากถึง 2.4 ล้านล้านล้าน รอบ ซึ่งไม่สามารถทำได้จริงในเชิงปฎิบัติ

โดยเฉพาะอย่างยิ่ง เมื่อนำไปใช้ในบริบทของ AI ซึ่งเป็น setting ที่ต้องการผู้เล่นมากถึง 100–100 คน (ซึ่งจะอธิบายต่อไปว่าคือยังไง??) ดังนั้น จึงเป็นไปไม่ได้เลยที่จะคำนวน Shapley Values แบบตรงๆ อย่างที่เล่าๆมา

_//เอ๋ สรุปที่เขียนมา คือ ไม่มีประโยชน์เหรอ ???_

แต่ก็ไม่ใช่ว่า จะไม่สามารถคำนวน Shapley Values ได้เลยซะทีเดียว

แนวทางนึงในการประมาณค่า Shapley Values คือ การประยุกต์ใช้ Monte Carlo Method กับการนิยามตามการนิยามแบบ Order Definition

หรือเรียกวิธีการนี้ว่า “[Shapley sampling values](https://link.springer.com/article/10.1007/s10115-013-0679-x)” โดยแทนที่สมการ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1cnC_Pc2LJjJBOAeQh6d6nq1Vwh-_EQcg" column=1 %}
</div>

ด้วยสมการใหม่ดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1FEgnv-cQYuzmNXWub6SiUxxrMcTYVS7Z" column=1 %}
</div>

โดยแทน M ด้วยจำนวนที่จะสุ่ม และ Πₘ เป็น เซตของลำดับจำนวน M ตัวที่สุ่มจาก Π

จากสมการข้างต้น บอกได้ว่า ยิ่ง M มาก จะยิ่งได้ค่า Shapley Values φ ที่แม่นยำมากขึ้น

**คำนวน Approximated Shapley Values**

สามารถคำนวน Shapley Values ได้โดยใช้แนวทาง [Shapley sampling values](https://link.springer.com/article/10.1007/s10115-013-0679-x) โดยใช้ pseducode ดังนี้

def ShapleySamplingValue(p):

 phi = 0

 for i in range(M):

 prm = getARandomPermutation(n=len(P))

 S = getPlayersFromPermu(prm, p)

 payoutWithP = v(S+{p})

 payoutWithoutP = v(S)

 phi += (payoutWithP - payoutWithoutP)
phi /= M

 return phi

## What about SHAP?

ผ่านไปมากกว่า 1500 คำ ที่พูดถึงแต่เรื่อง Shapley Values โดยไม่มีการกล่าวถึง SHAP 🤣🤣🤣

> แล้วอะไรคือ SHAP และ SHAP เหมือนหรือแตกต่างจาก Shapley Values อย่างไร ???

หากจะนิยามสั้นๆ ในเปเปอร์ของ S.M. Lundberg & S-I. Lee (2017) นิยาม SHAP ดังนี้

> [SHAP is] the Shapley values of a conditional expectation function of the original model

ใครงง?? ไม่เป็นไรนะครับ แต่ถ้าไม่งง? ก็ปิดบล๊อคนี้ไปได้เลยครับ จบแค่นี้แหละ… เพราะเนื้อหาต่อไปนี้ จะเป็นการอธิบายประโยคสั้นๆประโยคนี้

ตามคำอธิบายของ S.M. Lundberg & S-I. Lee กล่าวง่ายๆได้ว่า SHAP คือ การประยุกต์ใช้ Shapley Values ในการศึกษาพฤติกรรมของ AI Model

ถ้าจะให้พูดละเอียดมากขึ้น SHAP ปรับมุมมองให้ prediction จาก Model บน input หนึ่งๆ เป็น เหมือนกันเล่นเกม นั้นคือ

1.   ผู้เล่น (players) => ฟีเจอร์ต่างๆของ input x
2.   ผลลัพธ์ที่เกิดขึ้น (payout) => ค่า prediction ที่ได้จาก Model
3.   การมีส่วนร่วม (contributions) => ค่า feature importance ของ feature แต่ละตัว ต่อ prediction ที่เกิดขึ้น
4.   การหา Shapley Values => วิธีที่ยุติธรรมที่สุดในการประมาณ feature importance ของ feature แต่ละตัว ต่อ prediction ที่เกิดจากการทำงานของ Model หนึ่งๆ

โดยมีภาพรวมว่า ฟีเจอร์ต่างๆของ input x จะต้องร่วมมือกันเพื่อทำให้เกิดผลลัพย์บางอย่างจาก Model

ในมุมมองนี้ เป็นการเปลี่ยนจากคำถามเดิม ของ L. Shapley ที่ว่า

_“ผู้เล่น (players) แต่ละคนมีส่วน (contributions) มากน้อยเท่าไรในผลลัพธ์ที่เกิดขึ้นในเกม นึงๆ (payout)”_

เป็น

_“ฟีเจอร์ (features) แต่ละตัวมีความสำคัญ (feature importance) มากน้อยเท่าไรใน การคำนวนคำตอบ (prediction) ของโมเดล”_

แต่แค่เปลี่ยนมุมมองมันไม่พอที่จะนำ Shapley Values ไปใช้ เนื่องจากการทำงานของ Model แตกต่างจาก Cooperation Game แบบทั่วๆไป นั้นคือ

_โดยปกติแล้ว เป็นเรื่องที่ยากมากที่จะเทรน AI Model ต่างๆ ซ้ำๆด้วย จำนวนฟีเจอร์ที่แตกต่างกัน ซึ่งเป็นการเปลี่ยนแปลง model architecture ที่ทั้งยุ่งยาก เสียเวลา และซับซ้อน— With great “architecture change” comes great responsibility_

โดยเฉพาะอย่างยิ่ง เมื่อใช้งานกับโมเดลที่มีขนาดมากกว่า millions parameters ซึ่งเป็น standard model ที่ใช้ในปัจจุบัน

แต่การคำนวน prediction จากฟีเจอร์ที่แตกต่างกัน เป็นส่วนสำคัญ และ จำเป็นต่อการคำนวน value function: v(S) ที่ S เป็นเซตของฟีเจอร์แค่บางส่วนเท่านั้น

ด้วยเหตุนี้ จึงจำเป็นต้องมีการปรับแต่งเงื่อนไขบางอย่าง เพื่อให้สอดคล้องกับการใช้งานในแง่ของการศึกษา AI Model

> สั้นๆ: แปลว่า SHAP != Shapley Values นะจ๊ะ

ก่อนที่จะพูดต่อไปถึงการนิยาม SHAP ขอแวะนิยามตัวแปรต่างๆที่เกี่ยวข้องกันก่อน เริ่มจาก

1.   นิยาม ชุดข้อมูลนำเข้า X = {x¹, x², x³, …, xᶰ} โดย |X| = N
2.   นิยาม ข้อมูลนำเข้าที่ต้องการศึกษา ด้วย x = {x₁, x₂, x₃, …, xₖ} กล่าวคือ x แต่ละตัวประกอบไปด้วยฟีเจอร์ k ตัว หรือ x ∈ Rᵏ
3.   นิยาม x′ ∈ {0, 1}ᵏ แทน ข้อมูลนำเข้าแบบง่าย (simplified input) ของ x

โดย x′ᵢ = 0 แทนความหมายว่า ไม่ต้องสนใจ feature i

และ x′ᵢ = 1 แทนความหมายว่า ต้องสนใจ feature i
4.   นิยาม ฟังก์ชั่น hₓ เป็นฟังก์ชันที่แมพ binary input value ไปเป็น original input value ของข้อมูลนำเข้า x นั้นคือ hₓ(x′) = x
5.   นิยาม z′ ∈ {0, 1}ᵏ เช่นเดียวกับ x′ โดย z′ ≈ x′ กล่าวคือ z′ เป็น binary input vector ที่มีหน้าตาคล้ายๆกับ x′ (หรือมี distance จาก x′ ไม่มาก)
6.   นิยาม โมเดลที่ต้องการศึกษา หรือ the target model ด้วย _f(x) = ŷ_

เพื่อให้ SHAP มีคุณสมบัติสอดคล้องกับ Shapley Values ตามที่ตั้งใจ

S.M. Lundberg & S-I. Lee เริ่มต้นจากการจัดการกับปัญหาสำคัญที่กล่าวไป คือ ปัญหาการคำนวนผลลัพธ์จาก _f_ ในกรณีที่ต้องการใช้ features แค่บางตัว โดยไม่ต้องปรับโครงสร้าง หรือ เทรนโมเดลใหม่

โดย features บางตัวที่ว่า

ใน Shapley values จะใช้ S ซึ่งหมายถึง กลุ่มย่อยของผู้เล่น (ให้แค่บางคนร่วมเล่นในเกม)

ใน SHAP จะใช้ z′ₛ แทน กลุ่มย่อยของฟีเจอร์ S (ให้โมเดลใช้แค่บางฟีเจอร์ใน S) เนื่องจาก z′ ∈ {0, 1}ᵏ จะได้ว่า

*   โดย z′ₛᵢ = 0 ก็ต่อเมื่อ i ∉ S และ ไม่อนุญาติให้โมเดลใช้ feature i
*   โดย z′ₛᵢ = 1 ก็ต่อเมื่อ i ∈ S และ อนุญาติให้โมเดลใช้ feature i ได้

_// Quick Reminder: Features in SHAP = Players in Shapley Values_

เนื่องจากเราไม่สามารถเทรนโมเดลใหม่ได้ S.M. Lundberg & S-I. Lee จึงแก้ปัญหาโดยให้ f(h _ₓ_(z′ₛ)) หรือ f(zₛ) = ค่าเฉลี่ยของ predictions ที่ได้จากข้อมูลนำเข้า x แต่มีการเปลี่ยนข้อมูลในส่วนของฟีเจอร์ที่ไม่อยู่ใน S ด้วยข้อมูลของฟีเจอร์นั้นจากข้อมูลชิ้นอื่นแบบสุ่ม หรือ เขียนเป็นสมการได้ดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/118CiGwechJN3GaqFq4wjCKxaOJ1BZWLr" column=1 %}

<p>เข้าใจว่า สมการนี้ ต้องอยู่ภายใต้สมมติฐานว่า feature แต่ละตัว อิสระต่อกัน (feature independence) ถ้าใครรู้ฝากยืนยันหน่อยนะครับ 🙇</p>
</div>

_//สมการที่เขียนด้านบนแตกต่างจากคำอธิบายเล็กน้อย แต่ความหมายโดยรวมเหมือนกัน (มั้งนะ?_🤪_)_

นอกจากนี้แล้ว เพื่อการันตีว่า v(∅) = 0 (ให้สอดคล้องกับนิยามของ value function ของ Shapley values)

S.M. Lundberg & S-I. Lee ใช้ v(S) = _f(zₛ)_ - Eₓ[_f(x)_] แทนที่จะเป็น v(S) = f(zₛ) เนื่องจากนิยามแบบหลังจะไม่สามารถการันตีเงื่อนไขที่ว่า v(∅) = 0 ได้เสมอทุกๆกรณี

โดยมี Eₓ[_f(x)_] คือ ค่าเฉลี่ยของ _f(x)_ จากชุดข้อมูล X (โดยทั่วไปแล้ว จะใช้ training data) ซึ่งเป็นค่าคงที่ค่านึง

จะได้ว่า v(∅) = _f(_∅_)_ — Eₓ[_f(x)_] = Eₓ[_f(x)_] - Eₓ[_f(x)_] = 0 ตามที่ต้องการ

ท้ายที่สุด จะได้สมการของ SHAP ดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1Q9lSQ5-1mYaZQpWcYOJw4d41BTldZuxc" column=1 %}
</div>

โดยกำหนดให้ input ของ _f_ เป็นเวกเตอร์ _(xₛ, xⁱ\_ₛ)_ ที่ เอา _xₛ_ มารวมกับ _xⁱ\_ₛ_ โดยมีเงื่อนไข ดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1MPSbgtCPT8sbCTG-lOCaD_njQkCUGsFJ" column=1 %}
</div>

นั้นคือ สำหรับฟีเจอร์ j ∈ S จะใช้ข้อมูลช่องของ feature j จาก ข้อมูลนำเข้าเป้าหมายที่เราสนใจ แต่ถ้าฟีเจอร์ j ∉ S จะใช้ข้อมูลช่องของ feature j จากข้อมูลลำดับที่ i จาก training data

และ และ และ ในทางปฎิบัติ การคำนวน SHAP ก็จะเจอปัญหาเดียวกับการคำนวน Shapley Values นั้นคือ มันต้องใช้เวลาชั่วกัปป์ชั่วกัลป์ในการคำนวน ยิ่งเมื่อเจอ Deep Model ที่มีฟีเจอร์จำนวนมากๆ ยิ่งเป็นไปไม่ได้เลยที่จะคำนวน SHAP โดยใช้วิธีตรงๆ และแน่นอนว่า เราก็ยังสามารถสามารถหยิบยืม Monte Carlo Method คนดีคนเดิมมาใช้ได้ ดังนี้

**คำนวน Approximated SHAP**

สามารถคำนวน SHAP ได้โดยใช้แนวทาง [Shapley sampling values](https://link.springer.com/article/10.1007/s10115-013-0679-x) ตาม pseducode ดังนี้

def SHAPSampling(x, j):

 X = trainingData

 f = targetModel
phi = 0

 for i in range(M):

 prm = getARandomPermutation(n=len(P))

 S = getFeaturesFromPermu(prm, j)

xi = getARandomData(X)

 z1 = replaceFeatureValues(x, S+{j}, xi)

 z2 = replaceFeatureValues(x, S, xi)

payoutWithP = f(z1)

 payoutWithoutP = f(z2)

 phi += (payoutWithP - payoutWithoutP)

phi /= M

 return phi

ย้อนกลับไปที่ตอนแรก จากนิยามแรก ของ SHAP

> [SHAP is] the Shapley values of a conditional expectation function of the original model

จะเห็นว่าสิ่งที่อธิบายไปทั้งหมด เริ่มสอดคล้องเข้าด้วยกัน นั้นคือ SHAP เป็น Shapley values แต่ไม่ใช่สำหรับ Cooperative Game แต่เป็นสำหรับ “the original model”

โดยใช้ value function ที่อยู่ในรูปแบบของ a conditional expectation function นั้นคือ v(S) คำนวนจาก ค่าเฉลี่ย (expectation function) ของ _f(z)_ จาก z ที่มีรูปแบบภายใต้เงื่อนไข (conditional) ที่สอดคล้องกับกลุ่มย่อย S 😵‍💫😵‍💫😵‍💫😵‍💫😵‍💫😵‍💫😵‍💫

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1FGhLGjOhE4QzouskKnuTdmd80k1EMYx9" column=1 %}
</div>

## Introduction of KernalSHAP

หลายๆคนที่อ่านมาถึงจุดๆนี้ อาจจะอ้วกแตกกันไปแล้วหลายรอบ (/me included 🤢)

แต่เนื้อหาสำคัญที่เกี่ยวกับ SHAP ยังไม่หมด เพราะยังมีส่วนสำคัญอีกส่วนที่ไม่พูดถึงคงจะไม่ได้ นั้นคือ สิ่งที่เรียกว่า KernalSHAP

> ทำไมถึงต้องรู้จัก KernalSHAP ??

KernalSHAP เป็นเทคนิคสำหรับการประมาณ SHAP ที่นำเสนอโดย S.M. Lundberg & S-I. Lee ในเปเปอร์เดียวกัน

_//นอกจากนี้ KernalSHAP แล้ว ยังมี LinearSHAP, MaxSHAP, DeepSHAP และ TreeSHAP ซึ่งจะไม่พูดถึงในบล๊อคนี้_🤯🤯🤯

ถึงแม้ว่าเราจะมีวิธีการประมาณ SHAP โดยการใช้ sampling ตามที่อธิบายไปแล้วในหัวข้อก่อนหน้านี้ แต่อย่างไรก็ตาม หากพิจารณาดูผลการเปรียบเทียบในกราฟด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1TWSMacPV0igMw1qFYHBy1vDMsxcFMHef" column=1 %}

<p>cite: <a href="https://arxiv.org/abs/1705.07874">https://arxiv.org/abs/1705.07874</a></p>
</div>

ถึงแม้ว่า ค่าที่ได้จาก Sampling method และ KernalSHAP จะได้ค่าเฉลี่ยได้ใกล้เคียงกับ True Shapley Values เหมือนๆกัน แต่จะเห็นได้ว่า สิ่งที่ได้จาก Sampling method มี variance เยอะกว่า KernalSHAP มากๆ

จึงเป็นเหตุผลว่า ทำไม KernalSHAP จึงมีความสำคัญ

_//ส่วนตัว ประหลาดใจนิดนึงว่า ทั้ง 2 วิธีต่างลู่เข้าหา True Shapley Values ด้วยอัตราที่ไม่ต่างกันมาก อาจจะหมายความได้ว่า ในเชิงประสิทธิภาพแล้วภาพรวม น่าจะพอๆกัน_

> KernalSHAP ทำงานอย่างไร ??

KernalSHAP เป็นวิธีการที่เป็นส่วนผสมระหว่าง Linear LIME และ Shapley Values

โดยแนวคิดทั่วไปของ LIME ตั้งอยู่บนแนวคิดที่สำคัญ คือ การสร้าง explanation model _g_ ที่เป็นโมเดลง่ายๆขึ้นมาหนึ่งอัน เพื่อประมาณพฤติกรรมของ _f_ ที่ซับซ้อนจาก z′ ซึ่งอยู่ในพื้นที่รอบๆ x′

โดย inspiration ของเทคนิคแนวนี้ เกิดจาก ข้อสังเกตที่ว่าถึงแม้ว่า _f(x)_ จะเป็น non-linear function ที่ซับซ้อน แต่ถ้าซูมไปสนใจแค่บริเวณเล็กๆของ _f(x)_ จะพบว่า decision boundary สามารถประมาณได้ด้วย linear model ง่ายๆ ตามภาพด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1c0NPW0LKF6-Bo7GIMD0WDQRYJMdbfxHp" column=1 %}

<p>cite: <a href="https://www.slideshare.net/slideshow/machine-learning-explanations-lime-framework/249498861#10">https://www.slideshare.net/slideshow/machine-learning-explanations-lime-framework/249498861#10</a></p>
</div>

โดยในเปเปอร์ ของ S.M. Lundberg & S-I. Lee ต่อยอดแนวคิดนี้เพิ่มเติมให้กว้างขึ้น โดยนิยามให้ explanation model _g_ นิยามบนโดเมน {0, 1}ᵏ นั้นคือ _g_ รับข้อมูลนำเข้าที่เป็น (binary) feature space ที่มีข้อมูลว่า ถ้าใช้/ไม่ใช้ฟีเจอร์ j แล้วทำนายว่า โมเดลจะ output เป็นอย่างไร

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/13Syuy78mqVxKro0DeSOflcxN60vWvjGa" column=1 %}
</div>

ดังนั้นในงานของ S.M. Lundberg & S-I. Lee การประมาณ _g(z′)_ ≈ _f(hₓ(z′))_ จึงไม่ใช้การซูมและสร้าง _g_ แทน decision boundary แต่เป็นการประมาณพฤติกรรมของ _f_ จากด้วย linear model _g_ ใน (binary) feature space

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1BxZ2cD6hDC_7RheVrxfdq5zqJ7F9SAQM" column=1 %}

<p>กรณีนี้ ใช้ข้อมูลนำเข้าตัวอย่าง x เป็นประโยค โดยมี features เป็น คำในประโยคนั้นๆ</p>
</div>

และ keyword ที่สำคัญ คือ “Linear” การที่ S.M. Lundberg & S-I. Lee กำหนดให้ explanation model _g_ เป็น linear model จะได้ผลลัพธ์ที่อยู่ในรูปแบบ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1PRNCDektmnnTFNkQjZEUFIEMVLy-LyfJ" column=1 %}
</div>

ซึ่ง S.M. Lundberg & S-I. Lee ให้แนวคิดว่า เราน่าจะสามารถสร้าง _g_ ที่เหมาะสมเพียงพอ ที่จะทำให้

> {w₀, w₁, w₂, w₃, …, wₖ} → {φ₀, φ₁, φ₂, φ₃, …, φₖ}

_//โดยจริงๆแล้ว S.M. Lundberg & S-I. Lee พิสูจน์ว่า เทคนิคอื่นๆ อย่าง LIME, DeepLIFT, หรือ LRP ล้วนสามารถจัดรูปแบบให้อยู่ในรูปแบบเดียวกันนี้ แต่มีแค่ SHAP เท่านั้นแหละที่การันตีว่า feature importance ที่คำนวณได้จะมีคุณสมบัติเทียบเคียงกับ Shapley Values เสมอ!_

โดย KernalSHAP คือ แนวทางที่ S.M. Lundberg & S-I. Lee เสนอ เพื่อใช้ในการเทรน explanation model _g_ เพื่อให้มี weights ที่มีคุณสมบัติแบบเดียวกับ Shapley Values โดยมีรายละเอียดดังนี้

**# ขั้นที่ 1**สร้าง training data สำหรับ explanation model _g_ โดยการสุ่ม z′ ขึ้นมาหลายๆอันเป็นข้อมูลนำเข้า โดย z′ ต้องไม่ใช่ all 0's หรือ all 1's และ z′ ที่ดีต้องไม่ต่างจาก x′ มาก นั้นคือ |z′| ≈|x′| โดย |z′| หมายถึงจำนวนค่า 1's ใน z′

> Quick Reminder: z′ ∈ {0, 1}ᵏ เป็น binary feature vector

**# ขั้นที่ 2**คำนวน _f(hₓ(z′))_ เพื่อเป็นเป้าหมายที่ g ใช้เป็น labels

**# ขั้นที่ 3**คำนวนค่าน้ำหนัก (weights) สำหรับ z′ แต่ละตัว ตามสมการต่อไปนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1IlkLGJdjZBg4VkNZUnVxUUlx2JLD_Kcs" column=1 %}
</div>

โดยมี k = จำนวนฟีเจอร์ใน x และ |z′| = จำนวนค่า 1's ใน z′

โดยเมื่อ plot πₓ ออกมาดู จะได้กราฟหน้าตาแบบนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1L7FVx4ryRwe97bmiAHZ7sDQBamPGbhVr" column=1 %}

<p>cite: <a href="https://www.youtube.com/watch?v=hqr-AGOcG_s">https://www.youtube.com/watch?v=hqr-AGOcG_s</a></p>
</div>

จะเห็นว่า weights ถูกออกแบบในแนวคิดว่า เราจะสามารถเรียนรู้ข้อมูลเกี่ยวกับการทำงานของโมเดลได้มากที่สุด เมื่อมันอยู่เดี่ยวๆ — _We learn most about individual features if we can study their effects in isolation_

นั้นคือ ถ้า z′ มี 1 อยู่แค่ 1 ตัว ที่เหลือเป็น 0 หรือ มี 0 อยู่แค่ 1 ตัวที่เหลือมีค่าเป็น 1

จะได้ว่า z′ นั้นมีประโยชน์สูงที่สุด

เมื่อเทียบกับกรณีที่ z′ มี 1 และ 0 อยู่แบบครึ่งๆ เราจะแทบไม่รู้เลยว่าผลลัพธ์ที่ได้เป็นผลมาจากฟีเจอร์อะไร ?

ซึ่งนี้มีผลใน **# ขั้นที่ 1**ที่เราควรเลือกสุ่มเลือก z′ จากอันที่มี |z′| = 1 หรือ |z′| = k-1 ก่อน

และที่สำคัญอีกจุด คือ จะเห็นว่า πₓ(z′) = ∞ เมื่อ |z′| = 0 หรือ |z′| = k อันนี้ถูกออกแบบมาเพื่อที่จะบังคับให้ φ₀ = Eₓ[_f(x)_] และ _f(x)_ = φ₀ + φ₁ + φ₂ + φ₃ + … + φₖ

_//นั้นคือ ตัวแปรใน g จะลดลงไป 2 ตัวแปร เพื่อเป็น fixed values (_ φ _₀ และ_ φ _ₖ)_

**# ขั้นที่ 4**เทรน Linear Regression โดยใช้ Weighted Linear Square Loss (WLS) ตามสมการต่อไปนี้ โดยไม่มี regularisation term

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1J-nEkrN8_4dwrAXd6o85e_lpx9eI5xw-" column=1 %}
</div>

**# ขั้นที่ 5**ส่งออกค่า weights ที่ได้จาก Linear Regression เป็นค่า SHAP ที่ต้องการ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1aSzF_vAaj9oYR_TPH6TwrB4Oo-rFzs0l" column=1 %}
</div>

โดย fixed values φ _₀ และ_ φ _ₖ ตามนี้_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1JsYgpTkauiSurscfeiPHiwUd22Okkcov" column=1 %}
</div>

**คำนวน KernalSHAP**

สำหรับใครที่สนใจอ่านพิสูจน์ที่มาที่ไปของเงื่อนไขทั้งหมดนี้ สามารถอ่านได้จาก[ลิงค์นี้](https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Supplemental.zip)เลย

def KernalSHAP(x):

 X = trainingData

 f = targetModel
x_prime = [1 for f in feat(x)]

kernalX = []

 kernalY = []

 kernalWeight = []

for i in range(M):

 z_prime = getARandomCoalition(x_prime)

 xi = getARandomData(X)

z = replaceFeatureValues(x, z_prime, xi)

 yhat = f(z)

weight = getWeight(z_prime)

kernalX.append(z_prime)

 kernalY.append(yhat)

 kernalWeight.append(weight)

WLSloss = WeightedLinearSquares()

 M = LinearRegression(WLSloss)

 M.train(kernalX, kernalY, kernalWeight)

phi = M.weights

return phi

## From Local to Global

ข้อควรระวังหนึ่งในการใช้ SHAP คือ SHAP เป็น local explanation หมายความว่า ค่าที่ได้จาก SHAP เป็นค่าที่เฉพาะเจาะจงกับข้อมูลนำเข้า x เท่านั้น !!

> นั้นคือ ถ้า SHAP จาก x บอกว่าฟีเจอร์ที่ 2 เป็นฟีเจอร์ที่สำคัญที่สุด ไม่ได้แปลว่า ฟีเจอร์ที่ 2 จะเป็นฟีเจอร์ที่สำคัญที่สุดในทุกๆกรณี

แต่อย่างไรก็ตาม หากต้องการใช้ SHAP แบบ global explanation เพื่อดูภาพรวมว่า _“แต่ละฟีเจอร์มีความสำคัญต่อโมเดลมากน้อยอย่างไร”_

สามารถทำได้โดย หาค่าเฉลี่ยของ (ค่าสัมบูรณ์ของ (SHAP ของฟีเจอร์นั้นๆ))

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1OCo3qyTYmyyY7eMQ5lE3SCxki8kxuxyT" column=1 %}
</div>

> หลายคนอาจจะสงสัยว่า ทำไมต้องใช้ค่าสัมบูรณ์ ??

S.M. Lundberg อธิบายไว้ใน github ดังนี้

> “Positive and negative values are important, but if you allow them to cancel each other out when measuring global feature importance then you will not be measuring the importance of the features for the model, but rather how different the impact of each feature is between the samples you are explaining and your background set of samples.” — [S.M. Lundberg, 2020](https://github.com/shap/shap/issues/696)

แปลคร่าวๆได้ว่า เนื่องจาก φⱼ มีค่าเป็นไปได้ทั้งบวก และ ลบ ถ้าไม่ใช่ค่าสัมบูรณ์จะทำให้ φⱼ จากข้อมูลแต่ละก้อนหักลบกันเอง ผลลัพธ์ที่ได้ จึงไม่ใช่ feature importance ของฟีเจอร์ j ที่แท้จริง แต่เป็นการเปรียบเทียบระหว่างความสำคัญของฟีเจอร์นั้นๆบนข้อมูลที่ใช้ศึกษา และ ข้อมูลที่เป็นภาพรวมเฉลี่ยๆ

นอกจากนี้ S.M. Lundberg ยังเสนอเพิ่มเติมว่า การใช้ SHAP ใน global explanation อาจจะไม่ใช่คำตอบที่ดีที่สุดซะทีเดียว [แนวทางอื่นอาจจะดีกว่า](https://www.nature.com/articles/s42256-019-0138-9)

_ทั้งนี้ ส่วนตัวก็เห็นคล้ายๆกัน ไม่มั่นใจว่า การใช้ SHAP แบบนี้ จะรอบรับด้วยทฤษฎีของ Shapley Values ด้วยหรือไม่ ?? ทั้งนี้ ถ้าใครไม่มั่นใจ ยังมีเทคนิคคล้ายๆกัน SHAP ที่ใช้สำหรับ Global Explanation อย่าง_[_SAGE_](https://iancovert.com/blog/understanding-shap-sage/)_เป็นอีกหนึ่งตัวเลือก_

อย่างไรก็ตาม ถ้าใครยังคงต้องการดื้นดึงที่จะใช้ SHAP เป็น global explanation แนวทางนึงที่เป็นไปได้ คือการใช้ Summary Plot

> ตัวอย่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1ZDnON4T564POMPxOiWfU4XycSIYJiwqq" column=1 %}

<p><a href="https://christophm.github.io/interpretable-ml-book/shap.html#shap-summary-plot">https://christophm.github.io/interpretable-ml-book/shap.html#shap-summary-plot</a></p>
</div>

โดยเจ้า Summary Plot เป็นการ plot distribution ของ SHAP จากข้อมูลก้อนต่างๆในชุดข้อมูล ที่น่าสนใจ คือ ranking ที่ได้จาก Summary Plot ค่อนข้างสอดคล้องกับ Mean Absolute SHAP plot (กราฟด้านล่าง)

แต่ก็ปฎิเสธไม่ได้ว่า Summary Plot ค่อนข้างเข้าใจยากเลยทีเดียว

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1iIKLXdtLdXKORcm3FY3gVFW2_QvRLwCU" column=1 %}
</div>

## Limitation of SHAP

กว่าจะมาถึงหัวข้อนี้ นี่พยายามอธิบายว่า SHAP คืออะไร และ มีประโยชน์อย่างไร แต่การใช้งาน SHAP ที่ดีมีประสิทธิภาพ จำเป็นต้องเข้าใจข้อจำกัดของ SHAP ไปพร้อมๆกัน

ข้อจำกัด 2 ข้อที่สำคัญของ SHAP ที่ต้องรู้ คือ

### **#1. Feature Dependency**

การคำนวน SHAP ตั้งอยู่บนข้อสมมติฐานสำคัญเกี่ยวกับ feature independence ซึ่งในหลายกรณีไม่ได้สะท้อนความสัมพันธ์ที่แท้จริงระหว่างฟีเจอร์ในข้อมูลโลกแห่งความเป็นจริง

โดยที่มาส่วนหนึ่งของการใช้สมมติฐาน feature independence เกิดขึ้นในขั้นตอนการสุ่มเลือก Coalitions ของฟีเจอร์ เพราะว่า ในความเป็นจริง ฟีเจอร์แต่ละตัวไม่ได้ 100% อิสระต่อกัน

> ตัวอย่าง

ถ้าข้อมูลที่ต้องการศึกษา คือ ข้อความ “This is a cat” และ ใช้ words เป็น features ของข้อมูลนี้ จะได้ว่าเรามีข้อมูลนำเข้า 4 ตัวได้แก่ {This, is, a, cat}

ถ้าพิจารณาต่อ จะพบว่า ข้อมูลนำเข้า 4 ตัวนี้มีการเชื่อมโยงกันในเชิงแกรมม่า เช่น

This is _ cat → เราสามารถบอกได้ทันทีเลยว่า ต้องเติม “a”

This _ a cat → เราสามารถบอกได้ทันทีเลยว่า ต้องเติม “is”

This is a _ → เราสามารถบอกได้ว่าตัวเลือกที่สามารถเติมได้ ไม่ใช่ทุกๆคำ แต่ต้องเป็นคำนามเอกพจน์

ดังนั้น การแทนที่คำแบบสุ่ม (ที่ใช้ในการ approximate SHAP) จึงจะให้ข้อมูลที่ไม่ตรงตามหลักแกรมม่า และไม่ตรงกับความเป็นจริง ซึ่งแน่นอนว่าจะมีผลต่อค่า SHAP ที่ได้

### #2. Causal Inference

> SHAP is not a measure of how important a given feaure is in the real word but to the model

โจทย์ที่ SHAP ออกแบบมา คือเพื่อตอบคำถามที่ว่า

_“ฟีเจอร์ (features) แต่ละตัวมีความสำคัญ (feature importance) มากน้อยเท่าไรใน การคำนวนคำตอบ (prediction)_**_ของโมเดล_**_”_

และหลายคน อาจจะละเลยส่วนที่สำคัญอันนึงไป คือ “**_ของโมเดล_**” แปลว่า สิ่งที่ได้จาก SHAP เป็นแค่มาตรวัดความสำคัญของฟีเจอร์จากมุมมองของโมเดลที่เรียนรู้มาจากข้อมูล ไม่ใช่บริบทของโลกจริง

นั้นคือ ถึงแม้ว่า SHAP บอกว่า ส่วนที่เป็นหนวดในภาพเป็นส่วนที่สำคัญที่สุดในการ แยกระหว่างหมา และ แมว ไม่ได้แปลว่า ลักษณะของหนวด หรือ การมี/ไม่มีหนวด จะเป็น Key indicator ในการแยกหมา และ แมวในเชิงชีววิทยา

## Credit

บทความนี้ ต้องขอขอบคุณ

*   [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) เปเปอร์ต้นฉบับ จุดเริ่มต้นของเรื่องราวทั้งหมดของบล๊อคนี้
*   พูดสารภาพเลยว่า เนื้อหา 80% ที่เขียนในบล๊อคนี้ มีที่มาจาก playlist นี้ [Interpretable Machine Learning — Shapley](https://www.youtube.com/playlist?list=PLGViarxWrOJfVpJks8eYjwzpGCS7_aJeP) อยากแนะนำให้ทุกๆคนที่ต้องการศึกษา Shapley Values และ SHAP เข้าไปฟัง มันดีงามมากๆ 🤩
*   และ อีกแหล่งข้อมูลที่จะไม่พูดถึงไม่ได้ คือ หนังสือ [Interpretable Machine Learning: A Guide for Making Black Box Models Explainable](https://christophm.github.io/interpretable-ml-book/index.html) โดย C. Molnar

ทั้งนี้ขอขอบคุณผู้อ่านทุกๆคนที่ตามอ่านมาจนถึงตรงนี้ กราบ กราบ กราบ 🥳🥳🥳🥳
