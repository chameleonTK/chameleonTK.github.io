---
layout: post
title: Proof π is a transcendental number.
tags: [Archive, Mathematics]
thumbnail: "assets/feats/math-related/pi-is-what.png"
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
bootstrap: true
---

<style>
    .katex-display > .katex > .katex-html {
        width: 600px;
    }
</style>
<p style="display:none">
## TL;DR
อธิบายบทพิสูจน์ π เป็นจำนวนอดิศัย จากความเข้าใจของ /me
</p>
<!--more-->



$$\pi$$ = 3.1415926... นี่เชื่อว่า สิ่งนี้เป็นตัวเลขตัวนึงที่ทุกๆคนต้องได้เจอกันตั้งแต่เด็กยันโต ตัวเราเองก็เป็นหนึ่งในนั้น 

$$\pi$$ เป็นสิ่งใกล้ตัวเรามากๆ

$$\pi$$ อยู่ในทุกๆที่ มีวงกลมอยู่ที่ไหน ก็จะต้องเจอ $$\pi$$ ที่นั้น 

$$ Area(r) = \pi r^2 $$

แม้จะเป็นที่ที่ไม่มีวงกลมหลายๆที่ก็มี $$\pi$$ ไปโผล่อยู่เรื่อยๆ อย่าง ค่าผลรวมของ infinite serie $$  \frac{1}{2}+\frac{1}{4}+\frac{1}{9}+\frac{1}{16}+...$$ ก็ยังปรากฎ $$\pi$$ มาให้เห็น

$$ \sum_{n=1}^{\infty} (\frac{1}{n^2}) = \frac{\pi^2}{6}$$

อย่างในงาน AI ซึ่งมักพูดถึง Gaussian noise และเจ้า noise ที่ว่าก็ยังมีการปรากฎตัว $$\pi$$ 

$$ z \sim p(z) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(z-\mu)^2}{2\sigma^2}} $$

เรียกได้ว่า ตามหลอกหลอนไปอยู่ในทุกๆที่ ตั้งแต่สมัยเรียนมัธยม ไปจนถึงเรียนปริญญาเอก

<hr>

นึกย้อนกลับไป สมัยเด็กๆ ที่โรงเรียนจะสอนให้ท่องจำเอาว่า $$\pi$$ = 22/7 หรือ 3.14285714286 ซึ่งสมัยนั้นก็พลอยเข้าใจไปเองว่า มันคือ exact value ของ $$\pi$$

ต่อมาโตขึ้น จึงเข้าใจว่า $$\pi$$ ไม่ได้มีค่าสิ้นสุด ตัวเลข 3.14 หรือ 3.14285714286 ที่เคยท่องจำเป็นเพียงแค่ค่าประมาณของ $$\pi$$ เท่านั้น กลับกัน ค่าจริงๆของ $$\pi$$ กลับเป็นเลขที่มีทศนิยมยาวไปเรื่อยๆ ไม่ซ้ำ และ ไม่สิ้นสุด (a.k.a จำนวนอตรรกยะ) 

สำหรับตัวเราเอง เรื่องนี้เป็นเรื่องที่น่าตื่นเต้นมาก แค่อ่านในหนังสือก็สนุกแล้ว รู้สึกเหมือนได้เจอปริศนาอะไรบางอย่าง 

ต่อมาโตขึ้นอีก จึงรู้จัก  $$\pi$$ มากขึ้น และพบว่า  $$\pi$$ ยังมีคุณสมบัติอื่นๆอีกมากมายที่น่าสนใจมากๆ หนึ่งในนั้น คือ นอกจาก <a target="_blank" href="https://chameleontk.github.io/pi-is-irrational"> $$\pi$$ เป็นจำนวนอตรรกยะ (irrational number)</a> แล้ว $$\pi$$ ก็เป็นจำนวนอดิศัย (transcendental number) ด้วย

<hr>

## What is Transcendental Number?
#### จำนวนอดิศัย คืออะไร? 

ย้อนกลับไป การเรียนคณิตศาสตร์ของเราๆ มักจะเริ่มด้วยการทำความรู้จักตัวเลขในรูปแบบต่างๆ เริ่มต้นจาก จำนวนนับ 1, 2, 3, ... 

ต่อมา จึงขยายเป็นจำนวนเต็ม ... -3, -2, -1, 0, 1, 2, 3, ... ซึ่งมีทั้งเลขที่มากกว่า 0 และน้อยกว่า 0 

ต่อมา ก็ขยายเพิ่มเติมไปเรียน จำนวนตรรกยะ หรือ ตัวเลขที่แทนได้ด้วยเศษส่วนของจำนวนเต็ม หรือ แทนด้วยเลขทศนิยมซ้ำ อย่าง $$\frac{1}{2}$$, $$\frac{18}{14}$$, 2.555..., 3.142142142...

และ จำนวนที่เป็นขั้วตรงข้ามของมัน หรือ จำนวนอตรรกยะ ซึ่งไม่สามารถแทนด้วยเศษส่วน หรือ ทศนิยมซ้ำ ได้ เช่น  $$  \sqrt{2}$$, $$2\sqrt{3}$$, $$sin(1)$$, $$log(20)$$, และ ก็รวมไปถึง ค่าคงที่อย่าง $$e$$ และ $$ \pi $$ ด้วย

ต่อมาสามารถขยายต่อไปเป็น จำนวนจริง หรือ ตัวเลขทุกๆตัวที่เป็นไปได้ ที่สามารถเจอได้บนเส้นจำนวน  (??? เส้นยาวๆลากจาก $$-\infty$$ ถึง $$\infty$$) 

เราสามารถเขียนโครงสร้างของกลุ่มตัวเลขทั้งหมดที่พูดไป ในรูปแบบของ set ที่ซ้อนกันไปเรื่อยๆ ตามรูป

{% include aligner.html images="pi-is-transcendental/van-diagram.jpg" column=1 %}

แต่ทั้งนี้ ยังมีอีกหนึ่งเซตที่มักจะโดยข้ามไป คือ Algebraic Numbers <sup id="fnref:1"><a href="#fn:1">1</a></sup> และ คู่ตรงข้ามของมัน คือ Transcendental Numbers

<hr>

โดย เจ้า Algebraic Numbers เป็นส่วนขยายต่อจาก จำนวนตรรกยะ 

หากพิจารณาตามนิยามของ จำนวนตรรกยะ จะได้ว่า $$n$$ เป็นจำนวนตรรกยะ หรือ $$ n \in \mathbb{Q} $$ ก็ต่อเมื่อ $$n$$ สามารถเขียนอยู่ในรูปเศษส่วนของจำนวนเต็ม $$ n = \frac{p}{q}$$ หรือ

$$ n \in \mathbb{Q} \Leftrightarrow \exists p,q \in \mathbb{Z} \text{ such that }   n = \frac{p}{q}$$

ซึ่งสามารถปรับให้อยู่ในรูปแบบดังนี้ 

$$ n \in \mathbb{Q} \Leftrightarrow \exists p,q \in \mathbb{Z} \text{ such that }   q*n + p = 0 $$

จะได้ว่า จำนวนตรรกยะ สามารถนิยามใหม่เป็น จำนวน $$ x $$ ใดๆก็ตามที่สามารถทำให้สมการ $$ a*x + b = 0 $$ เป็นจริงได้ หรือพูดอีกอย่างว่า จำนวนตรรกยะ คือ เซตของตัวเลขที่เป็นคำตอบที่เป็นไปได้ทั้งหมด ของสมการ linear ใดๆ ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม


ด้วยคอนเซปนี้ นักคณิตศาสตร์จึงตั้งคำถามต่อไปว่า จะเป็นยังไงนะถ้าเราเปลี่ยน สมการ linear เป็น polynomial degree อื่นๆ 

{% include aligner.html images="pi-is-transcendental/quadatic-number.png" column=1 %}

สิ่งที่เกิดขึ้น คือ 

ถ้าเราเปลี่ยน สมการ linear เป็น polynomial degree 2 หรือ quadratic polynomial สิ่งที่ได้ คือ quadratic numbers -- เซตของตัวเลขที่เป็นคำตอบที่เป็นไปได้ทั้งหมด ของสมการ quadratic polynomial $$ a*x^2 + bx + c = 0 $$ ใดๆ ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม 

ตัวอย่าง quadratic numbers เช่น $$ 2+sqrt(2) $$ ซึ่งเป็นคำตอบจากสมการ $$x^2-4x+2 = 0$$ หรือ $$ \phi $$ (สัดส่วนทองคำ) หรือ $$ \frac{1+sqrt(5)}{2} $$ จากสมการ $$x^2-x-1 = 0$$

