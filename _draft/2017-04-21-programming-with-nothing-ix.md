---
layout: post
title: "Programming with Nothing : Epilogue"
tags: [Archive, Code Code and Code, Programming With Nothing]
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(19, 196, 165)
---

## TL;DR



<!--more-->

https://en.wikipedia.org/wiki/Lambda_calculus#Arithmetic_in_lambda_calculus
Victory
Why?

Epilogue

What is lambda calculus?

Why?
Being limited to Proc.new and Proc#call sounds impossibly restrictive, but I’ve tried to present enough evidence to convince you that we can still build any data structure and implement any algorithm.

In this alien world there is no data, only code. Data is an inert artefact for controlling the behaviour of the code that reads it, but you can always cut out the middleman by replacing a piece of data with the living code that does what the data-reading code would have done when it read that data.

We don’t know how to design a programming language, or even make a computer, that has more computational power than this combination of Proc.new and Proc#call. I think this is an awe-inspiring fundamental fact — like knowing that every atom in your body that isn’t hydrogen, helium or lithium was either synthesised in the heart of a star or in the subsequent supernova that distributed its matter throughout the universe. It tells us what we, as programmers, are made of.

So why doesn’t everyone just use Proc.new and Proc#call if they’re so powerful? Why do we have more elaborate programming languages at all, and what differentiates them from each other if they’re all equivalently capable of computation?

The answers are obvious: programming languages have different degrees of expressiveness and aesthetic appeal; some of them are safe, some of them are flexible, and that’s a trade-off; some of them have better performance than others; different languages have different qualities of ecosystem.

In fact, every aspect of a programming language’s design is a trade-off — what is expressive for your work may not be expressive for someone else’s — but there is a particular sweet spot among those trade-offs for people who care about simplicity, flexibility and syntactic beauty; Ruby is in our sweet spot.

There are many languages like Ruby, but this one is ours.

Epilogue
The simple programming language demonstrated in this article is the untyped lambda calculus, and the implementations of datatypes are Church encodings. The lambda calculus is powerful because it’s Turing complete.

If you’d like to play with these implementations, please download the supplementary code, where you can find specs for everything I’ve shown you.

If you’re feeling brave you can start from scratch and try to make all these specs pass with your own proc-based implementations; if you’re not feeling brave, there’s another branch which walks you through writing those implementations (e.g. implementing ADD, MULTIPLY and POWER) as well as doing a bit of refactoring (e.g. extracting a proc called INJECT).

Enjoy!