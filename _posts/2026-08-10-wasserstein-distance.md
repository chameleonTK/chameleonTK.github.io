---
layout: post
title: "Wasserstein Distance" 
tags: [Archive, Mathematics]
thumbnail: "assets/feats/math-related/wasserstein.jpg"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(83 171 222)
jquery: true
encrypt: true
---

<style>
    .inline-figure .katex-display {
        display: inline-block;
        margin: auto;
    }

    .inline-figure .katex-display > .katex > .katex-html {
        width: auto;
    }

    .littlefoot__content .katex-display {
        display: inline-block;
        margin: auto;
    }

    .littlefoot__content .katex-display > .katex > .katex-html {
        width: auto;
    }

    .language-python.highlighter-rouge{
        max-height: 450px;
        overflow: scroll;
    }

    .katex-display > .katex > .katex-html {
        /* width: auto; */
        width: 800px;
    }

    button.littlefoot__button {
        padding: 0px 5px;
    }
</style>

Wasserstein Distance หรือ Earth Mover’s Distance เป็นหนึ่งในหัวข้อที่ /me เจอในสมัยเรียนโท เพราะ ได้เขียนธีสิสเกี่ยวกับ GAN และ WGAN แต่จบมาแล้วหลายปี ก็ยังไม่เข้าใจว่า มันคำนวนยังไง?? ในที่สุดก็พอมีเวลาได้อ่านคำอธิบายจริงๆจังๆ เลยรู้สึกว่า น่าจะถือโอกาสนี้ เขียนสรุปสิ่งที่ได้เรียนรู้ไปด้วยเลย
<!--more-->

ก่อนอื่น ต้องขอขอบคุณแหล่งข้อมูลสำคัญสำหรับบล๊อคนี้ [Wasserstein GAN and the Kantorovich-Rubinstein Duality](https://vincentherrmann.github.io/blog/wasserstein/) จาก Prof. Vincent Herrmann 

ถ้าใครอยากอ่านรายละเอียดเพิ่มเติม สามารถตามไปอ่านที่ original post ได้เลยคับ

<hr>

## GAN & WGAN

ก่อนอื่นอยากจะทบทวนกันก่อนว่า ทำไมเราจึงจำเป็นต้องรู้จัก Wasserstein Distance (อ่านว่า /วอส-เซอร์-สไตน์/ อ่านยากพอๆกับ Worcestershire sauce)


ที่ Wasserstein Distance ถูกยกขึ้นมาพูดถึง ส่วนนึงเพราะเปเปอร์ [Wasserstein GAN](https://arxiv.org/abs/1701.07875) ซึ่งต่อยอดโมเดล GAN ให้มีประสิทธิภาพมากขึ้น 

โดยเจ้า GAN ที่ว่า มีชื่อเต็มๆว่า **G**enerative **A**dversarial **N**etwork เป็นโมเดลตระกูล Generative Models หรือ โมเดลที่ใช้ในการสร้างสรรค์ภาพ (ในช่วงแรกๆ จำกัดอยู่แค่ ภาพ ที่หลังๆมีการขยายไปสร้างสรรค์ข้อมูลอื่นๆอีกหลายๆประเภท)

โดยหลักการของ GAN คือ การเทรนโมเดลขึ้นมา 2 ตัว Ganerator (ผู้สร้าง) และ Discriminator (ผู้แยกแยะ) และให้โมเดลทั้ง 2 ตัวนี้แข่งกันเอง โดยตัว Ganerator จะพยายามสร้างข้อมูลปลอมๆขึ้นมาให้มีลักษณะคล้ายกับข้อมูลจริงให้ได้มากที่สุด และ Discriminator จะรับข้อมูลจริง + ข้อมูลปลอมๆที่ Generator สร้างขึ้นมา แล้วพยายามแยกให้ออกว่า ข้อมูลไหนเป็นข้อมูลจริง และ ข้อมูลไหนเป็นข้อมูลปลอม

นั้นคือ

* Ganerator จะได้แต้ม เมื่อไรก็ตามที่มันสามารถหลอก Discriminator ได้ 

* กลับกัน Discriminator ก็จะได้แต้ม เมื่อไรก็ตามที่มันสามารถแยกข้อมูลปลอมๆ ของ Ganerator จากข้อมูลจริงๆได้ถูกต้อง

<div class="blockquote">
การเทรน GAN ไม่ต่างจากการเทรน ตำรวจ กับ แสกมเมอร์ โดย แสกมเมอร์ จะพยายามหาวิธีใหม่ๆในการหลอกผู้คน และกลับกัน ตำรวจก็ต้องพยายามศึกษาวิธีการนั้นๆเพื่อหาทางจับแสกมเมอร์ วนๆไป
</div>

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1m-oxwWaVaIrLbH8J-hNi1c9b4t59Jy7j" column=1 %}
</div>

สามารถเขียนเป็นฟังก์ชัน Objective จะได้ว่า

$$ 
\min_{G} \max_{D} \mathbb{E}_{x \sim P_r}[\log D(x)] + \mathbb{E}_{z \sim P_z}[\log (1-D(G(z)))] 
$$

หรือ เขียนอีกแบบได้ว่า

$$ 
\min_{G} \max_{D} \mathbb{E}_{x \sim P_r}[\log D(x)] + \mathbb{E}_{x' \sim P_g}[\log (1-D(x'))] 
$$

โดย 
* $$G$$ แทน Generator
* $$D$$ แทน Discriminator
* $$P_r$$ และ $$P_g$$ แทน Probability Distribution จากข้อมูลจริง และ จากข้อมูลปลอมๆที่สร้างโดย Generator
* $$P_z$$ แทน Probability Distribution จาก Normal Distribution

จุดสำคัญที่น่าสังเกต คือ เจ้า Discriminator ในการเทรน GAN จะต้องแยกแยะว่า $$x$$ และ $$x'$$ เป็นข้อมูลจริง หรือ ปลอม โดยการให้คะแนนความเนียน ที่จะอยู่ในช่วง [0, 1] เพื่อใช้เป็น signal ให้ Generator เอาไปเรียนรู้ว่าต้องทำอย่างไรเพื่อเลี่ยงการตรวจจับ

ซึ่งสิ่งนี้ทำให้เกิด Dilemma นั้นคือ

* **#1 ถ้า Discriminator ทำตัวแย่มากๆ** จะทำให้ Generator ไม่มี signal ที่ดีมากพอที่จะเรียนรู้ว่า อะไรคือสิ่งที่ Discriminator ใช้ในการตรวจจับ ทำให้ Generator ทำได้แค่สร้างข้อมูลห่วยๆไปเรื่อยๆ

คล้ายๆว่า แทนที่ตำรวจจะตรวจสอบตามหน้าที่ ตำรวจกลับจับแสกมเมอร์แบบสุ่มๆ ถูกบ้างไม่ถูกบ้าง มั่วไปเรื่อย ซึ่งจะทำให้แสกมเมอร์ ก็ไม่รู้ว่าจะต้องทำยังไง เพราะสุดท้ายแล้วก็จะโดยสุ่มจับ ถ้าโชคดีก็สุ่มไม่โดนอยู่ดี 

ถ้าโชคร้ายก็จะโดนจับ //ฟังดูเหมือนจะดี เพราะ แสกมเมอร์ไม่ได้เก่งขึ้น แต่กลับกัน สังคมแบบนี้ก็จะมีคนในสังคมที่โดนหลอกอยู่เรื่อยๆวนๆไป เพราะกำจัดแสกมเมอร์ทั้งหมดไม่ได้ เพราะตำรวจทำได้แค่สุ่มๆไปเรื่อย

* **#2 ถ้า Discriminator ทำตัวเก่งมากๆ** จะทำให้ Generator มี signal เยอะ แต่ปรับ weights ยังไงก็ไม่สามารถหลอก Discriminator ได้สักที สุดท้ายก็เกิด Vanishing gradients เพราะ ไม่รู้ว่าเริ่มต้นปรับ weights ไปทิศทางไหน และในที่สุดก็ยอมแพ้ไป

คล้ายๆว่า สังคมที่มีตำรวจที่เก่งมากๆ ไม่ว่าแสกมเมอร์ จะใช้เทคนิคอะไรก็ตามจับได้หมด จนสุดท้าย แสกมเมอร์ไม่สามารถตั้งตัวได้เลย พยายามทีไรก็โดนจับไปก่อนทุกที //สังคมในฝันที่เราต้องการ แต่ไม่ใช่โมเดลที่เราต้องการ

...