ถ้าเราเปลี่ยนไปใช้ polynomial degree 3 ก็จะได้ cubic numbers

ถ้าเราเปลี่ยนไปใช้ polynomial degree 4 ก็จะได้ quartic numbers

...

ถ้าเราเปลี่ยนไปใช้ any polynomial ก็จะได้ algebraic numbers นั้นเอง

สรุป คือ algebraic numbers คือ เซตของตัวเลขที่เป็นคำตอบที่เป็นไปได้ทั้งหมดของสมการ polynomial ใดๆ ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม 

และ ตรงกันข้าม transcendental numbers คือ เซตของตัวเลขที่ไม่สามารถเป็นคำตอบของสมการ polynomial (ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม) ใดๆ

และ $$\pi$$ ก็เป็นสมาชิกหนึ่งของ transcendental numbers นี้เอง

แปลว่า เราจะไม่สามารถหาจำนวนเต็ม a, b, c ใดๆที่ทำให้สมการนี้ $$ a*\pi^2 + b\pi + c = 0 $$ เป็นจริง และรวมไปถึง สมการ integer polynomial<sup id="fnref:2"><a href="#fn:2">2</a></sup> ใดๆ 

<hr>

## Proving that π is transcendental
#### บทพิสูจน์ว่า π เป็นจำนวนอดิศัย

จะว่าไปแล้ว ส่วนตัวพยายามทำความเข้าใจบทพิสูจน์นี้มานับรวมๆก็ร่วม 10 ปีแล้ว สิ่งที่เข้าใกล้มากที่สุด ก็คือ บล๊อคเมื่อ 9 ปีก่อน <a target="_blank" href="https://chameleontk.github.io/pi-is-irrational">สรุปบทพิสูจน์ $$\pi$$ เป็นจำนวนอตรรกยะ</a>

แต่จากบทพิสูจน์ irrational มาเป็น transcendental เหมือนจะเป็น super steep step ขั้นบันไดที่ชันมากๆ ด้วยความสามารถที่ไม่ถึงขั้นทั้งในด้านความรู้ทางภาษา (ไม่เข้าใจคำอธิบาย) รวมไปถึง ด้านความรู้ทางคณิตศาสตร์ (ไม่เข้าใจเทคนิค/กระบวนการ)

เวลาผ่านไป ความรู้ทางภาษาเริ่มไปวัดไปวาได้ พอเข้าใจภาพรวมของบทพิสูจน์ แต่ก็ยังทะเลาะกับหลายๆ ทฤษฎีบทที่ต้องใช้<sup id="fnref:3"><a href="#fn:3">3</a></sup> แต่ช่วงไม่กี่ปีที่ผ่านมา มี ChatGPT และผองเพื่อน ตรรหนักได้ว่า เราสามารถใช้ AI เหล่านี้เป็นเครื่องมือช่วยทำความเข้าใจบทพิสูจน์ที่ซับซ้อนอันนี้ได้หนิหน่า

ไปๆมา ถือโอกาสใช้มันเป็นคู่หูช่วยอ่านไปซะเลย เป็นการทดลองครั้งแรก และปรากฎว่า มันสามารถทำงานได้ดีอย่างไม่น่าเชื่อ<sup id="fnref:4"><a href="#fn:4">4</a></sup> จนคิดว่า น่าจะถึงจุดที่บอกได้ว่า "ในที่สุด เราก็เข้าใจ บทพิสูจน์บทนี้แล้ว" Obviously!

<hr>

เกริ่มนำมานาน ขอเริ่มละนะ

<div class="accordion mb-3" id="accordion1">
    <div class="card border">
        <div class="card-header" id="accordion1-heading">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left p-0" type="button" data-toggle="collapse" data-target="#accordion1-collapse" aria-expanded="true" aria-controls="accordion1-collapse"> Credit </button>
            </h2>
        </div>
        <div id="accordion1-collapse" class="collapse show border" aria-labelledby="accordion1-heading" data-parent="#accordion1">
            <div class="card-body"> 
            บทพิสูจน์มาจาก บทพิสูจน์ ของ <a target="_blank" href="https://link.springer.com/chapter/10.1007/978-3-642-50831-8_1">D. Hilbert (1893)</a> แปลและสรุปเพิ่มเติมโดย <a target="_blank" href="https://www.qedcat.com/notes/e%20%2b%20pi%20transcendental.pdf">M. Ross (2018) </a> จากยูทูปชาเนล <a target="_blank" href="https://www.youtube.com/watch?v=WyoH_vgiqXM">Mathologer</a>
            </div>
        </div>
    </div>
</div>


### Proof Structure

สิ่งนี้เป็นสิ่งหนึ่งที่เรียนรู้จากการอ่าน proof มาหลายๆรอบ พึ่งเข้าใจจริงๆว่า บทพิสูจน์ต่างๆ ไม่ได้เกิดจากจากอากาศ หรือ เสกขึ้นมา แต่มาจากการออกแบบมาเป็นอย่างดี เพื่อให้ได้ arguments ที่สอดคล้องกับสิ่งที่ต้องการพิสูจน์ 

ดังนั้นก่อนที่ไปดูรายละเอียดของบทพิสูจน์ อยากจะขอมาทำความเข้าใจภาพรวมกันก่อน 

โดยรวมแล้ว บทพิสูจน์ $$\pi$$ is transcendental เริ่มจากนิยาม นั้นคือ $$ \pi $$ จะไม่เป็นคำตอบของสมการพนุนามดีกรีใดๆ ที่มี coefficents เป็นจำนวนเต็ม เขียนเป็นนิพจน์คณิตศาสตร์ ได้ว่า 

$$ \forall a_0, a_1, ...a_n \in \mathbb{Z}, a_0  \mathrel{\char`≠} 0 \\
\tag{1} a_0 + a_1 \pi + a_2\pi^2 + ... + a_n \pi^n \mathrel{\char`≠}  0$$

ซึ่งเราจะพิสูจน์นิจน์นี้ ด้วยเทคนิค Proof by Contradiction นั้นคือ 

สมมติให้ นิเสธของ (1) เป็นจริง แล้วจะทำให้เกิดข้อขัดแย้ง (contradiction) บางอย่าง แปลว่า เราไม่สามารถทำให้มันเป็นจริงได้ = นิพจน์ (1) เป็นจริง<sup id="fnref:5"><a href="#fn:5">5</a></sup>

นั้นคือ เราจะกำหนดให้ 

