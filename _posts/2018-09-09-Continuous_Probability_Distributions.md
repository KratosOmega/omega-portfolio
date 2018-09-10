---
layout: post
section-type: post
title: Continuous Probability Distributions
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### Characterizing Continuous Probability Distributions
<br>
> #### Continuous Randome Variables
> - Discrete Random Variables:<br>
> -- DRV have a continum of possible values.<br>
> -- DRV have more than a countable collection of possible values. (weight, height)<br>
> -- Can only be measured instead of counting.<br>
> -- DRV can take on any value in a interval of real numbers.<br>
> -- No guarantee that all values will we found in a sample if one looks long enough.<br>
> -- No value can be ruled out as a possible observation.<br>

>- Probability assignment for continuous random variables<br>
> -- CRV can have **infinite** number of possible outcomes.<br>
> -- Thus, it can not be assigned a **positive probability** to each possible outcome & ensurethat they sum to 1.<br>
> -- But, we can assign positive probabilities to **intervals** of real numbers in a manner consisten with probability axioms.<br>

>- Using mathematical model (function that fit the CRV distribution) for relative frequency of the data. Then calculate the integral base on interested interval.

<br>

> #### Probability Density Function
<br>
> A function _f(x)_ that models the relative frequency behavior of the continuous valued data is called **probability density function (pdf)**. For _f(x)_ to be a **pdf**, the following criteria should be met:<br>
> \begin{equation}f(x)\;\geq\;0,\;\forall x\end{equation}
> \begin{equation}\int_{-\infty}^{\infty}f(x)dx\;=\;1\end{equation}
> \begin{equation}p(a\;\leq\;x\;\leq\;b)\;=\;\int\_{a}^{b}f(x)dx\end{equation}
> Note:<br>
> \begin{equation}p(x\;=\;a\;=\;\int\_{a}^{a}f(x)dx\;=\;0\end{equation}
> -- x must be a interval instead of an individual outcome, since the chance of observing this particular outcome (x = a) is quite small.<br>
> _p(a &le; x &le; b) = p(a < x &le; b) = p(a &le; x < b) = p(a < x < b)_, only works for **continuous random variables**.<br>

<br>

> #### Cumulative Distribution Function (cdf)
> - The distribution fuction for a random variable _x_ is defined as:
> \begin{equation}cdf(b)\;=\;p(x\;\leq\;b)\end{equation}
> - If _x_ is continuous with pdf _f(x)_, then:
> \begin{equation}cdf(b)\;=\;\int_{-\infty}^{b}f(x)dx\end{equation}
<br>
>- CDF of a **continuous RV** is **continuous** over the whole real line, in contrast to a **discrete RV** which is a step function.
>- 4 properties of CDF are:
> \begin{equation}\lim_{x \rightarrow -\infty}cdf(x)\;=\;0\end{equation}
> \begin{equation}\lim_{x \rightarrow \infty}cdf(x)\;=\;1\end{equation}
> \begin{equation}cdf(x)\;\text{is a non-decreasing fnction, if }a\;<\;b,\;\;\;cdf(a)\;\leq\;cdf(b)\end{equation}
> \begin{equation}cdf(x)\;\text{is right-hand continuous, }lim_{h \rightarrow 0+}cdf(x\;+\;h)\;=\;cdf(x)\end{equation}
> In addition, the cdf of a continuous RV is also **left-hand continuous**:
> \begin{equation}lim_{h \rightarrow 0-}cdf(x\;+\;h)\;=\;cdf(x)\end{equation}
> pdf can also be derived from cdf:
> \begin{equation}pdf\;f(x)\;=\;\frac{d}{dx}cdf(x),\;\;\;x\;\in\;\mathbb{R}\end{equation}

<br>

> #### Expectation (Mean) & Variance of a continuous RV
>- **Expected value** of a continuous RV, x that has a pdf _f(x)_ is given by:
> \begin{equation}E(x)\;=\;\int_{-\infty}^{\infty}xf(x)dx\end{equation}
>- If _x_ is a continuous RV with pdf _f(x)_, and if g(x) is any real-valued function of x, then:
> \begin{equation}E(g(x))\;=\;\int_{-\infty}^{\infty}g(x)f(x)dx\end{equation}
>- **Variance** of a continuous RV, x that has a pdf _f(x)_ is given by:
> \begin{equation}\sigma^{2}\;=\;E[(x\;-\;\mu)^{2}]\;=\;\int_{-\infty}^{\infty}(x\;-\;\mu)^{2}f(x)dx\;=\;E(x^{2})\;-\;\mu^{2},\;\;\;(\mu\;=\;E(x))\end{equation}

<br>
<hr>
<br>

### Standard Distributions

<br>
> #### Uniform Distribution
>- Consider an experiment that consists of observing events in a certain time frame _(a, b)_. (arrival of buses at a bus stop within a period)
>- We are interested in the probability distribution of the actual time of occurrence _(x)_ of the event (a bus arrived between 8：00 and 8：10).
>- A simple model assumes that _x_ is equally likely to lie in any subinterval (of length _d_), that is irrespective of where it lies within _(a, b)_.
>- This assumption leads to the **uniform probability distribution**.

>- Probability density function<br>
<br>
> Uniform distribution has a pdf:
> ![Probability Density Function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/probability_density_function.png){:class="img-responsive"}
<br>
>- Cumulative distribution function<br>
<br>
> Uniform distribution has a cdf:
> ![Cumulative Distribution Function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/cumulative_distribution_function.png){:class="img-responsive"}
<br>
>- Uniform distribution (plots)<br>
<br>
> ![Uniform distribution plots]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/uniform_distribution_plots.png){:class="img-responsive"}
<br>
>- How we get "_1/(b-a)_"?<br>
> _P(c &le; x &le; c+d)_<br>
> = _P(x &le; c+d) - P(x &le; c)_<br>
> = _cdf(c+d) - cdf(c)_<br>
> = _(c+d-a)/(b-a) - (c-a)/(b-a)_<br>
> = _d/(b-a)_<br>
> which indicates that, the probability **ONLY** depends on _d_, the length of the interval.<br>

