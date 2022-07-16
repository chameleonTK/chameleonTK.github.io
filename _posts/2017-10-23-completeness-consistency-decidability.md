---
layout: post
title: Completeness, Consistency, Decidability
tags: [Archive, Mathematics]
thumbnail: "assets/feats/completeness-consistency-decidability/algorithm-math-seo-fade-ss-1920.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(247 214 56)

---

## TL;DR
เมื่อนักคณิตศาสตร์หลายคนเริ่มเกิดคำถามที่เป็นที่น่าหวั่นใจของนักคณิตศาสตร์มากที่สุด “สมการที่ได้มาจากการต่อยอดกันมานับ 100 ปี ในแต่ละสาขา มันไม่ขัดแย้งกันจริงๆใช่ไหม?”

<!--more-->

ถ้าพูดถึง Mathematics คงต้องพูดถึงตัวเลขยุบยับ, สมการ, ความสัมพันธ์นู้นนี้ๆ, สัญญาลักษณ์ถั่วงอกสุดสยองที่เรียกว่า อินทิเกิล

ไม่ว่าจะเป็นรูปทรง, ลูกบิค, เสียงเพลง หรือแม้กระทั้งปมเชือก ต่างก็สามารถเป็น Mathematics ได้เหมือนๆกัน ตลอด 1,000 ปี ของการพัฒนาตัวเองของมนุษย์ Mathematics ค่อยๆแตกขยายไปเป็นหลายๆสาขา หลายๆหัวข้อ เพื่อแก้ในแต่ละปัญหา

และเมื่อหัวข้อมากขึ้น นักคณิตศาสตร์หลายคนเริ่มเกิดคำถามที่เป็นที่น่าหวั่นใจของนักคณิตศาสตร์มากที่สุด "สมการที่ได้มาจากการต่อยอดกันมานับ 100 ปี ในแต่ละสาขา มันไม่ขัดแย้งกันจริงๆใช่ไหม?" เสมือนการเขียนโปรแกรมหลายๆฟีเจอร์มาประกอบกัน ถึงแม้ว่าแต่ละส่วนจะทดสอบมาเป็นอย่างดีว่า ไม่มีความผิดพลาด แต่เมื่อนำมาประกอบกัน ก็ไม่ได้แปลว่ามันจะใช้งานร่วมกัันได้อย่างสมบูรณ์

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1W3mPxgAHZqFAIEtsmMK80ibYjHat-Fpc" column=1 %}

นี้จึงเป็นจุดเริ่มต้นของการพยายามศึกษา Foundation of Mathematics เพื่อพยายามหาความเชื่อมโยงในของแต่ละสาขาเข้าด้วยกัน ตลอดหลายสิบปีที่ผ่านมา การตามหา Foundation of Mathematics นี้จึงเป็นเหมือนตามหาจอกศักดิ์สิทธิ์ที่สูญหายไป

แต่ความพิเศษของ การศึกษาเรื่องนี้ คือ ยิ่งศึกษายิ่งทำให้นักคณิตศาสตร์เข้าใจความเป็นคณิตศาสตร์มากยิ่งขึ้น หลายๆสาขาเป็นแค่คนละมุมมองในของสิ่งเดียวกัน เช่น Geometry ก็แค่การแสดงผล Arithmetic ในเชิงรูปภาพ หรือ Propability ก็ไม่ต่างกับการศึกษา Real Analytics เพียงแต่ศึกษาในภาพกว้างเท่านั้นเอง

ในปี 17xx การเริ่มต้นตามหาจอกศักดิ์สิทธิ์ เริ่มต้นขึ้นโดยนักคณิตศาสตร์ชื่อดัง 2 คน คือ Leibniz และ Lambert แต่จุดเปลี่ยนสำคัญเกิดขึ้นใน 1879 โดย Gottlob Frege ซึ่งพูดถึงคุณสมบัติ 3 ประการของ Foundation of Mathematics ที่ต้องมี ดังนี้

(และมันคือหัวข้อที่จะเขียนวันนี้ แต่เกริ่นยาวมาก~)

# Completeness

ทุกๆประโยคในระบบ จะต้องสามารถบอกได้ว่ามันเป็นจริง หรือ เท็จ หมายความว่า ทุกๆ conjecture/hypothesis ในคณิตศาสตร์จะต้องสามารถหาค่าความจริงของมันได้ อาจจะจริง หรือ เท็จก็โอเค

# Consistency

ทุกๆประโยคในระบบ จะต้องเป็นจริง หรือ เท็จ แค่อย่างใดอย่างหนึ่งเท่านั้น จะไม่มีประโยคใดๆที่สามารถเป็นได้ทั้งจริงและเท็จพร้อมกัน จริงๆ