$$ \exists a_0, a_1, ...a_n \in \mathbb{Z}, a_0  \mathrel{\char`≠} 0 \\
\tag{2} a_0 + a_1 \pi + a_2\pi^2 + ... + a_n \pi^n = 0 $$

โดยเรียกสมการด้านบนด้วย 

$$ \tag{3} p(x) = a_0 + a_1 x + a_2 x^2 + ... + a_n x^n$$

$$ \tag{4} p(\pi) = 0 $$

ต่อมา เราสามารถสร้าง 

$$ \tag{5} q(x) = p(ix)p(-ix) $$

โดยที่ $$ q(x) $$ ก็เป็น integer polynomial เช่นกัน แต่จะแสดงต่อไปว่า $$ q(x) $$ ไม่สามารถสร้างได้ ดังนั้น $$ p(x) $$ ก็จะไม่มีอยู่จริง

แต่ แต่ แต่ $$ q(x) $$ ที่ว่า เป็น integer polynomial จริงๆรึปล่าวนะ??

<div class="accordion mb-3" id="accordion2">
    <div class="card border">
        <div class="card-header" id="accordion2-heading">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left p-0" type="button" data-toggle="collapse" data-target="#accordion2-collapse" aria-expanded="true" aria-controls="accordion2-collapse"> 
                Lemma #1:  ถ้า p(x) เป็น integer polynomial แล้ว q(x) เป็น integer polynomial เช่นกัน</button>
            </h2>
        </div>
        <div id="accordion2-collapse" class="collapse border" aria-labelledby="accordion2-heading" data-parent="#accordion2">
            <div class="card-body"> 
            กำหนดให้ $$ p(x) = a_0 + a_1 x + a_2 x^2 + ... + a_n x^n $$ 

            หรือ เขียนอีกแบบได้ว่า 

            $$p(x) = \sum_{k=0}^{n} a_k x^k \text{ with } a_k \in \mathbb{Z}$$ 

            จะได้ว่า

            $$p(ix) = \sum_{k=0}^{n} a_k i^k x^k $$ 

            และ

            $$p(-ix) = \sum_{l=0}^{n} a_l i^l (-1)^l x^l $$ 

            นั้นคือ 
            
            $$q(x) = p(ix)p(-ix) = (\sum_{k=0}^{n} a_k i^k x^k) * (\sum_{l=0}^{n} a_l i^l (-1)^l x^l)$$ 

            ถ้ากระจายพจน์ออกมาก จะได้ว่า q(x) จะมีทั้งหมด 2n พจน์ โดยแต่ละพจน์ xᵏ เกิดจาก ผลรวมจากการคูณของพจน์ย่อยที่ดีกรี รวมกันเท่ากับ k 

                <div class="example my-3 border p-3 bg-light">
                    <b>ตัวอย่าง</b> กำหนด s(x) และ r(x) ดังนี้
                    
                    $$s(x) = 2x^3 - 3x^2 + x - 1$$ และ $$r(x) = x^3 + 2x^2 + 5x + 3$$ 

                    จะได้ว่า s(x)r(x) เป็นพหุนามดีกรี 6 และ ถ้าพิจารณาพจน์ x⁴ จะเห็นว่า มันเกิดจาก

                    $$\begin{array}{rcl}
                        c_4 x^4 & = & (2x^3)(5x) + (-3x^2)(2x^2) + (x)(x^3) \\
                        & = & (2*5 + (-3)*2 + 1*1)x^4
                    \end{array}$$  

                </div>
        
            ดังนั้น จึงสรุปได้ว่า

            $$q(x) =\sum_{k=0}^{2n} c_k x^k $$  

            

            <div class="example my-3 border p-3 bg-light">
                Note: k มีค่าตั้งแต่ 0 ถึง 2n โดยที่ cₖ ซึ่งเกิดจากคู่พจน์ใดๆที่ดีกรีรวมกันได้ k 
            </div>

            <br><br>
            พิจารณา คำนวน cₖ 

            <div class="example my-3 border p-3 bg-light">
                ลองพิจารณาตามดัวอย่างต่อไปนี้ 
                <br><br>
                <b>ตัวอย่าง</b> ในกรณีที่ ถ้า n=4 และ k=3
                จะได้ว่า c₃ เกิดจาก {(a₀, b₃x³), (a₁x, b₂x²), (a₂x², b₁x), (a₃x³, b₃)}
                <br><br>
                <b>ตัวอย่าง</b>  ในกรณีที่ ถ้า n=4 และ k=5
                จะได้ว่า c₅ เกิดจาก {
                    (a₀, b₅x⁵), (a₁x, b₄x⁴), (a₂x², b₃x³), (a₃x³, b₂x²), (a₄x⁴, b₁x), (a₅x⁵, b₀)
                }
                <br><br>
                แต่ทั้งนี้ เนื่องจาก n = 4 ดังนั้น aₖ, bₖ ที่ k > 4 จึงไม่มีอยู่จริง  
                <br><br>
                ดังนั้น c₅ จึงควรเกิดจาก {(a₁x, b₄x⁴), (a₂x², b₃x³), (a₃x³, b₂x²), (a₄x⁴, b₁x)}
                <br><br>

                จะได้ว่า 

                $$ c_k = \sum_{l} (a_l) (b_{k-l}) $$ 

                โดย 0 ≤ l ≤ n กรณีที่ 0 ≤ k ≤ n <br>
                และ 0 ≤ k-l ≤ n หรือ n-k ≤ l ≤ k กรณีที่ n < k ≤ 2n 
                <br><br>
                หรือก็คือ 

                $$ c_k = \sum_{l=max(0, k-n)}^{min(n, k)} (a_l) (b_{k-l}) $$ 

                ทั้งนี้ ถ้ากำหนดให้ 

                $$ \forall k > 2n, a_k, b_k = 0 $$ 
                
                จะสามารถ simplify cₖ ได้ โดยไม่สูญเสียนัยทั่วไป (WLOG;without loss of generality) ดังนี้
            
                $$ c_k = \sum_{l=0}^{k} (a_l) (b_{k-l}) $$ 
            </div>

            
            จากตัวอย่างข้างต้น จะได้ว่า

            $$\begin{array}{rcl}
                c_k & = & \sum_{l=0}^{k} (a_l i^l) (a_{k-l} i^{k-l} (-1)^{k-l})\\\\
                & = & (i^k) \sum_{l=0}^{k} (a_l) (a_{k-l} (-1)^{k-l})
            \end{array}$$  

            เมื่อพิจารณา แต่ละพจน์ cₖ สามารถแบ่งได้เป็น 2 กลุ่ม คือ 
            <br><br>
            1. ถ้า k เป็นเลขคู่ พจน์ i จะหายไปเป็น ±1 
            <br><br>
            2. ถ้า k เป็นเลขคี่ 

            <br>
            <br>

            พิจารณา 
            $$ \tag{5.1} c_k = (i) \sum_{l=0}^{k} (a_l) (a_{k-l} (-1)^{k-l}) $$  

            จัดรูป โดยให้ (-1)ᵏ⁻ˡ = (-1)ᵏ(-1)ˡ จะได้ว่า 

            $$ \tag{5.2} c_k = (-i) \sum_{l=0}^{k} (a_l) (a_{k-l} (-1)^{l}) $$  

            และ ถ้าเปลี่ยนตัวแปร l เป็น m = k-l  จาก (5.1) จะได้ว่า

            $$ \tag{5.3}  c_k  = (i) \sum_{m=0}^{k} (a_{k-m}) (a_{m} (-1)^{m})$$ 
            
            เนื่องจาก l เป็นตัวแปรจาก 0 ถึง k <br>
            จะได้ว่า m เป็นตัวแปรจาก k ถึง 0 (หรือ กลับกัน 0 ถึง k)

            <br><br>
            จาก (5.2) และ (5.3) จะได้ว่า

            $$ c_k  = - c_k $$ 

            ซึ่งเป็นไปไม่ได้ ยกเว้น cₖ = 0 

            <br><br>
            นั้นคือ เมื่อ k เป็นเลขคี่ cₖ = 0 เสมอ
            
            <br><br>
            แปลว่า q(x) จะไม่มีพจน์ที่มี coefficeint ที่มี i เลย

            <br><br>
            แปลว่า <i>ถ้า p(x) เป็น integer polynomial แล้ว q(x) เป็น integer polynomial เช่นกัน □</i>

            </div>
        </div>
    </div>
</div>


<hr>

### Step 1 Finding Contradiction target

เพื่อที่จะแสดงว่า $$ q(x) $$ ไม่มีอยู่จริง สิ่งที่เราต้องเตรียม คือ หาจุดที่จะทำให้เกิดข้อขัดแย้ง

เริ่มต้นจาก (5) $$ q(x) = p(ix)p(-ix)$$ และ (4) $$p(\pi) = 0$$ จะได้ว่า 

$$\begin{array}{rcl}
    q(i\pi) & = & p(i*i\pi)p(-i*i\pi)\\\\
    & = & p(-\pi)p(\pi)\\\\
    & = & 0
\end{array}$$  

แปลว่า $$ i\pi $$ เป็นหนึ่งในคำตอบของ $$q(x)$$ 

<hr>

ถ้าให้ $$ \alpha_1, \alpha_2, ..., \alpha_n \in \mathbb{C} $$ เป็นคำตอบทั้งหมดของสมการ $$q(x)=0$$

จะสามารถจัดรูปแบบของ $$q(x)$$ ใหม่เป็น

$$\tag{6} q(x) = a(x-\alpha_1)(x-\alpha_2)...(x-\alpha_n), a \mathrel{\char`≠} 0  $$ 

โดยที่ $$ a \in \mathbb{Z}$$ และกำหนดให้ $$ \alpha_1 = i\pi $$

จาก Euler's identity $$ e^{i\pi}+1 = 0 $$ จะได้ว่า

$$\tag{7} (1+e^{\alpha_1})(1+e^{\alpha_2})...(1+e^{\alpha_n}) = 0  $$ 

เมื่อกระจายพจน์ออกมา จะได้ว่า 

$$\tag{8} e^{\beta_1} + e^{\beta_2}+ ... + e^{\beta_{2^n}} = 0  $$ 

โดยที่ $$\{\beta_i\}$$ เท่ากับ all combinations ที่เป็นไปได้ของ $$\{\alpha_i\}$$

<div class="example my-3 border p-3 bg-light">
    <b>ตัวอย่าง</b> 

    $$\begin{array}{rcl}
        (1+e^2)(1+e^5) & = & (1(1) + 1(e^5) + e^2(1) + e^2(e^5))\\\\
        & = & 1^{sum(\phi)} + e^{sum(\{2\})} + e^{sum(\{5\})} + e^{sum(\{2, 5\})}\\\\
        & = & 1 + e^2 + e^5 + e^7
    \end{array}$$  
</div>

เนื่องจาก $$\beta_i$$ เกิดจากผลรวมของ any combination ของ $$\alpha_i$$ ซึ่งอาจจะมีค่าได้ทั้ง 0 และ ไม่เป็น 0