**สิ่งที่เกิดขึ้น** คือ การเทรน GAN จึงเป็นเรื่องที่ challanging มากๆ เพราะมันไม่ใช่แค่เทรนๆไป แต่ถ้า Discriminator และ Generator ไม่สมดุลกัน สุดท้ายก็ไม่สามารถทำให้ได้โมเดลที่ดีขึ้นมาได้ 

//จริงๆแล้ว GAN ยังมีปัญหาอื่นๆอีกหลายๆประเด็น สำหรับใครที่สนใจ สามารถอ่านเพิ่มเติมได้ที่ [From GAN to WGAN](https://lilianweng.github.io/posts/2017-08-20-gan) เลยฮะ

 ...

แนวคิดของ WGAN จึงเกิดขึ้นเพื่อเพิ่ม training stability ของ GAN โดยเปลี่ยนบทบาท _Discriminator_ ด้วย _Critic_

ใน GAN แบบเดิม จะใช้ Discriminator ซึ่งจะรับข้อมูลทีละตัว แล้วจำแนกว่าเป็นข้อมูลนั้น เป็นข้อมูลจริงหรือข้อมูลปลอมที่ Generator สร้างขึ้น

แต่ใน WGAN จะใช้ Critic ซึึ่งไม่ได้มีหน้าที่จำแนกข้อมูลว่า "จริง" หรือ "ปลอม" ทำให้ไม่จำเป็นต้องให้ผลลัพธ์อยู่ระหว่าง 0 ถึง 1 แต่ Critic จะทำหน้าที่ กำหนดคะแนนให้แก่ข้อมูลแต่ละตัว โดยจะพยายามทำให้ ข้อมูลจริงควรได้รับคะแนนสูงกว่าข้อมูลที่ Generator สร้างขึ้น และนำคะแนนเหล่านี้ ไปคำนวน เพื่อตรวจสอบว่า "Probability Distribution จากข้อมูลจริง (หรือ $$P_r$$) มันต่างจาก Probability Distribution จากข้อมูลปลอม  (หรือ $$P_g$$) แค่ไหน??"

โดยถ้า $$P_r$$ และ $$P_g$$ หน้าตาต่างๆกัน / อยู่ห่างๆกัน จะต้องได้ Distance($$P_r$$, $$P_g$$) เป็นค่ามากๆ

แต่ถ้า $$P_r$$ และ $$P_g$$ หน้าตาเหมือนๆกัน + อยู่ใกล้ๆกัน จะต้องได้ Distance($$P_r$$, $$P_g$$) จะต้องมีค่าน้อยๆ 

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1569Kv5yRwOVjJqgv5LWskQzscOE6_ig3" column=1 %}
</div>

ไปๆมาๆ Distance ที่ WGAN ก็คือ Wasserstein Distance นั้นเอง ซึ่งจะนิยามเป็นฟังก์ชัน Objective ได้ดังนี้

$$ 
\min_{G} \max_{\lVert C \lVert _L \le 1} \mathbb{E}_{x \sim P_r}[C(x)] - \mathbb{E}_{x' \sim P_g}[C(x')] 
$$

//คำถาม คือ เจ้าสมการที่ว่านี้ มันมาได้อย่างไร??

---------------

## Wasserstein Distance 

ก่อนที่จะไปทำความเข้าใจฟังก์ชัน Objective ที่ดูยุ่งๆ ของ WGAN 

อยากจะมาทำตอบคำถามที่ง่ายกว่านั้นกันก่อน 

<div class="blockquote">
Wasserstein Distance คืออะไรนะ??
</div>

...

ก่อนอื่นขอมาพูดถึง Distance แบบทั่วๆไปกันก่อน โดยทั่วไปแล้ว Distance คือ วิธีการวัดระยะห่างระหว่างของ 2 อย่าง 

ตัวอย่างที่ทุกๆคนน่าจะรู้จักกันอยู่แล้ว เช่น

$$ 
\tag{\text{Absolute value}} d(a, b) = | a - b |
$$

ซึ่งสามารถมองได้ว่า มันเป็นระยะห่างระหว่างตัวเลข 2 ตัว $$a$$ และ $$b$$ 

$$ 
\tag{\text{Euclidean distance}}  d(a, b) = \sqrt((x_1 - y_1)^2 +  (x_2 - y_2)^2)
$$

ถ้าใครเรียน "ทฤษฎีบทพีทาโกรัส" มาก่อน จะพอรู้ว่า มันคือวิธีที่ใช้ในการวัดระยะระหว่าง 2 จุด บน Cartesian Plane $$a = (x_1, y_1)$$ และ $$b = (x_2, y_2)$$

...

นอกจากนี้ยังมี distance แบบอื่นๆอีก อย่าง Cosine Similarity เป็น Distance สำหรับ Vector หรือ Cross-Entropy ก็อาจจะนับเป็น Distance แบบนึงได้เหมือนกัน สำหรับใช้วัด Distance ระหว่าง Encoding Efficiency สำหรับรูปแบบ Encoder สองแบบ <sup id="fnref:1"><a href="#fn:1">1</a></sup>

...

แล้ว Wasserstein Distance ละ??


Wasserstein Distance ถูกออกแบบมาเป็น Distance สำหรับ Probability Distribution 2 อัน โดยมองว่า Probability Distribution แต่ละก้อน เป็นเหมือนกองทรายกองนึง แล้วตั้งคำถามว่า **"เราต้องทำงานน้อยที่สุดเท่าไรในการย้ายกองทรายกองนึง ไปเป็นอีกกองนึง"**

โดยกำหนด _งาน = ปริมาณทราย x ระยะทาง_

<div class="inline-figure" style="border: 1px solid #eee;padding: 0em 1.2em 0.6em; margin-bottom:1.2em" markdown="1">

#### Example #1
//เพื่อให้เห็นภาพง่ายๆ ขอยกตัวอย่างเป็น Discrete Probability Distribution นะ

กำหนดให้ $$ P_r $$ และ $$ P_g $$ เป็น Discrete Probability Distribution ที่มี $$\Omega = {1,2,3,4}$$ 

โดยมี $$ P_r(x_i) $$ และ $$ P_g(x_i) $$ มีค่าดังนี้

|     |$$P_r(x)$$|$$P_g(x)$$|
|-----|----------|----------|
| x=1 |    0.1   |    0.1   |
| x=2 |    0.4   |    0.5   |
| x=3 |    0.3   |    0.1   |
| x=4 |    0.2   |    0.3   |

</div>

พิจารณา รูปตัวอย่างการย้าย Probability Mass ของ $$ P_r(x=1) $$ ไปที่ $$ P_g(x=4) $$ จำนวน 0.3 หน่วย 

<div class="inline-figure" style="text-align: center;margin-bottom:20px">
{% include aligner.html images="https://lh3.googleusercontent.com/d/1oUCFn0ya5o7AQ_4m_BCeA2v-FWvCS8Kk" column=1 %}
</div>

จะเห็นว่า งานที่เกิดขึ้น = ปริมาณทราย (0.3) x ระยะทาง (2) = 0.6 หน่วย

โดยเราสามารถเขียนออกมาเป็น Matrix ได้ดังนี้

|              | $$P_g(x=1)$$ | $$P_g(x=2)$$ | $$P_g(x=3)$$ | $$P_g(x=4)$$ |
|--------------|--------------|--------------|--------------|--------------|
| $$P_r(x=1)$$ |              |              |              |              |
| $$P_r(x=2)$$ |              |              |              |      0.3     |
| $$P_r(x=3)$$ |              |              |              |              |
| $$P_r(x=4)$$ |              |              |              |              |

เราจะเรียก เจ้า Matrix ที่ว่านี้ว่า "_Transport plan_" หรือ $$\Gamma(x_i, x_j)$$ 

โดยแต่ละค่าใน Matrix แทน Probability Mass ที่ต้องการย้ายจาก $$ P_r(x=x_i) $$ ไปที่ $$ P_g(x=x_j) $$

...

ลองดูตัวอย่าง $$\Gamma(x_i, x_j)$$  ที่เติมจนเต็มแล้ว เช่น

|              | $$P_g(x=1)$$ | $$P_g(x=2)$$ | $$P_g(x=3)$$ | $$P_g(x=4)$$ |
|--------------|--------------|--------------|--------------|--------------|
| $$P_r(x=1)$$ |       -      |      0.1     |       -      |       -      |
| $$P_r(x=2)$$ |       -      |       -      |      0.1     |      0.3     |
| $$P_r(x=3)$$ |       -      |      0.3     |       -      |       -      |
| $$P_r(x=4)$$ |      0.1     |      0.1     |       -      |       -      |