ถ้าคิดต่อยอดจะพบว่า ระบบที่ inconsistency จะเป็นระบบที่ทำให้ทุกๆประโยคเป็นจริงได้เสมอ เพราะ (P and P') มีค่าเป็น false และ ถ้า false แล้ว X ใดๆ จะได้ค่าความจริงเป็น true เสมอ

# Decidability

จะต้องมีบางวิธีการที่สามารถพิสูจน์ว่า ทุกๆประโยคเป็นจริง หรือ เท็จ โดยระบบที่ Consistency แต่ไม่ Decidability คือ ระบบที่ทุกๆประโยคในระบบไม่ชัดแย้งกัน แต่อย่างไรก็ตาม จะมีบางประโยคที่เราไม่รู้ว่ามันเป็นจริง หรือ เท็จ

หลังจากนั้นในปี 1900 David Hilbert จัดปัญหานี้(คณิตศาสตร์มันไม่ขัดแย้งกันใช่ไหม?)เป็นหนึ่งใน 23 Hilbert's problems


<div class="blockquote"> When we are engaged in investigating the foundations of a science, we must set up a system of axioms which contains an exact and complete description of the relations subsisting between the elementary ideas of that science. ... But above all, I wish to designate the following as the most important among the numerous questions which can be asked with regard to the axioms: To prove that they are not contradictory, that is, that a definite number of logical steps based upon them can never lead to contradictory results. In geometry, the proof of the compatibility of the axioms can be effected by constructing a suitable field of numbers, such that analogous relations between the numbers of this field correspond to the geometrical axioms. ... On the other hand, a direct method is needed for the proof of the compatibility of the arithmetical axioms -- David Hilbert
</div>

แต่ว่า ปัญหาที่ Hilbert พูดจริงๆ สนใจเจาะจงเฉพาะ consistentcy of arithmetic และหนึ่งในความพยายามแก้ปัญหานี้มาจากนักคณิตศาสตร์ 2 คน คือ Gödel และ Gentzen

{% include aligner.html images="https://drive.google.com/uc?export=view&id=1v0mlMZHv2yDbodFRkz9dRivw_iX9BrWd" column=1 %}

โดย Gödel พิสูจน์ว่า arithmetic ไม่สามารถใช้แค่ตัวมันเองพิสูจน์ความเป็น consistentcy ของตัวมันเองได้ ซึ่งข้อพิสูจน์นี้ เป็นส่วนหนึ่งของ Gödel's incompleteness theorem ที่กล่าวว่า "ระบบ arithmetic ที่ Consistency จะไม่ Completeness และไม่สามารถพิสูจน์ความ Consistency ของตัวมันเองได้"

แต่ Gentzen พิสูจน์ในปี 1936 ว่า arithmetic เป็นระบบที่ consistentcy โดยการสร้างระบบใหม่ที่มีความสามารถมากกว่าระบบเดิม แล้วใช้มันพิสูจน์ ระบบ arithmetic

PS. Arithmetic ในที่นี้ คือ ระบบการคำนวนที่เกี่ยวกับตัวเลขจำนวน เช่น บวก ลบ คูณ หาร

# Conclusion

จริงๆแล้ว วันนี้พึ่งสามารถเข้าใจ Gödel's incompleteness theorem เป็นครั้งแรก เลยรู้สึกตื่นเต้น และทฤษฏีนี้เป็นรากฐานในหลายๆปัญหา เช่น Undefinability theorem, Entscheidungsproblem และ halting problem (ปัญหาสุดแสบในวงการคอมพิวเตอร์)

Gödel's incompleteness theorem เป็นสิ่งที่บั่นทอนกำลังใจในเชิงคณิตศาสตร์เป็นวงกว้างมาก เพราะเป็นการบอกเราว่า ปัญหาที่เรากำลังเจออยู่นั้น อาจจะไม่ใช่จริง/เท็จ แต่มันอาจจะไม่สามารถพิสูจน์ได้เลย บางทีหลายๆ conjecture อย่าง twin prime conjecturre หรือ riemann hypothesis อาจจะเป็นหนึ่งในนั้นก็ได้

แต่อย่างไรก็ตาม Gödel's incompleteness theorem มีเงื่อนไขเฉพาะตัวของมัน แปลว่า เรายังมีโอกาสในการหาระบบคณิตศาสตร์ใหม่ๆมาทดแทนระบบเดิม บางทีนอกจากจะเลี่ยงข้อจำกัดที่เกิดจาก Gödel's incompleteness theorem แล้ว มันอาจจะเป็น Foundation of Mathematics อันใหม่ก็เป็นไปได้