ถ้ากำหนดให้ $$ \beta_1, \beta_2, ..., \beta_m $$ เป็นเฉพาะ $$\beta$$ ที่ไม่ใช่ 0 จะได้ว่า

$$ \tag{9} r + e^{\beta_1} + e^{\beta_2}+ ... + e^{\beta_m} = 0  $$ 

โดยที่ $$ r = 2^n - m $$ และ $$ r > 0 $$ เนื่องจาก มีอย่างน้อย 1 $$\beta$$ ที่เป็น 0 ซึ่งเกิดจาก empty combination (a.k.a sum($$\phi$$))

<div class="example my-3 border p-3 bg-light">
    Note: <span class="katex-inline">$$\alpha_i$$ และ $$\beta_i$$ เป็นจำนวนเชิงซ้อน (complex number)</span>
</div>

<hr>

ต่อไป เราจะประมาณ $$ e^{\beta_k} $$  โดยให้

$$ e^{\beta_k} = \frac{N_k + \delta_k}{N}  $$ 

โดย $$ N \in \mathbb{Z} $$ จะเป็นจำนวนเต็ม 

และ $$ N_k \in \mathbb{C} $$, $$ \delta_k ≈ 0 $$ เป็นค่าเล็กๆค่านึงใกล้ๆ 0

ซึ่งจะทำให้สมการ (9) เปลี่ยนไป

$$\begin{array}{rcl}
    r + e^{\beta_1} + e^{\beta_2}+ ... + e^{\beta_m}  & = & 0\\\\
    r + \frac{N_1 + \delta_1}{N} + \frac{N_2 + \delta_2}{N}+ ... + \frac{N_m + \delta_m}{N}  & = & 0 \\\\
    rN + (N_1+N_2+...+N_m)+ (\delta_1+\delta_2+...+\delta_m)  & = & 0
\end{array}$$  

สรุปได้ว่า

$$ \tag{10} rN + (N_1+...+N_m)+ (\delta_1+...+\delta_m) = 0  $$ 

ถ้าสามารถออกแบบ $$ N $$, $$ N_k $$ และ $$ delta_k $$ ที่ทำให้ 

1. rN + (N₁+...+Nₘ) ≠ 0  
2. (δ₁+...+δₘ) ≈ 0

หรือก็ คือ ผลรวมของส่วนที่ rN + (N₁+...+Nₘ) ไม่เป็น 0 และ (δ₁+...+δₘ) จะไม่สามารถไปหักล้าง ส่วนที่เหลือจนเป็น 0 ได้ จะได้ว่า

$$ \tag{11} rN + (N_1+...+N_m)+ (\delta_1+...+\delta_m) \mathrel{\char`≠} 0  $$ 

และเนื่องจาก (10) และ (11) เป็นจริงพร้อมกันไม่ได้ เท่ากับว่า เราได้ข้อขัดแย้งที่ต้องการแล้ว...

<div class="example my-3 border p-3 bg-light">
    Note: อย่าลืมว่า ตอนนี้ยังไม่เสร็จสิ้นนะ เพราะเรายังไม่มี N, Nₖ และ δₖ ที่มีคุณสมบัติตามที่เราต้องการ
</div>

<hr>

### Step 2 Define N, Nₖ และ δₖ

ทบทวนเงื่อนไขของ  $$ N $$, $$ N_k $$ และ $$ delta_k $$ กันอีกครั้ง

* N เป็นจำนวนเต็ม ที่ไม่เท่ากับ 0

$$\tag{cond 1} N \in \mathbb{Z}, N \mathrel{\char`≠} 0 $$

* $$ N $$, $$ N_k $$ และ $$ delta_k $$ ต้องทำให้ความสัมพันธ์เหล่านี้เป็นจริง

$$\tag{cond 2} e^{\beta_k} = \frac{N_k + \delta_k}{N} $$

$$\tag{cond 3} rN + (N_1+N_2+...+N_m) \mathrel{\char`≠} 0  $$

$$\tag{cond 4} \delta_1+\delta_2+...+\delta_m \approx 0  $$

<hr>
#### แรงบันดาลใจ

เพื่อออกแบบ $$ N $$, $$ N_k $$ และ $$ \delta_k $$ ให้ได้ตามเงื่อนไขข้างต้น ในบทพิสูจน์ต้นฉบับ (น่าจะ)ได้หยิบยืมแรงบรรดาลใจมาจาก Tayler Expansion ของ function $$e^x$$

$$\begin{array}{rcl}
    e^x  & = & \sum_{n=0}^{\infty} \frac{x^n}{n!} \\\\
    & = & \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + ... \\\\
    & = & \frac{1 + x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + ... \\\\
    & = & \frac{2 + 2x + x^2}{2!} + \frac{x^3}{3!} + ... \\\\
    & = & \frac{6 + 6x + 3x^2 + x^3}{3!} + \frac{\delta}{3!}
\end{array}$$  

จะเห็นได้ว่า $$ e^{x} $$ สามารถจัดอยู่ในรูปแบบคล้ายๆกับสิ่งที่เราต้องการได้

$$ e^{x} = \frac{N(x) + \delta(x)}{p!} $$

เราพออนุมาณได้ว่า เราควรนิยาม $$ N = p! $$

ทั้งนี้ทั้งนั้น เนื่องจากเราคำนวนอยู่กับ complex number ตัวเลือกที่ดีกว่าของ $$p!$$ คือ Gamma function โดยมีนิยามดังนี้ 

$$\begin{array}{rcl}
    \Gamma(z+1)  & = & \int_{0}^{\infty} e^{-t}t^{z} dt \\\\
    & = & z!
\end{array}$$ 

<hr>

#### ออกแบบ N

จากแรงบันดาลใจข้างต้น D. Hilbert จึงเลือกใช้ N ตามนิยามต่อไปนี้

$$ \tag{12} N = \frac{1}{(p-1)!} \int_{0}^{\infty} e^{-z} f(z) dz $$

โดยที่ 

$$ \tag{13} f(z) = z^{p-1} g^p(z) $$

และ $$ g(z) $$ เป็น integer polynomial ที่จะนิยามเพิ่มเติมต่อไป และ p คือ จำนวนเฉพาะขนาดใหญ่ตัวนึง ที่จะนิยามเงื่อนไขต่อไปเช่นกัน

ที่น่าสนใจ คือ เนื่องจาก กำหนดให้ $$ g(z) $$ เป็น integer polynomial จะได้ว่า $$f(z)$$ เป็น integer polynomial เช่นกัน สามารถเขียนแทนด้วย

$$ \tag{14} f(z) = \sum_{k=0}^{n} b_k z^k, b_0 \mathrel{\char`≠} 0 $$

<div class="example my-3 border p-3 bg-light">
    Note: <span class="katex-inline">ถ้า $$b_0 = 0 $$ แปลว่า เราสามารถหาร $$f(z)$$ ด้วย z แล้วก็จะได้ $$b_1 \mathrel{\char`≠} 0 $$ แทน  $$b_0 $$ นั้นคือ ใน $$f(z)$$  ที่เป็น integer polynomial จะจัดรูปให้มี $$b_0 \mathrel{\char`≠} 0 $$ ได้เสมอ</span>
</div>

แทนค่า $$f(z)$$ จาก (14) ลงใน (12) จะได้ว่า

$$\begin{array}{rcl}
    \int_{0}^{\infty} e^{-z} f(z) dz  
    & = & \int_{0}^{\infty} e^{-z} z^{p-1}(\sum_{k=0}^{n} b_k z^k) dz   \\\\
    & = & \sum_{k=0}^{n} b_k (\int_{0}^{\infty} e^{-z} z^{k+p-1} dz) \\\\
    & = & \sum_{k=0}^{n} b_k (k+p-1)! \\\\
\end{array}$$ 

ดังนั้น

$$\begin{array}{rcl}
    N 
    & = & \frac{1}{(p-1)!} \sum_{k=0}^{n} b_k (k+p-1)! \\\\
    & = & \frac{1}{(p-1)!} [b_0*(p-1)! + b_1*(p)! + b_2*(p+1)! + ... + b_n*(n+p-1)!] \\\\
    & = & b_0 + b_1*(p) + b_2*(p+1)(p) + ... + b_n*(n+p-1)(n+p)(...)(p) \\\\
    & = & b_0 + (p)(b_1* + b_2*(p+1) + ... + b_n*(n+p-1)(n+p)(...)(p-1)) \\\\
\end{array}$$ 


<div class="example my-3 border p-3 bg-light">
    Note: assume k ≥ 0 หรือ g(z) เป็น integer polynomial ดีกรีมากว่า 0