สิ่งที่น่าสนใจ คือ ค่าที่อยู่ใน $$\Gamma(x_i, x_j)$$ ไม่ใช่ค่าอะไรก็ได้ เพราะ $$\Gamma(x_i, x_j)$$ ที่ถูกต้อง จะต้องมีคุณสมติ 2 ข้อ นั้นคือ

$$ \tag{1} \sum_{x_j} \Gamma(x_i, x_j) = P_r(x=x_i) $$

$$ \tag{2} \sum_{x_i} \Gamma(x_i, x_j) = P_g(x=x_j) $$

และ ตัวอย่าง $$\Gamma(x_i, x_j)$$ ด้านบน ก็เป็นไปตามคุณสมบัติ (1) และ (2)

|              | $$P_g(x=1)$$ | $$P_g(x=2)$$ | $$P_g(x=3)$$ | $$P_g(x=4)$$ | $$\sum_{x_j} \Gamma(x_i, x_j)$$ |
|--------------|--------------|--------------|--------------|--------------|--------------|
| $$P_r(x=1)$$ |       -      |      0.1     |       -      |       -      |      0.1     |
| $$P_r(x=2)$$ |       -      |       -      |      0.1     |      0.3     |      0.4     |
| $$P_r(x=3)$$ |       -      |      0.3     |       -      |       -      |      0.3     |
| $$P_r(x=4)$$ |      0.1     |      0.1     |       -      |       -      |      0.2     |
| $$\sum_{x_i} \Gamma(x_i, x_j)$$ |      0.1     |      0.5     |      0.1     |      0.3     |              |

...

และ จาก transport plan เราสามารถนิยาม "งานทั้งหมดของ transport plan $$\Gamma(x_i, x_j)$$" เท่ากับ 

$$ Work(\Gamma) = \sum_{i,j}  \lVert x_i - x_j \lVert \cdot \Gamma(x_i, x_j) $$

ซึ่งสามารถคำนวนได้ดังนี้

$$\begin{array}{rcl}
    Work  & = & 0.1 * (2-1) + 0.1 * (3-2) + 0.3 * (4-2) + 0.3 * (3-2) + 0.1 * (4-1) + 0.1 * (4-2)  \\\\
          & = & 0.1 + 0.1 + 0.6 + 0.3 + 0.3 + 0.2  \\\\
          & = & 1.6
\end{array}$$  

และ Wasserstein Distance คือ $$ Work(\Gamma) $$ ที่น้อยที่สุดที่เป็นไปได้ของทุกๆ Transport plan $$\Gamma$$ ที่เป็นไปได้

ถ้ากำหนดให้ $$\Pi(P_r, P_g)$$ เป็น Transport plan ที่เป็นไปได้ทั้งหมดในการย้าย Probability Mass ระหว่าง $$ P_r $$ และ $$ P_g $$ จะได้ว่า

$$
Wasserstein(P_r, P_g) = \inf_{\Gamma \in \Pi(P_r, P_g)} \sum_{i,j} \lVert x_i - x_j \lVert \cdot \Gamma(x_i, x_j)
$$

<div class="blockquote inline-figure">
แล้วเราจะหา Transport plan ที่ดีที่สุดได้ยังไง??? 
</div>

เพราะถ้า พิจารณาดีๆ จะเห็นว่า Transport plan ที่เป็นไปได้ มีได้ไม่จำกัด (infinitly many) !! 
แต่ ความดีงาม คือ สิ่งนี้สามารถหาคำตอบนี้ได้โดยใช้สิ่งที่เรียกว่า "**Linear Programming**"

----

## Linear Programming

Linear Programming (LP) เป็นปัญหาในกลุ่มปัญหา optimization ซึ่งมีเป้าหมาย คือ _การหาคำตอบที่ให้ cost ที่น้อยที่สุด (หรือ มากที่สุด) <sup id="fnref:2"><a href="#fn:2">2</a></sup> โดยที่คำตอบนั้นๆ ต้องอยู่ภายใต้เงื่อนไขในรูปแบบเชิงเส้น (linear condition) ที่กำหนดไว้_

ถ้าระบุแบบที่จริงจังขึ้นมาหน่อย จะได้ว่า องค์ประกอบของปัญหาใน LP จะต้องประกอบด้วย

1. **Decision variables**: กำหนดให้ $$x$$ เป็นสิ่งที่ต้องการ optimized
2. **Objective function**: มีเป้าหมายเป็นสมการเชิงเส้น ในรูปแบบดังนี้ $$ \min c^Tx = c_1x_1 + c_2x_2 + ... + c_nx_n$$ 
3. **Constraints**: มีเงื่อนไขเป็นสมการเชิงเส้นเช่นกัน ซึ่งสามารถจัดให้อยู่ในรูป $$ Ax=b $$ 
4. **Non-negative restrictions**: กำหนดให้ $$x\geq0$$ 

<div class="inline-figure" style="border: 1px solid #eee;padding: 0em 1.2em 0.6em; margin-bottom:1.2em" markdown="1">

#### Example #2

**เป้าหมาย:** ต้องการหา cost ที่ดีที่สุดในการขนย้ายขนมแมวจาก _คลังเก็บสินค้า_ ไปยัง _บ้านแมว_

โดยมีสิ่งที่กำหนดให้ดังนี้ 
1. เรามี คลังเก็บสินค้า 2 แห่ง: กรุงเทพ และ นนทบุรี
2. เรามี บ้านแมว 3 ราย: แมวส้ม, แมวสลิด และ แมวดำ

3. การส่งขอไปแต่ละบ้านมีค่าใช้จ่ายดังนี้

    |        |   แมวส้ม  | แมวสลิด | แมวดำ  |
    |--------|----------|--------|--------|
    | กรุงเทพ |   10฿    |   5฿   |   30฿  |
    | นนทบุรี  |   20฿    |   5฿   |   5฿   |


4. คลังเก็บสินค้า แต่ละที่มีขนมแมวที่มี ดังนี้

    |           |   จำนวนขนมแมวที่มี (ซอง)  |
    |-----------|------------------------|
    | W1:กรุงเทพ |             20         |
    | W2:นนทบุรี  |             50         |

5. บ้านแมว แต่ละที่ต้องการขนมแมว ดังนี้

    |            |   จำนวนขนมแมวที่ต้องการ (ซอง)  |
    |------------|-----------------------------|
    | C1:แมวส้ม   |             10              |
    | C2:แมวสลิด  |             40              |
    | C3:แมวดำ   |             20              |


**คำถาม:** เราควรจะมีแผนการส่งอย่างไร?? ให้ได้ cost = ค่าใช้จ่ายที่จะต้องจ่ายทั้งหมด น้อยที่สุด

</div>

#### Solution

จากโจทย์ สามารถกำหนด $$x_{i,j} $$ เป็นจำนวนขนมแมว ที่ต้องส่งจาก คลังเก็บสินค้า $$W_i$$ ไป บ้านแมว $$C_j$$ จะได้ตารางดังนี้

|           |      C1:แมวส้ม    |    C2:แมวสลิด    |    C3:แมวดำ    |
|-----------|------------------|-----------------|----------------|
| W1:กรุงเทพ |   $$x_{1,1}$$    |   $$x_{1,2}$$   |   $$x_{1,3}$$  |
| W2:นนทบุรี  |   $$x_{2,1}$$    |   $$x_{2,2}$$   |   $$x_{2,3}$$  |

และ เราสามารถนิยาม ค่าใช้จ่ายที่จะต้องจ่าย ได้ดังนี้

|           |      C1:แมวส้ม    |    C2:แมวสลิด    |    C3:แมวดำ    |
|-----------|------------------|-----------------|----------------|
| W1:กรุงเทพ |   $$10 x_{1,1}$$    |   $$5 x_{1,2}$$   |   $$30 x_{1,3}$$  |
| W2:นนทบุรี  |   $$20 x_{2,1}$$    |   $$5 x_{2,2}$$   |   $$5 x_{2,3}$$  |

ค่าใช้จ่ายที่จะต้องจ่ายทั้งหมด เท่ากับ


$$
\text{Total cost} = 10 x_{1,1} + 5 x_{1,2} + 30 x_{1,3} + 20 x_{2,1} + 5 x_{2,2} + 5 x_{2,3}
$$

โดยมีเงื่อนไขดังนี้

* **(4) ไม่สามารถส่งขนมแมวได้มากกว่าที่มีอยู่ในคลังเก็บสินค้า**

$$ \tag{4.1}  x_{1,1} + x_{1,2} + x_{1,3} = 20$$