>- Relationship between Uniform and Poission<br>
<br>
>Suppose that the # of events that occur in an interval, say, _(0, t)_ - has a Poisson distribution. If exactly one of these events is known to have occurred in the interval _(a, b)_, then the conditional probability distribution of the actual time of occurrence for this event is uniform over _(a, b)_.<br>
<br>
> -- Uniform Distribution: p(actual time of occurence | 1 event occurence within time interval)<br>
> -- Poisson Distribution: p(# of occurence | within time interval)

>- Mean of Uniform distribution<br>
<br>
> ![Mean of Uniform distribution]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/mean_of_uniform_distribution.png){:class="img-responsive"}
<br>
> Mean lies at the midpoint of the interval.<br>
<br>
>- Variance of Uniform distribution<br>
<br>
> Since we know:
> \begin{equation}\sigma^{2}\;=\;E[(x\;-\;\mu)^{2}]\;=\;E(x^{2})\;-\;\mu^{2}\;\;\;and\;\;\;\mu\;=\;\frac{a+b}{2}\end{equation}
> then:<br>
<br>
> ![Variance of Uniform distribution (a)]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/variance_of_uniform_distribution_a.png){:class="img-responsive"}
<br>
> ![Variance of Uniform distribution (b)]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/variance_of_uniform_distribution_b.png){:class="img-responsive"}
<br>
> Variance depends **ONLY** on the length of the interval.

<br>
> #### Exponential Distribution
>- Exponential curve seems to fit many RV in engineering and the sciences.

>- Probability density function<br>
<br>
> ![Probability density function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/probability_density_function_exponential_distribution.png){:class="img-responsive"}
<br>
> where the parameter _&theta;_ is a constant (&theta; > 0), _&theta;_ is the rate at which the curve decreases.<br>
<br>
>- Cumulative distribution function<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/cumulative_distribution_function_exponential_distribution.png){:class="img-responsive"}

