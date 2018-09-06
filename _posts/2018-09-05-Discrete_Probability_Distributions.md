---
layout: post
section-type: post
title: Discrete Probability Distributions
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### Characterizing Discrete Probability Distributions
<br>
> #### Discrete Probability Distribution
>- **Discrete random variable**: if it can take on only a finite number - or a countably infinite number - of possible values (value is obtained by counting).
> -- e.g.: number of students present.
>- **Continuous random variable**: variable whose value is obtained by measuring.
> -- e.g.: height of students in class.
<br> 
>- **Probability mass function**: the probability distribution of a discrete random variable.
> Mass of probability is associated with discrete states in the domain.

<br>

> #### Cumulative Distribution Function
>- **Cumulative distribution function** _cdf(b)_ for a random variable x is:
> \begin{equation}cdf(b)\; = \; p(x\leq b)\;=\;\sum_{x=-\infty}^{b} p(x)\end{equation}
>- CDF is discontinuous at points of +ve probability. --- ?
>- The CDF is _right-hand continous_, NOT _left-hand continuous_. --- ?

<br>

> #### Expectation
>- Discrete probability distribution shows the long-run relative frequency of occurrences for numerical outcomes.
>- Expectation or Expected value is a one number summary of the distribution.
> \begin{equation}E(x)\;=\;\sum_{x}xp(x)\end{equation}
>- Think of it as the average of a large number of "draws" x1, x2, ..., xn from the distribution.
> \begin{equation}E(x)\;\approx\;\frac{1}{n}\sum_{i=1}^{n}x_{i}\;\;\;\text{(Law of large numbers)}\end{equation}
>- Expectation is also referred to as a mean: 
> \begin{equation}E(x)\;=\;\mu\end{equation}
>- Expectation of g(x):
> If x is a discrete random variable with probability distribution p(x), and if g(x) is any real-valued function of x, then:
> \begin{equation}E(g(x))\;=\;\sum_{x}g(x)p(x)\end{equation}

> #### Properties of Expectations
>- Property 1:<br>
> If X is a random variable and a is a constant,
> \begin{equation}E(aX)\;=\;aE(X)\end{equation}
>- Property 2:<br>
> If X1, X2, ..., Xn are random variables, a1, a2, ..., an are constant values,
> \begin{equation}E(\sum_{i}a_{i}X_{i})\;=\;\sum_{i}a_{i}E(X_{i})\end{equation}
>- Property 3:<br>
>If X1, X2, ..., Xn are independent random variables,
> \begin{equation}E(\prod_{i}X_{i})\;=\;\sum_{i}E(X_{i})\end{equation}

<br>

> #### Variance / Standard Deviation
>- Variance
> The variance of a random variable x with expected value _&mu;_ is given as:
> \begin{equation}\sigma^{2}\;=\;E[(x\;-\;\mu)^{2}]\end{equation}
> Variance can be thought of as the **average squared distance between the values of x and the expected &mu;**.<br>
<br>
> When all the probability is concentrated at a _single point_:
> \begin{equation}\sigma^{2}\;=\;0\end{equation}
> &sigma;<sup>2</sup> becomes large as the points with non-zero probability spread out more.
<br>
<br>
>- Standard Deviation
> Standard deviation of a random variable x is the square root of variance:
> \begin{equation}\sigma\;=\;\sqrt{\sigma^{2}}\;=\;\sqrt{E[(x\;-\;\mu)^{2}]}\end{equation}

<br>
<hr>
<br>

### Standard Discrete Probability Distributions 
<br>
> #### Bernoulli Distribution
<br>
>- **Bernoulli trials** are numerouns experiments have two possible outcomes:
> -- A coin toss may result in a head or a tail.<br>
> -- An piece of fruit is either damaged or not damaged.<br>
<br>
>- One outcome of a bernoulli trial is identified as a _success_ and the other is identified as a _failure_.
>- Probability of observing a success is _p_, and probability of observing failure is _1-p_ or _q_.
>- Probability distribution of x is:
> \begin{equation}p(x)\;=\;p^{x}(1\;-\;p)^{1\;-\;x},\;\;\;x\;=\;0,\;1\end{equation}
<br>
>- Expectation of Bernoulli Distribution
> \begin{equation}E(x)\;=\;\sum_{x}xp(x)\;=\;p,\;\;\;x\;=\;0,\;1\end{equation}
>- Variance of Bernoulli Distribution
> \begin{equation}\sigma^{2}\;=\;E[(X\;-\;\mu)^{2}]\;=\;E(X^{2})\;-\;[E(X)]^{2}\\;=\;\sum_{x}x^{2}p(x)\;-\;[\sum_{x}p(x)]^{2}\;=\;p(1\;-\;p)\end{equation}
<br>

> #### Binomial Distribution
>- Setup: 
> -- n **independent Bernoulli** trials, **each** with a probability _p_ of success.
> -- x is a random variable of success in the n trials.
> Probability of x success in n trials is:
> \begin{equation}p(x)\;=\;{n \choose x}\;p^{x}(1\;-\;p)^{n\;-\;x}, \;\;\;x\;=\;0,\;1,\;2,\;...,\;n\end{equation}
<br>
>- Binomial Distribution: mean and variance
> Originally, it should be:
> \begin{equation}E(x)\;=\;\sum_{x}xp(x)\;=\;\sum_{x=0}^{n}x{n \choose x}p^{x}(1\;-\;p)^{n-x}\end{equation}
> But it is not easy to solve, thus, using Bernoulli random variables _y1_, _y2_, ..., _yn_, we have:
> \begin{equation}E(x)\;=\;E(\sum_{i=1}^{n}y_{i})\;=\;\sum_{i=1}^{n}E(y_{i})\;=\;\sum_{i=1}^{n}p\;=\;np\end{equation}
> Using Bernoulli random variables for variance, we have:
> \begin{equation}\sigma^{2}(x)\;=\;\sum_{i=1}^{n}\sigma^{2}(y_{i})\;=\;\sum_{i=1}^{n}p(1\;-\;p)\;=\;np(1\;-\;p)\end{equation}
<br>

