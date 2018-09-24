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
> - CRV have a continum of possible values.<br>
> - RV have more than a countable collection of possible values. (weight, height)<br>
> - Can only be measured instead of counting.<br>
> - CRV can take on any value in a interval of real numbers.<br>
> - No guarantee that all values will we found in a sample if one looks long enough.<br>
> - No value can be ruled out as a possible observation.<br>

>- Probability assignment for continuous random variables<br>
> -- CRV can have **infinite** number of possible outcomes.<br>
> -- Thus, it can not be assigned a **positive probability** to each possible outcome & ensurethat they sum to 1.<br>
> -- But, we can assign positive probabilities to **intervals** of real numbers in a manner consisten with probability axioms.<br>

>- Using mathematical model (function that fit the CRV distribution) for relative frequency of the data. Then calculate the integral base on interested interval.<br>
<br>
> ![Probability Density Function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/pdf_vs_pmf.png){:class="img-responsive"}

<br>
<hr>
<br>

> #### Probability Density Function
<br>
> A function _f(x)_ that models the relative frequency behavior of the continuous valued data is called **probability density function (pdf)**. For _f(x)_ to be a **pdf**, the following criteria should be met:<br>
> \begin{equation}f(x)\;\geq\;0,\;\forall x\end{equation}
> \begin{equation}\int_{-\infty}^{\infty}f(x)dx\;=\;1\end{equation}
> \begin{equation}p(a\;\leq\;x\;\leq\;b)\;=\;\int\_{a}^{b}f(x)dx\end{equation}
> Note:<br>
> \begin{equation}p(x\;=\;a)\;=\;\int\_{a}^{a}f(x)dx\;=\;0\end{equation}
> -- x must be a interval instead of an individual outcome, since the chance of observing this particular outcome (x = a) is quite small.<br>
> _p(a &le; x &le; b) = p(a < x &le; b) = p(a &le; x < b) = p(a < x < b)_, only works for **continuous random variables**.<br>

<br>
<hr>
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
<hr>
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

>- Probability density function (Uniform distribution):<br>
<br>
> ![Probability Density Function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/probability_density_function.png){:class="img-responsive"}
<br>
>- Cumulative distribution function (Uniform distribution):<br>
<br>
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
<hr>
<br>

> #### Exponential Distribution
>- Exponential curve seems to fit many RV in engineering and the sciences.

>- Probability density function (exponential distribution):<br>
<br>
> ![Probability density function]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/probability_density_function_exponential_distribution.png){:class="img-responsive"}
<br>
> where the parameter _&theta;_ is the **MEAN** of the exponential distribution (constant &theta; > 0), _&theta;_ is the rate at which the curve decreases.<br>
<br>
>- Cumulative distribution function (exponential distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/cumulative_distribution_function_exponential_distribution.png){:class="img-responsive"}
<br>
>- Gamma Function:
> \begin{equation}\Gamma(\alpha)\;=\;\int_{0}^{\infty}x^{\alpha-1}e^{-x}dx\end{equation}
>- Gamma function properties:
> \begin{equation}\Gamma(\alpha\;+\;1)\;=\;\alpha\Gamma(\alpha)\;=\;\alpha(\alpha\;-\;1)\Gamma(\alpha\;-\;1\;=\;\alpha !)\end{equation}
> \begin{equation}\Gamma(n)\;=\;(n\;-\;1)!\end{equation}
> thus:
> \begin{equation}\Gamma(\alpha\;+\;1)\;=\;\int_{0}^{\infty}x^{\alpha}e^{-x}dx\end{equation}
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

>- Mean (exponential distribution):<br>
<br>
> ![Mean of Exponential Distribution of Gamma]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/mean_of_exponential_distribution_gamma.png){:class="img-responsive"}<br>
> Parameter _&theta;_ is actually the mean of the distribution.

>- Variance (exponential distribution):<br>
<br>
> ![Variance of Exponential Distribution of Gamma]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/variance_of_exponential_distribution_gamma.png){:class="img-responsive"}<br>


> Memoryless Property:
>- **Geometric distribution** is memoryless among the **discrete distributions**.
>- Only Geometric distribution has this unique memoryless property in discrete distributions.
>- **Exponential distribution** is the **continuous distribution** that is memoryless:
> \begin{equation}p(x\;>\;a\;+\;b\mid x\;>\;a)\;=\;p(x\;>\;b)\end{equation}
>- This memoryless property sometimes causes concerns about the exponential distribution's usefulness as a model.<br>
<br>
> Example: given a light bulb has burned for 1000 hours, the memoryless property implies that, the probability of the bulb will burn at least 10 more hours is the same as the probability of a **new** light bulb burn for 10 hours. (which is not true in real life.)<br>
<br>
> This failure to account for the **deterioration** of the bulb over time is the property arises question the appropriateness of the exponential model for **life-time** data.

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
<hr>
<br>