$$ \tag{4.2}  x_{2,1} + x_{2,2} + x_{2,3} = 50$$

* **(5) ต้องไม่ส่งขนมแมวไปน้อยกว่าที่บ้านแมวแต่ละที่ต้องการ**

$$ \tag{5.1}  x_{1,1} + x_{2,1} = 10$$

$$ \tag{5.2}  x_{1,2} + x_{2,2} = 40$$

$$ \tag{5.3}  x_{1,3} + x_{2,3} = 20$$

* **และ (6) จำนวนขนมแมวที่ต้องส่ง ต้องไม่ติดลบ**

$$ \tag{6}  x_{i,j} \ge 0$$

...

**สิ่งที่เราต้องการ** คือ หาว่า $$x = [ ..., x_{i,j}, ...]  $$ ที่ให้ค่า Total cost ที่น้อยที่สุด ที่เป็นไปตามเงื่อนไขเชิงเส้นที่กำหนดไว้ 

ลองเทียบองค์ประกอบของปัญหาใน LP อีกครั้ง

1. ✅ Decision variables = ตัวแปร $$ x_{i,j} $$ ที่เรากำหนด
2. ✅ Objective function = สมการ $$\text{Total cost}  = 10 x_{1,1} + ... + 5 x_{2,3}$$ 
3. ✅ Constraints = เงื่อนไข (4) และ (5)
4. ✅ Non-negative restrictions = เงื่อนไข (6) "จำนวนขนมแมวที่ต้องส่ง ต้องไม่ติดลบ"

ดูเหมือนว่า ปัญหาในตัวอย่าง เป็นไปตามเงื่อนไขของ LP 

...

คราวนี้ ลองมาแก้ปัญหานี้พร้อมกันๆ

จากโจทย์ จะเห็นว่า โจทย์ต้องการหาค่าของตัวแปร $$ x_{i,j}$$ ทั้งหมด 6 ตัว + เงื่อนไข 5 สมการ แปลว่า เราจะต้องสามารถลดรูปให้ ทุกๆ ตัวแปร อยู่ในรูปของ $$ x_{1,1}$$ และ $$ x_{1,2}$$ ได้ดังนี้

จาก (5.1) สามารถจัดรูปได้ว่า 

$$ \tag{6}  x_{2,1} = 10 - x_{1,1}$$

จาก (5.2) สามารถจัดรูปได้ว่า 

$$ \tag{7}  x_{2,2} = 40 - x_{1,2}$$

จาก (4.1) สามารถจัดรูปได้ว่า 

$$ \tag{8}  x_{1,3} = 20 - x_{1,1} - x_{1,2} $$

จาก (4.2) สามารถจัดรูปได้ว่า 

$$\begin{array}{rcl}
    x_{2,3}  & = & 50 - x_{2,1} - x_{2,2} \\
             & = & 50 - (10 - x_{1,1}) - (40 - x_{1,2}) \\
             & = & x_{1,1} + x_{1,2}
\end{array}$$  

จะได้ข้อสรุปว่า

$$ \tag{9} x_{2,3} = x_{1,1} + x_{1,2} $$

เอา (6) - (9) แทนลงในสมการ cost จะได้ว่า

$$\begin{array}{rcl}
    \text{Total cost}  & = & 10 x_{1,1} + 5 x_{1,2} + 30 x_{1,3} + 20 x_{2,1} + 5 x_{2,2} + 5 x_{2,3} \\
                       & = & 10 x_{1,1} + 5 x_{1,2} + 30 (20 - x_{1,1} - x_{1,2}) + 20 (10 - x_{1,1}) + 5 (40 - x_{1,2}) + 5 (x_{1,1} + x_{1,2}) \\
                       & = & 10 x_{1,1} + 5 x_{1,2} + 600 - 30 x_{1,1} - 30 x_{1,2} + 200 - 20 x_{1,1} + 200 - 5 x_{1,2} + 5 x_{1,1} + 5 x_{1,2} \\
                       & = & 1000 - 35 x_{1,1} - 25 x_{1,2}
        
\end{array}$$  

จะได้ข้อสรุปว่า

$$ \tag{10}  \text{Total cost} = 1000 - 35 x_{1,1} - 25 x_{1,2} $$


และเพราะว่า $$ x_{i,j} \ge 0$$

$$ \tag{11}  (x_{2,1} = 10 - x_{1,1}) \ge 0$$

$$ \tag{12}  (x_{2,2} = 40 - x_{1,2}) \ge 0$$

$$ \tag{13}  (x_{1,3} = 20 - x_{1,1} - x_{1,2}) \ge 0$$

$$ \tag{14}  (x_{2,3} = x_{1,1} + x_{1,2}) \ge 0$$

ลองเอาเงื่อนไข (11) - (14) มาพล๊อตกราฟ โดยใช้แกนแนวนอนแทนด้วย $$a = x_{1,1}$$ และ $$b = x_{1,2}$$ จะได้ดังนี้ 

<div style="display:flex;">
    <div class="inline-figure" style="text-align: center;margin-bottom:20px">
    {% include aligner.html images="https://lh3.googleusercontent.com/d/1IHPFp7PkwGmAqGDSCnqq-bAT82uSRd1E" column=1 %}
    </div>

    <div style="min-width: 280px;">

    $$\begin{array}{rcl}
        a  & \ge & 0 \\
        b  & \ge & 0 \\
        a  & <= & 10 \\
        b  & <= & 40 \\
        a+b  & <= & 20 \\
        a+b  & \ge & 0 \\    
    \end{array}$$  

    </div>
</div>

สิ่งที่เกิดขึ้น คือ เราจะได้ ส่วนที่แรงเงาสีแดง ซึ่งประกอบด้วยจุดต่างๆ ที่ตรงตามเงื่อนไขทุกๆข้อที่เราต้องการ และ เราจะเรียกพื้นที่ส่วนนี้ว่า **Feasible region** ซึ่ง [Fundamental Theorem of Linear Programming](https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_programming) บอกว่า "คำตอบที่ดีที่สุดที่เราตามหา คือ จุดใดจุดหนึ่งในบรรดามุมของ feasible region หนิแหละ"


ซึ่งในกรณีของเรา จะได้ว่า คำตอบจะต้องเป็นจุดใดจุดหนึ่งในบรรดาจุดต่อไปนี้ $${(0, 20), (10, 10), (0, 0), (10, 0)}$$

และถ้าเราตรวจคำตอบดีๆ

จาก (10) จะสามารถคำนวน Total Cost ได้ดังนี้

$$ Cost(a, b) = 1000 - 35 x a  - 25 x b $$

$$ Cost(0, 20) = 1000 - 25 x 20 = 500 $$

$$ Cost(10, 10) = 1000 - 35 x 10  - 25 x 10 = 400 $$

$$ Cost(0, 0) = 1000 $$

$$ Cost(10, 0) = 1000 - 35 x 10 = 650 $$

จะได้ว่า $$(a, b)$$ ที่ให้ cost น้อยที่สุด คือ จุด $$a = 10$$ และ $$b = 10$$

แทนค่ากลับไปที่สมการทั้งหมด จะได้


|           |      C1:แมวส้ม    |    C2:แมวสลิด    |    C3:แมวดำ    |
|-----------|------------------|-----------------|----------------|
| W1:กรุงเทพ |   $$x_{1,1} = 10$$    |   $$x_{1,2} = 10$$   |   $$x_{1,3} = 0$$  |
| W2:นนทบุรี  |   $$x_{2,1} = 0 $$    |   $$x_{2,2} = 30$$   |   $$x_{2,3} = 20$$  |

YEAHHHH 🎉🎉🎉🎉

--------


## Wasserstein Distance as LP Problem

คราวนี้ กลับมาต่อกันที่ Wasserstein Distance ถ้ามองดีๆ จะเห็นว่า การหา Wasserstein Distance ก็สามารถทำในรูปแบบเดียวกับการแก้ปัญหา LP


| LP Problem        | Wasserstein Problem                               |
| ----------------- | ------------------------------------------------- |
| คลังเก็บสินค้า        | Source Probability Distribution $$P_r$$           |
| บ้านแมว            | Target Probability Distribution $$P_g$$           |
| ขนมแมว            | Probability mass                                  |
| แผนการส่งของ       | Transport plan $$\Gamma(x_i, x_j)$$               |
| เงื่อนไข (1)        | $$ \sum_{x_j} \Gamma(x_i, x_j) = P_r(x=x_i) $$    |
| เงื่อนไข (2)        | $$ \sum_{x_i} \Gamma(x_i, x_j) = P_g(x=x_j) $$    |
| เงื่อนไข (3)        | $$ \Gamma(x_i, x_j) \ge 0 $$                      |
| ค่าใช้จ่ายที่จะต้องจ่าย  | $$ \lVert x_i - x_j \lVert $$                     |
| Minimum cost      | Wasserstein distance                              |


