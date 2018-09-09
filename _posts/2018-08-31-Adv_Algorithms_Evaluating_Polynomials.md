---
layout: post
section-type: post
title: Adv. Algorithms - Evaluating Polynomials
category: Algorithms
tags: [ 'python', 'algorithm', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
</head>

### Normal way of find polynomial value with given value of x:
> Polynomial takes form as:
>\begin{equation}p(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... + a_{1}x + a_{0}\end{equation}
>Thus, a normal way of get the value of p(x) at x = v, is calculate each term and then do a sum of the terms.<br>

<hr>

##### pseudo code:
>**function** PolyEval(a[0:n], v) <br>
>**Input**: a[0:n] (an array of real numbers), v (a real number) <br>
>**Output:** the value of the polynomial a<sub>n</sub>*x<sup>n</sup> + a<sub>n-1</sub>*x<sup>n-1</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> at x = v*<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sum := a[0] <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Product := 1 <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **FOR** i := 1 **TO** n **DO**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Product := Product * v<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sum := Sum + a[i] * Product<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ENDFOR**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **RETURN(Sum)**<br>
**end** PolyEval <br>

>Performance: 2n multiplications & n additions.

<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of PolyEval
        """
~~~
<br>

<hr>

### W. G. Horner's method of find polynomial value:
> Horner's method is based on a clever parenthesizing of the polynomial.
>\begin{equation}p(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + ... + a_{1}x + a_{0} = (...((a_{n} * x + a_{n-1}) * x + a_{n-2}) * ... * x + a_{1}) * x + a_{0}\end{equation}
>This rewriting can be done for a polynomial of **any** degree n!<br>
>It can be proved that any algorithm for evaluating an n_th degree polynomial that only uses (\*, /, +, -) must perform at least n times of (\* or /) and at least n times of (+ or -).<br>
>Thus, **HornerEval** is an optimal algorithm for evaluating polynomials.

<hr>

##### pseudo code:
>**function** HornerEval(a[0:n], v) <br>
>**Input**: a[0:n] (an array of real numbers), v (a real number) <br>
>**Output:** the value of the polynomial a<sub>n</sub>*x<sup>n</sup> + a<sub>n-1</sub>*x<sup>n-1</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> at x = v*<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sum := a[n] <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **FOR** i := n - 1 **DOWNTO** 0 **DO**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sum := Sum * v + a[i]<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ENDFOR**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **RETURN(Sum)**<br>
**end** HornerEval <br>

>Performance: n multiplications & n additions.


<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of HornerEval
        """
~~~
<br>

<hr>

#### Resources:
This post is derived from book [Algorithms: Foundations and Design Strategies](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjXxpDXqZvdAhUF9IMKHd-EBBMQFjAAegQIChAB&url=https%3A%2F%2Fwww.amazon.com%2FAlgorithms-Foundations-Strategies-Kenneth-Berman%2Fdp%2F0692993762&usg=AOvVaw3nkti_AUzVC1V8GF_CMFlH) as well as [Ph.D. Berman's](https://eecs.ceas.uc.edu/~berman/) CS7081 course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Berman's](https://eecs.ceas.uc.edu/~berman/)'s authorization.
<br>
