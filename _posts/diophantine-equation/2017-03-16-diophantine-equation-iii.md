---
layout: post
title: "How to solve diophantine equation III : Ax2 + Bxy + Cy2 + Dx + Ey + F = 0"
tags: [Archive, Mathematics]
thumbnail: "assets/feats/math-related/math.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR

ตอนนี้ก็เป็น ตอนที่ 3 สำหรับระเบียบวิธีการแก้สมการ  BQDEs รอบนี้คือ ลุยกับกรณีสุดท้าย Hyperbolic case ซึ่งเกี่ยวข้องกับการทำ Linear Tranform และ Pell's Equation
<!--more-->

ตอนนี้ก็เป็น ตอนที่ 3 สำหรับระเบียบวิธีการแก้สมการ

$$ Ax^{2}+Bxy+Cy^{2}+Dx+Ey+F = 0 $$


หรือ เรียกสั้นๆว่า BQDEs ซึ่งอธิบายไปแล้วในหลายๆตอน

[ตอนที่ 1](http://wp.curve.in.th/diophantine-equation-i) พูดถึงลักษณะของสมการ Diophantine Equations และพูดถึงวิธีการแก้สมการ BQDEs ในกรณี Linear case และ Simple hyperbolic case

[ตอนที่ 2](http://wp.curve.in.th/diophantine-equation-ii) ต่อกับการแก้ BQDEs ในกรณี Elliptical case และ Parabolic case

และ ตอนนี้ก็ถึงกรณีสุดท้าย และเป็นกรณีที่ซับซ้อนที่สุดของ BQDEs ซึ่งเรียกว่า Hyperbolic case

# Hyperbolic case

เกิดจากกรณีที่ $$ B^2-4AC > 0 $$ หรือ เรียกอย่างเป็นทางการว่า เป็นกรณีที่มี discriminant $$ \triangle > 0 $$

เตรียมตัว เตรียมใจ ลุย!

ในกรณี Hyperbolic case เราจะพิจารณาแยกอีกเป็น 2 กรณี คือ

#### สำหรับกรณี $$ \triangle = k^2$$


โดยที่ k เป็นจำนวนเต็มใดๆ ซึ่งถ้าเกิดจาก $$ A = C = 0$$ ก็จะต้องย้อนกลับไปดูวิธีการแก้ในกรณี Simple hyperbolic case ที่อธิบายไปแล้วใน ตอนที่ 1

แต่อาจจะเกิดจากกรณี $$ A = 0$$ หรือ $$ C = 0$$ แค่ตัวใดตัวหนึ่งก็ได้

$$
Ax^{2} + Bxy + Cy^2 + Dx + Ey + F = 0\\\\
4AAx^{2} + 4ABxy + 4ACy^2 4ADx + 4AEy + 4AF = 0\\\\
((2Ax)^{2} + 2(2Ax)By + (By)^2) - (By)^2 + 4ACy^2 + 4ADx + 4AEy + 4AF = 0\\\\
(2Ax+By)^2 - (B^2 - 4AC)y^2 + 4ADx + 4AEy + 4AF = 0\\\\
$$


แต่เนื่องจาก เราพิจารณา กรณีที่ $$ B^2-4AC = k^2 $$

$$
((2Ax+By)^2 - (ky)^2) + 4ADx + 4AEy + 4AF = 0\\\\
(2Ax+By-ky)(2Ax+By+ky) + 4ADx + 4AEy + 4AF = 0\\\\
$$

ถ้าแทน

$$
s = 2Ax+By+ky\\\\
t=2Ax+BY-ky\\\\
$$


หรือ พูดอีกอย่างคือ

$$
x = \frac{Bt+ks+kt-Bs}{4Ak},\\\\
y = \frac{s-t}{2k}\\\\
$$


เมื่อแทนค่า x, y ด้วย s, t แล้ว จะสามารถจัดสมการใหม่ให้อยู่ในรูป

$$ B'st+D's+E't+F' = 0 $$


แล้วกลับไปแก้ด้วยวิธีเดียวกับกรณี Simple hyperbolic case

แต่อย่างไรก็ตาม คำถามสำคัญคือ หลังจากที่เราเปลี่ยน x, y ด้วย s, t ทุกๆคำตอบ (s, t) จะให้ (x, y) ที่เป็นจำนวนเต็มเสมอ หรือไม่?

STEP ต่อมา จึงต้องตรวจทุกๆคำตอบ (s,t) สำหรับกรณีที่ (s,t) มีจำนวนจำกัด N ตัว เราก็สามารถเช็คทีละคำตอบได้เลยทันที แต่สำหรับกรณีที่ (s,t) มีคำตอบไม่จำกัด เราจะแบ่งคำตอบที่ได้เป็นกลุ่มๆ ทั้งหมด 4Ak กลุ่มโดย กลุ่มที่ i คือ กลุ่มที่ $$ s \equiv i \mod{4Ak}$$ โดยให้ i ตั้งแต่ 0 ถึง 4Ak-1

หรือ พูดอีกอย่างคือ การแบ่งกลุ่มจากเศษจากการหาร s ด้วย 4Ak



> พิจารณา $$ (s_{1}, t_{1}) $$ และ $$ (s_{2}, t_{2}) $$ ที่เป็นคำตอบที่เป็นจำนวนเต็มของสมการ $$ B'st+D's+E't+F' = 0$$ โดย $$ s_{1} \equiv s_{2} \mod{4Ak}$$ ($$ s_{1}$$ และ $$ s_{2}$$ หาร 4Ak แล้วเหลือเศษเท่ากัน)

> **Claim :** ถ้า $$ (s_{1}, t_{1})$$ ให้คำตอบ $$ (x_{1}, y_{1}) $$ ที่เป็นจำนวนเต็ม แล้ว $$ (s_{2}, t_{2})$$ ให้คำตอบ $$ (x_{2}, y_{2}) $$เป็นจำนวนเต็มเช่นกัน ... ยังไม่มีไอเดียสำหรับการพิสูจน์อันนี้




ดังนั้นหากเลือกตัวแทนจากแต่ละกลุ่มเพื่อเช็คคำตอบ ถ้าตัวแทนจากกลุ่มนั้นสามารถให้ (x,y) เป็นจำนวนเต็มได้ แสดงว่าทุกๆ (s,t) ในกลุ่มนั้น สามารถสร้างคำตอบที่ของสมการ diophantine ได้นั้นเอง

#### สำหรับกรณี $$ \triangle \neq k^2$$


สำหรับกรณีนี้ มีวิธีการแก้ปัญหาได้หลากหลายวิธี แต่กระบวนการสำคัญของการแก้ปัญหา คือ การแปลงสมการ

$$ Ax^{2}+Bxy+Cy^{2}+Dx+Ey+F = 0 $$


ไปเป็นสมการในรูปแบบที่เรารู้วิธีการแก้อยู่แล้ว โดยทั่วไปแล้ว 2 สมการสำคัญที่มักพูดถึงกันบ่อยๆ คือ

$$ Ax^{2}+Bxy+Cy^{2} = N $$


เรียกอีกชื่อหนึ่งว่า binary quadratic form แต่เราจะไม่พูดถึงวิธีการแก้สมการนี้นะ อีก 1 สมการสำคัญคือ

$$ x^{2}-Dy^{2} = N $$


หรือ เรียกสมการนี้ว่า Pell's Equation ซึ่งมีนักคณิตศาสตร์หลายๆท่านศึกษา และแก้สมการนี้มาตั้งแต่ศตวรรษที่ 11 และมีการเสนอระเบียบวิธีแก้มาเยอะมากๆ โดยวิธีแก้ที่ /me อ้างถึง เป็นวิธีการที่ใช้เครื่องมือที่ชื่อว่า continued fractions ซึ่งเรียบเรียงโดย Joseph-Louis Lagrange ในช่วงศตวรรษที่ 17

ซึ่งการเปลี่ยนแปลงสมการยุ่งๆอันนี้ ไปเป็นรูปแบบที่เราต้องการ เรียกกระบวนการนี้ว่า Linear Tranformation

## Linear Tranformation

คือ การพยายามลดความซับซ้อนของสมการโดยใช้การบวก และการคูณ หรือก็คือ การแทน x, y ให้อยู่ในรูป

$$
x = rX + sY + v\\\\
y = tX + uY + w\\\\
$$


โดยมี r, s, t, u, v, w เป็นจำนวนตรรกยะ โดยสามารแทนให้อยู่ในรูปแบบ Matrix ดังนี้

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}r & s \\t & u \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix} + \begin{bmatrix}v \\w \end{bmatrix}
$$


