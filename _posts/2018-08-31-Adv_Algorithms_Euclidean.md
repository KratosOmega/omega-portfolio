---
layout: post
section-type: post
title: Adv. Algorithms - Euclidean Algorithm
category: Algorithms
tags: [ 'python', 'algorithm', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
</head>

### Greatest common divisor:
>The idea is to find the gcd(a, b) of two positive integers a and b.<br>
>A naive algorithm computes the prime factorization of a and b and collects common prime powers whose product is then equal to gcd(a, b).<br>
>However, it will be inefficient for large a and b.<br>
>Thus, A more efficient algorithm was published in Euclid's Elements.<br>
><br>
>Euclid's algorithm is based on the observation that for a >= b, an integer divides both a and b if, and ONLY IF, it divides a - b and b.
>\begin{equation}gcd(a,b) = gcd(a-b,b), \; a\geq b, \; gcd(a,a)=a \end{equation}<br>
>However, if we implement this algorithm at this point, there will be a while loop to repeat:<br>
>&nbsp;&nbsp;&nbsp;&nbsp;a := a - b for a > b<br>
>&nbsp;&nbsp;&nbsp;&nbsp;b := b - a for b > a<br>
>&nbsp;&nbsp;&nbsp;&nbsp;until a == b<br>
>Euclid's gcd algorithm using **r = a - nb** to replace the while loop subtraction, which leads to formular:<br>
>\begin{equation}gcd(a,b) = gcd(b, a \; mod \; b)\end{equation}<br>

<hr>

<br>

##### pseudo code:
>**function** EuclidGCD(a, b) <br>
>**Input**: a, b (two nonnegative integers)<br>
>**Output:** gcd(a, b) (the greates common divisor of a and b) <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **WHILE** b != 0 **DO**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Remainder := a **mod** b<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a := b<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b := Remainder<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ENDWHILE**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **RETURN(a)**<br>
**end** EuclidGDC <br>

>Performance: log_2(max(a,b))
<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of EuclidGDC
        """
~~~
<br>

<hr>

#### Resources:

<br>