> #### Gamma Distribution
>- Exponential distribution is a **special** case of Gamme distribution. (substitue &alpha; = 1)
>- Gamma distribution in case of electronic components:<br>
> -- few have very short life lenght<br>
> -- many have something close to an average life length<br>
> -- very few have extraordinarily long life length<br>
<br>
>- Probability Density Function (gamma distribution):
<br><br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_distribution_pdf.png){:class="img-responsive"}<br>
<br>
> where Gamma Dist. integral of pdf (-&infin;, &infin;) = 1
> \begin{equation}\int_{-\infty}^{\infty}f(x)=1\end{equation}

>- Plot (gamma distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_distribution_plot.png){:class="img-responsive"}<br>
> Note: _&alpha;_ is the shape parameter & _&beta;_ is the rate parameter.

>- Mean & Variance of Gamma Distribution<br>
<br>
> Mean (gamma distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_distribution_mean.png){:class="img-responsive"}<br>
<br>
> Variance (gamma distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gamma_distribution_variance.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Inverse-Gamma Distribution
>- If a RV _1/x_ follows Gamma distribution with parameters _&alpha;_ and _&beta;_, then _x_ has **Inverse-Gamma Distribution**.
>- Inverse-Gamma Dist. is generally used in Bayesian analysis.<br>
<br>
>- Probability Density Function (inverse-gamma distribution):
<br><br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/inverse-gamma_distribution_pdf.png){:class="img-responsive"}<br>
<br>
>- InverseGamma vs. Gamma Plots<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/inverseGamma_vs_gamma_plots.png){:class="img-responsive"}<br>
<br>
> Note: that the symbol "_~_" is denoted as "draws from" or "**follows**".

<br>
<hr>
<br>

> #### Chi-Square Distribution
>- **Chi-square distribution** is a **special** case of Gamma distribution, which _&alpha; = k/2_ and _&beta; = 2_.
>- This is also expressed as:
> \begin{equation}X_{k}^{2}\;\sim\;\Gamma(\frac{k}{2},\;2)\end{equation}
>- Probability Density Function (chi-square distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/chi-square_distribution_pdf.png){:class="img-responsive"}<br>
<br>
>- Chi-square has **additive property** since the inverse scale parameter is fixed:
> If _x<sub>1</sub> ~ (X<sub>k<sub>1</sub></sub>)<sup>2</sup>_ and _x<sub>2</sub> ~ (X<sub>k<sub>2</sub></sub>)<sup>2</sup>_ are independent _X<sup>2</sup>_ variables, then _x<sub>1</sub> + x<sub>2</sub> ~ (X<sub>k<sub>1</sub>+k<sub>2</sub></sub>)<sup>2</sup>_

<br>
<hr>
<br>

> #### Inverse Chi-Square Distribution
>- **Inverse Chi-square distribution** is a **special** case of Gamma distribution, which _&alpha; = k/2_ and _&beta; = 2_.<br>
<br>
>- Probability Density Function (inverse chi-square distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/inverse-chi-square_distribution_pdf.png){:class="img-responsive"}<br>
<br>
> NOTE: There is NO InverseChisq function in Julia, but InverseGamma can be used to sample from this distribution by setting _&alpha; = x/2_ and _&beta; = 2_.

<br>
<hr>
<br>

> #### Normal/Gaussian Distribution
>- Many naturally occurring measurements (e.g., heights of men) tend to have a relative frequency distribution:<br>
>-- with some small values.<br>
>-- with most values close to the average.<br>
>-- with some high values, resulting in a bell shaped symmetric curve.<br>
<br>
>- Gaussian distribution is the most widely used probability distribution.<br>
<br>
>- Probability Density Function (gaussian/normal distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/gaussian_distribution_pdf.png){:class="img-responsive"}<br>
<br>
>- Mean (gaussian/normal distribution):<br>
> \begin{equation}E(x)\;=\;\int_{-\infty}^{\infty}xf(x)dx\;=\;\int_{-\infty}^{\infty}x\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^{2}/2\sigma^{2}}dx\;=\;\mu\end{equation}
>- Variance (gaussian/normal distribution):<br>
> \begin{equation}E[(x\;-\;\mu)^{2}]\;=\;\sigma^{2}\end{equation}