หรือ

$$
\left(\begin{array}{c}x\\ y\end{array}\right) = P \left(\begin{array}{c}X\\ Y\end{array}\right) + Q
$$


แต่อย่างไรก็ตาม r, s, t, u, v, w ที่ได้ อาจจะไม่ใช่ จำนวนเต็ม อย่างที่เราคาดหวัง แปลว่า คำตอบที่เป็นจำนวนเต็ม (X, Y) อาจจะให้คำตอบ (x, y) ที่ไม่เป็นจำนวนเต็ม ดังนั้นจะต้องมีเงื่อนไขเพื่อเช็คทุกๆคำตอบจาก (X, Y) อีกที

ในที่นี้ /me จะแสดงวิธีการแปลงไปสู่ Pell's Equation แล้วเราก็จะจบด้วยการแก้ปัญหา Pell's Equation และเช็คทุกๆคำตอบ

ปล. ใครอ่านมาถึงตรงนี้ อยากจะขอแสดงความยินดีที่จะบอกว่า ทุกๆกรณีที่พูดถึงไปแล้ว สามารถแปลงเป็น Pell's Equation ได้หมดเลย ดังนั้น เราจึงไม่จำเป็นต้องแก้ BQDEs กันอย่างจริงๆจังๆก็ได้ :)

