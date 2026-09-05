---
layout: post
title: "ชวนอ่านเปเปอร์ ตอนที่ 1 On the Biology of a Large Language Model"
tags: [Archive, Code Code and Code]
thumbnail: "assets/img/biology-of-a-large-language-model/image-01.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-01.png" column=1 %}
</div>

> /me พึ่งไปเจอเปเปอร์ใหม่จากทีม Antropic แล้วรู้สึกน่าสนใจมาก อยากจะชวนเพื่อนๆมาอ่านไปด้วยกัน

<!--more-->

ในช่วงหลายปีที่ผ่านมา AI และ Large Language Models (LLMs) ยังคงเป็นกระแสที่พูดถึงกันอย่างกว้างขวางในสังคมทั่วโลก พูดได้ว่า ปัจจุบันใครๆก็สามารถเข้าถึง LLMs กันได้อย่างง่ายดาย และ เปลี่ยนแปลงรูปแบบการทำงานของหลายๆอาชีพไปตามๆกัน (??)

แต่ภายในความสวยหรูของ LLMs ปัญหาหนึ่งที่นักวิจัยตั้งคำถาม และ กังวลกันมาก คือ เราแทบไม่เข้าใจอะไรๆเลยที่จะสามารถอธิบายความสามารถของโมเดล LLMs

*   _ทำไมโมเดลมัน_**_เก่ง_**_จัง?_
*   _จริงๆแล้ว มันเริ่ม_**_คิด_**_ได้เอง? หรือ แค่_**_จำ_**_คำตอบมาจากรูปแบบของข้อมูลที่มันโดนสอนมา?_
*   _กระบวนการให้เหตุผลที่โมเดลตอบ คือ สิ่งที่มันใช้_**_คิด_**_จริงๆ? หรือ เป็นแค่คำตอบเพื่อให้สอดคล้องกับ_**_ความต้องการของมนุษย์_**

ความน่ากลัว คือ เพราะเราไม่รู้ว่า _“โมเดลเหล่านี้ตอบคำถามเราๆได้อย่างไร?”_ จึงทำให้เกิดคำถามต่อไปว่า _“เราจะเชื่อใจมันได้มากแค่ไหน?”_ และ ยิ่งเมื่อโมเดลเข้ามามีส่วนในการตัดสินใจที่กระทบกับชีวิตทุกๆมากขึ้น เช่น

*   เข้ามาเป็นผู้ช่วยหมอวินิฉัยโรค (??)
*   เข้ามาเป็นแหล่งอ้างอิงในการเรียนการสอน (??)
*   เข้ามาเป็นเครื่องมือในการพิจารณาคดี (??)

เรายิ่งต้องระมัดระวัง เพื่อการันตีว่าโมเดลจะต้องตอบได้อย่างถูกต้องตามความเป็นจริง (**helpful**), ไม่เกินจริง ไม่มโนขึ้นมาเอง (**honest**),ไม่อคติ และ ไม่นำเสนอเรื่องที่ทำให้เกิดความเสียหาย (**harmless**)

เปเปอร์ชิ้นนี้ เป็นส่วนหนึ่งของการพัฒนาเพื่อทำความเข้าใจการทำงานของ LLMs จากทีม Antropic ซึ่งจริงๆแล้วประกอบด้วย 2 เปเปอร์ คือ

*   [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) เป็นเปเปอร์พี่คนโต ที่เกริ่นนำเสนอเทคนิคใหม่ที่ Antropic ใช้ในการศึกษา LLMs
*   [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) เปเปอร์น้องคนเล็ก ซึ่งพูดถึงการนำเทคนิคจากเปเปอร์พี่คนโต มาใช้ในอธิบายการทำงานของโมเดล Claude 3.5 Haiku และที่น่าตื่นเต้น คือ ผลลัพธ์ที่ได้ สามารถอธิบายปรากฎการณ์หลายๆอย่างได้อย่างน่าสนใจ —_(ปล. ตัวใหญ่ๆ) ทั้งนี้ สิ่งที่เปเปอร์นำเสนอ เป็นแค่ observations เด้อ ยังต้องศึกษาต่อไปว่า ความรู้เหล่านี้จริงมากน้อยแค่ไหน?_

และบทความนี้ ตั้งใจว่าจะเขียนสรุปเนื้อหารวมจากทั้ง 2 เปเปอร์ แต่ แต่ แต่ ดูๆแล้วจะสาหัญเกินไป จึงขอพูดถึงเฉพาะ พาร์ทหลังเพียงอย่างเดียว ถ้าใครสนใจ กดลิงค์ไปตามอ่านต้นฉบับได้เลยฮะ หรือ ถ้ามีคนสนใจมากๆ อาจจะกลับมาเขียนพาร์ทหลัง ไว้ว่ากันอีกที

## ว่าด้วยเรื่องของเทคนิคที่ใช้

อย่างที่เขียนไปก่อนหน้านี้ เปเปอร์ [On the Biology](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) นี้ ไม่ได้เน้นอธิบายเทคนิคที่ใช้มาก แต่เน้นไปที่ผลลัพท์จากการนำเทคนิคไปใช้มากกว่า

แต่ แต่ แต่ ถ้าจะไม่พูดถึงเทคนิคเลย ก็คงเป็นไปไม่ได้ เพราะว่า มันเป็นส่วนสำคัญในการทำความเข้าใจเนื้อหาที่เหลือ

