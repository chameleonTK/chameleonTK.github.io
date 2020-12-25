---
layout: post
title: "How to solve diophantine equation IV : Ax2 + Bxy + Cy2 + Dx + Ey + F = 0"
tags: [Archive, Mathematics]
thumbnail: "assets/img/math-related/math.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR


<!--more-->

* สรุป idea การใช้ even/odd ในกรณี +-1
http://mathworld.wolfram.com/PellEquation.html

อ่าน
พิสูจน์เรื่อง continue fraction
http://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf

* สรุปไอเดีย ขั้นตอนการคำนวนอย่างเป็นระบบ
Solving the generalized Pell equation x2 − Dy2 = N

{\displaystyle x_{k}+y_{k}{\sqrt {n}}=(x_{1}+y_{1}{\sqrt {n}})^{k},}

\displaystyle x_{k+1} = x_1 x_k + n y_1 y_k,
{\displaystyle \displaystyle y_{k+1}=x_{1}y_{k}+y_{1}x_{k}.} \displaystyle y_{k+1} = x_1 y_k + y_1 x_k.

* brute-force
* LMM
-> +-1
-> behavoir fundemantal solution
-> D^2 < N -> D^2 > N // reduce