## STEP 1 : Make A and C not Zero

แปลง $$ A=0 $$ หรือ $$ C=0 $$ ให้อยู่ในรูปที่ $$ A \neq 0 $$ และ $$ C \neq 0 $$

#### กรณี A=0 และ C=0 เราจะแทน P, Q ในรูปแบบดังนี้

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & 1 \\1 & 2 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$

หรือ

$$
x = X + Y\\\\
y = X + 2Y\\\\
$$

ซึ่งจะได้

$$
(0)x^{2}+Bxy+(0)y^{2}+Dx+Ey+F = 0\\\\
B(X+Y)(X+2Y)+D(X+Y)+E(X+2Y)+F = 0\\\\
BX^2+3BXY+2BY^2+(D+E)X+(D+2E)Y+F = 0\\\\
$$

//สำหรับกรณีอื่นๆ จะไม่แทนค่าให้ดูละนะ

#### กรณี A=0 อย่างเดียว เราจะแทน P, Q ในรูปแบบดังนี้

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & 0 \\1 & 1 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$

หรือ

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & 0 \\-1 & 1 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$

#### กรณี C=0 อย่างเดียว ให้เปลี่ยน x เป็น y และ y เป็น x แล้วกลับไปที่กรณี A=0

## STEP 2 : Make B Zero


เราจะแทน $$ x=pX+qY $$ เพื่อทำให้เกิดพจน์ $$ XY $$ จาก พจน์ $$ x^2 $$ ซึ่งจะไปหักล้างกันพอดีกับ $$ XY $$ ที่มาจากพจน์ $$ xy $$ แต่ยังคงใช้ $$ Y $$ ตัวเดิม

ดังนั้น

$$
Ax^{2}+Bxy+By^{2}+Dx+Ey+F = 0\\\\
A(pX+qY)^{2}+B(pX+qY)Y+BY^{2}+D(pX+qY)+EY+F = 0\\\\
Ap^2X^2 + 2pqAXY +q^2AY^2+pBXY+qBY^2+BY^{2}+ ... = 0\\\\
$$


พิจารณา

$$
2pqA + pB = 0\\\\
q = \frac{-B}{2A}
$$


โดย p เป็นอะไรก็ได้ แต่ต้องเป็นจำนวนตรรกยะ เพื่อให้ได้คำตอบที่เป็นจำนวนเต็ม ดังนั้น Tranform Matrix ก็คือ

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & \frac{-B}{2A} \\0 & 1 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$


จากนั้น คูณสมการที่ได้ด้วยจำนวนเต็ม(สักค่า)เพื่อปรับให้สัมประสิทธิ์ทุกตัวเป็นจำนวนเต็ม

หลังจากการ tranform จะพบว่า discriminant $$ \triangle' = k^2 \triangle $$ หรือ discriminant มีค่าเพิ่มขึ้น $$ k^2$$ เท่า (k อาจจะเป็นเศษส่วนก็ได้นะ) ดังนั้น จึงไม่ต้องหวังว่า tranform แล้ว เราจะไม่ต้องไปแก้ Pell's Equation เพราะ มันไม่ได้เปลี่ยน case

## STEP 3 : Make C, D Zero


