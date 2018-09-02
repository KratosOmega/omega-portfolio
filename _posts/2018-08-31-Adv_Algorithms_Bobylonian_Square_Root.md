---
layout: post
section-type: post
title: Adv. Algorithms - Babylonian Square Roots
category: Algorithms
tags: [ 'python', 'algorithm', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
</head>

### Algorithm to solve Square Roots:
>To find sqrt(5), start with a rectangle with l = 5 & w = 1. (Note: the integer that we try to find the square root should be updated with the avg(l, w)):
>- rec_1 := (l := avg(5, 1) = 3, w := 5/3)
>- rec_2 := (l := avg(3, 5/3) = 7/3, w := 15/7)
>- rec_3 := (l := avg(7/3, 15/7) = 47/21, w := 105/57)
>- ...
>- rec_n := (l := sqrt(5), w := sqrt(5))

>Thus, from the idea above, we can see that one dimension of the new rectangle is updated with average of the 2 dimensions from previous rectangle.<br>
>And the other dimension of the new rectangle is updated with the result of 5 (which we try to find square root with) divided by the new dimension.<br>
<br>
>Then, we have the formula for finding sqrt(a) as following:<br>
>\begin{equation}x_{i} = \frac{x_{i-1}+(a/x_{i-1})}{2}, \; i = 2, 3,...\end{equation}<br>
>Start with an initial guess x = x1 for sqrt(a); we calculate successive approximations x2, x3, ... to sqrt(a) using this formula.

<hr>

<br>

##### pseudo code:
>**function** BabylonianSQRT(a, error) <br>
>**Input**: a (a positive number), error (a positive real number) <br>
>**Output:** sqrt(a) accurate to within error <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x := a <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **WHILE** |x - a/x| > error **DO**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x := (x + a/x) / 2<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ENDWHILE**<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **RETURN(x)**<br>
**end** BabylonianSQRT <br>

>Performance: ...

<hr>

##### Python Implementation:
<br>
~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: Implementation of Babylonian SQRT
        """
~~~
<br>

<hr>

<br>
### Roots of polynomial:
>Finding square roots is a special instance of the problem of determining the (approximate) roots of a polynomial (note that sqrt(a) is the positive root of the polynomial x^2) - a).<br>
>- Bisection method
>- Sir Isaac Newton's Method: 
>\begin{equation}x_{i} = x_{i-1} - \frac{f(x_{i-1})}{f'(x_{i-1})}, \; i = 2, 3,...\end{equation}
![Formulas]({{site.baseurl}}/assets/img/posts_img/2018-08-31-Adv_Algorithms_Bobylonian_Square_Root/Use-the-Newton-Raphson-Method-Without-Calculus.png){:class="img-responsive"}
([Figure 1](https://www.wikihow.com/Use-the-Newton-Raphson-Method-Without-Calculus))
<br>
<br>
>1. Pick a point on x-axis as p0 and draw a tangent line on f(p) at point (p0, f(p0)).
>2. Then the intersection point of this tangent line and x-axis will be the p1.
>3. Repeating drawing tangent line as the first step will result p2, p3, p4, ... which yields exactly the Babylonian square root, as well as f(pn) = 0

<hr>

#### Resources:
This post is derived from book [Algorithms: Foundations and Design Strategies](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjXxpDXqZvdAhUF9IMKHd-EBBMQFjAAegQIChAB&url=https%3A%2F%2Fwww.amazon.com%2FAlgorithms-Foundations-Strategies-Kenneth-Berman%2Fdp%2F0692993762&usg=AOvVaw3nkti_AUzVC1V8GF_CMFlH) as well as Ph.D. Berman's CS7081 course in University of Cincinnati.
<br>
