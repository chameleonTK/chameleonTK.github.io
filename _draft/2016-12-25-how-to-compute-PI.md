---
layout: post
title: How computer compute PI?
tags: [Archive]
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(165,42,42)

---

The development of computers in the mid-20th century again revolutionized the hunt for digits of π. American mathematicians John Wrench and Levi Smith reached 1,120 digits in 1949 using a desk calculator.[107] Using an inverse tangent (arctan) infinite series, a team led by George Reitwiesner and John von Neumann that same year achieved 2,037 digits with a calculation that took 70 hours of computer time on the ENIAC computer.[108] The record, always relying on an arctan series, was broken repeatedly (7,480 digits in 1957; 10,000 digits in 1958; 100,000 digits in 1961) until 1 million digits were reached in 1973.[109]

Two additional developments around 1980 once again accelerated the ability to compute π. First, the discovery of new iterative algorithms for computing π, which were much faster than the infinite series; and second, the invention of fast multiplication algorithms that could multiply large numbers very rapidly.[110] Such algorithms are particularly important in modern π computations, because most of the computer's time is devoted to multiplication.[111] They include the Karatsuba algorithm, Toom–Cook multiplication, and Fourier transform-based methods.[112]

The iterative algorithms were independently published in 1975–1976 by American physicist Eugene Salamin and Australian scientist Richard Brent.[113] These avoid reliance on infinite series. An iterative algorithm repeats a specific calculation, each iteration using the outputs from prior steps as its inputs, and produces a result in each step that converges to the desired value. The approach was actually invented over 160 years earlier by Carl Friedrich Gauss, in what is now termed the arithmetic–geometric mean method (AGM method) or Gauss–Legendre algorithm.[113] As modified by Salamin and Brent, it is also referred to as the Brent–Salamin algorithm.

The iterative algorithms were widely used after 1980 because they are faster than infinite series algorithms: whereas infinite series typically increase the number of correct digits additively in successive terms, iterative algorithms generally multiply the number of correct digits at each step. For example, the Brent-Salamin algorithm doubles the number of digits in each iteration. In 1984, the Canadian brothers John and Peter Borwein produced an iterative algorithm that quadruples the number of digits in each step; and in 1987, one that increases the number of digits five times in each step.[114] Iterative methods were used by Japanese mathematician Yasumasa Kanada to set several records for computing π between 1995 and 2002.[115] This rapid convergence comes at a price: the iterative algorithms require significantly more memory than infinite series.[115