<br>
<hr>
<br>

> #### Beta Distribution
>- Exponential, Gamma, and Normal distributions are positive over an infinite interval.
>- Beta distribution is constrained to the interval (0, 1).<br>
<br>
>- Probability Density Function (gaussian/normal distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/beta_distribution_pdf.png){:class="img-responsive"}<br>
> where Beta Dist. integral of pdf(-&infin;, &infin;) = 1
> \begin{equation}\int_{-\infty}^{\infty}f(x)=1\end{equation}<br>
<br>
>- Plot (gaussian/normal distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/beta_distribution_plots.png){:class="img-responsive"}<br>

>- Mean & Variance of Beta Distribution<br>
<br>
> Mean (beta distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/beta_distribution_mean.png){:class="img-responsive"}<br>
<br>
> Variance (beta distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/beta_distribution_variance.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Weibull Distribution
<br>
>- When Gamma distribution is used to model life lengths of components, the failure rate function for Gamma distribution has an **upper bound**, which limits applicability to real systems.<br>
>- Weibull distribution provides a **better** distribution for **life length data**.
<br>
> Probability Density Function (weibull distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/weibull_distribution_pdf.png){:class="img-responsive"}<br>
<br>
>- For &gamma; = 1, this becomes **exponential distribution**.
>- For &gamma; > 1, the function looks like Gamma functions, with different mathematical properties.<br>
<br>
> CDF (weibull distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/weibull_distribution_cdf.png){:class="img-responsive"}<br>

>- Mean & Variance of Weibull Distribution<br>
<br>
> Mean (weibull distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/weibull_distribution_mean.png){:class="img-responsive"}<br>
<br>
> Variance (weibull distribution):<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/weibull_distribution_variance.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

### Bivariate & Multivariate Probability Distribution
> Note: Previous posts discussed about the **Joint Probability** p(x, y) when _x_ & _y_ are **Discrete RV**. Here, we will discuss about the **Joint Probability** p(x, y) when _x_ & _y_ are **Continuous RV**.

<br>
> #### Joint Probability Distribution: Discrete Case
> - Let _X_ and _Y_ be discrete randome variables. The **joint probability distribution** of _x_ and _y_ is given by:
> \begin{equation}p(x,\;y)\;=\;P(X\;=\;x,\;Y\;=\;y)\end{equation}
> defined for all states _x_ and _y_.<br>
<br>
>- All joint probability functions must satisfy:<br>
<br>
>-- 1) _p(x, y) &ge; 0, &nbsp;&nbsp;&nbsp; x, y &isin; (R)_<br>
>-- 2) _&sum;<sub>x</sub>&sum;<sub>y</sub>p(x, y) = 1_<br>
<br>
>- The cumulative distribution function (discrete RV) is defined as:
> \begin{equation}cdf(x,\;y)\;=\;P(X\;\leq\;x,\;Y\;\leq\;y),\;\;\;(x,\;y)\;\in\;\mathbb{R}^{2}\end{equation}
> \begin{equation}cdf(x,\;y)\;=\;\sum_{x=-\infty}^{a}\sum_{x=-\infty}^{b}p(x,\;y)\end{equation}

<br>
<hr>
<br>

> #### Joint Probability Distribution: Continuous Case
>- Let _X_ and _Y_ be continuous randome variables.
>- Let _f(x, y)_ be a **bivariate** function which forms a probability surface in three dimensions.
>- The probability that _x_ lies in one interval and that _y_ lies in another interval is represented as a volume under this surface.
> \begin{equation}P(a\;\leq\;X\;\leq\;b,\;c\;\le\;Y\;\le\;d)\;=\;\int_{c}^{d}\int_{a}^{b}f(x,\;y)dxdy\end{equation}
>- Cumulative distribution function (Continuous RV):
> \begin{equation}cdf(a,\;b)\;=\;P(X\;\leq\;a,\;Y\;\le\;b)\;=\;\int_{-\infty}^{b}\int_{-\infty}^{a}f(x,\;y)dxdy\end{equation}

<br>
<hr>
<br>

> #### Marginal Probability Distribution: Conitnuous Case
> - Marginal probability function of _x_ and _y_ is given by:
> \begin{equation}f(x)\;=\;\int_{-\infty}^{\infty}f(x,\;y)dy\end{equation}
> and
> \begin{equation}f(y)\;=\;\int_{-\infty}^{\infty}f(x,\;y)dx\end{equation}

