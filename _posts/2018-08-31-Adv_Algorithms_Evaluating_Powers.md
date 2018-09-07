---
layout: post
section-type: post
title: Adv. Algorithms - Evaluating Powers
category: Algorithms
tags: [ 'python', 'algorithm', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
</head>

### Left-to-Right Binary Method for computing: \begin{equation}x^{e}\end{equation}

##### Refer to Pingala's Hindu classic **Chandah-sutra**, we have following formula to implement our algorithms:
- when e = even:
\begin{equation}x^{e} = (x^{e/2})^{2}\end{equation}
- when e = odd:
\begin{equation}x^{e} = x*(x^{(e-1)/2})^{2}\end{equation}

<br>

###### Image to help understand the idea of Left-to-Right method:
<br>
![Formulas]({{site.baseurl}}/assets/img/posts_img/2018-08-31-Adv_Algorithms_Evaluating_Powers/karatsuba.exponentiation.gif){:class="img-responsive"}
([Figure 1](http://www.excel-ticker.com/calculation-of-very-large-numbers-in-excel-part-4-exponentiation/))

<br>

<hr>

##### Thus, we can implement our pseudo code as below:
> **function** Left-to-Right Binary Method for computing x^e <br>
> **Input**: x (a real number), e (a positive integer) <br>
>**Output:** x^e <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute the binary representation of **e** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pow := e <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scan binary representation from left to right, **starting with 2nd position** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IF** 0 is encountered: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pow := Pow * Pow <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ELSE** (1 is encountered): <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pow := x * Pow * Pow <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ENDIF** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RETURN(Pow)** <br>
**end** Left-to-Right Binary Method <br>

<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of Left-to-Right Binary Method for computing x^e
        """
~~~
<br>

<hr>

### Right-to-Left Binary Method for computing: \begin{equation}x^{e}\end{equation}

##### Refer to **al-Kashi**'s method, we know that:
\begin{equation}e = 2^{i} + b_{i-1}2^{i-1} + b_{i-2}2^{i-2} + ... + b_{0}\end{equation}
> Note: 
>- **i** = the index of e in binary representation from left to right.
>- **b** = the biniary digit of e at current binary index of e.

<br>

##### From above formula, let:
\begin{equation}z = b_{i-1}2^{i-1} + b_{i-2}2^{i-2} + ... + b_{0}\end{equation}

<br>

##### Thus, we can rewrite our power evaluation into:
\begin{equation}x^{e} = x^{2^{m}+z} = x^{2m}x^{z}\end{equation}

<br>

<hr>

##### The corresponding pseudo code:
> **function** Right-to-Left Binary Method for computing x^e <br>
> **Input**: x (a real number), e (a positive integer) <br>
>**Output:** x^e <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute the binary representation of **e** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pow := e <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AccumPowers := 1 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scan binary representation from right to left, **omitting the last binary digit** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IF** 1 is encountered: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AccumPowers := Pow * AccumPowers <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ENDIF** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pow := Pow * Pow <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RETURN(Pow * AccumPowers)** <br>
**end** Right-to-Left Binary Method <br>

<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of Right-to-Left Binary Method for computing x^e
        """
~~~
<br>

<br>
<hr>
<br>

### Using Modular Exponentiation for Encryption
>- Given a senario, first Alice sends Bob the value of an integer base b and an integer p. Now Alice, Bob, and Eve all know b and p. Then Alice chooses a large integer n, (which ONLY she knows), and sends Bob the value b<sup>n</sup> mod p. Then Bob chooses a large integer m (which ONLY he knows), and sends Eve b<sup>m</sup> mod p. Now they ALL know values b, p, b<sup>n</sup> mod p, and b<sup>m</sup> mod p.
<br>
>- Then let _k = (b<sup>n</sup> mod p)(b<sup>m</sup> mod p) = b<sup>m+n</sup> mod p_ ==> NET SECURITY
<br>
>- Alice: (b<sup>m</sup> mod p)<sup>n</sup> = b<sup>mn</sup>(mode p)
<br>
>- Bob: (b<sup>n</sup> mod p)<sup>m</sup> = b<sup>mn</sup>(mode p)

<br>
<br>

<hr>

#### Resources:
This post is derived from book [Algorithms: Foundations and Design Strategies](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjXxpDXqZvdAhUF9IMKHd-EBBMQFjAAegQIChAB&url=https%3A%2F%2Fwww.amazon.com%2FAlgorithms-Foundations-Strategies-Kenneth-Berman%2Fdp%2F0692993762&usg=AOvVaw3nkti_AUzVC1V8GF_CMFlH) as well as [Ph.D. Berman's](https://eecs.ceas.uc.edu/~berman/) CS7081 course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Berman's](https://eecs.ceas.uc.edu/~berman/)'s authorization.
<br><br>
>- [Modular exponentiation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiz6PKJrqTdAhVS21MKHWHvAv8QFjAAegQIBhAB&url=https%3A%2F%2Fwww.khanacademy.org%2Fcomputing%2Fcomputer-science%2Fcryptography%2Fmodarithmetic%2Fa%2Fmodular-exponentiation&usg=AOvVaw3_orSdiVr3mthy1JOxWFvL)
<br>