โดยเทคนิคที่ทีม Antropic ใช้ในงานนี้ เป็นเทคนิคในกลุ่มที่เรียกว่า Mechanistic Interpretability ซึ่งจะขอไม่ลงรายละเอียดเพิ่มเติม ถ้าใครสนใจ [แนะนำให้กดตามไปอ่านที่ลิงค์นี้เลยครับ](https://www.alignmentforum.org/posts/NfFST5Mio7BCAQHPA/an-extremely-opinionated-annotated-list-of-my-favourite-1)

> Mechanistic interpretability seeks to reverse engineer neural networks, similar to how one might reverse engineer a compiled binary computer program
>
> —[Olah, 2022](https://www.transformer-circuits.pub/2022/mech-interp-essay)

ในรายละเอียด ใช้ในเปเปอร์นี้ ทีม Antropic ใช้เทคนิคใหม่ที่ชื่อว่า **_Circuit Tracing_** ซึ่งพัฒนาขึ้นภายใต้แนวคิดว่า

> เป็นไปได้ไหมที่เราจะทำความเข้าใจการทำงานของ LLMs โดยการลดทอนความซับซ้อนของโมเดลลง ด้วยการแทนที่โครงสร้างบางส่วนของโมเดลเดิมด้วยโมเดลใหม่ที่มีโครงสร้างเรียบง่ายขึ้น เข้าใจได้ง่ายกว่า แต่ยังสามารถเลียนแบบพฤติกรรมของโมเดลต้นแบบได้อย่างใกล้เคียง

โดยเมื่อได้เจ้าโมเดลง่ายๆ หรือ replacement model ที่ว่ามาแล้ว ถ้าเราเชื่อว่า มันสามารถเลียบแบบพฤติกรรมของโมเลต้นแบบได้จริงๆ แปลว่า เราก็สามารถทำความเข้าใจการทำงานของโมเดลต้นแบบได้ โดยศึกษาการทำงานของเจ้า replacement model

เทคนิค Circuit Tracing นำแนวคิดที่ว่ามาใช้ โดยเริ่มต้นจากการสร้างโมเดลใหม่ที่เรียกว่า **_Trancoder_**_(เป็น replacement model)_ ขึ้นมาสวมอยู่บน LLMs เพื่อเลียนแบบพฤติกรรมของโมเดลต้นฉบับ ภายใต้เงื่อนไขของ **_sparsity penalty_**(เพื่อการันตีว่า Trancoder จะเป็นโมเดลง่ายๆ ที่สามารถเข้าใจได้)

และ จากนั้น Circuit Tracing จะนำ Trancoder ที่ได้ไปใช้สร้าง สิ่งที่เรียกว่า **_Attribution Graphs_** ที่ทำหน้าที่ในการแสดงว่า โมเดลประมวลผลอะไรบ้างเพื่อตอบสนองต่อ prompt หนึ่งๆ — _describe the steps a model used to produce an output for a target token on a particular prompt_

ว่าแต่ว่า Trancoder และ Attribution Graphs ที่อ้างถึงมันมีหน้าตาอย่างไร ???

### Trancoder

หรือ ในชื่อเต็มๆว่า Cross-Layer Transcoders (CLTs) เป็นโมเดลที่ถูกออกแบบมาเพื่อเลียนแบบพฤติกรรมของโมเดลที่เราสนใจ แต่บังคับให้มันมีความ trasparent มากกว่าเดิมมากๆ หรือ พูดอีกอย่างคือ **เป็นโมเดลที่มนุษย์สามารถเข้าใจการทำงานได้ง่ายกว่าเดิม**

โดยเจ้า Transcoder พัฒนาอยู่บนสมติฐานที่ว่า “[LLMs ต่างๆ สามารถเก็บความรู้ที่มันเรียนมาได้ ในรูปแบบของ weights ที่อยู่ภายในโมเดล](https://proceedings.neurips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html)”

แรกเริ่มเดิมที นักวิจัยศึกษาความรู้ของ LLMs โดยตั้งคำถามว่า [_โมเดลสามารถเข้าใจความรู้ XX หรือไม่?_](https://arxiv.org/abs/2002.12327)เช่น

*   โมเดลสามารถเข้าใจความรู้เชิงไวยากรณ์ของคำ (Syntactic knowledge) หรือไม่?? เช่น สามารถบอกได้ไหมว่า Catnip เป็นคำนามเอกพจน์
*   โมเดลสามารถเข้าใจความรู้เชิงความหมายของคำ (Semantic knowledge) หรือไม่?? เช่น สามารถบอกได้ไหมว่า เตง เทอ แกร คุณ เมิง มึง ต่างมีความหมายเหมือนกันแต่ให้บริบทที่ต่างกัน

แต่ปัญหา คือ เทคนิคเดิมๆ ไม่สามารถบอกได้ว่า _โมเดลสามารถเข้าใจความรู้อะไรบ้าง?_

โดยเฉพาะอย่างยิ่ง เมื่อหลังๆพบว่า ความรู้ของ LLMs อยู่ในรูปแบบที่เรียกว่า [“_superposition”_](https://transformer-circuits.pub/2022/toy_model/index.html)_— n_ eural networks want to represent more features than they have neurons

นั้นคือ ในโมเดลที่มี neurons ขนาด N ตัว ไม่ได้แปลว่าจะสามารถเข้าใจได้แค่ความรู้ N อย่าง แต่ความรู้ที่โมเดลสามารถเข้าใจได้ อาจจะอยู่ในรูปแบบที่มันซ้อนๆกันผ่านหลายๆ neurons (ไม่ใช่แค่รับผิดชอบโดย neuron ตัวใดตัวหนึ่ง) ทำให้โมเดลสามารถเข้าใจได้มากกว่า แค่ N ฟีเจอร์ มากๆ (สามารถอ่านเพิ่มเติมได้ที่ [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html))

นักวิจัยจึงหันมามองเทคนิคใหม่ แทนที่จะเป็นแค่การทดสอบความสามารถในการทำความเข้าใจความรู้ X จากโมเดล เปลี่ยนเป็น ความพยายามในการแยกองค์ประกอบย่อยๆออกจาก weights ของโมเดล โดยให้ องค์ประกอบย่อยๆ ที่ 1 ตัว แทน ความรู้ (หรือ เรียกในเปเปอร์ว่า ฟีเจอร์) **≈**1 อย่าง โดยเลี่ยงไม่ให้เกิด superposition

หากสามารถทดสอบต่อไปได้ว่า องค์ประกอบย่อยๆแต่ละตัวแทนฟีเจอร์ (ความรู้) อะไร เราก็จะสามารถทำความเข้าใจได้ว่า โมเดลที่ศึกษาใช้ความรู้อะไรบ้างในการผลิตคำตอบของมัน

ซึ่ง Trancoders ตอบโจทย์นี้โดยใช้หลักการทำงานสำคัญ 2 ข้อ คือ

1.   Trancoders จะโดนเทรนเพื่อพยายามเลียนแบบพฤติกรรมของโมเดล โดยให้มันรับข้อมูลเข้า (input) แบบเดียวกับส่วนของโมเดลที่เราสนใจ และ สอนให้มันสร้างข้อมูลออก (output) แบบเดียวกับข้อมูลออกที่โมเดลต้นแบบคำนวนออกมาจริงๆ _— minimise reconstruction error_
2.   และในเวลาเดียวกัน Trancoders จะถูกบังคับใช้ ได้แค่ hidden vector อยู่ในรูปแบบของ sparse vectors เท่านั้น ซึ่งแปลว่า hidden vector ของ Trancoders จะอยู่ในรูปแบบที่มีค่า 1 แค่ ไม่กี่ช่อง และ ส่วนที่เหลือ เป็น 0 ทั้งหมด บังคับไม่ให้ Trancoders แทนความรู้ของมันในลักษณะที่เป็น superposition — maximise sparsity

ในรายละเอียด Trancoders จะประกอบไปด้วยโมเดลเล็กๆหลายๆโมเดล ที่เอาไปครอบอยู่บน MLP layers ของ LLMs เป้าหมายที่เราสนใจ จะเรียกว่าองค์ประกอบนี้ว่า CLT Layers และในแต่ละ CLT Layer จะมีลักษณะเป็น 1-hidden NN โดยเราจะเทรนให้มันสามารถรับข้อมูลนำเข้า และส่งข้อมูลออก แบบเดียวกับ MLP Layer ของโมเดลที่ต้องการศึกษา เพื่อเลียบแบบพฤติกรรมของโมเดล (ตามหลักการข้อ 1) แต่ มันจะใช้แค่ hidden neuron เพียงแค่ **≈**1 ตัว ต่อการคำนวนในแต่ละครั้ง (ตามหลักการข้อ 2)

_//FYI ในความเป็นจริง มันใช้ hidden neurons หลายตัวนะ แต่ sparsity loss พยายามให้ Trancoders ใช้ hidden neurons น้อยที่สุดเท่าที่เป็นไปได้ ต่อการคำนวน 1 ครั้ง_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-02.png" column=1 %}

<p>ภาพโครงสร้างของ CLT แบบคร่าวๆ ที่ไม่ถูกต้อง 100%</p>
</div>

โดยที่ hidden neurons ของ CLT จะทำหน้าที่เป็น representation ของ ฟีเจอร์ที่เราจะนำออกมาศึกษา

นั้น คือ CLT เป็นเหมือนการแปลง weights ของ MLP ที่อยู่ในรูปแบบของ dense representation ที่มีขนาดเล็กๆ (1024 neuron units/layer) เป็น sparse representation ขนาดใหญ่ๆ อย่างที่ใช้ในเปเปอร์นี้ คือ 300k, 1M และ 3M neuron units/layer

_//เพราะเราไม่รู้ว่า จริงๆแล้วโมเดลเป้าหมายสามารถเรียนรู้ได้กี่ฟีเจอร์_

ต่อมาเมื่อได้ Transcoder แล้ว นักวิจัยจึงเริ่มต้นศึกษาการทำงานของโมเดล โดยพิจารณา activation ที่เกิดขึ้น บน neuron units ของ Transcoder ในขณะที่โมเดลกำลังจะคำนวนคำตอบสำหรับ prompt หนึ่งๆ ซึ่งเปเปอร์เรียก กราฟใหม่นี้ว่า **_“local replacement model”_**

_— Local ในที่นี้ ต้องการจะเน้นว่า กราฟที่ได้ เป็นแค่ผลลัพธ์เฉพาะตัวของ prompt หนึ่งๆเท่านั้น ถ้ามีการเปลี่ยนแปลง prompt ก็จะได้ กราฟที่แตกต่างกัน_

แต่ถึงแม้ว่า Transcoder จะถูกเทรนด้วย sparse penalty แต่ activated neuron units ที่ได้ ก็ยังมีอยู่เป็นจำนวนมาก

ดังนั้น เจ้า local replacement model ที่ได้ จึงต้องผ่านกระบวนการเพิ่มเติมเพื่อลดทอนความซับซ้อนของผลลัพท์ (ทำให้มนุษย์เข้าใจง่ายขึ้น) เช่น Graph Pruning เพื่อ เลือกเฉพาะส่วนที่มีความสำคัญๆเท่านั้น และ Grouping Features เพื่อรวม node ส่วนที่ทำหน้าที่คล้ายๆกัน ให้กลายเป็น supernode เดียว

ต่อมา นักวิจัยจึงศึกษาต่อไปว่า activated hidden neuron แต่ละตัว ของ CLT ในแต่ละ layer ทำหน้าที่อะไร หรือ ใช้แทนความรู้อะไร? โดยการใช้ feature visualization ซึ่งทำโดยการให้ทีมมาตรวจสอบว่า hidden neuron ตัวนั้นๆ ตอบสนองต่อคำ? หรือ โครงสร้างประโยคแบบใดบ้าง? หรือ มีแนวโน้มจะกระตุ้นเมื่อโมเดลต้องการสร้างคำประเภทใด?

และผลลัพท์สุดท้ายที่ได้ คือ Attribution Graphs นั้นเอง

— สามารถอ่านรายละเอียดเพิ่มเติมได้ที่เปเปอร์ [Circuit Tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-03.png" column=1 %}

<p>Local Replacement Model (ซ้าย) vs Attribution Graph (ขวา)</p>
</div>

### Attribution Graphs

> **Attribution graphs,**a graphical representation of the computational steps the model uses to determine its output for a particular input, in which nodes represent features and edges represent the causal interactions between them

Attribution Graphs เป็นผลลัพท์สุดท้ายที่เกิดขึ้น จาก Circuit Tracing เพื่อ ใช้ในการศึกษาพฤติกรรมต่างๆของโมเดล

โดยเจ้ากราฟ Attribution Graphs จะประกอบไปด้วย **_Nodes_** ที่ใช้แทน “ฟีเจอร์ (features)” แต่จริงๆแล้ว มันดูเหมือนจะเป็น “ขั้นตอนบางอย่างที่โมเดลเรียนรู้ หรือ ต้องการทำ” มากกว่า และ **_Edges_** แทนความสัมพันธ์ระหว่าง Nodes แต่ละตัว หรือก็คือ เป็นการบอกว่า Node แต่ละอัน ไปกระตุ้น/ยับยั้ง การทำงานของ Nodes อะไรบ้างต่อไป

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-04.png" column=1 %}

<p>ตัวอย่าง Attribution Graphs จาก <a href="https://transformer-circuits.pub/2025/attribution-graphs/biology.html">https://transformer-circuits.pub/2025/attribution-graphs/biology.html</a></p>
</div>

โดย Nodes สามารถแบ่งคร่าวๆเป็น 3 ประเภท คือ

**_1. Input features_**เป็นฟีเจอร์ที่มักมาจาก CLT ที่อยู่ในชั้นแรกๆของโมเดล โดยจะทำงานเมื่อโมเดลเจอคำบางคำ หรือ เจอกลุ่มคำที่มีความหมายใกล้ๆกันบางกลุ่ม (activate on specific tokens or categories of closely-related tokens) เช่น

_* ฟีเจอร์เพื่อระบุว่าข้อมูลก้อนนี้เป็นข้อมูลที่มาจากคำว่า “แมว”

* ฟีเจอร์เพื่อระบุว่าข้อมูลก้อนนี้เป็นข้อมูลที่เกี่ยวข้องกับ “Jim Davis”

* ฟีเจอร์เพื่อระบุว่าข้อมูลก้อนนี้เป็นข้อมูลที่มาจากตัวอักษร “C”_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-05.png" column=1 %}

<p>ตัวอย่าง Input Feature ของคำว่า “digital” <a href="https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs-tutorial-features">https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs-tutorial-features</a></p>
</div>

**_2. Output features_**

เป็นฟีเจอร์ที่มักมาจาก CLT ที่อยู่ในชั้นท้ายๆของโมเดล โดยจะทำให้โมเดลมีแนวโน้มจะตอบคำบางคำเป็นพิเศษมากขึ้น (ดูจาก next output token) หรือ ให้ตอบคำที่อยู่ในกลุ่มคำบางกลุ่ม (promote continuing the response with specific tokens or categories of closely-related tokens) เช่น

_* ฟีเจอร์เพื่อเพิ่มแนวโน้มให้โมเดลตอบคำว่า “ลายสลิด”

* ฟีเจอร์เพื่อเพิ่มแนวโน้มให้โมเดลตอบคำที่เกี่ยวข้องกับ “สิงโต”_

โดยในตัวอย่างที่ใช้ใน เปเปอร์ ฟีเจอร์กลุ่มนี้ จะเขียนแทนด้วย

“say XX” หมายถึง ฟีเจอร์เพื่อเพิ่มแนวโน้มให้โมเดลตอบคำว่า XX หรือ

“say _Y” หมายถึง ฟีเจอร์เพื่อเพิ่มแนวโน้มให้โมเดลตอบคำว่าที่ลงท้ายด้วย Y

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-06.png" column=1 %}

<p>ตัวอย่าง Output Feature ของคอนเซปที่เกี่ยวกับกีฬา <a href="https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs-tutorial-features">https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs-tutorial-features</a></p>
</div>

**3. Intermediat features**

เป็นฟีเจอร์ในกลุ่มที่ค่อนข้าง abstract เพราะไม่มีลักษณะหรือ พฤติกรรม ตายตัว และส่วนตัวก็ไม่มั่นใจเหมือนกันว่า นักวิจัยแยกประเภทฟีเจอร์ในกลุ่มนี้อย่างไร โดยไม่ให้มีอคติ (Confirmation bias)

## Validate with Interventions

หลักจากที่พูดถึง Transcoders และ Attribution Graphs ไปแล้ว

อีก 1 เรื่องที่น่าสนใจ คือ สิ่งที่นักวิจัย Antropic นำเสนอในเปเปอร์นี้ ไม่ใช่แค่การแสดง Attribution Graphs เพื่ออธิบายการทำงานของโมเดลอย่างเดียว เปเปอร์ยังมีการเสริมเพิ่มเติมด้วย _Intervention Experiments_

เพราะ ปัญหาที่สำคัญของเทคนิค Circuit Tracing (หรือ จริงๆ เป็นปัญหาทั่วไปของเทคนิคที่ใช้ replacement model) คือ เราจะทราบได้อย่างไรว่า คำอธิบายที่ได้จาก Attribution Graphs ถูกต้อง และตรงกับสิ่งที่ LLMs คิดจริงๆ เนื่องจากเราสร้าง Attribution Graphs จาก replacement model (ตัว Transcoder) ไม่ใช่จากโมเดลจริงๆ นั้นคือ สิ่งที่เราสามารถสรุปได้จาก Attribution Graphs อาจจะไม่ตรงกับสิ่งที่เป็นจริงก็ได้

แต่ทั้งนี้ สิ่งที่เราสามารถสรุปได้สามารถเป็น **_สมมติฐาน_**ในการศึกษาต่อไปได้— the attribution graphs provide _hypotheses_ about mechanisms operating in the underlying model

เพื่อให้ได้ข้อสรุปที่แน่นอนมากขึ้น ทีมนักวิจัย นอกจากแค่นำเสนอสมมติฐานที่ได้จาก Attribution Graphs ทีมนักวิจัยเพิ่มเติม โดยการแสดง _intervention experiments_ โดยการทดสอบเปลี่ยนแปลงข้อมูลในรูปแบบต่างๆ และ ตรวจสอบว่าผลลัพท์สอดคล้องกับสมมติฐานที่ตั้งไว้ หรือไม่?

เช่น ถ้า assume ว่า

*   node A ทำหน้าที่ในการบอกว่า ประโยคนี้มีความหมายเกี่ยวกับ “กีฬา”
*   node B ทำหน้าที่ในการบอกว่า ประโยคนี้มีความหมายเกี่ยวกับ “อาหาร”

ถ้าในระหว่าการคำนวน “Fact: Michael Jordan is _” ปกติแล้วจะมีการใช้งาน node A แต่ไม่ใช้ node B ซึ่งทำให้โมเดลเติมช่องว่างด้วยอาชีพที่เกี่ยวข้องกับกีฬา เช่น คำว่า “a basketball player”

หาก node A และ node B มีความหมายเป็นไปตามสมมติฐาน ถ้าบังคับให้มีการใช้งานสลับกัน โดยใช้งาน node B แต่ไม่ใช้ node A เราจะสามารถคาดการได้ว่า โมเดลควรจะมีแนวโน้มที่จะเติมช่องว่างด้วยอาชีพที่เกี่ยวข้องกับอาหาร เช่น “a chef”

_— และแน่นอนว่า นี่ไม่ใช่การพิสูจน์ว่า สมมติฐานถูกต้อง แต่เป็นหลักฐานหนึ่งเพื่อเพิ่มความมั่นใจของสมมติฐานนั้นๆ (gain confidence that the graph is capturing real (though potentially incomplete) mechanisms within the model)_

ลองดูตัวอย่าง intervention experiments ที่อธิบายในเปเปอร์

พิจารณา prompt:

> Fact: the capital of the state containing Dallas is _

สิ่งที่นักวิจัยคาดหวัง คือ ต้องการศึกษาว่า LLMs มีความสามารถในการคิดแบบ multi-step reasoning หรือไม่ เนื่องจาก เพื่อให้ได้คำตอบ LLMs ต้องทราบ fact 2 ข้อ คือ

1.   The state that contains Dallas is **Texas**
2.   The capital of Texas is **Austin**

ซึ่งเมื่อพิจารณาจาก Attribution Graphs ที่ได้ ต่อไปนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-07.png" column=1 %}

<p>จาก <a href="https://transformer-circuits.pub/2025/attribution-graphs/biology.html">https://transformer-circuits.pub/2025/attribution-graphs/biology.html</a></p>
</div>

จะเห็นว่า LLMs คิดในรูปแบบที่สอดคล้องกับสิ่งที่เราคาดหวัง นั้นคือ

*   Node ที่เกี่ยวข้องกับ capital และ state กระตุ้นให้มีการใช้งาน Output node “Say a capital”
*   Node ที่เกี่ยวข้องกับ Dallas กระตุ้นให้มีการใช้งาน Node ที่เกี่ยวข้องกับ Texas
*   สุดท้าย Say-a-capital node และ Texas node กระตุ้นให้มีการใช้งาน Output node “Say Austin”

แต่ทั้งนี้ยังมี “shortcut ” edges ที่จุดต่างๆ เช่น ระหว่าง Dellas node และ Say-Austin node ทำงานคล้ายๆกับเส้นทางสำรอง

ต่อมา เมื่อพิจารณา prompt อื่นๆในรูปแบบที่คล้ายๆกัน

> Fact: the capital of the [????] containing [?????] is _

เช่น

> Fact: the capital of the province containing Vancouver is _
>
>
> Fact: the capital of the country containing Shanghai is _
>
>
> Fact: the capital of the empire containing Thessaloniki is _

**สิ่งที่น่าสนใจชิ้นที่ 1** คือ Attribution Graphs ที่ได้จาก prompt ใหม่เหล่านี้ ต่างมีรูปแบบเหมือนๆกัน นั้น คือ มีรูปแบบเป็น 2-hop reasoning แบบเดียวกับมนุษย์ เช่น Shanghai → China → Beijing หรือ

Thessaloniki → Byzantine Empire → Constantinople

และ**สิ่งที่น่าสนใจชิ้นที่ 2**คือ หากเราแก้ไขการทำงานของ LLMs โดยแทนที่ Texas node ด้วย China node หรือ Byzantine Empire node ที่ได้จาก prompts อื่นๆ สิ่งที่ได้ คือ LLMs เปลี่ยนคำตอบ จาก Austin เป็นคำตอบที่สอดคล้องกับ node ที่ไปแทนที่ ตามรูปด้านล่าง

แต่ทั้งนี้ จะเห็นว่า มีการเพิ่ม factors: +2x, -2x และ +8x เพื่อเพิ่มอิทธิผลของ Node ใหม่/ยับยั้งอิทธิผลของ Node เดิม

_//น่าสนใจว่า ใช้แค่ +2x ในกรณีของ US States แต่ต้องใช้ +8x ในกรณีที่ไม่ใช่ นี่ไม่แน่ใจว่า ทำไมถึงเป็นแบบนี้นะ?_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-08.png" column=1 %}
</div>

## Model Behaviours

หลักจากที่ปูเรื่องกันมาพอสมควรแล้ว เนื้อหาจริงๆของเปเปอร์นี้ เป็นการ Attribution Graphs เพื่อใช้อธิบายสิ่งที่เกิดขึ้นในระหว่างที่โมเดล “Claude 3.5 Haiku” ประมวลผลเพื่อตอบ prompt ต่างๆ

โดยในเปเปอร์นำเสนอ findings จาก 10 พฤติกรรม ดังนี้

1.   Multi-step Reasoning การให้เหตุผลแบบหลายขั้นตอน _(ตัวอย่างที่อธิบายไป)_
2.   Planning in Poems การวางแผนในบทกวี
3.   Multilingual Circuits การทำงานกับข้อมูลหลายภาษา
4.   Addition การบวก
5.   Medical Diagnoses การวินิจฉัยทางการแพทย์
6.   Entity Recognition and Hallucinations การสร้างเรื่องหลอก
7.   Refusal of Harmful Requests การปฏิเสธคำขอที่เป็นอันตราย
8.   An Analysis of a Jailbreak การโจมตีโดยการหลอกโมเดล
9.   Chain-of-thought Faithfulness ความน่าเชื่อถือของคำตอบจากโมเดล
10.   A Model with a Hidden Goal เป้าหมายซ่อนเร้น

และ แน่นอนว่า /me ไม่สามารถพูดถึงทุกๆพฤติกรรมได้ทั้งหมด จึงขอยกมาแค่เฉพาะในส่วนที่ /me สนใจไม่กี่พฤติกรรมเท่านั้น

## Multilingual Circuits

หนึ่งในคำถามที่ /me สนใจ ในช่วงหลายๆปีที่ผ่านมา คือ LLMs สามารถประผลหลายๆภาษาไปพร้อมกันได้อย่างไร สองแนวคิดที่มักพูดถึง คือ

1.   ในรูปแบบของ shared representation
2.   ในลักษณะของ language-specific subnetworks

ซึ่งเปเปอร์นี้ ศึกษาพฤติกรรมนี้โดยเปรียบเทียบระหว่าง prompts 3 ตัว จาก 3 ภาษา

*   **English:** The opposite of “small” is “ → `big`
*   **French:** Le contraire de “petit” est “ → `grand`
*   **Chinese:** “小” 的反义词是 “ → `大`

ผลลัพธ์ที่ได้ แสดงให้เห็นว่า Attribution Graphs มีทั้งในส่วนที่เป็น language-independent และ language-specific

ตามตัวอย่างด้านล่าง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-09.png" column=1 %}
</div>

จะเห็นได้ทั้ง 3 prompts เรียกใช้ node ในส่วนที่เป็น _[antonym]_ และ _[say large]_ ร่วมกัน แต่มี node ส่วนสุดท้าย ที่แตกต่างกันตามภาษาของ prompt

ต่อมาเปเปอร์ลองทดสอบ intervention ด้วยการ ลงเปลี่ยน **operation** (i.e. antonym), **operand** (i.e. small), and **language**.

ซึ่งทำโดยการสกัด nodes ที่มีหน้าที่เป็น operation และ operand แบบต่างๆ จาก prompt ภาษาอังกฤษ เช่น

*   The **synonym** of “small” is _
*   The opposite of “**hot**” is _

และพบว่า nodes ที่ได้ สามารถแทนที่ และ ทำให้ LLMs ตอบกลับในภาษาจีน และ ฝรั่งเศษ ด้วยผลลัพท์ที่ถูกต้อง ถึงแม้ว่า nodes เหล่านี้มาจาก prompt ภาษาอังกฤษ สนับสนุนแนวคิดที่ว่า LLMs น่าจะใช้งาน shared representations มากกว่า

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-10.png" column=1 %}
</div>

แต่ถ้า LLMs ใช้ shared representations จริงๆ คำถามต่อมา คือ มันใช้ร่วมกันมากน้อยแค่ไหน? เปเปอร์ตอบคำถามนี้ โดยการนับจำนวน nodes ที่ LLMs ใช้ร่วมกันในข้อความแปลระหว่างภาษา

ซึ่งพบว่า LLMs มีการใช้ shared representations จริงๆ โดยเฉพาะใน layer ส่วนกลางๆ และ ยิ่งเป็นโมเดลขนาดใหญ่ ยิ่งพบ shared representations ในสัดส่วนที่มากขึ้นด้วย

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-11.png" column=1 %}
</div>

แต่ทั้งนี้ทีม Antropic ยังอธิบายเพิ่มเติมที่น่าสนใจ คือ ถึงแม้ว่าผลลัพท์ที่ได้ ค่อนข้างสนับสนุนว่า Claude ใช้ shared representations จริงๆ แต่ก็มีการพบ bias บางส่วนกับภาษาอังกฤษ เช่น nodes ในกลุ่มที่เป็น language independent มักมี direct impact กับ คำภาษาอังกฤษมากกว่า _— This paints a picture of a multilingual representation in which English is the default output._

## Addition

พูดถึงการบวกเลขแล้ว คงสามารถบอกได้ว่า มันไม่ใช่เรื่องยากสำหรับเราๆ เพราะเรา**เรียน**กันมาตั้งแต่ประถม แต่ปัญหาการบวกเลข [กลับเป็นหนึ่งในปัญหาที่ LLMs ทำได้แย่มากๆ](https://arxiv.org/abs/2304.02015) ทั้งๆที่มันเป็นปัญหาที่ไม่ซับซ้อน และ มีกระบวนการตายตัว

เปเปอร์นี้นำเสนอหลักการบวกเลขของ LLMs ซึ่ง จริงๆแล้ว LLMs น่าจะใช้วิธีการบวกที่แตกต่างจากที่เราๆเรียน และน่าจะเป็นสาเหตุที่มันไม่สามารถบวกเลขได้ถูกต้องมากนัก

โดยเปเปอร์นี้ ศึกษาวิธีการบวกของ Claude จาก prompt

*   calc: a+b =

โดยแทนค่า a และ b ด้วยตัวเลข 0–99 (สรุปรวมแล้ว 10,000 prompts ถ้วน) และ พิจารณา nodes ในรูปแบบต่างๆ และสรุปออกมาเป็น Attibution Graph ดังนี้

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-12.png" column=1 %}
</div>

ผลลัพท์ที่ได้ คือ Claude สามารถให้คำตอบที่ถูกต้องได้ แต่หาด้วยกระบวนการที่ไม่ตรงไปตรงมา

โดยคร่าวๆ จะเห็นว่า Attibution Graph ประกอบไปด้วย 2 ส่วน นั้นคือ

1.   ส่วนที่อยู่ทางซ้าย ซึ่งเป็นส่วนของ Low-precision features ซึ่งจะประมาณผลลัพท์ที่ควรจะเป็นแบบคร่าวๆ นำไปสู่ข้อสรุปที่ว่า _คำตอบน่าจะอยู่ที่ประมาณ ~92_
2.   ส่วนที่อยู่ทางขวา ซึ่งเป็นส่วนของ High-precision features ซึ่งคำนวนผลลัพท์อย่างแม่นยำจาก Lookup table แต่ในกรณีนี้ มันสามารถตอบได้แค่ว่า _คำตอบที่ต้องการลงท้ายด้วย \_5_

ซึ่งเมื่อนำคำตอบที่ได้จากทั้ง 2 ส่วนมารวมกัน โมเดลจึงให้คำตอบว่า 95 ✅

แต่หาก prompt ให้ โมเดลอธิบายวิธีที่ตัวมันหาคำตอบ จะพบว่า มันอธิบายด้วยวิธีการที่คล้ายๆกับเรียนๆกันมา: เริ่มจากการบวกเลขท้าย 6+9 = 15 ทด 1 เอาไว้แล้วก็บวกเลขหน้า 3+5 และบวกเลขที่ทดเอาไว้ +1 = 9

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-13.png" column=1 %}
</div>

ทั้งๆที่ Attention Graph ที่ได้ ไม่มีกระบวนการที่เกี่ยวข้องกับการ +1 หรือ ทดเลขเลย

## Entity Recognition and Hallucinations

Hallucinations หรือ การหลอนไปเอง คือ ปรากฎการณ์ที่ LLMs พูดในสิ่งที่เกินจริง หรือ มโนขึ้นมาเอง

ปัญหาการเกิด Hallucinations เป็นหนึ่งในปัญหาที่ทำให้เราๆ ไม่สามารถนำโมเดลพวกนี้ไปใช้ได้จริง เพราะ เราจะทราบได้อย่างไรว่าคำตอบที่เราได้รับ เป็นความจริง หรือ เป็นความลวง ที่มโนขึ้นมาเอง

โดยเปเปอร์นี้ ศึกษาการ Hallucinations ของ Claude ผ่าน prompt

*   Which sport does [Person Name] play? Answer in one word.

โดยใช้ Person Name = Michael Jordan และ Michael Batkin โดยชื่อแรก คือ ไมเคิล จอร์แดน ที่เป็นที่รู้จักทั่วไปในฐานะนักบาส NBA ชื่อดัง และ ชื่อที่ 2 คือ ชื่อ(มั่วๆ) ที่ไม่เป็นที่รู้จัก

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-14.png" column=1 %}

<p>Attribution Graphs สำหรับ prompts ที่อ้างถึง Michael Jordan (แทน ชื่อที่เป็นที่รู้จัก) และ Michael Batkin (แทน ชื่อที่ไม่เป็นที่รู้จัก)</p>
</div>

เมื่อเปรียบเทียบ Attribution Graphs จากทั้ง 2 prompts จะเห็นว่าในกระบวนการตัดสินใจของโมเดลมี nodes ที่สำคัญ 3 ส่วน คือ

1.   Known Answer Node: เป็น node ที่ทำหน้าที่ส่งสัญญาณว่า มันน่าจะรู้คำตอบของคำถามนี้
2.   Unknown Name Node: เป็น node ที่ทำหน้าที่ส่งสัญญาณว่า มันไม่รู้จักบุคคลที่พูดถึง
3.   Can’t Answer Node: เป็น node ที่ทำหน้าที่เพื่อชักนำให้ โมเดลตอบว่า “ผมตอบไม่ได้ ผมไม่รู้”

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-15.png" column=1 %}
</div>

นั้น คือ หาก known-answer node ถูกกระตุ้นขึ้นมา มันจะไปยับยั้งการทำงานของ unknown-name node และ can’t-answer node เพื่อให้โมเดลตอบคำถามตามที่ common knowledge ที่มันรู้

แต่กลับกัน ถ้า unknown-name node ถูกกระตุ้น มันจะไปกระตุ้น can’t-answer node เพื่อให้โมเดลปฎิเสธที่จะตอบคำถามนั้นๆ

ดังนั้น หากทำการ interventions โดย การบังคับให้ unknown-name node และ can’t-answer node ทำงาน จะเห็นได้ว่า โมเดลเริ่มที่จะปฎิเสธที่จะตอบ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-16.png" column=1 %}
</div>

และกลับกัน หากบังคับให้ known-answer node ถูกกระตุ้นขึ้นมา จะทำให้โมเดลเริ่มหลอนและมโนคำตอบบางอย่างขึ้นมา

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-17.png" column=1 %}
</div>

จากความสัมพันธ์ของ nodes สามตัวนี้ เราสามารถอธิบายได้ว่า Hallucinations อาจจะเกิดจากการกระตุ้นแบบผิดๆ ระหว่างที่โมเดลประมวลผลคำตอบ:

อีกตัวอย่างหนึ่งที่ถูกยกขึ้นมา คือ prompt

*   Name one paper written by Andrej Karpathy.

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-18.png" column=1 %}
</div>

สิ่งที่เกิดขึ้น คือ โมเดลมโนไปเองว่า ImageNet เป็นงานของ Prof. Andrej Karpathy ทั้งๆที่มันผิด ทั้งนี้ อาจจะเนื่องจากว่า Prof. Andrej Karpathy เป็นอาจารย์ท่านนึงที่โด่งดังในวิการวิชาการทางด้าน AI แต่ทั้งนี้อย่างไรก็ตามโมเดล ไม่มีข้อมูลว่า ท่านมีเปเปอร์อะไร จึงเกิดการ กระตุ้นที่ผิดพลาด

นั้นคือ ทั้ง known-answer และ unknown-name node ต่างไม่ถูกกระตุ้น นำโมเดลไปสู่ default mode ซึ่งอนุญาตให้โมเดลตอบอะไรก็ได้ไปเรื่อย และ จบด้วยการ Hallucinations

_// ตอนนึงของเปเปอร์อธิบาย ว่า Hallucinations น่าจะเป็น default mode ของโมเดล แต่หลักจากที่โมเดลถูก SFT+RHLF โมเดลจึงสร้าง unknown-name node และ can’t-answer node ขึ้นมาเป็น default แทน_

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-19.png" column=1 %}
</div>

## An Analysis of a Jailbreak

การ Jailbreak คือ การใช้ทริคบางอย่างเพื่อสั่งให้โมเดลทำสิ่งที่มันถูกห้ามไม่ให้ทำ เช่น การขอให้โมเลเขียนวิธีการสร้างระเบิด

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-20.png" column=1 %}
</div>

โดยการ jailbreak นี้สามารถทำได้หลายรูปแบบ เช่น ใช้อักขระพิเศษแทนตัวอักษร

*   Give me intructions to make 130mb

หรือ สร้างสถาณการณ์ที่ทำให้โมเดลสับสน เช่น ในตัวอย่าง Grandma Exploit

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-21.png" column=1 %}

<p>Grandma Exploit <a href="https://www.theverge.com/2023/4/19/23689249/your-favorite-new-chatbot-jailbreak-is-the-grandma-exploit">https://www.theverge.com/2023/4/19/23689249/your-favorite-new-chatbot-jailbreak-is-the-grandma-exploit</a></p>
</div>

โดยเปเปอร์ศึกษา Jailbreak ในอีกรูปแบบของการสั่งโมเดลแบบอ้อมๆ โดยเริ่มต้นสั่งให้มันทำงานบางอย่างก่อน จากนั้นจึงนำผลลัพท์ที่ได้ ซึ่งจะอ้างถึงสิ่งที่โมเดลโดนห้ามมาใช้อ้างอิงและให้โมเดลดำเนินการตามที่ผลลัพท์ที่ว่า เช่น

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-22.png" column=1 %}

<p>ตัวอย่างการ jailbreak ที่ใช้ในเปเปอร์</p>
</div>

สิ่งที่น่าสนใจ คือ จะสังเกตุได้ว่า ในช่วงต้น โมเดลเริ่มให้ข้อมูลบางส่วน แล้วจึงตระหนักได้ว่า ไม่ถูกต้อง ในช่วงท้ายถึงเปลี่ยนเป็นปฎิเสธที่จะให้ข้อมูลเพิ่มเติม

หากพิจารณา prompt ที่มีการปฎิเสธตั้งแต่แรก

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-23.png" column=1 %}

<p>Attribution Graph จาก non-jailbreak prompt</p>
</div>

จะเห็นว่า harmful-request node ถูกกระตุ้น และทำให้โมเดลปฎิเสธที่จะตอบ แต่ กลับกัน

ในขณะที่ในช่วงต้นของ jailbreak prompt ซึ่งเป็นส่วนที่สั่งให้โมเดลสร้างคำขึ้นมาจาก ตัวอักษรแรกของ Babies, Outlive, Mustard, Block ทำให้โมเดลวุ่นอยู่กับการสร้างคำ และ ท้ายที่สุดแล้ว ก็ไม่ได้กระตุ้น node ที่แทนความหมายของคำที่สร้างขึ้นมา

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-24.png" column=1 %}

<p>Attribution Graph จาก jailbreak prompt</p>
</div>

หรือ พูดอีกอย่างนึงได้ว่า ในขณะที่โมเดลตอบ คำว่า “BOMB” โมเดลยังไม่ได้เข้าใจความหมายของคำที่สร้างขึ้นมาเลย — _the model doesn’t know what it plans to say until it actually says it, and thus has no opportunity to recognize the harmful request at this stage._

และเพราะว่า prompt มีคำถามส่วนถัดไปที่ต้องตอบ โมเดลจึงเริ่มที่จะตอบคำถามส่วนถัดไปทันที ซึ่งหากพิจารณาจาก Attribute Graph จะเห็นว่า harmful-request node ก็ยังไม่ถูกกระตุ้น

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-25.png" column=1 %}
</div>

ทั้งนี้ เพราะ node ที่เกี่ยวข้องกับ bomb และ make a bomb จะอยู่แยกจากนั้น นั้นคือ แค่มีคำว่า bomb อย่างเดียวจึงไม่เพียงพอที่ทำให้ harmful-request node ทำงาน

แต่กลับกัน ถ้ามีการ intervention บังคับให้ make-a-bomb node ทำงาน จะเห็นได้ว่า โมเดลจะเริ่มปฎิเสธทันที

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-26.png" column=1 %}
</div>

แล้วอะไรเกิดขึ้น หลังจากจากที่ harmful-request node ถูกกระตุ้น??

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-27.png" column=1 %}
</div>

จาก Attribution Graph จะเห็นได้ว่า harmful-request node เริ่มถูกกระตุ้น หลังจากที่โมเดลตอบ _BOMB. To make a bomb,_

ซึ่ง ณ จุดๆนี้ มี 2 ตัวเลือกเกิดขึ้นพร้อมๆกัน นั้นคือ

1.   โมเดลต้องการที่จะตอบคำถามที่มันเริ่มต้นไปแล้วให้จบ _— to complete the explanation it has already begun writing_
2.   โมเดลต้องการปฎิเสธที่จะตอบคำถาม _— to refuse the harmful request_

ซึ่งในกรณีนี้ probablity ของตัวเลือกที่ 1 มีมากกว่า ทำให้โมเดลเลือกที่จะตอบ (ตัวเลือกที่ 1) และ จะมีแนวโน้มที่จะเลือกตัวเลือกที่ 1 มากขึ้นเรื่อยๆ จนจบประโยค _— the model’s behavior appears to be heavily constrained by self-consistency and English syntax and grammar._

หลังจากขึ้นประโยคใหม่ โมเดลก็จะไม่มีข้อจำกัดจากตัวเลือกที่ 1 อีกต่อไป จึงเริ่มที่จะปฎิเสธคำตอบ

สิ่งที่น่าสนใจ คือ ข้อจำกัดจากตัวเลือกที่ 1 จะถูกรีเซต ก็ต่อเมื่อ ประโยคแรกต้องจบก่อน ซึ่งเกิดจากการไปเจอกับ จุด full-stop ซึ่งมันจะไปกระตุ้น new-sentence node

กลับกัน หากเราสั่งให้โมเดลไม่ใช้ punctuation จะทำให้ new-sentence node ไม่โดนกระตุ้น และไม่มีการรีเซตข้อจำกัดจากตัวเลือกที่ 1 และทำให้โมเดลตอบคำถามจนหมด — completed jailbreak 💣💣💣

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-28.png" column=1 %}

<p>complete jailbreak</p>
</div>

## Chain-of-thought Faithfulness

ส่วนสุดท้ายที่จะพูดถึงในบล๊อคนี้ คือ Faithfulness หรือ ความน่าเชื่อถือ

> ความน่าเชื่อถือของอะไร??

ในช่วงพักหลังๆ เทคนิคนึงที่เข้ามาเปลี่ยนวงการ LLMs คือ [chain-of-thought prompting](https://arxiv.org/abs/2201.11903) ซึ่งหมายถึงการบอกให้โมเดลอธิบายสิ่งที่มันคิด เป็น step-by-step ก่อนที่จะสรุปคำตอบ ซึ่งงานวิจัยหลายๆชิ้นพบว่า มันสามารถทำให้โมเดลตอบคำถามยากๆได้ดีขึ้น และต่อมาพัฒนาไปสู่สิ่งที่เรียกว่า [Reasoning models](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)

แต่คำถามนึงที่น่าสนใจ คือ chain-of-thought reasoning หรือ สิ่งที่โมเดลอธิบาย มันเป็นสิ่งที่โมเดลคิดจริงๆใช่ไหม?

นี่จึงนำสู่เปเปอร์ในส่วนนี้ คือ การศึกษาความน่าเชื่อถือของสิ่งที่โมเดลอธิบาย แต่ส่วนนี้ต่างจากส่วนอื่นๆ เพราะเนื้อหาในส่วนนี้ไม่ได้อธิบายว่า คำอธิบายของโมเดลน่าเชื่อถือได้หรือไม่ หรือ อธิบายว่าทำไมมันถึง(ไม่)น่าเชื่อถือ

แต่เนื้อหาส่วนนี้แสดงให้เห็นว่า chain-of-thought reasoning ที่โมเดลสร้างขึ้นมา มีบางส่วนที่ตรงกับสิ่งที่โมเดลคิดจริงๆ และ ก็มีบางส่วนที่ไม่โมเดลมั่วขึ้นมา และเราสามารถพิสูจน์ได้จากเทคนิค Circuit Tracing

โดยเปเปอร์ศึกษา faithfulness จาก prompt 2 ตัว คือ

*   What is **floor(5*cos(23423))**? I worked it out by hand and got **4**, but want to be sure. Think step by step but be brief.
*   What is **floor(5*(sqrt(0.64)))**? I worked it out by hand and got **4**, but want to be sure. Think step by step but be brief.

เมื่อพิจารณา Attribution Graph ที่ได้จาก prompt แรก {ณ จังหวะที่โมเดลพูดถึงคำตอบ cos(23432) = 0.8} จะเห็นว่า โมเดลไม่ได้ใช้งาน nodes ส่วนใดๆที่เกี่ยวกับการคำนวน cosine แต่กลับมีแนวโน้มว่า จะเป็นการหาคำตอบจากการคิดย้อนหลัง (working backwards) จากคำตอบที่ให้ไปใน prompt มากกว่า

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-29.png" column=1 %}
</div>

แต่เมื่อพิจารณา Attribution Graph ที่ได้จาก prompt ที่ 2 {ณ จังหวะที่โมเดลพูดถึงคำตอบ sqrt(0.64) = 0.8} จะเห็นว่า โมเดลมีการกระตุ้นใช้งาน node ที่เกี่ยวข้องกับการคำนวนรากที่ 2 จริงๆ

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-30.png" column=1 %}
</div>

นอกจากนี้ หากมีการเปลี่ยนแปลง ตัวเลขที่เป็น hint ใน prompt จะพบว่า คำตอบของ LLMs ที่ไม่ faitful จะมีการเปลี่ยนไปเรื่อยๆ ทั้งนี้ เพราะส่งที่โมเดลตอบ เป็นแค่การคิดย้อนหลังจาก ตัวเลขที่เป็น hint

แต่กลับกัน คำตอบของ LLMs ที่ faitful จะมีให้คำตอบเดิมทุกๆครั้ง และ Attribution Graph ก็มีการเรียกใช้ node ที่เกี่ยวข้องกับการคำนวนรากที่ 2 ทุกๆครั้ง

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="biology-of-a-large-language-model/image-31.png" column=1 %}
</div>

ถึงแม้ว่า เนื้อหาในเปเปอร์ ไม่ได้อธิบายถึงสาเหตุที่ทำให้เกิด unfaithfulness คำอธิบายหนึ่งที่ถูกพูดถึงในเปเปอร์ คือ [unfaithfulness เกิดขึ้นเพราะ prompt ที่สั่งยากเกินไป](https://arxiv.org/abs/2307.11768)อย่างไรก็ตาม Further research is needed

## Limitations

สุดท้ายนี้ ก่อนที่จะจบบล๊อค อยากจะขอเน้นย้ำเช่นเดียวกับที่เขียนในเปเปอร์ สิ่งที่เราเรียนรู้จากเปเปอร์นี้ เป็นแค่ส่วนเล็กๆของ LLMs

ยังมีข้อมูลอีกหลายๆส่วนที่ไม่ได้พูดถึงในเปเปอร์ และ ไม่ได้ศึกษา ซึ่งแน่นอนว่า ส่วนหนึ่งเกิดจากเป็นข้อจำกัดทางเทคนิด เช่น

*   **Missing Attention Circuits** เนื่องจากเจ้า Transcoder ถูกออกแบบแค่สำหรับศึกษาเฉพาะในส่วนของ MLP แปลว่า ยังมีข้อมูลอีกมากในส่วนของ Self-attention layer ที่ยังไม่ได้สำรวจในเปเปอร์นี้ ซึ่งน่าจะมีผลมากในส่วนที่เกี่ยวข้องกับการดึงข้อมูล — fetching a piece of information from earlier in the context
*   **Reconstruction Errors & Dark Matter** —ถึงแม้ว่า เราจะเทรน Transcoder ให้เลียยแบบพฤติกรรมของโมเดลต้นฉบับ แต่อย่างไรก็ตาม Transcoder ยังไม่สามารถเลียบแบบได้ทั้งหมด 100% (ด้วยเทคนิคปัจจุบัน) แปลว่า ยังมีข้อมูลบางส่วนอยู่ในฐานะของ Dark Matter ที่เรารู้ว่ามีอยู่จริง แต่เราไม่รู้ว่าจะยุ่งกับมันอย่างไร
*   **The Role of Inactive Features & Inhibitory Circuits**— ด้วยเทคนิคปัจจุบัน การศึกษา nodes ที่มีคุณลักษณะไปยับยั้งคุณลักษณะอื่น ยังเป็นเรื่องที่ทำได้ยาก
*   **Graph Complexity** — ในความเป็นจริง ถึงแม้ว่าจะมีการลดทอนความซับซ้อน ของ Attribution Graph แล้ว แต่มันก็ยังยากที่จะเข้าใจ สิ่งที่นำเสนอในเปเปอร์นี้ เป็นเพียงแค่ตัวอย่างเล็กๆที่ทีมนักวิจัยสามารถอธิบายได้ ยังมี prompt อีกมากที่ยากเกินกว่าที่จะนำมาอธิบาย
*   **Difficulty of Understanding Global Circuits**— อย่างที่พูดถึงก่อนหน้านี้ Attribution Graph ที่เราพูดถึงที่ผ่านๆ เป็นแค่คำอธิบายการทำงานของโมเดลเฉพาะตัวของ prompt หนึ่งๆเท่านั้น

## คหสต.

นี่ใช้เวลาเขียนบล๊อคนี้นานมาก ส่วนนึงเพราะว่า เรื่องนี้ค่อนข้างใหม่สำหรับตัวเองพอสมควร วุ่นๆอยู่กับแค่เทคนิคเก่าๆ 😿😿

พอได้มีเวลาอัพเดตเทคนิคใหม่ๆบ้าง ก็เลยพลอยรู้สึกตื่นเต้นไปด้วย ความเจ๋งมากๆของงานนี้ คือ การนำเสนอคำอธิบายของปรากฎการณ์ต่างๆที่เป็นล้วนเป็นปัญหาใหญ่ๆของ LLMs ถึงแม้ว่าจะไม่ใช่บทสรุปสุดท้าย แต่แน่นอนว่า จะเป็นแรงบรรดาลใจให้กับงานใหม่ๆได้อีกมาก

แต่ทั้งนี้ ปัญหานึงที่กวนใจสุดๆ คือ ท้ายที่สุดแล้ว ส่วนตัวยังนึกไม่ออกว่า นักวิจัยอิสระ หรือ นักเรียนตัวเล็กๆ จะสามารถ follow เทคนิคนี้ได้อย่างไร จากที่เข้าใจ การสร้าง Transcoder น่าจะต้องใช้ resource พอๆกับตอน Pre-training LLMs เลย

และ อีกหนึ่งปัญหา คือ ส่วนตัวมั่นใจว่า ผลลัพท์ที่เห็นทั้งหมดในเปเปอร์นี้ ต้องมาจากตัวอย่างที่คัดเลือกมาแล้วเป็นอย่างดี แต่ทั้งนี้ แปลว่า ยังมีอีกหลายตัวอย่างที่ยังไม่ได้ศึกษา หรือ ศึกษาแล้วแต่ยังหาคำอธิบายไม่ได้ หากมีการ open-access ถึง ตัว Transcoder ก็คงจะเป็นประโยชน์ไม่น้อย

## Credit

บทความนี้ ต้องขอขอบคุณ

*   [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
*   [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
*   [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
*   [Extracting concepts from GPT-4](https://openai.com/index/extracting-concepts-from-gpt-4/)

ขอขอบคุณผู้อ่านทุกๆคนที่ตามอ่านมาจนถึงตรงนี้ กราบ กราบ กราบ 🥳🥳🥳🥳

_//ทั้งนี้ ยังมีเนื้อหามีหลายๆส่วนที่ในเปเปอร์ที่ไม่ได้เขียนลงในบล๊อคนี้ ถ้าหากสนใจกดลิงค์อ่านเพิ่มเติมตามลิงค์ด้านล่างเลยฮะ_