...

ขอย้อนกลับไปนิยาม องค์ประกอบของปัญหาใน LP แบบจริงๆจังๆ สำหรับ Wasserstein Problem กันอีกครั้ง

ถ้ากำหนดให้ $$ P_r $$ และ $$ P_g $$ เป็น Discrete Probability Distribution ที่มี $$\Omega = {1,2, ..., n}$$ 

**1. Decision variables หรือ $$x$$ สิ่งที่ต้องการ optimized**

นิยาม ให้ $$ vec(A)$$ เป็นฟังก์ชั่นที่สามารถเปลี่ยน Matrix ขนาด m x n เป็น Matrix ขนาด 1 x mn 

เราจะได้ว่า

$$ x = [\Gamma(1, 1), \Gamma(1, 2), ..., \Gamma(1, n), \Gamma(2, 1), \Gamma(2, 2), ..., \Gamma(n, n)]$$

หรือ เขียนแบบสั้นๆ ได้ว่า 

$$ \tag{15} x = vec(\Gamma) $$

**2. Objective function หรือ เป้าหมายของการ optimize**

ปกติแล้ว เราต้องการเขียน Objective function ในรูปแบบ $$ \min c^Tx $$ 

และเพราะเรารู้ว่า สำหรับ Wasserstein Problem เราต้องการนิยาม cost ระหว่างจุด $$(i,j)$$ คือ ระยะทางระหว่าง $$P_r(x=x_i)$$ และ $$P_g(x=x_j)$$

ดังนั้น ถ้าเรานิยามให้ $$ D(i, j) = \lVert x_i - x_j \lVert $$

จะได้ว่า 

$$ \tag{16} c = vec(D) $$

และ objective function ของเรา จะเท่ากับ $$ \min c^Tx $$ ตามที่ต้องการ เพราะ

$$\begin{array}{rcl}
    c^Tx  & = &  [\Gamma(1, 1), \Gamma(1, 2), ..., \Gamma(n, n)]^T [D(1, 1), D(1, 2), ..., D(n, n)] \\
          & = &  \Gamma(1, 1) \cdot D(1,1) + \Gamma(1, 2) \cdot D(1,2) + ... + \Gamma(n, n) \cdot D(n,n)\\
          & = &  \sum_{i,j} \lVert x_i - x_j \lVert \cdot \Gamma(x_i, x_j) \\
        
\end{array}$$  


**3. Constraints หรือ เงื่อนไขในรูปแบบของสมการเชิงเส้น**

ทำนองเดียวกับ Objective function ปกติแล้ว เราต้องการเขียน Constraints ในรูปแบบ $$ Ax=b $$ 

...

ก่อนอื่น ต้องเริ่มจากการนิยาม $$b$$ = ?

จาก ตารางเปรียบเทียบก่อนหน้านี้ จะเห็นว่า เงื่อนไขเป้าหมายของเรา คือ 

$$ \sum_{x_j} \Gamma(x_i, x_j) = P_r(x=x_i) $$

$$ \sum_{x_i} \Gamma(x_i, x_j) = P_g(x=x_j) $$

เพราะต้องรวมสมการทั้งสองอันเข้ามาเป็น ตัวแปรเดียวกัน ดังนั้น $$b$$ ต้องอยู่ในรูปของ vector ของ Probability Values ของทั้ง $$P_r$$ และ $$P_g$$ 

$$ b = [P_r;P_g] $$

หรือ เขียนให้ชัดๆ จะได้หน้าตาประมาณนี้

$$ \tag{17} b = [P_r(x=x_1), P_r(x=x_2), ... P_r(x=x_n);P_g(x=x_1), P_g(x=x_2), ... P_g(x=x_n)] $$

...

แล้ว Matrix $$A$$ ละ???

เพื่อให้เห็นภาพมากขึ้น ขอเริ่มจากการกระจาย terms เงื่อนไขเป้าหมายที่เราสนใจ จะได้ว่า

$$ \sum_{x_j} \Gamma(x_i, x_j) = P_r(x=x_i) $$

สามารถแยกเป็น $$n$$ เงื่อนไข ดังนี้

$$\begin{array}{rcl}
    P_r(x=x_1)  & = & \Gamma(x_1, x_1) + \Gamma(x_1, x_2) + ... + \Gamma(x_1, x_n) \\ 
    P_r(x=x_2)  & = & \Gamma(x_2, x_1) + \Gamma(x_2, x_2) + ... + \Gamma(x_2, x_n) \\ 
    P_r(x=x_3)  & = & \Gamma(x_3, x_1) + \Gamma(x_3, x_2) + ... + \Gamma(x_3, x_n) \\ 
    ...  & = & ... \\ 
    P_r(x=x_n)  & = & \Gamma(x_n, x_1) + \Gamma(x_n, x_2) + ... + \Gamma(x_n, x_n) \\ 
\end{array}$$  

...

ทำนองเดียวกัน

$$ \sum_{x_i} \Gamma(x_i, x_j) = P_g(x=x_j) $$

สามารถแยกเป็น $$n$$ เงื่อนไข ดังนี้

$$\begin{array}{rcl}
    P_g(x=x_1)  & = & \Gamma(x_1, x_1) + \Gamma(x_2, x_1) + ... + \Gamma(x_n, x_1) \\ 
    P_g(x=x_2)  & = & \Gamma(x_1, x_2) + \Gamma(x_2, x_2) + ... + \Gamma(x_n, x_2) \\ 
    P_g(x=x_3)  & = & \Gamma(x_1, x_3) + \Gamma(x_2, x_3) + ... + \Gamma(x_n, x_3) \\ 
    ...  & = & ... \\ 
    P_g(x=x_n)  & = & \Gamma(x_1, x_n) + \Gamma(x_2, x_n) + ... + \Gamma(x_n, x_n) \\ 
\end{array}$$  

...

เราจึงพอสามารถออกแบบ $$A$$ ได้ดังนี้

$$
\begin{array}{c}
\begin{array}{ccccccccccccc}
& \:\:\: \overbrace{\qquad\qquad\quad}^{1}
& \:\:\:\:\: \overbrace{\qquad\qquad\quad}^{2}
& \cdots
& \:\:\: \overbrace{\qquad\qquad\quad}^{n}
\end{array}
\\[-0.3em]
\mathbf{A} = \left[
\begin{array}{cccc|cccc|c|cccc}
1 & 1 & \cdots & 1
& 0 & 0 & \cdots & 0
& \cdots
& 0 & 0 & \cdots & 0
\\
0 & 0 & \cdots & 0
& 1 & 1 & \cdots & 1
& \cdots
& 0 & 0 & \cdots & 0
\\
\vdots & \vdots & \ddots & \vdots
& \vdots & \vdots & \ddots & \vdots
& \ddots
& \vdots & \vdots & \ddots & \vdots
\\
0 & 0 & \cdots & 0
& 0 & 0 & \cdots & 0
& \cdots
& 1 & 1 & \cdots & 1
\\ \hline
1 & 0 & \cdots & 0
& 1 & 0 & \cdots & 0
& \cdots
& 1 & 0 & \cdots & 0
\\
0 & 1 & \cdots & 0
& 0 & 1 & \cdots & 0
& \cdots
& 0 & 1 & \cdots & 0
\\
\vdots & \vdots & \ddots & \vdots
& \vdots & \vdots & \ddots & \vdots
& \ddots
& \vdots & \vdots & \ddots & \vdots
\\
0 & 0 & \cdots & 1
& 0 & 0 & \cdots & 1
& \cdots
& 0 & 0 & \cdots & 1
\end{array}
\right]
\end{array}
$$

//HW: ฝากเป็นการบ้านให้ไปลองดูว่า $$Ax = b$$ จริงอย่างที่อ้างรึปล่าว??

**4. Non-negative restrictions**

สำหรับคุณสมบัติสุดท้าย เพราะว่า $$x = [..., \Gamma(i, j), ...]$$ ซึ่งจากนิยามตั้งต้น เราไม่อนุญาตให้ $$\Gamma(i, j)$$ มีค่าน้อยกว่า 0 อยู่แล้ว

จึงสรุปได้ว่า $$x\geq0$$ เป็นไปตามเงื่อนไขของ LP

...