<br>
> #### Gamma Distribution
>- Gamma Function:
> \begin{equation}\gamma(\alpha)\;=\;\int_{0}^{\infty}x^{\alpha-1}e^{-x}dx\end{equation}
>- Gamma function properties:
> \begin{equation}\gamma(\alpha\;+\;1)\;=\;\alpha\gamma(\alpha)\;=\;\alpha(\alpha\;-\;1)\gamma(\alpha\;-\;1\;=\;\alpha !)\end{equation}
> \begin{equation}\gamma(n)\;=\;(n\;-\;1)!\end{equation}
> thus:
> \begin{equation}\gamma(\alpha\;+\;1)\;=\;\int_{0}^{\infty}x^{\alpha}e^{-x}dx\end{equation}
>- Using integration by parts, let:
> \begin{equation}\mu\;=\;x^{\alpha}\;\;\;and\;\;\;v\;=\;-e^{-x}\end{equation}
> \begin{equation}d\mu\;=\;\alpha x^{\alpha-1}\;\;\;and\;\;\;dv\;=\;e^{-x}dx\end{equation}
> then:
> ![Gamma Function Integration]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_function.png){:class="img-responsive"}
<br>
>- Introducing &beta;
> \begin{equation}\int_{0}^{\infty}x^{\alpha-1}e^{-x/\beta}dx\end{equation}
> for positive constants _&alpha;_ and _&beta;_ can be evaluated by introducing _y = x/&beta;_ or _x = &beta;y_, where _dx = &beta;dy_.<br>
<br>
> ![Gamma Function Integration with beta]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_function_beta.png){:class="img-responsive"}

>- Mean of Exponential Distribution (Gamma)<br>
<br>
> ![Mean of Exponential Distribution of Gamma]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/mean_of_exponential_distribution_gamma.png){:class="img-responsive"}<br>
> Parameter _&theta;_ is actually the mean of the distribution.

>- Variance of Exponential Distribution (Gamma)<br>
<br>
> ![Variance of Exponential Distribution of Gamma]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/variance_of_exponential_distribution_gamma.png){:class="img-responsive"}<br>


> Memoryless Property:
>- Geometric distribution is memoryless among the discrete distributions.
>- Exponential distribution is the continuous distribution that is memoryless:
> \begin{equation}p(x\;>\;a\;+\;b\mid x\;>\;a)\;=\;p(x\;>\;b)\end{equation}
>- This memoryless property sometimes causes concerns about the exponential distribution's usefulness as a model.

> Connection with Poisson distribution:
>- If the number of events _x_ in a specified area has Poisson distribution, the distance between any event and the next event has exponential distribution.
>- For events occuring according to Poisson distribution, the waiting time from occurrence of any event until the next has an exponential distribution.<br>
> -- Suppose events are occuring in time according to Poisson distribution with rate of _&lambda;_ events/hour.<br>
> -- _y_ be the # of events in _t_ hours, with mean _&lambda;t_.<br>
> -- How long do I have to wait to see the first event occur?<br>
> -- _x_ be the length of time until first event:<br>
> \begin{equation}p(x\;>\;t)\;=\;p[y\;=\;0\;\text{on the interval}\;(0,\;t)]\;=\;\frac{(\lambda t)^{0}e^{-\lambda t}}{0!}\;=\;e^{-\lambda t}\end{equation}
> \begin{equation}p(x\;\leq\;t)\;=\;1\;-\;p(x\;>\;t)\;=\;1\;-\;e^{-\lambda t}\end{equation}
> Notice that _p(x &le; t) = cdf(t)_, has the form of cdf of exponential distribution &lambda; = 1/&theta;.<br>
<br>
> Differentiating this, we see that pdf of x is:
> \begin{equation}f(t)\;=\;\frac{d(cdf(t))}{dt}\;=\;\frac{d(1-e^{-\lambda t})}{dt}\;=\;\lambda e^{-\lambda t}\;=\;\frac{1}{\theta}e^{-t/\theta},\;\;\;t\;<\;0\end{equation}
> This is the **pdf for exponential distribution**.

<br>
> #### Normal/Gaussian Distribution
>-

<br>
> #### Beta Distribution
>-

<br>
> #### Weibull Distribution
>-










<br>

> NOTE: for integral, _f(x)dx_ means ==> anti-derivative _f(x)_ to get _F(x)_:
> \begin{equation}\int_{a}^{b}f(x)dx\;=\;F(x)|_{a}^{b},\;where\;f(x)dx\;=\;F(x)\end{equation}


<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