<br>
<hr>
<br>

> #### Conditional Probability Distributions: Continuous Case
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-09-Continuous_Probability_Distributions/conditional_probability_distributions_discrete_continuous_cases.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Independent Random Variables: Continuous Case
>- Discrete Case: Two discrete RV _x_ and _y_ are independent, **if and only if**, for all states _r_ and _s_ of variables _x_ and _y_,
> \begin{equation}p(x\;=\;r,\;y\;=\;s)\;=\;p(x\;=\;r)p(y\;=\;s)\end{equation}
> for all states _r_ of _x_.<br>
<br>
> NOTE: <br>
> Joint Probability, _p(x=r, y=s)_ = the product of **independent** Marginal Probability, _p(x=r)p(y=s)_.<br>
<br>
>- Continuous Case: Continuous RV _x_ and _y_ are said to the independent if,
> \begin{equation}f(x,\;y)\;=\;f(x)f(y)\end{equation}
> for all values of _x_ and _y_.<br>

<br>
<hr>
<br>

> #### Expected Values: Continuous Case
>- If _x_ and _y_ are discrete RV and _g(x, y)_ is any real-valued functions, the expected value of _g(x, y)_ is:
> \begin{equation}E[g(x,\;y)]\;=\;\sum_{x}\sum_{y}g(x,\;y)p(x,\;y)\end{equation}
> The sum is over all values of _(x, y)_ for which _p(x, y) > 0_.<br>
<br>
>- If _x_ and _y_ are continuous RV and _f(x, y)_ is a joint probability density function, the expected value of _g(x, y)_ is:
> \begin{equation}E[g(x,\;y)]\;=\;\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(x,\;y)f(x,\;y)dxdy\end{equation}<br>
<br>
>- If _x_ and _y_ are **independent** with means _&mu;<sub>x</sub>_ and _&mu;<sub>y</sub>_, then:
> \begin{equation}E(xy)\;=\;E(x)E(y)\end{equation}<br>
<br>
>- If _x_ and _y_ are independent, _g_ is a function of _x_ alone and _h_ is a function of _y_ alone, then:
> \begin{equation}E[g(x)h(y)]\;=\;E[g(x)]E[h(y)]\end{equation}<br>

<br>
<hr>
<br>

> #### Covariance: Continuous Case
>- Covariance helps to assess the relationship between two variables.<br>
<br>
>- Two variables have positive covariance:<br>
>-- If _y_ tends to be large when _x_ tends to be large.<br>
>-- If _y_ tends to be small when _x_ tends to be small.<br>
<br>
>- Two variables have negative covariance:<br>
>-- If _y_ tends to be small when _x_ tends to be large.<br>
>-- If _y_ tends to be large when _x_ tends to be small.<br>

>- Covariance between two random variables _x_ and _y_ is given by:
> \begin{equation}cov(x,\;y)\;=\;E[(x\;-\;\mu_{x})(y\;-\;\mu_{y})]\;=\;E(xy)\;-\;\mu_{x}\mu_{y}\end{equation}
> where _&mu;<sub>x</sub> = E(x)_ and _&mu;<sub>y</sub> = E(y)_.

<br>
<hr>
<br>

> #### Correlation: Continuous Case
>- Covariance depends on the **units of measurement**. (ex: covariance = 0.2 m<sup>2</sup> = 200 cm<sup>2</sup>)
>- We need a measure that allows us to judge the strength of the association regardless of the units.

>- Correlation between two random variables _x_ and _y_ is given by:
> \begin{equation}\rho\;=\;\frac{E[(x\;-\;\mu_{x})(y\;-\;\mu_{y})]}{\sqrt{\sigma_{x}^{2}\sigma_{y}^{2}}}\;=\;\frac{cov(x,\;y)}{\sqrt{\sigma_{x}^{2}\sigma_{y}^{2}}}\;=\;\frac{cov(x,\;y)}{\sigma_{x}^{2}\sigma_{y}^{2}}\end{equation}
>- It is a unitless quantity that takes on values between -1 and +1.
>- If _x_ and _y_ are independent RV. Then:
> \begin{equation}cov(x,\;y)\;=\;E(xy)\;-\;E(x)E(y)\;=\;E(x)E(y)\;-\;E(x)E(y)\;=\;0\end{equation}

<br>
<hr>
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