</div>

จากสมการข้างต้น สามารถจัดรูปได้เป็น

$$ N = b_0 + p * (SOME\:INTEGER)$$ 

เนื่องจาก bₖ, p ทั้งหมดต่างเป็นตำนวนเต็ม จะได้ว่า N ก็เป็นจำนวนเต็มเช่นกัน

$$ \tag{15} N \in \mathbb{Z} $$

และ เนื่องจากเราสามารถเลือก p เป็นจำนวนเฉพาะอะไรก็ได้ ดังนั้น 

*"ถ้าเลือก p เป็นจำนวนเฉพาะที่ใหญ่กว่า b₀"*

จะได้ว่า $$p \nmid b_0$$ ทำให้ N เป็นจำนวนเต็มที่ไม่สามารถหารได้ด้วย p ลงตัว

$$ \tag{15.1} p \nmid N $$

นอกจากนี้ เนื่องจาก b₀ ≠ 0 จะได้ว่า N ไม่เท่ากับ 0 (พิสูจน์ได้ด้วย contradiction)

$$ \tag{15.2} N \mathrel{\char`≠} 0 $$


และ *ถ้าเลือก p เป็นจำนวนเฉพาะที่ใหญ่กว่า r (และใหญ่กว่า b₀)* 

จะได้ว่า rN เป็นจำนวนเต็มที่ไม่สามารถหารได้ด้วย p ลงตัว //จะมีประโยชน์ในตอนที่จะทำให้ (cond 3) เป็นจริง

$$ \tag{15.3} p \nmid rN $$

จากทั้งหมด สรุปได้ว่า 

*N จะต้องเป็นจำนวนเต็ม ที่ไม่เท่ากับ 0* 

ตรงตาม (cond 1) ✅ 

<hr>

#### ออกแบบ Nₖ และ δₖ

เพื่อเป็นไปตามเงื่อนไขที่ต้องการ D. Hilbert เลือกใช้

$$ \tag{16} N_k = \frac{e^{\beta_k}}{(p-1)!} \int_{\beta_k}^{\infty} e^{-z} f(z) dz $$

$$ \tag{17} \delta_k = \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\beta_k} e^{-z} f(z) dz $$

สังเกตได้ว่า $$N_k$$ และ $$ \delta_k $$ มาจากการแบ่ง Limits of integration เป็น 2 ส่วน แค่นั้นเอง 

ทั้งนี้ทั้งนั้น จะเห็นได้ว่า

$$\begin{array}{rcl}
    \delta_k +  N_k 
    & = & \frac{e^{\beta_k}}{(p-1)!} (\int_{0}^{\beta_k} e^{-z} f(z) dz + \int_{\beta_k}^{\infty} e^{-z} f(z) dz) \\\\
    & = & \frac{e^{\beta_k}}{(p-1)!} (\int_{0}^{\infty} e^{-z} f(z) dz) \\\\
    & = & e^{\beta_k} N \\\\
\end{array}$$ 

ตรงตาม (cond 2) ✅ 

แต่ แต่ แต่ สมการข้างต้นถูกต้อง เฉพาะในกรณีที่เราใช้ $$\beta_k$$ เป็นจำนวนจริงเท่านั้น แต่ในกรณีนี้ $$\beta_k$$ สามารถเป็นจำนวนเชิงซ้อนได้ วิธีการข้างต้นจึงไม่ถูกต้องซะทีเดียว

<div class="accordion mb-3" id="accordion3">
    <div class="card border">
        <div class="card-header" id="accordion3-heading">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left p-0" type="button" data-toggle="collapse" data-target="#accordion3-collapse" aria-expanded="true" aria-controls="accordion3-collapse"> 
                Lemma #2:  <span class="katex-inline">$$ \delta_k +  N_k  = e^{\beta_k} N $$ เป็นจริงแม้ว่า $$\beta_k \in \mathbb{Z}$$</span></button>
            </h2>
        </div>
        <div id="accordion3-collapse" class="collapse border" aria-labelledby="accordion3-heading" data-parent="#accordion3">
            <div class="card-body"> 

                สารภาพเลยว่า ส่วนตัวไม่ค่อยรู้เรื่อง Integration บนระบบจำนวนเชิงซ้อนมาก คำอธิบายส่วนใหญ่ในส่วนนี้ จะเอามาจาก ChatGPT + อ่านเองเพิ่มเติม ซึ่งอาจจะมีส่วนผิดอยู่บ้าง //ขออภัยไว้ล่วงหน้า
                <br><br>

                ถ้าเป็น Integration บนระบบจำนวนจริง การแบ่ง Limits of integration สามารถทำได้เลย โดยไม่มีปัญหาอะไร เนื่องจากระบบมีลักษณะเป็น 1 มิติ นั้นคือ มีเส้นทางที่เป็นไปได้แค่เส้นเดียวจากจุด A ไป B

                <br><br>
                
                แต่ในระบบจำนวนเชิงซ้อน เนื่องจากระบบมีลักษณะเป็น 2 มิติ มีเส้นทางที่เป็นไปได้มากกว่า 1 เส้นจากจุด A ไป B

                {% include aligner.html images="pi-is-transcendental/complex-integration2.png" column=1 %}

                แปลว่า เราต้องระบุอย่างชัดเจนว่า Nₖ และ δₖ มาจาก intregration จาก path ไหน (หรือ path independence) และมันยังให้ความสัมพันธ์เดิมแบบที่เราต้องการหรือไม่

                <br><br>

                กลับมาที่นิยามเดิม
                
                $$ N_k = \frac{e^{\beta_k}}{(p-1)!} \int_{\beta_k}^{\infty} e^{-z} f(z) dz $$
                
                กำหนดให้ Nₖ เป็น integrate จาก เส้นนอนตรงๆ จาก βₖ ถึง +∞ (along the horizontal line from βₖ to +∞)

                $$ \delta_k = \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\beta_k} e^{-z} f(z) dz $$
                
                กำหนดให้ δₖ เป็น integrate จาก เส้นรัศมีจาก 0 ถึง βₖ (along the radial path from 0 to βₖ)

                <br><br>

                <b>พิสูจน์</b>
                <br><br>

                กำหนดให้มี path γ เป็นเส้นทางปิด (a closed contour) จาก 0 ถึง βₖ ถึง βₖ+T ถึง T แล้วกลับมาที่ 0 ตามรูป

                {% include aligner.html images="pi-is-transcendental/complex-integration3.png" column=1 %}

                จาก <a target="_blank" href="https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem">Cauchy’s theorem</a> 

                <br><br>
                <div class="example my-3 border p-3 bg-light">
                ถ้า φ(z) เป็นฟังก์ชั่นที่ analytic (holomorphic) ทุกๆที่ภายในและบนเส้นทางปิด C ใดๆ (inside and on a simple closed contour C) แล้ว

                $$ \oint_{C} \phi(z)dz = 0 $$
                </div>

                เนื่องจาก <span class="katex-inline">$$ e^{-z} f(z) $$ เป็นฟังก์ชั่นที่ analytic ทุกๆที่บน  $$ \mathbb{C}$$ ดังนั้น</span> เขียนได้ว่า 

                $$ \oint_{\gamma} e^{-z} f(z) dz = 0 $$

                แปลว่า 

                $$ \int_{0}^{T} e^{-z} f(z) dz + \int_{T}^{\beta_k+T} e^{-z} f(z) dz = \int_{0}^{\beta_k} e^{-z} f(z) dz + \int_{\beta_k}^{\beta_k+T} e^{-z} f(z) dz  $$

                เมื่อใส่ลิมิต T เข้าใกล้ +∞ จะได้ว่า

                $$ \int_{0}^{\infty} e^{-z} f(z) dz  = \int_{0}^{\beta_k} e^{-z} f(z) dz + \int_{\beta_k}^{\infty} e^{-z} f(z) dz  $$

                เพิ่มค่าคงที่ และจัดรูปนิดหน่อย

                $$ \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\infty} e^{-z} f(z) dz  = \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\beta_k} e^{-z} f(z) dz + \int_{\beta_k}^{\infty} e^{-z} f(z) dz  $$

                จัดรูปอีกครั้ง 

                $$ e^{\beta_k} N = \delta_k + N_k $$

                <br><br>


                <i>ตรงตาม (cond 2) แม้ว่าจะใช้งานบนระบบจำนวนเชิงซ้อน □</i>


            </div>
        </div>
    </div>
</div>

<hr>

#### คุณสมบัติของ Nₖ

ทบทวนนิยามของ Nₖ กันอีกครั้ง 

จาก (16)

$$ N_k = \frac{e^{\beta_k}}{(p-1)!} \int_{\beta_k}^{\infty} e^{-z} f(z) dz $$

จาก (13) 

$$ f(z) = z^{p-1} g^p(z) $$ 

โดยมี $$g(z)$$ เป็น integer polynomial ที่มีดีกรีมากกว่า 0

<hr>

ถึงเวลาที่จะกลับมานิยาม $$g(z)$$ กันแล้ว

ตามต้นฉบับ D.Hilbert เลือกใช้ 

$$ \tag{18} g(z) = a^m (z-\beta_1)(z-\beta_2)...(z-\beta_m)$$

โดยใช้ a, m, $$\{\beta_i\}$$ จาก (6) และ (9)

<div class="accordion mb-3" id="accordion4">
    <div class="card border">
        <div class="card-header" id="accordion4-heading">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left p-0" type="button" data-toggle="collapse" data-target="#accordion4-collapse" aria-expanded="true" aria-controls="accordion4-collapse"> 
                Lemma #3:  <span class="katex-inline">$$ g(z) = a^m (z-\beta_1)(z-\beta_2)...(z-\beta_m)$$ เป็น integer polynomial</span></button>
            </h2>
        </div>
        <div id="accordion4-collapse" class="collapse border" aria-labelledby="accordion4-heading" data-parent="#accordion4">
            <div class="card-body"> 

                ส่วนตัวมีความเห็นว่า ส่วนนี้เป็นส่วนที่งงที่สุดในบทพิสูจน์นี้เลยทีเดียว ส่วนนึงเพราะ เขาใช้สิ่งที่เรียกว่า  <b>the elementary symmetric polynomials</b> ซึ่งนี่ไม่เคยรู้จักมาก่อน ทั้งๆที่เป็นคอนเซปที่เรียบง่ายมากๆ

                <br><br>
                ขอย้อนกลับไปดูนิยามของ q(x) ใน (6)

                $$q(x) = a(x-\alpha_1)(x-\alpha_2)...(x-\alpha_n) $$ 

                ซึ่งสามารถกระจายออกมาได้เป็น

                $$ \begin{array}{rcl}
                    q(x) & = & ax^n \\\\
                    & - & a(\alpha_1+\alpha_2+...+\alpha_n)x^{n-1} \\\\
                    & + & a(\alpha_1\alpha_2+\alpha_1\alpha_3+...+\alpha_2\alpha_3+...+\alpha_{n-1}\alpha_n)x^{n-2}\\\\
                    & - & a\sum_{1\le i\lt j\lt k\le n}(\alpha_i\alpha_j\alpha_k) x^{n-2} \\\\
                    & + & ... \\\\
                    & + & (-1)^n a(\alpha_1\alpha_2...\alpha_n) \\\\
                \end{array} $$ 

                <div class="example my-3 border p-3 bg-light">
                    <b>ตัวอย่าง</b> กำหนด q(x) มี α₁, α₂ และ α₃ เป็นคำตอบของสมการ จะได้ว่า

                    $$\begin{array}{rcl}
                        q(x) & = & (x-\alpha_1)(x-\alpha_2)(x-\alpha_3) \\\\
                            & = & (x^2-\alpha_2x-\alpha_1x+\alpha_1\alpha_2)(x-\alpha_3) \\\\
                            & = & (x^3-\alpha_2x^2-\alpha_1x^2+\alpha_1\alpha_2x-\alpha_3x^2+\alpha_2\alpha_3x+\alpha_1\alpha_3x+\alpha_1\alpha_2\alpha_3) \\\\
                            & = & (x^3-(\alpha_1+\alpha_2+\alpha_3)x^2+(\alpha_1\alpha_2+\alpha_2\alpha_3+\alpha_1\alpha_3)x+(\alpha_1\alpha_2\alpha_3))
                    \end{array}$$  
                </div>

                แก้ไขปรับให้ดูสวยงามขึ้น ดังนี้

                $$ \begin{array}{rcl}
                    q(x) & = & a(x^n - e_1 x^{n-1} + e_2 x^{n-2}-...+(-1)^n e_n) \\\\
                    e_1 & = & \sum_{1\le i \le n} \alpha_i \\\\
                    e_2 & = & \sum_{1\le i \lt j \le n} \alpha_i\alpha_j \\\\
                    ... \\\\
                    e_n & = & \alpha_1\alpha_2...\alpha_n \\\\
                \end{array} $$ 

                โดยเราจะเรียกเจ้า {e₁, e₂, ..., eₙ} คือ the elementary symmetric polynomials ของคัวแปร {α₁, α₂, ..., αₙ} 

                <br><br>

                ซึ่งเจ้าสิ่งนี้ มีคุณสมบัติพิเศษ คือ ถึงแม้ว่าจะสลับ {αᵢ} ยังไง ก็จะได้ {eᵢ} เหมือนเดิมเสมอ (สมมาตรบน {αᵢ})!! 

                <br><br>

                แต่ที่สำคัญกว่า คือ เนื่องจากเรานิยามว่า q(x) เป็น integer polynomial แปลว่า coefficient ทุกตัวของ q(x) จะต้องเป็นจำนวนเต็ม แปลว่า

                $$ \tag{18.1} {e_1, e_2, ..., e_n} \in \mathbb{Z}$$

                นอกจากนี้ จาก <a target="_blank" href="https://en.wikipedia.org/wiki/Elementary_symmetric_polynomial">the Fundamental Theorem of Symmetric Polynomials (FTSP)</a> 

                <div class="example my-3 border p-3 bg-light">

                    <span class="katex-inline">พหุนามสมมาตรใดๆ (symmetric polynomial) ใน $$\{\alpha_i\}$$ ​สามารถเขียนใหม่ได้ ให้อยู่ในรูปของพหุนามสมมาตรเชิงมูลฐาน (the elementary symmetric polynomials) $$\{e_i\}$$
                    </span>
                </div>

                <div class="example my-3 border p-3 bg-light">
                    <b>ตัวอย่าง</b> กำหนด q(x) มี α₁, α₂ และ α₃ เป็นคำตอบของสมการ ต้องการหา $$\alpha_1^2+\alpha_2^2+\alpha_3^2$$

                    <span class="katex-inline">จะเห็นว่า $$\alpha_1^2+\alpha_2^2+\alpha_3^2$$ เป็น symmetric polynomial เนื่องจาก ถ้าสลับ ($$\alpha_i$$, $$\alpha_j$$) ใดๆ ก็ไม่ทำให้สมการเปลี่ยนไป</span>


                    ถ้าให้ e₁, e₂ และ e₃ เป็น the elementary symmetric polynomials ของ α จะได้ว่า

                    $$ e_1 = \alpha_1 + \alpha_2 + \alpha_3$$
                    $$ e_2 = \alpha_1\alpha_2 + \alpha_1\alpha_3 + \alpha_2\alpha_3$$
                    $$ e_3 = \alpha_1\alpha_2\alpha_3$$

                    ดังนั้น 
                    $$ \begin{array}{rcl}
                        e_1^2 & = & (\alpha_1 + \alpha_2 + \alpha_3)^2 \\\\
                        & = & \alpha_1^2+\alpha_2^2+\alpha_2^2 + 2(\alpha_1\alpha_2 + \alpha_1\alpha_3 + \alpha_2\alpha_3) \\\\
                        & = & \alpha_1^2+\alpha_2^2+\alpha_2^2 + 2(e_2) \\\\
                        \alpha_1^2+\alpha_2^2+\alpha_2^2 & = & e_1^2 - 2e_2
                    \end{array} $$ 

                </div>

                ย้อนกลับมาดูที่ฟังก์ชั่นต้นเรื่อง g(z) จาก (18)

                $$ g(z) = a^m (z-\beta_1)(z-\beta_2)...(z-\beta_m)$$

                จะเห็นว่า g(z) มีความสมมาตรบน {βᵢ} เนื่องจาก ถึงแม้ว่าเราจะสลับ (βᵢ, βⱼ) ใดๆ ก็ไม่ทำให้สมการเปลี่ยนไป

                <br><br>

                และ เพราะว่า {βᵢ} เกิดจาก "ผลรวมของ any combination ของ αᵢ" ก็สรุปได้ว่า g(z) มีความสมมาตรบน {αᵢ} ด้วยเหมือนกัน

                <br><br>
                ดังนั้น coefficents ของ g(z) ก็จะถือว่าเป็น symmetric polynomial บน {αᵢ} ทำให้สามารถใช้ FTSP ได้ว่า 

                <br><br>
                <i>coefficents ของ g(z) จะต้องอยู่ในรูปของพหุนามของ the elementary symmetric polynomials ของ {αᵢ}</i>

                <br><br>

                และจาก (18.1) ซึ่งบอกว่า the elementary symmetric polynomials ของ {αᵢ} เป็นจำนวนเต็ม จะได้ว่า coefficents ของ g(z) ก็ต้องเป็นจำนวนเต็มเช่นกัน

                <div class="example my-3 border p-3 bg-light">

                    ทั้งหมดนี้ ไม่ได้บอกว่า {αᵢ} หรือ {βᵢ} เป็นจำนวนเต็มนะ แต่บอกแค่ว่า coefficents ของ g(z) ซึ่งเกิดจาก {βᵢ} มายำรวมๆกัน จะต้องลงเอยเป็นจำนวนเต็ม

                    เช่น {βᵢ} อาจจะเป็น {β₁ = π+4, β₂ = π²} และ cₖ = (β₁*β₁-β₂-8β₁) เมื่อเราบวกลบๆแล้ว จะได้ว่า cₖ = 64 
                </div>

                จากทั้งหมดนี้ จึงสรุปได้ว่า <i>g(z) จะต้องเป็น integer polynomial □</i>

            </div>
        </div>
    </div>
</div>

กลับมาพิจารณา $$N_k$$ ต่อ

$$ N_k = \frac{e^{\beta_k}}{(p-1)!} \int_{\beta_k}^{\infty} e^{-z} f(z) dz $$

จัดรูป $$N_k$$ 

$$ N_k = \frac{1}{(p-1)!} \int_{\beta_k}^{\infty} e^{\beta_k-z} f(z) dz $$

แทน $$w = \beta_k-z$$ จะได้ว่า

$$ N_k = \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} f(w+\beta_k) dw $$

พิจารณา $$f(w+\beta_k)$$ จาก (13) และ $$g(w+\beta_k)$$ จาก (18)

$$ \begin{array}{rcl}
    f(w+\beta_k) & = & (w+\beta_k)^{p-1} g^p(w+\beta_k) \\\\
    & = &  (w+\beta_k)^{p-1} (a^m \prod_{i=1}^{m}(w + \beta_k -\beta_i))^p \\\\
    & = &  (w+\beta_k)^{p-1} a^{mp} w^p \prod_{i=1, i \mathrel{\char`≠} k}^{m}(w + \beta_k -\beta_i) \\\\
