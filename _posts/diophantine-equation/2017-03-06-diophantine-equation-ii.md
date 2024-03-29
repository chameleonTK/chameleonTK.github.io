---
layout: post
title: "How to solve diophantine equation II : Ax2 + Bxy + Cy2 + Dx + Ey + F = 0"
tags: [Archive, Mathematics]
thumbnail: "assets/feats/math-related/math.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

ตอนที่ 2 ในการแก้ สมการ Diophantine BQDEs ซึ่งจะพูดถึงวิธีการแก้ในกรณี Elliptical case และ Parabolic case (= 3=)//
<!--more-->

กลับมาต่อในตอนที่ 2 สำหรับการแก้สมการ diophantine ของสมการ

$$ Ax^{2}+Bxy+Cy^{2}+Dx+Ey+F = 0 $$


หลังจากค้นๆข้อมูลเพิ่มเติม /me พึ่งรู้ทีหลังว่า เจ้าสมการที่เรากำลังพูดถึงกันอยู่นี้ มันมีชื่อทางการว่า Binary Quadratic Diophantine Equations หรือ BQDEs ซึ่งเป็นเรื่องราวที่ค่อนข้างจะเป็น pure mathematics มากๆ ส่วนตัว /me ก็ไม่ทราบว่าเรื่องพวกนี้จะไปประยุกต์ใช้กับเรื่องอะไรบ้าง เท่าที่ค้นๆมา เรามีการประยุกต์ใช้ Diophantine Equation ค่อนข้างมากในวิชาเกี่ยวกับเคมี นอกจากนี้ Diophantine Equation ยังเป็นส่วนสำคัญที่ทำให้เราเข้าใจพฤติกรรมของ curve แบบต่างๆได้

# ความเดิมตอนที่แล้ว

