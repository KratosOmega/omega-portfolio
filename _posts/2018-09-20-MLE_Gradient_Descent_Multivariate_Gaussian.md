---
layout: post
section-type: post
title: MLE, Gradient Descent, Multivariate Gaussian
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>


### Gradient Descent Approach for MLE
<br>
> #### Gradient Descent
>- A numerical optimization technique used to find the parameter vector **w** that minimizes an objective function _E(w)_.

<br>
<hr>
<br>

> #### MLE using Gradient Descent
>- Determine the distribution model & have _pdf_ formula available. 
>- Get _Likelihood Function_ from _pdf_.
>- Get _Log-Likelihood Function_ from _Likelihood Function_.
>- Get _Negative Log-Likelihood Function_ from _Log-Likelihood Function_.
>- Compute _partial derivatives_ from _Negative Log-Likelihood Function_ with respect of each RV.
>- Setup Gradient Descent update rules: _x &larr; x - &lambda;(df/dx)_, where &lambda; is the learning rate.
> 
<br>
<hr>
<br>

> #### Limitations of Gradient Descent
>- It can converge to a local minimum (global minimum is what we want) and result in a different value in different runs (multiple local minimums).
>- Tends to be slow when it is close to the minimum.
>- In poorly conditioned convex problems, "zigzags" when gradients point nearly orthogonally to the shortest direction.
> 
<br>
<hr>
<br>

### Multivariate Gaussian
<br>
> #### TBC
>-
>- 
> 
<br>
<hr>
<br>

> #### TBC
>-
>- 
> 
<br>
<hr>
<br>


> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/){:class="img-responsive"}<br>



<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