\end{array} $$ 

จากการจัดรูป และแทน $$f(w+\beta_k) = w^p F(w, \beta_k) $$ จะได้ว่า

$$ \begin{array}{rcl}
    N_k & = & \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} f(w+\beta_k) dw \\\\
    & = &  \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} w^p F(w, \beta_k) dw \\\\
\end{array} $$ 

ปัญหา คือ ถึงแม้ว่า $$F(w, \beta_k)$$ จะเป็น polynomial แต่มัน(อาจจะ)ไม่ใช่ integer polynomial เราจึงไม่สามารถสรุปได้เหมือน (15)

<hr>

เพื่อแก้ปัญหานี้ ขอย้อนกลับไปที่จุดตั้งต้น ที่ (cond 3)

สิ่งที่เราต้องการพิสูจน์ คือ

$$ rN + (N_1+N_2+...+N_m) \mathrel{\char`≠} 0  $$

แปลว่า สิ่งที่เราสนใจ คือ $$N_1+N_2+...+N_m$$ ไม่ใช่แค่ $$N_k $$

แทนค่า $$f(w+\beta_k)$$ ไปอีกครั้ง จะได้ว่า 

$$ \begin{array}{rcl}
    N_1+N_2+...+N_m & = & \sum_{k=1}^{m} \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} f(w+\beta_k) dw \\\\
    & = &  \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} \{\sum_{k=1}^{m} f(w+\beta_k)\} dw \\\\
    & = &  \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} h(w) dw \\\\
\end{array} $$ 

โดยมี

$$ \begin{array}{rcl}
    h(w) & = & \sum_{k=1}^{m} f(w+\beta_k) \\\\
    & = &  \sum_{k=1}^{m} w^p F(w, \beta_k) \\\\
    & = &  w^p (\sum_{k=1}^{m} F(w, \beta_k))\\\\
    & = &  w^p H(w)
\end{array} $$ 

ถึงแม้ว่า $$ F(w+\beta_k) $$ แค่อย่างเดียว ไม่ได้สมมาตรบน {βᵢ}<sup id="fnref:6"><a href="#fn:6">6</a></sup> แต่ $$H(w) = \sum_{k=1}^{m} F(w, \beta_k) $$ สมมาตรบน {βᵢ} 

เราจึงสามารถใช้เหตุผลแบบเดียวกับที่พิสูจน์ว่า $$ g(z) $$ เป็น integer polynomial จะได้ว่า $$H(w)$$ ก็เป็น integer polynomial เช่นกัน 

จึงจะสรุปได้ว่า

$$ \tag{19} H(w) = \sum_{k=0}^{n} c_k w^k $$

แทนกลับ

$$ \begin{array}{rcl}
    N_1+N_2+...+N_m & = & \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} h(w) dw \\\\
    & = &  \frac{1}{(p-1)!} \int_{0}^{\infty} e^{w} w^p H(w) dw \\\\
    & = &  \frac{1}{(p-1)!} \sum_{k=0}^{n} \int_{0}^{\infty} e^{w} w^p (c_k w^k) dw \\\\
    & = &  \frac{1}{(p-1)!} (\sum_{k=0}^{n} c_k (p+k)!) \\\\
    & = &  \frac{p!}{(p-1)!} (c_0 + c_1(p+1) + c_2(p+2)(p+1) + ...+ c_n(p+n)(...)(p+1))\\\\
    & = &  p (c_0 + c_1(p+1) + c_2(p+2)(p+1) + ...+ c_n(p+n)(...)(p+1))
\end{array} $$ 

เนื่องจาก $$c_k$$, p ทั้งหมดต่างเป็นตำนวนเต็ม จะได้ว่า $$N_1+N_2+...+N_m$$ ก็เป็นจำนวนเต็มเช่นกัน

$$ \tag{20} N_1+N_2+...+N_m \in \mathbb{Z} $$

และที่สำคัญ คือ p เป็นตัวประกอบของ $$N_1+N_2+...+N_m$$

$$ \tag{21} p \mid N_1+N_2+...+N_m $$

ย้อนกลับไป (15.3) จะเห็นว่า

$$ p \nmid rN $$

<div class="accordion mb-3" id="accordion5">
    <div class="card border">
        <div class="card-header" id="accordion5-heading">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left p-0" type="button" data-toggle="collapse" data-target="#accordion5-collapse" aria-expanded="true" aria-controls="accordion5-collapse"> 
                Lemma #4: <span class="katex-inline">$$ rN + N_1+N_2+...+N_m \mathrel{\char`≠} 0 $$</span></button>
            </h2>
        </div>
        <div id="accordion5-collapse" class="collapse show border" aria-labelledby="accordion5-heading" data-parent="#accordion5">
            <div class="card-body"> 
            
            กำหนดให้ <span class="katex-inline">$$ A = rN, B = N_1+N_2+...+N_m $$</span>

            <br><br>
            จาก (15.3) และ (21) เราสามารถเขียนได้ว่า

            $$ p \nmid A $$ 
            $$ p \mid B $$ 

            ถ้าให้ A+B = 0 แปลว่า A = -B 
            <br><br>

            เพราะ <span class="katex-inline"> $$ p \mid B $$  ดังนั้น $$p \mid -B $$ และ $$p \mid A $$ </span>

            <br><br>

            ดังนั้น <span class="katex-inline"> $$A+B \mathrel{\char`≠} 0$$ </span>

            <br><br>
            สรุป <i>rN + N₁+N₂+...+Nₘ ≠ 0 □ </i>

            </div>
        </div>
    </div>
</div>

จาก Lemma #4 จึงได้ข้อสรุปว่า  *rN + N₁+N₂+...+Nₘ ที่ไม่เท่ากับ 0* 

ตรงตาม (cond 3) ✅ 

<hr>

#### คุณสมบัติของ δₖ

เช่นเดียวกับ Nₖ ขอเริ่มต้นด้วยการทบทวนนิยามของ δₖ กันอีกครั้ง 

จาก (17)

$$ \begin{array}{rcl}
    \delta_k & = & \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\beta_k} e^{-z} f(z) dz \\\\
    & = &  \frac{1}{(p-1)!} \int_{0}^{\beta_k} e^{\beta_k-z} f(z) dz 
\end{array} $$ 


โดยที่ $$ f(z) = z^{p-1} g^p(z) $$ และ $$ g(z) = a^m \prod_{i=1}^{m}(z - \beta_i) $$

<hr>

สิ่งที่เราต้องการ คือ ประมาณค่าของ $$ \delta_k $$ เพื่อจะบอกว่า $$ \delta_k \approx 0$$ 

เริ่มต้นจาก กำหนดให้ $$ M = max(\|\beta_k\|)$$ และ เนื่องจากเรา integrate $$dz$$ จาก $$0 \to \beta_k$$

จะได้ว่า $$ 0 \le \|z\| \le M$$ ดังนั้น $$ \|z^{p-1}\| \le M^{p-1}$$

และ $$ \|z - \beta_i\| \le 2M $$ ดังนั้น $$ g(z) \le \|a\|^m(2M)^m $$

จะได้ว่า

$$ \tag{22} f(z) \le M^{p-1}(\|a\|^m(2M)^m)^p $$

<hr>

ต่อมา เมื่อพิจารณาส่วนของ integration จะได้ว่า $$dz: 0 \to \beta_k \le M$$ และ  $$e^{\beta_k-z} \le e^M$$


$$ \begin{array}{rcl}
    \delta_k & = & \frac{1}{(p-1)!} \int_{0}^{\beta_k} e^{\beta_k-z} f(z) \\\\
    & \le & \frac{M e^M M^{p-1}(|a|^{mp}(2M)^{mp}) }{(p-1)!}
\end{array} $$ 

สิ่งที่เกิดขึ้น คือ 

$$ \begin{array}{rcl}
    \delta_k & \le & C \frac{D^{p}}{(p)!}
\end{array} $$ 

โดยที่ $$ C = e^M $$ และ $$ D = M^{m+1} \|a\|^m (2)^m $$

จะเห็นได้ว่า ถ้า $$ p \to \infty $$ แล้ว $$\delta_k \to 0 $$

<hr>

หรือ พิสูจน์ได้ด้วย the ratio test ดังนี้ 

$$ \begin{array}{rcl}
    \frac{\delta_{k, p+1}}{\delta_{k, p}} \\\\
    & = & \frac{D^{p+1}}{(p+1)!} * \frac{(p)!}{D^{p}} \\\\
    & = & \frac{D}{p+1} \\\\
\end{array} $$ 

ถ้าให้ $$p \to \infty $$ แล้ว $$ \frac{\delta_{k, p+1}}{\delta_{k, p}} \to 0 $$ 

<hr>

สรุปได้ว่า $$ delta_k \approx 0$$ 

แปลว่า 

$$ \tag{23} \delta_1+\delta_2+...+\delta_m \approx 0 $$


จึงได้ข้อสรุปว่า  *δ₁+δ₂+...+δₘ ค่าเล็กๆค่านึงใกล้ๆ 0* 

ตรงตาม (cond 4) ✅ 

<hr>
#### สรุป

สรุปจากเนื้อหาทั้งหมด เราเริ่มจาก

1. นิยาม จำนวนอดิศัย คือ ตัวเลขที่จะไม่เป็นคำตอบของสมการพนุนามดีกรีใดๆ ที่มี coefficents เป็นจำนวนเต็ม
2. กำหนดให้มีพนุนาม p(x) ที่ทำให้ p(π)=0
3. จาก p(x) นำไปสู่การนิยาม q(x) = p(ix)p(-ix) และ q(iπ) = 0
4. นิยาม {α₁, α₂, ..., αₙ} เป็นคำตอบของ q(x)=0
5. นิยาม {β₁​, β₂​, ..., βₘ} เป็น all combinations ที่เป็นไปได้ของ $$\{\alpha_i\}$$ ที่ไม่เท่ากับ 0
6. เราพบว่า <span class="katex-inline">$$ r + e^{\beta_1} + e^{\beta_2}+ ... + e^{\beta_{m}} = 0  $$ </span>
7. เราบอกว่าเราสามารถเปลี่ยน <span class="katex-inline">$$ e^{\beta_k} = \frac{N_k + \delta_k}{N}  $$ </span>
8. ดังนั้น <span class="katex-inline">$$ rN + (N_1+N_2+...+N_m) + (\delta_1+\delta_2+...+\delta_m) = 0  $$ </span>
9. นิยาม N, Nₖ และ δₖ โดยมี p เป็นจำนวนเฉพาะที่มากกว่า g(0) และ r
    * <span class="katex-inline">$$ N = \frac{1}{(p-1)!} \int_{0}^{\infty} e^{-z} f(z) dz  $$ </span>
    * <span class="katex-inline">$$ N_k = \frac{e^{\beta_k}}{(p-1)!} \int_{\beta_k}^{\infty} e^{-z} f(z) dz  $$ </span>
    * <span class="katex-inline">$$ \delta_k = \frac{e^{\beta_k}}{(p-1)!} \int_{0}^{\beta_k} e^{-z} f(z) dz $$ </span>
    * <span class="katex-inline">$$ f(z) = z^{p-1} g^p(z) $$ </span>
    * <span class="katex-inline">$$ g(z) = a^m (z-\beta_1)(z-\beta_2)...(z-\beta_m) $$ </span>

10. เราพบว่า rN เป็น จำนวนเต็มที่ไม่เท่ากับ 0 และ p หารไม่ลงตัว
11. เราพบว่า <span class="katex-inline">$$ (N_1+N_2+...+N_m) $$ </span> เป็นจำนวนเต็มที่ p หารลงตัว
12. เราพบว่า <span class="katex-inline">$$ rN + (N_1+N_2+...+N_m) > 0  $$ </span>
13. เราพบว่า ถ้าเลือก p ใหญ่ๆ จะทำให้ <span class="katex-inline">$$ (\delta_1+\delta_2+...+\delta_m) \approx 0  $$ </span>

14. ดังนั้น <span class="katex-inline">$$ rN + (N_1+N_2+...+N_m) + (\delta_1+\delta_2+...+\delta_m) \mathrel{\char`≠} 0  $$ </span>