[ตอนที่ 1](https://chameleontk.github.io/diophantine-equation-i) /me ได้พูดถึงวิธีการหาคำตอบที่เป็นจำนวนเต็มของ BQDEs สำหรับกรณี Linear case และ Simple hyperbolic case ไปแล้ว เรามาเริ่มกันต่อที่กรณีต่อไปกันเลยดีกว่า

# Elliptical case

สำหรับกรณีนี้ เกิดจากกรณีที่ $$ B^2-4AC < 0 $$ กราฟของสมการที่เราสนใจจะอยู่ในรูปของวงรีซึ่งหมายความว่า ค่าที่เป็นจำนวนเต็มที่เป็นไปได้ จะจำกัดอยู่ในช่วงของ x ที่อยู่ระหว่าขั้วทั้ง 2 ข้างของวงรี ดังนั้นเป้าหมายของการปรับแต่งสมการ คือ การหาว่า x ที่เป็นขั้วทั้ง 2 อยู่ที่ตำแหน่งอะไร?

$$
Ax^{2}+Bxy+Cy^{2}+Dx+Ey+F = 0\\\\
Cy^{2}+(Bx+E)y+(Ax^{2}+Dx+F) = 0\\\\
y = \frac{-(Bx+E)\pm\sqrt{(Bx+E)^2-4C(Ax^{2}+Dx+F)}}{2C}\\\\
$$

//บรรทัดสุดท้าย คือ มองให้เป็นสมการกำลังสอง แล้วแทน "y = ลบบีบวกลบรูทบีกำลังสองลบสีเอซีส่วนสองเอ" <span class="tag-en">#ทำเสียงเหมือนตอนกำลังท่องให้คุณครูฟัง</span> เผื่อใครลืม

จากผลเฉลยที่ได้ จะพบว่า ทุกๆจุด x จะให้ค่า y สองค่า คือ ส่วนที่ + รากที่ 2 และส่วนที่เป็น - รากที่ 2 
ยกเว้นจุดเดียวที่ให้ค่า y เพียงค่าเดียวก็คือ จุดที่เป็นจุดวกกลับหรือจุดขั้วนั้นเอง ซึ่งเกิดจาก $$ 
\sqrt{(Bx+E)^2-4C(Ax^{2}+Dx+F)} = 0 $$

ดังนั้น ค่า x ที่เป็นคำตอบที่เป็นจำนวนเต็ม จะต้องอยู่ในช่วงที่ได้จากผลเฉลยของสมการ

$$ (Bx+E)^2-4C(Ax^{2}+Dx+F) = 0  $$


หรือ

$$ (B^2-4AC)x^2+2(BE-2CD)x+(E2-4CF) = 0  $$


ถ้าไม่มีจุด x ใดๆ ในช่วงนี้ให้ค่า y ที่เป็นจำนวนเต็ม แล้ว สมการ diophantine นั้นก็จะไม่มีผลเฉลย **Q.E.D.**


# Parabolic case


ในกรณีนี้เกิดจาก $$ B^2-4AC = 0 $$

ก่อนอื่น กำหนด g = gcd(A,C) แล้วให้ a = A/g, b = B/g และ c = G/g เพื่อทำให้สมการของเราดูง่ายยิ่งขึ้น สำหรับบางคนอาจจะสงสัยว่า b จะได้ยังคงเป็นจำนวนเต็มรึปล่าว คำตอบคือ b จะต้องเป็นจำนวนเต็มแน่นอน เพราะ

$$
B^2 = 4AC\\\\

$$

* ถ้า g สามารถหาร A และ C ลงตัวแล้ว g ก็จะต้องหาร B ลงตัวด้วยเหมือนกัน

* $$ B^2$$ เป็นจำนวนบวก ทำให้ AC จะต้องเป็นจำนวนบวกเช่นกัน
* A และ C จะต้องเป็นจำนวนเต็มที่มีเครื่องหมายเหมือนกัน (บวกทั้งคู่ หรือ ลบทั้งคู่)
* ถ้าเลือก g ที่มีเครื่องเหมือนเหมือนกับ A แล้ว a และ c จะได้เป็นบวกเสมอ

* จาก $$ b^2=(2^2)ac$$ และ $$ gcd(a,c) = 1$$ ดังนั้น a และ c จะต้องเป็น perfect square เสมอ

* หรือพูดอีกอย่างหนึ่ง คือ เราสามารถแทน $$ a = p^2, c = q^2$$ โดยที่ p,q เป็นจำนวนเต็ม

หลังจากที่เราศึกษาเอกลักษณ์ของกรณีนี้กันแล้ว ก็ถึงเวลาแล้วที่จะมาหาคำตอบของสมการ

$$
Ax^{2}+Bxy+Cy^{2}+Dx+Ey+F = 0\\\\
(ag)x^{2}+(bg)xy+(cg)y^{2}+Dx+Ey+F = 0\\\\
g((\sqrt{a}x)^{2}+(2\sqrt{a}\sqrt{c})xy+(\sqrt{c}y)^{2})+Dx+Ey+F = 0\\\\
g(\sqrt{a}x+\sqrt{c}y)^{2}+Dx+Ey+F = 0\\\\
\sqrt{a}g(\sqrt{a}x+\sqrt{c}y)^{2}+\sqrt{a}Dx+\sqrt{a}Ey+\sqrt{a}F = 0\\\\
\sqrt{a}g(\sqrt{a}x+\sqrt{c}y)^{2}+\sqrt{a}Dx+\sqrt{a}Ey+\sqrt{a}F + (\sqrt{c}Dy-\sqrt{c}Dy)= 0\\\\
\sqrt{a}g(\sqrt{a}x+\sqrt{c}y)^{2}+D(\sqrt{a}x+\sqrt{c}y)+(\sqrt{a}E-\sqrt{c}D)y+\sqrt{a}F= 0\\\\

$$



แทน $$ u=\sqrt{a}x+\sqrt{c}y$$

$$
\sqrt{a}g(u)^{2}+D(u)+(\sqrt{a}E-\sqrt{c}D)y+\sqrt{a}F= 0\\\\
\sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F = (\sqrt{c}D-\sqrt{a}E)y \\\\

$$



จากการแทนค่า $$ u=\sqrt{a}x+\sqrt{c}y$$


อย่าลืม property ที่สำคัญ คือ **"u เป็นจำนวนเต็ม ก็ต่อเมื่อ x,y เป็นจำนวนเต็ม"** เพราะ สัมประสิทธิ์ $$ 
\sqrt{a}, \sqrt{c}$$ เป็นจำนวนเต็ม ตามคุณสมบัติปิดการบวก และการคูณ ดังนั้น u จึงต้องเป็นจำนวนเต็ม

จากสมการที่เราจัดรูปกันมาแล้ว เราจะมาพิจารณาแยกเป็น 2 กรณี คือ

1. กรณี $$ (\sqrt{c}D-\sqrt{a}E) = 0 $$ หรือก็คือ

$$
\sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F = 0

$$



จะเห็นว่า เราสามารถหาคำตอบของสมการตัวแปร u ได้ทันที โดยกำหนดให้ คำตอบจากสมการตัวแปร u คือ $$ u_1, 
u_2 $$ แล้วแทนค่ากลับลงในสมการเดิม

$$
\sqrt{a}x+\sqrt{c}y = u_1,
\sqrt{a}x+\sqrt{c}y = u_2

$$


สมการทั้ง 2 ต่างอยู่ในรูป linear case ซึ่งเราสามารถแก้มันได้ โดยใช้วิธีการที่พูดถีงไปแล้วใน [ตอนที่ 1](https://chameleontk.github.io/diophantine-equation-i) <span class="tag-en">#ไม่เสียแรงที่ร่ำเรียน</span>

2. กรณี $$ (\sqrt{c}D-\sqrt{a}E) \neq 0 $$

เมื่อพิจารณาสมการ

$$
\sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F = (\sqrt{c}D-\sqrt{a}E)y \\\\

$$



เราสามารถพูดอีกแบบได้ว่า $$ \sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F $$ เป็นตัว y เท่าของ $$ (\sqrt{c}D-\sqrt
{a}E) $$


เมื่อกำหนด $$ f(u) = \sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F , M = (\sqrt{c}D-\sqrt{a}E) $$ แล้ว


ถ้า $$ f(u) = k_1(M) $$ แล้ว $$ f(u+M) = k_2(M) $$

เพราะ

$$
f(u+M) = \sqrt{a}g(u+M)^{2}+D(u+M)+\sqrt{a}F\\\\
f(u+M) = \sqrt{a}g(u^2+2uM+M^2)+Du+DM+\sqrt{a}F\\\\
f(u+M) = \sqrt{a}gu^2+\sqrt{a}g2uM+\sqrt{a}gM^2+Du+DM+\sqrt{a}F\\\\
f(u+M) = (\sqrt{a}gu^2+Du+\sqrt{a}F)+M(\sqrt{a}g2u+\sqrt{a}gM+D)\\\\
f(u+M) = f(u)+M(\sqrt{a}g2u+\sqrt{a}gM+D)\\\\

$$



ดังนั้น ถ้า $$ f(u) = k_1(M) $$ แล้ว $$ f(u+M) = k_2(M) $$

เมื่อเป็นเช่นนั้นเราจะสามารถหาคำตอบที่เป็นจำนวนเต็มของสมการ

$$
\sqrt{a}g(u)^{2}+D(u)+\sqrt{a}F = (\sqrt{c}D-\sqrt{a}E)y \\\\

$$



โดยทดสอบแค่เฉพาะตัวเลขที่อยู่ในช่วง $$ 0 \leq u_i \leq (\sqrt{c}D-\sqrt{a}E)$$


สำหรับทุกๆ $$ u_i $$ ที่ให้คำตอบที่เป็นจำนวนเต็ม จะให้ $$ u_i+(\sqrt{c}D-\sqrt{a}E)t $$ เป็นคำตอบด้วยเช่นกัน


จากนั้นแทนค่า $$ u_i+(\sqrt{c}D-\sqrt{a}E)t $$ ลงในสมการ

$$ u=\sqrt{a}x+\sqrt{c}y$$

เราก็จะได้คำตอบที่เป็นจำนวนเต็มทุกตัวของสมการ **Q.E.D.**

# กราบขอขอบคุณ
[Dario Alpern's Generic Two integer variable equation solver](https://www.alpertron.com.ar/JQUAD.HTM)

PS. จากเดิม /me คิดว่า จะเขียนบทความสั้นๆไม่ยาวมาก จากเดิมที่คาดว่าจะเขียนแค่ 2 ตอน ดูเหมือนว่าจะเปลี่ยนเป็น 4 ตอนซะแล้วซิ ฝากติดตามด้วยนะฮะ