ตอนนี้ก็พอเห็นว่าแล้วการหา Wasserstein Distance สามารถจัดให้อยู่ในรูปแบบของ LP problem ได้ 

ขอย้อนกลับไปทบทวนตัวอย่าง $$P_r$$ และ $$P_g$$ ในตัวอย่าง Example #1 กันอีกสักรอบ

|     |$$P_r(x)$$|$$P_g(x)$$|
|-----|----------|----------|
| x=1 |    0.1   |    0.1   |
| x=2 |    0.4   |    0.5   |
| x=3 |    0.3   |    0.1   |
| x=4 |    0.2   |    0.3   |


สำหรับคนที่ตั้งใจอ่านมาถึงจุดๆนี้ /me มั่นใจว่า ทุกๆคนคงจะสามารถหาคำตอบได้ โดยใช้วิธีแบบ algebra ตามที่อธิบายไปก่อนหน้านี้ 
* เริ่มจากกำหนดตัวแปรที่เราสนใจ 
* แล้วค่อยๆปรับเงื่อนไขจนเป็นอสมการที่อยู่ในรูปแบบที่เข้าใจได้ 
* จากนั้นก็หา feasible region 
* ก็เอามุมของ feasible region มาคำนวน เป็น cost 
* แล้วหาว่า มุมไหนที่ให้ cost น้อยที่สุด ก็เลือกมุมนั้น เป็นคำตอบ

ฟังเหมือนง่าย แต่ในเชิงปฎิบัติ จะมีอัลกอรีทึมไหนไหม?? ที่จะสามารถแก้ปัญหานี้ได้แบบอัตโนมัติ

และข่าวดี คือ เรามีอัลกอรีทึมที่สามารถแก้ปัญหา LP problem ได้อยู่แล้ว อย่าง Simplex Method และ Interior Points Methods

และสิ่งนี้ก็มี implement มาให้แล้วใน python ตามโค้ดด้านล่างนี้

```python
import time
import numpy as np
from scipy.optimize import linprog

Pr = np.array([0.1, 0.4, 0.3, 0.2])
Pg = np.array([0.1, 0.5, 0.1, 0.3])

support_r = np.array([1, 2, 3, 4])
support_g = np.array([1, 2, 3, 4])

n = len(Pr)
m = len(Pg)


# Cost vector: c
C = np.abs(support_r[:, None] - support_g[None, :])
c = C.flatten()


# Constraint matrix: A
A = []
b = []

# sum_j x_ij = Pr(i)
for i in range(n):

    row = np.zeros(n * m)

    for j in range(m):
        row[i * m + j] = 1

    A.append(row)
    b.append(Pr[i])


# sum_i x_ij = Pg(j)
for j in range(m):

    row = np.zeros(n * m)

    for i in range(n):
        row[i * m + j] = 1

    A.append(row)
    b.append(Pg[j])


A = np.array(A)
b = np.array(b)


start_time = time.perf_counter()

result = linprog(
    c,
    A_eq=A,
    b_eq=b,
    bounds=(0, None),
    method="highs"
)

end_time = time.perf_counter()
execution_time = end_time - start_time

# ============================================================
# Results

if result.success:
    print("Optimal solution found")

    print("\nc =")
    print(c)

    print("\nA =")
    print(A)

    print("\nb =")
    print(b)

    print("\nx =")
    print(result.x)

    # Convert x back into transport matrix
    transport_matrix = result.x.reshape(n, m)

    print("\nOptimal transport matrix:")
    print(transport_matrix)

    print("\nWasserstein Distance:")
    print(result.fun)

else:
    print("Optimization failed:")
    print(result.message)
    
    
print("\nExecution Time:")
print(f"{execution_time:.6f} seconds")
```

ถ้าใครลองเอาไปรัน จะได้ตาราง Transport plan ตามนี้

|              | $$P_g(x=1)$$ | $$P_g(x=2)$$ | $$P_g(x=3)$$ | $$P_g(x=4)$$ |
|--------------|--------------|--------------|--------------|--------------|
| $$P_r(x=1)$$ |      0.1     |       -      |       -      |       -      |
| $$P_r(x=2)$$ |       -      |      0.4     |       -      |       -      |
| $$P_r(x=3)$$ |       -      |      0.1     |      0.1     |      0.1     |
| $$P_r(x=4)$$ |       -      |       -      |       -      |      0.2     |

ซึ่งสามารถคำนวน **งานทั้งหมด** ได้ดังนี้

$$\begin{array}{rcl}
    Work  & = & 0.1 * (1-1) + 0.4 * (2-2) + 0.1 * (3-2) + 0.1 * (3-3) + 0.1 * (4-3) + 0.2 * (4-4)  \\\\
          & = & 0.1 + 0.1 \\\\
          & = & 0.2
\end{array}$$

ถ้าเทียบกับ Work จาก Transport plan ก่อนหน้านี้ (ได้ค่า Work = 1.6) จะเห็นได้ชัดเจนว่า Transport plan อันใหม่นี้ได้ Work ที่น้อยกว่ามากๆ (และ อัลกอริึมการันตีว่า ได้ optimal แล้ว)

นั้นเท่ากับว่า

$$
Wasserstein(P_r, P_g) = 0.2
$$

สำหรับ $$P_r$$ และ $$P_g$$ ในตัวอย่าง 

YEAHHHH 🎉🎉🎉🎉

-----

## Dual Form

ทุกอย่างดูเหมือนจะจบลงแล้ว เพราะเราสามารถคำนวนหา Wasserstein Distance โดยการแปลงให้อยู่ในรูปของปัญหา Linear Programming ได้ แต่ อย่างไรก็ตาม วิธีนี้เหมาะกับกรณีที่ข้อมูลมีจำนวนไม่มากเท่านั้น

ลองย้อนกลับไปยังตัวอย่างก่อนหน้า $$P_r$$ และ $$P_g$$ มีค่าที่เป็นไปได้ $$\Omega$$ ฝั่งละ 4 ค่า เราต้องสร้างตัวแปร $$x_{i,j}$$ เพื่อแทนปริมาณที่เคลื่อนย้ายจากทุกจุดใน $$P_r$$ ไปยังทุกจุดใน $$P_g$$ ดังนั้น จำนวนตัวแปรทั้งหมดจึงเท่ากับ

$$n = 4*4 = 16 $$

ปัญหาขนาดนี้ยังสามารถแก้ด้วย Linear Programming ได้ไม่ยาก แต่เมื่อจำนวนข้อมูลเพิ่มขึ้น จำนวนตัวแปรจะเพิ่มขึ้นเร็วมากๆ

โดยทั่วไป หาก $$P_r$$ มีข้อมูล $$M$$ จุด และ $$P_g$$ มีข้อมูล $$N$$ จุด เราจะต้องพิจารณาเส้นทางการเคลื่อนย้ายทั้งหมด

$$n = m\times n $$

เส้นทาง ตัวอย่างเช่น หากแต่ละฝั่งมีข้อมูล 10,000 จุด จะต้องหาค่าตัวแปรมากถึง $$n = 10000 x 10000 = 10^8 $$ ตัวแปร

...

ปัญหายิ่งซับซ้อนขึ้นเมื่อข้อมูลเป็นรูปภาพ เพราะ "หนึ่งจุด" ในที่นี้ไม่ได้หมายถึง pixel หนึ่ง pixel แต่หมายถึงรูปภาพหนึ่งภาพ

โดย รูปภาพ RGB ขนาด $$100 \times 100$$ หนึ่งภาพ จะประกอบด้วยค่าตัวเลขทั้งหมด $$n = 100 \times 100 \times 3 = 3x10^4$$ ค่า และแต่ละค่าสามารถมีค่าได้ตั้งแต่ 0 ถึง 255 ดังนั้น จำนวนรูปภาพที่อาจเกิดขึ้นได้ในทางทฤษฎีจึงมีมากถึง $$ 256^{30000}$$ รูป

แน่นอนว่าเราไม่สามารถรวบรวมรูปภาพที่เป็นไปได้ทั้งหมด ไม่สามารถระบุความน่าจะเป็นของทุกรูป และ แน่นอนว่าไม่สามารถสร้างตัวแปรเพื่อพิจารณา transport plan ระหว่างรูปภาพทุกคู่ได้ <sup id="fnref:3"><a href="#fn:3">3</a></sup>

ตอนนี้ น่าจะพอเห็นภาพแล้วว่า ในทางปฎิบัติ เป็นไปไม่ได้เลยที่จะสามารถคำนวน Wasserstein Distance จากวิธีธรรมดาๆ