> #### Categorical Distribution
<br>
>- While Bermoulli distribution deals with **two outcomes**, _categorical distribution_ can allow **multiple** outcomes (say _k_).
> e.g., roll of a dice (6 possible outcomes)
<br><br>
>- Setup:
<br>
> -- k mutually exclusive outcomes for a trial
<br>
> -- _p<sub>i</sub>_ is the probability associated with outcome _i_.
<br>
> -- _&Sigma;<sub>i</sub>p<sub>i</sub>_ = 1
<br>
> -- _x_ is **randome variable** of seeing one of the _k_ outcomes
<br><br>
> Probability of x is:
> \begin{equation}p(x\;=\;i)\;=\;p_{i},\;x\;=\;i\;...\;k\;\;\;(or)\;\;\;p(x)\;=\;p_{1}^{[x=1]}p_{2}^{[x=2]}...p_{k}^{[x=k]}\end{equation}
> where _[x = i]_ evalutes to 1 if outcome is _i_, 0 otherwise.

<br>

> #### Multinomial Distribution
<br>
>- Setup:
<br>
> -- n **independent** '**Categorical**' trials,
<br>
> -- probability of each of the _k_ outcomes p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>k</sub> (&Sigma;<sub>i</sub>p<sub>i</sub> = 1), these probabilities are same across trials.
<br>
> -- _x_ is a **random variable** of counts of each of the _k_ possible outcomes over _n_ trials.
<br>
<br>
> The probability of seeing [x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>k</sub>] coutcomes in _n_ trials is:
> \begin{equation}p(x_{1},\;x_{2},\;...,\;x_{k})\;=\;\frac{n!}{x_{1}!x_{2}!\;...\;x_{k}!}p_{1}^{x_{1}}p_{2}^{x_{2}}\;...\;p_{k}^{x_{k}}\end{equation}
<br>
>- Multinomial distribution Mean
> For i &isin; {1, 2, ..., k}, the mean of x<sub>i</sub> is:
> \begin{equation}E(x_{i})\;=\;np_{i}\end{equation}
>- Multinomial distribution Variance
> For i &isin; {1, 2, ..., k}, the variance of x<sub>i</sub> is:
> \begin{equation}\sigma^{2}(x_{i})\;=\;np_{i}(1\;-\;p_{i})\end{equation}
>- Multinomial distribution Covariance
> In general, for distinct i, j &isin; {1, 2, ..., k}, the co-variance of x<sub>i</sub> and x<sub>j</sub> is:
> \begin{equation}cov(x,\;y)\;=\;E[(x\;-\;E(x))(y\;-\;E(y))]\end{equation}

<br>

> #### Geometric Distribution
<br>
>- It suited for modeling the number of failures before a first success, when each experiment is a Bernoulli trial with a constant probability of success.
>- The geometric probability distribution is:
> \begin{equation}p(x)\;=\;(1-p)^{x}p\;=\;q^{x}p\end{equation}
> where _q = 1 - p_<br>
<br>
> This r.v. can take on a countably infinite number of possible values.
>- Mean
> \begin{equation}E(x)\;=\;\sum_{x}xp(x)\;=\;\sum_{x=0}^{\infty}xpq^{x}\end{equation}
> Using geometric progression, this will be _E(x) = q/p_.
>- Variance
> \begin{equation}\sigma^{2}\;=\;\frac{q}{p^{2}}\end{equation}
>- Memoryless property: only discrete distribution
> \begin{equation}p(x\;\geq\;j\;+\;k\;|\;X\;\geq\;j)\;=\;p(x\;\geq\;k)\end{equation}
> If we observed _j_ straight failures, then the probability of observing at least _k_ more failures (_j+k_ total failures) before a success is the same as if we were just beginning and wanted to dtermine the probability of observing at least _k_ failures prior to a success.
<br>

> #### Negative Binomial Distribution
<br>
>- Geometric distribution model the probabilistic behavior of # failures prior to first success in a sequence of Bernoulli trials.
>- A negative binomial models the # of failures prior to the **2nd** success, or **3rd** success or **r<sup>th</sup>** success.
> \begin{equation}p(x)\;=\;{x+r-1 \choose r-1}p^{r}q^{x},\;\;\;x\;=\;0,\;1,\;...\end{equation}
>- Mean
> \begin{equation}E(x)\;=\;\frac{rq}{p}\end{equation}
>- Variance
> \begin{equation}\sigma^{2}\;=\;\frac{rq}{p^{2}}\end{equation}
<br>

> #### Poisson Distribution
<br>
>- It is typically used to model counts of _rare events_ in a **given area or volume or time**.
>- **NO** unique way to choose the _n_ and _p_ for the binomial model - as n &rarr; &#x221e;, p &rarr; 0 - we also restrict the mean to remain a constant &lambda;, _&lambda; = np_.
>- The probability of _x_ number of accidents can be written, using Binomial distribution, as:
> \begin{equation}p(x)\;=\;lim_{n\rightarrow\infty}{n \choose x}\frac{\lambda^{x}}{n}(1\;-\;\frac{\lambda}{n})^{n-x}\;=\;\frac{\lambda^{x}}{x!}e^{-\lambda},\;\;\;x\;=0,\;1,\;2,\;...\;for\;\lambda\;\>\;0\end{equation}
> &lambda; denotes the mean occurrences of events in one time period.


<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