ขั้นตอนนี้จะคล้ายๆกับ STEP 2 โดย

เราจะแทน $$ x=pX+q $$ เพื่อทำให้เกิดพจน์ $$ X $$ จาก พจน์ $$ x^2 $$ ซึ่งจะไปหักล้างกันพอดีกับ $$ X $$ ที่มาจากพจน์ $$ x $$ เดิม และทำนองเดียวกับ ก็เปลี่ยน $$ y=rY+s $$ ด้วยเช่นกัน

พิจารณาทีละกรณี เริ่มจาก $$ x=pX+q $$

$$
Ax^{2}+Dx+... = 0\\\\
A(pX+q)^{2}+D(pX+q)+... = 0\\\\
A(p^2X^2+2pqX+q^2)+pDX+qD+... = 0\\\\
p^2AX^2+2pqAX+pDX+... = 0\\\\
$$


พิจารณา

$$
2pqA + pD = 0
q = \frac{-D}{2A}
$$


และทำนองเดียวกัน จะได้ว่า $$ s= \frac{-E}{2B} $$ โดน p, r เป็นค่าคงที่อะไรก็ได้ และได้ Tranform matrix คือ

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & 0 \\0 & 1 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix} + \begin{bmatrix}\frac{-D}{2A} \\\frac{-E}{2B} \end{bmatrix}
$$

## STEP 4 : Reduce Coefficient

หลังจากผ่านมาหลายขั้นตอน เราควรจะได้สมการในรูป
$$ Ax^2+Cy^2+F=0 $$


โดยที่ A และ C มากกว่า 0 และสามารถปรับให้ gcd(A, C, F) = 1 จะพบว่า

* ถ้า gcd(A, C) = k แล้ว k จะต้องหาร F ลงตัว ถ้า k ไม่สามารถหาร F ลงตัวแล้ว สมการนี้จะไม่มีคำตอบที่เป็นจำนวนเต็ม

* ถ้า gcd(A, F) = p ที่ p > 1 แล้ว กำหนดให้ A=pa และ F = pf จะได้ว่า

$$
pax^2+Cy^2+pf=0\\\\
$$


แต่ p ไม่เป็นตัวประกอบของ C เพราะว่า gcd(A, C) = 1 และ gcd(F, C) = 1 เพราะว่า gcd(A, C, F) = 1 ดังนั้น p จะต้องเป็นตัวประกอบของ y

สามารถแทน y = pY หรือ

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}1 & 0 \\0 & p \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$

* ถ้า gcd(C, F) = p ที่ p > 1 แล้ว กำหนดให้ C=pc และ F = pf แล้วทำในทำนองเดียวกัน
* ถ้า $$ a \equiv b \equiv 1 (mod 2)$$ (a และ c เป็นเลขคี่), $$ a \equiv b (mod 4)$$ และ $$ f \equiv 0 (mod 4)$$ แล้ว จะสามารถ tranform

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}2 & 0 \\0 & 2 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$


มาจากคุณสมบัติเลขคู่คี่ //ลองนึกดูดีๆ

และทั้ง 3 กรณีนี้สามารถทำวนไปเรื่อยๆจนกว่าจะได้ A, C และ F ที่น้อยที่สุด เพื่อลุยในขั้นตอนสุดท้าย

## STEP 5 : Form Pell's Equation


คูณทั้งสมการ ด้วย A

$$
Ax^2+Cy^2+F=0\\\\
(Ax)^2+ACy^2+AF=0\\\\
$$


แล้วแทน x = AX, D = -AC และ N = -AF

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}A & 0 \\0 & 1 \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix}
$$

จะได้สมการหน้าตาดุลดั่ง Pell's Equation สมใจ

$$ x^{2}-Dy^{2} = N $$


ปล. แต่อย่างไรก็ตาม ยังมี Tranform Matrix ที่ใช้ค่าต่างออกไป แต่ยังคงสามารถเปลี่ยน BQDEs ให้เป็น Pell's Equation ได้เหมือนกัน และอาจจะให้ค่า D ที่เล็กกว่าวิธีการนี้ เพราะยิ่ง D มีค่าเล็กๆ จะยิ่งสามารถแก้ Pell's Equation ได้ง่ายขึ้น

## Recovering solutions