เพราะเหตุนี้ จึงต้องพึ่งเทคนิคที่เรียกว่า **Dual Form** 

...

เพื่อที่จะความรู้จักกับ Dual Form 

เราต้องเริ่มจากการเรียกรูปแบบการนิยามปัญหา LP แบบก่อนหน้านี้ทั้งหมดว่า **Primal Form** 

และ ทุกๆปัญหา LP ใน Primal Form จะสามารถจัดรูปแบบใหม่เป็น **Dual Form** ได้ดังนี้

$$\begin{array}{c|c}

\mathbf{primal \ form:} & \mathbf{dual \ form:}\\

\begin{array}{rrcl}
\mathrm{minimize} \ & z & = & \ \mathbf{c}^T \mathbf{x}, \\
\mathrm{so \ that} \ & \mathbf{A} \mathbf{x} & = & \ \mathbf{b} \\
\mathrm{and}\  & \mathbf{x} & \geq &\ \mathbf{0}
\end{array} &

\begin{array}{rrcl}
\mathrm{maximize} \ & \tilde{z} & = & \ \mathbf{b}^T \mathbf{y}, \\
\mathrm{so \ that} \ & \mathbf{A}^T \mathbf{y} & \leq & \ \mathbf{c} \\ \\
\end{array}

\end{array}$$