15. ข้อ 8. และ 14. ขัดแย้งกัน
16. q(x) ไม่มีอยู่จริง
17. p(x) ที่ทำให้ p(π) = 0 ไม่มีอยู่จริง
18. π เป็นจำนวนอดิศัย □

<hr>

## Final Thought

ในที่สุดก็เขียนจบ เขียนมา 1 วีค เหนื่อยสุดๆ เอาจริงๆ ไม่คิดว่าจะได้เขียนจนจบ เพราะมันซับซ้อนมาก อ่านต้นฉบับทวนอยู่หลายสิบรอบ ดีใจที่ได้เขียน ไว้คราวหน้าจะลองหยิบบทพิสูจน์สนุกๆ(?)มาเขียนอีก

//แล้วเจอกัน ในวันที่มีเวลา

<span style="color:#fff;display:none">HBD 🎉🎉</span>

<div class="footnotes">
    <ol>
        <li class="footnote" id="fn:1">
            <p>ตามรูป คือ Real Algebraic Numbers เพราะว่า เราสนใจเฉพาะตัวเลขที่อยู่ในจำนวนจริง //ไม่นับสิ่งที่อยู่ในจำนวนจินตภาพ/จำนวนเชิงซ้อน</p>
        </li>
        <li class="footnote" id="fn:2">
            <p>ขอละ "ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม" ออกไปนะฮะ ให่้เข้าใจว่า เวลาพูดถึง <b>สมการ polynomial</b> จะหมายถึง <b>สมการ polynomial (ที่มีสัมประสิทธิ์ (coefficients) เป็นจำนวนเต็ม)</b> เสมอ</p>
        </li>

        <li class="footnote" id="fn:3">
            ความเจ็บปวดหนึ่งจากการอ่านเปเปอร์ทางคณิตศาสตร์ คือ ส่วนใหญ่มักจะข้ามบางขั้นตอนไป แล้วแทนด้วย obviously หรือ trivially แต่ฉันไม่สามารถคิดตามสิ่งที่ obviously ของท่านๆทั้งหลายได้
        </li>

        <li class="footnote" id="fn:4">
            ดูบทสนธนาได้ที่ <a target="_blank" href="https://chatgpt.com/share/68b25749-2cc0-800e-ab18-a8791281a39f">https://chatgpt.com/share/68b25749-2cc0-800e-ab18-a8791281a39f</a>
        </li>

        <li class="footnote" id="fn:5">
            เพราะ นิเสธ หรือ นิพจน์ จะต้องเป็นจริง อย่างใดอย่างนึง ตามนิยามของ นิเสธ และ นิพจน์ ในวิชาตรรกศาสตร์ (Logic)
        </li>

        <li class="footnote" id="fn:6">
            เพราะ F(w+βₖ) มีแค่ βₖ อย่างเดียว ไม่ใช่ symmetric polynomials บน {β} จึงไม่สามารถอ้างโดยใช้ FTSP ได้
        </li>
    </ol>
</div>