จาก Linear Tranform เราเลี่ยงไม่ได้ที่จะใช้การหาร ซึ่งมันทำให้เกิดการเปลี่ยนแปลงคำตอบบางส่วนจากจำนวนเต็มไปเป็นเศษส่วน หรือ พูดอีกอย่างคือ

<div class="blockquote">คำตอบที่เป็นจำนวนเต็มจาก Pell's Equation ที่เราแปลงไป อาจจะไม่ให้คำตอบที่เป็นจำนวนเต็มสำหรับ BQDEs </div>

แต่อย่างไรก็ตาม เราสามารถรับประกันได้ว่า ไม่มีคำตอบไหนที่เป็นคำตอบใน BQDEs แต่ไม่เป็นคำตอบใน Pell's Equation จากการแปลง

สังเกตว่า ทุกๆครั้งที่เกิดการแปลง /me จะกำกับไว้ด้วย Tranform matrix เพราะว่า ถ้าไม่มี Tranform matrix มันจะยากมาก หากพิจารณาการแปลงหลายๆครั้ง มันจะทำให้เราสับสนว่าจะจะแปลง x, y ตั้งต้นให้กลายเป็น X, Y ในสมการสุดท้ายได้อย่างไร

พิจารณา การแปลง x ไปเป็น x' และ x' ไปเป็น x''

$$
\left(\begin{array}{c}x\\ y\end{array}\right) = P_1 \left(\begin{array}{c}x'\\ y'\end{array}\right) + Q_1
$$

$$
\left(\begin{array}{c}x'\\ y'\end{array}\right) = P_2 \left(\begin{array}{c}x''\\ y''\end{array}\right) + Q_2
$$


สามารถแทน $$ \left(\begin{array}{c}x'\\ y'\end{array}\right)$$ ลงในสมการแรก จะได้ว่า

$$
\left(\begin{array}{c}x\\ y\end{array}\right) = P_1(P_2 \left(\begin{array}{c}x''\\ y''\end{array}\right) + Q_2) + Q_1\\\\

\left(\begin{array}{c}x\\ y\end{array}\right) = P\left(\begin{array}{c}x''\\ y''\end{array}\right) + Q\\\\
$$


โดย P, Q จะเป็น Matrix สุดท้าย หรือ ก็คือ จริงๆแล้วการแปลงหลายๆขั้นของเรา สามารถรวมกันเป็นการแปลงแค่ขั้นเดียวได้เลย <span class="tag-en">#สุดยอดไปเลยลูกเพ่</span>

พิจารณา

$$
\begin{bmatrix}x \\y \end{bmatrix} = \begin{bmatrix}r & s \\t & u \end{bmatrix} \begin{bmatrix}X \\Y \end{bmatrix} + \begin{bmatrix}v \\w \end{bmatrix}
$$

* สำหรับกรณีที่ ได้ (X, Y) เป็นแค่ไม่กี่ค่า(finitely many solutions) เราสามารถแทนค่าทั้งหมด เพื่อเช็ค (x, y) ได้
* สำหรับกรณีที่ r, s, t, u, v และ w เป็นจำนวนเต็มทั้งหมด ก็สามารถรับประกันได้เลยว่า (x, y) ต้องเป็นจำนวนเต็มเสมอ ถ้าได้ (X, Y) เป็นจำนวนเต็ม

แต่สำหรับกรณีนอกเหนือจากนี้ ก็ต้องทดสอบกันไป แต่อย่างไรก็ตาม /me จะไม่เขียนละเอียด เพราะว่า /me ก็ไม่เข้าใจเหมือนกัน LOL //อ่านเพิ่มเติมได้จากเครดิตที่ให้ไว้

ความจริงต้องมีการพิสูจน์เพิ่มเติมว่า ทุกๆคำตอบที่เป็นจำนวนเต็มใน BQDEs จะได้คำตอบที่เป็นจำนวนเต็มใน Pell's Equation จากการแปลง

ติดตามกันใหม่ตอนหน้า สำหรับการแก้ Pell's Equation และบทสรุปของการแก้สมการ BQDEs

# กราบขอขอบคุณ
* [Dario Alpern's Generic Two integer variable equation solver](https://www.alpertron.com.ar/JQUAD.HTM)

* John P. Robertson, Solving the equation ax2 +bxy+cy2 +dx+ey+f =0, 2013.
* John P. Robertson, Solving the generalized Pell equation x2 − Dy2 = N, 2013.
* Evan Dummit, Number Theory (part 6): Continued Fractions and Diophantine Equations, 2014.