สำหรับใครที่สนใจอยากอ่านเพิ่มเติมว่า Dual Form มันคืออะไรกันแน่?? แนะนำให้อ่าน 2 บล๊อคนี้เลยฮะ [Intuition for the Dual in Linear Programming](https://mikespivey.wordpress.com/2021/03/31/intuition-for-the-dual-in-linear-programming/) และ [Duality in Linear Programming](https://www.science4all.org/article/duality-in-linear-programming/)

สิ่งที่น่าสนใจ คือ $$ \tilde{z} $$ ที่ได้ จะเป็นมีค่าขั้นต่ำของ $$z$$ ซึ่งพิสูจน์ได้ดังนี้

$$\begin{array}{rcl}
    A^Ty  & \le & c  \\
    (A^Ty)^Tx  & \le & c^Tx  & \quad \text{since } x \ge 0 \\
    y^TAx  & \le & c^Tx \\
    y^Tb  & \le & c^Tx \\
    b^Ty  & \le & c^Tx \\
    \tilde{z}  & \le & z \\
\end{array}$$

//เราเรียกสิ่งนี้ว่า __"Weak Duality theorem"__ นั้นคือ 

<div class="inline-figure blockquote">
ทุกๆคำตอบ $$ y $$ จาก Dual Form จะให้ค่า cost ไม่เกิน คำตอบที่ดีที่สุด $$x^*$$ ของ Primal Form
</div>

และเรายังมีขั้นกว่าที่ซับซ้อนไปอีกขั้น คือ __"Strong Duality theorem"__  ซึ่งกล่าวว่า

<div class="inline-figure blockquote">
ถ้า Primal Form มีคำตอบที่ดีที่สุด $$x^*$$ จริงๆ จะได้ว่า Dual Form ก็จะต้องสามารถหา $$ y $$ ที่ $$ c^Tx^* = b^Ty $$ ได้เสมอ
</div>

//บนเงื่อนไขว่า primal form ต้องมีคำตอบ $$x$$ อย่างน้อย 1 คำตอบ และ มีคำตอบที่ดีที่สุด $$x^*$$ แค่ finitely many

...

สำหรับใครที่ งง ระหว่าง "คำตอบ $$x$$ ของ Primal Form" และ "คำตอบที่ดีที่สุด $$x^*$$ ของ Primal Form"  

อยากให้ลองนึกย้อนไปตอนที่หา $$x$$ โดยวิธีแบบ algebra 

สิ่งที่เกิดขึ้นคือ ทุกๆจุดที่อยู่ใน feasible region จริงๆแล้วก็คือ "คำตอบ $$x$$ ของ Primal Form" เพราะ ทุกๆ $$x$$ เป็นไปตามเงื่อนไข $$Ax = b$$ อยู่แล้ว

แต่มีแค่จุดมุม จุดเดียวที่เป็น "คำตอบที่ดีที่สุด $$x^*$$ ของ Primal Form"

//เช่นเดียวกันกับ Dual Form

$$
\begin{array}{c}
\underbrace{b^Ty}_{\text{Dual feasible}}
\le
\underbrace{b^Ty^*}_{\text{Dual optimum}}
=
\underbrace{c^Tx^*}_{\text{Primal optimum}}
\le
\underbrace{c^Tx}_{\text{Primal feasible}}
\end{array}
$$


จากทั้ง Weak Duality theorem และ Strong Duality theorem จะได้ข้อสรุปว่า **"คำตอบที่ได้จาก Dual Form ก็คือคำตอบเดียวกันกับคำตอบที่จะได้จาก Primal Form"**

ถ้าเราสามารถหาคำตอบจาก Dual Form แบบง่ายๆได้ เราก็จะสามารถหา Wasserstein Distance ได้แบบง่ายๆ


----------

## Wasserstein Distance in Dual Form

วนไปเรื่อง Dual Form อยู่นานนนน ขอกลับมาพูดถึง Wasserstein Distance กันอีกหน่อย 

เดิม เรานิยาม Wasserstein Distance ดังนี้

$$
Wasserstein(P_r, P_g) = \inf_{\Gamma \in \Pi(P_r, P_g)} \sum_{i,j} \lVert x_i - x_j \lVert \cdot \Gamma(x_i, x_j)
$$

ต่อมา เราพบว่า การหา Wasserstein Distance ก็คือการแก้ปัญหา LP เราจึงนิยามใหม่ได้ดังนี้

$$
Wasserstein(P_r, P_g) = \min \: \{c^Tx\} \quad \text{s.t. } Ax=b; x \ge 0
$$

และ สามารถเขียนใน Dual Form ได้ดังนี้

$$
Wasserstein(P_r, P_g) = \max \: \{b^Ty\} \quad \text{s.t. } A^Ty \le c
$$

คำถามที่น่าสนใจ คือ $$y$$ ในที่นี้ คือ อะไร?? 

...

ถ้าพิจารณาว่า $$ b^Ty $$ = ตัวเลขหนึ่งตัว จะพอเดาได้ว่า $$y$$ ต้องเป็น vector ที่มีขนาดเท่ากับ $$b$$

ซึ่งสามารถย้อนไปดู จะเห็นว่า $$ b = [P_r;P_g] $$ 

ดังนั้น $$y$$ จะต้องสามารถจัดอยู่ในรูปแบบดังนี้

$$
y = [f_1, f_2, ..., f_n, g_1, g_2, ..., g_n]
$$

โดยถ้าเรามองว่า $$ f(x_i) = [f_1, f_2, ..., f_n] $$ และ $$ g(x_i) = [g_1, g_2, ..., g_n] $$

จะได้ว่า

$$
\tilde{z} = b^Ty = \sum_i P_r(x=x_i) \cdot f(x_i) +  \sum_j P_g(x=x_j) \cdot g(x_j)
$$

และเพราะว่า $$ c_{ij} = \lVert x_i - x_j \lVert$$ หากพิจารณาเงื่อนไข $$A^Ty \le c$$ เราจะสามารถกระจายได้ดังนี้

$$\begin{array}{rcl}
    f(x_1) + g(x_1)  & \le & \lVert x_1 - x_1 \lVert \\ 
    f(x_1) + g(x_2)  & \le & \lVert x_1 - x_2 \lVert \\ 
    f(x_1) + g(x_3)  & \le & \lVert x_1 - x_3 \lVert \\ 
    ...  & = & ... \\ 
    f(x_n) + g(x_n)  & \le & \lVert x_n - x_n \lVert
\end{array}$$  

ถ้าลองพิจารณาเฉพาะ กรณี $$i = j$$ ซึ่ง $$\lVert x_i - x_j \lVert = 0$$ จะได้ว่า

$$f(x_i) + g(x_i)  \le 0 $$

$$g(x_i)  \le - f(x_i) $$

และเพราะว่า $$P_r(x=x_i) \ge 0$$ และ $$P_g(x=x_i) \ge 0$$

ถ้าพิจารณาที่ $$f(x_i)$$ เป็นค่าคงที่ จะได้ว่า $$g(x_i)$$ ที่ดีที่สุด ที่จะทำให้ $$\tilde{z}$$ มีค่ามากที่สุด คือ $$g(x_i)$$ ที่ $$g(x_i) = - f(x_i)$$

และ $$g(x) = - f(x)$$ ก็ยังสามารถใช้หา คำตอบที่ดีที่สุดได้ ในกรณีที่ $$i \neq j$$ เช่นกัน

//จะขอละการพิสูจน์ไว้นะฮะ (keyword: Kantorovich–Rubinstein Duality)

...

ย้อนกลับมาแทนค่า $$g(x) = - f(x)$$ เพื่อใช้หา Wasserstein Distance เราจะได้ว่า

$$
\tilde{z} = \sum_i P_r(x=x_i) \cdot f(x_i) -  \sum_j P_g(x=x_j) \cdot f(x_j)
$$

โดยมีเงื่อนไขว่า

$$
f(x_i) - f(x_j)  \le \lVert x_i - x_j \lVert
$$

พิจารณาสลับ $$i, j$$ จะได้ว่า

$$
f(x_j) - f(x_i)  \le \lVert x_j - x_i \lVert
$$

แต่เพราะว่า $$\lVert x_i - x_j \lVert = \lVert x_j - x_i \lVert $$ จะได้ว่า

$$
-\lVert x_i - x_j \lVert \le f(x_i) - f(x_j)  \le \lVert x_i - x_j \lVert
$$

จัดในอีกรูปแบบนึง ได้ว่า 

$$
\tag{18} \lVert f(x_i) - f(x_j) \lVert \:\le \lVert x_i - x_j \lVert
$$

ซึ่งอสมการ (18) เป็นการบอกว่า $$f$$ ไม่ใช่ฟังก์ชันอะไรก็ได้ แต่ต้องเป็นฟังก์ชันที่มีคุณสมบัติ **1-Lipschitz condition** เท่านั้น

//เขียนย่อๆ ว่า $$ \lVert f \lVert _L \le 1 $$

...

จากทั้งหมดที่ผ่านมา จึงได้ข้อสรุปว่า

$$
\tag{19} Wasserstein(P_r, P_g) = \sup_{\lVert f \lVert _L \le 1} [\sum_i P_r(x_i) \cdot f(x_i) -  \sum_j P_g(x_j) \cdot f(x_j)]
$$

และสังเกตุได้ว่า $$ \sum_i P_r(x=x_i) \cdot f(x_i) $$ จริงๆแล้ว มันก็คือ $$ \mathbb{E}_{x \sim P_r}[f(x_i)]$$

เราจึงสามารถนิยาม $$ Wasserstein(P_r, P_g)$$  ใหม่ ได้ดังนี้

$$
\tag{20} Wasserstein(P_r, P_g) = \sup_{\lVert f \lVert _L \le 1} \mathbb{E}_{x \sim P_r}[f(x)] -  \mathbb{E}_{x \sim P_g}[f(x)]
$$

จุดๆนี้ ทำให้เราเห็นว่า 

ในการคำนวนหา Wasserstein Distance เราสามารถเปลี่ยนมุมมองแบบ Primal Form แทนที่จะถามว่า "จะเคลื่อนย้าย Probability mass จาก $$P_r$$ ไปยัง $$P_g$$ ได้อย่างไร โดยทำงานน้อยที่สุด?"

เป็นมุมมองแบบ Dual Form ซึ่งเปลี่ยนมาถามว่า "มีฟังก์ชันให้คะแนน f ใดที่สามารถแยก $$P_r$$ ไปยัง $$P_g$$ ออกจากกันได้มากที่สุด? โดย f ต้องอยู่ภายใต้ 1-Lipschitz condition"

...

จริงๆแล้วจุดๆนี้ ยังไม่ได้ช่วยทำให้การคำนวน $$ Wasserstein(P_r, P_g)$$ เป็นไปดีขึ้น หรือ ง่ายขึ้น เพราะ สุดท้ายแล้วเรายังไม่รู้ว่าจะหา $$ f(x) $$ ได้ยังไง??

----------------------

## Back to WGAN

จากตอนที่แล้ว เราพอได้ข้อสรุปว่า ถ้าต้องการคำนวนหา $$ Wasserstein(P_r, P_g)$$ เราสามารถหาได้จากการตามหาฟังก์ชัน $$f(x_i)$$ พิเศษตัวนึง ที่มีคุณสมบัติ **1-Lipschitz condition** แล้วหาไปเรื่อยๆ จนกว่าจะได้ $$f(x_i)$$ ที่ให้ค่า $$ Wasserstein(P_r, P_g)$$ ที่มากที่สุด


แต่ แต่ แต่ แทนที่จะหา $$f(x_i)$$ แบบมั่วๆไปเรื่อนๆ ทำไมเราไม่แทน $$f(x_i)$$ เป็น neural network สักตัวไปเลยละ ??

และ เจ้า neural network ที่ว่านั้น ก็คือ Critic ที่อยู่ใน WGAN นั้นเอง

ดังนั้น สิ่งที่ WGAN เสนอ จึงเป็นการเปลี่ยน Discriminator จากเดิมทำหน้าที่ในการให้คะแนนความแนบเนียนของ $$x$$ ใดๆ ไปเป็น Critic ซึ่งทำหน้าที่เป็นแค่ฟังค์ชันผู้ช่วย $$f(x)$$ ใช้สำหรับการเปรียบเทียบระหว่าง $$P_r$$ และ $$P_g$$ โดยมี loss ของทั้งระบบ คือ Wasserstein distance โดยตรง

และเพื่อให้ Critic เป็นฟังก์ชันที่มีคุณสมบัติ **1-Lipschitz condition** 

WGAN จึงเสนอให้มีการ Weight clipping เพื่อบังคับให้ weights ของ Critic อยู่ในช่วงตัวเลขเล็กๆอันนึง เช่น [-0.01, 0.01] แต่วิธีนี้ไม่ค่อยมีประสิทธิภาพขนาดนั้น

ต่อมา WGAN-GP จึงเสนอแนวทางใหม่ โดยแทนที่ Weight clipping ด้วย gradient penalty แล้วก็จบพัฒนาการของ WGAN


// จบแล้ววววววว 🎉🎉🎉🎉

-------------

# สรุป

Wasserstein Distance คือ metric ที่ใช้วัดความเหมือน/ต่าง ระหว่าง Probability Distribution 2 อัน โดยให้มอง Probability Distribution แต่ละก้อน เป็นเหมือนกองทรายกองนึง แล้วตั้งคำถามว่า **เราต้องทำงานน้อยที่สุดเท่าไรในการย้ายกองทรายกองนึง มาเป็นอีกกองนึง**

โดยการคำนวน Wasserstein Distance สามารถแปลงเป็นปัญหาที่เรียกว่า Linear Programming และแก้โดยใช้ LP Solver แต่ในเชิงปฏิบัติ มันจะช้ามากๆ 

จึงต้องหยิบยืม Kantorovich–Rubinstein Duality เพื่อปัญหา LP ที่อยู่ใน Dual Form ให้สามารถคำนวนได้แบบง่ายๆ โดยใช้ neural network ที่ต้องบังคับให้มีคุณสมบัติ 1-Lipschitz condition และไอเดียนี้ก็ถูก implement ไปเป็น WGAN นั้นเอง


## อ้างอิง
* [Wasserstein GAN and the Kantorovich-Rubinstein Duality](https://vincentherrmann.github.io/blog/wasserstein/)
* [From GAN to WGAN](https://lilianweng.github.io/posts/2017-08-20-gan)


<div class="footnotes">
    <ol>
        <li class="footnote" id="fn:1">
            <p>technically, ทั้ง cosine similarity และ cross-entropy ไม่ได้เป็น distance ในเชิงคณิตศาสตร์ ตามนิยามของ metric space แต่ ในที่นี้ /me ต้องการแค่เปรียบเทียบว่า ทั้งสอง สามารถตีความในรูปแบบคล้ายๆกับ distance ได้</p>
        </li>

        <li class="footnote" id="fn:2">
            <p>ในบล๊อคนี้ จะเขียน LP ในรูปแบบของการหาค่า $$\min$$ แต่ทั่วไปแล้ว ถ้าต้องการหา $$\max$$ เราสามารถทำได้โดยการ ปรับ Objective function เป็น $$ -c^Tx $$  เพราะว่า $$ \argmax_x c^Tx = \argmin_x -c^Tx $$</p>
        </li> 


        <li class="footnote" id="fn:3">
            <p>สำหรับคนที่อยากอ่านหัวข้อนี้เพิ่มเติม สามารถอ่านได้ที่ลิงค์นี้เลยฮะ [Computational Optimal Transport](https://arxiv.org/abs/1803.00567)</p>
        </li> 

        


    </ol>
</div>


