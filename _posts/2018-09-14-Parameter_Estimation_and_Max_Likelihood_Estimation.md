---
layout: post
section-type: post
title: Parameter Estimation & Max Likelihood Estimation
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>


### Probabilistic Inference vs. Parameter Estimation
<br>
> #### Probabilistic Inference
>-  *Probabilistic Inference* involves computation of probabilities for events, given a _model family_ and _choices for the parameters_.<br>
>- Given parameter a, the probability for each state of _x_ can be computed using **Binomial Distribution**:
> \begin{equation}p(x)\;=\;{n\choose x}a^{x} (1\;-\;a)^{n-x},\;\;\;x\;=\;1,\;2,\;3,\;...,\;n\end{equation}
<br>
<hr>
<br>

> #### Source of Probability Distributions
>- In reality, ONLY **Samples** & **Data** are available to us. **Parameter** (_a_ in our formula) is not available, but needs to be estimated.
>- In general, we need to determine both the **probability model** & the **parameters** from the question.<br>
> -- We have some understanding of how to choose a suitable probability model from a given situation.<br>
> -- We need to estimate parameters using the collected data.<br>

<br>
<hr>
<br>

> #### Parameter Estimation
>- **Parameter Estimation** involves estimation of parameters, given a _parametric model_ & _observed data_ drawn from it.<br>
> -- e.g.: 20 apples were inspected and 3 apples were found to be damaged.<br>
> -- Then, parameter _a_ = 3/20, however, we need to be careful of estimate our parameter, since the same parameter can be generated from different Distributions.<br>

<br>
<hr>
<br>

> #### Approaches for Parameter Estimation - Maximum Likelihood Estimation (MLE)
>- Parameters are assumed to be **fixed** but **unknown**.<br>
>- ML solution seeks the solution that _best explains the dataset X_<br>
<br>
> \begin{equation}\hat{\theta\;}\_{MLE}\;=\;argmax\_{\theta}p(X\mid \theta)\end{equation}
> -- _X_ is the dataset that is drawn from **some** probability distribution _p(|&theta;)_, using **some** parameter _&theta;_.<br><br>
> -- Also, assume that we know the model family of probability distribution _p(|&theta;)_ that we used for sample _X_ (which is also available to us).<br><br>
> -- Using all available information, we try to estimate _&theta;_.<br><br>
> -- _p(X|&theta;)_, refers to the likelihood that the dataset _X_ is generated using &theta;. This likelihood is a function _f(&theta;)_ of _&theta;_. <br><br>
> -- _argmax<sub>&theta;</sub>_, refers to that the _&theta;_ at which this likelihood is maximized. In other words, we need to find the _&theta;_ that best explains the dataset _X_.<br><br>
>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/MLE_a.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Approaches for Parameter Estimation - Bayesian Estimation
>- Parameters are assumed to be **random variables** with some **known** a _priori_ distribution _p(&theta;)_ (before we have access to dataset _X_).<br>
>- Bayesian methods seek to estimate the _posterior_ density _p(&theta;|X)_ (after we have access to dataset _X_).<br>
<br>
> \begin{equation}p(\theta\mid X)\;\propto\;p(X\mid\theta)p(\theta)\end{equation}
> \begin{equation}\hat{\theta\;}\_{MAP}\;=\;argmax\_{\theta}p(\theta\mid X)\end{equation}

> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/MAP_a.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Properties of Estimators
>- **Consistency**: An estimator is consistent if the estimate _&theta;^_ it constructs, is guaranteed to converge to the true parameter value _&theta;_ as the quantity of data to which it is applied increases.<br>
<br>
>- **Bias**: The bias of an estimator _&eta;_ is defined as the deviation of the expectation of the estimate from the true value:<br>
> \begin{equation}E[\hat{\theta\;}\_{\eta}]\end{equation}
> when the sampling of data is viewed as a stochastic process, then the estimated parameter _&theta;^<sub>&eta;</sub>_ can be viewed as a continuous random variable. And _E[&theta;^<sub>&eta;</sub>]_ is the average expectation of all _&theta;^_.
> \begin{equation}E[\hat{\theta\;}\_{\eta}]\;=\;\theta\;\Rightarrow\;\text{the estimator is Unbiased}\end{equation}
> \begin{equation}E[\hat{\theta\;}\_{\eta}]\;\neq\;\theta\;\Rightarrow\;\text{the estimator is Biased}\end{equation}
<br>
>- **Variance (and efficiency)**: All else being equal, an estimator with smaller variance is preferable to one with greater variance.
> \begin{equation}V[\hat{\theta\;}\_{\eta}]\;=\;\\end{equation}

<br>
<hr>
<br>

> #### Estimating Bias
>- Estimator of mean is unbiased if:<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/estimating_bias_mean.png){:class="img-responsive"}<br>
>- Estimator of variance is unbiased if:<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/estimating_bias_variance.png){:class="img-responsive"}<br>

<br>
<hr>
<br>


> #### Assessing Bias in an estimator:
>- The question is whether or not the estimator differs from the actual parameter.<br>
>- If the actual value is not different from the estimated value, we call it an unbiased estimator.<br>

<br>
<hr>
<br>

> #### Bias vs. Variance
>- Bias: How close is the estimate to the true value (on average)><br>
>- Variance: How much does it change for different datasets?<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/bias_vs_variance.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Bias-Variance Tradeoff
>- In most cases, you can only decrease one of them at the expense of the other.<br>
>- Due to conflict in trying to simultaneously minimize these two sources of error:<br>
> -- 1) Error due to wrong assumptions in the learning algorithm (missses regularities in the data - underfitting).<br>
> -- 2) Error from sensitivity to small fluctuations (noise) in the data (models noise in the data-overfitting).<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/bias-variance_tradeoff.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

### Max. Likelihood vs. Bayesian
<br>
> #### Random Sampling: Independent & Identically Distributed
>- _x ~ p_: _x_ is a sample that is drawn from distribution _p_.
>- Sampling depends on several items:<br>
>-- Distribution (along with the parameters)<br>
>-- Sample size _n_<br>
>-- Method of sampling (with or without replacement)<br>
<br>
>- _x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>_ form a random sample of size _n_ if:<br>
>-- x<sub>i</sub>'s are independently sampled.
>-- Ever x<sub>i</sub> is drawn from the same probability distribution (same model family & same parameters), i.e., identically distributed.<br>
<br>
>- If a random sample satisfies the above two properties, we say x<sub>i</sub>'s are I.I.D..

<br>
<hr>
<br>

> #### Joint Probability for observations / samples / data
>- The probability density function (pdf) of a RV _x_, conditioned on the set of parameters &theta;, is denoted as _f(x|&theta;)_.<br>
>-- This function identifies the data generating process that underlies an observed sample of data.<br>
<br>
>- For a variable _x_, a set of I.I.D. observations _D=(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>)_ are drawn using a pdf _f(x|&theta;)_.<br>
<br>
>- The joint density of _n_ I.I.D. observations from this process is:
> \begin{equation}p(x\_{1},\;x\_{2},\;...,\;x\_{n}\mid\theta)\end{equation}
<br>
>- As each of the observations are **independent** and **identically distributed**:
> \begin{equation}p(x\_{1},\;x\_{2},\;...,\;x\_{n}\mid\theta)\;=\;p(x\_{1}\mid\theta)p(x\_{2}\mid\theta)...p(x\_{n}\mid\theta)\;=\;\prod\_{i=1}^{n}f(x_{i}\mid\theta)\end{equation}

<br>
<hr>
<br>

> #### Likelihood function _L(&theta;|D)_
>- This joint density is the **likelihood function**, defined as a function of the **unknown parameter** _&theta;_:<br>
> \begin{equation}p(x\_{1},\;x\_{2},\;...,\;x\_{n}\mid\theta)\;=\;\prod\_{i=1}^{n}f(x_{i}\mid\theta)\;=\;L(\theta\mid x)\end{equation}
>- Note that we write the joint density of observations as _p(D|&theta;)_, whereas the likelihood function, is written as _L(\theta|D)_.<br>
<br>
>- Likelihood function is also denoted as _L(&theta;)_ for simplicity.<br>

<br>
<hr>
<br>

> #### PDF vs. Likelihood Function
>- Probability density function _p(x)_:<br>
>-- Function of state of RV _x_.<br>
>-- Normalized &sum;<sub>x</sub>p(x) = 1.<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/pdf_example.png){:class="img-responsive"}<br>
<br>

>- Likelihood function L(&theta;|x):<br>
>-- Function of unknown parameter _&theta_.<br>
>-- Unnormalized.<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/likelihood_example.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

<br>
> #### Maximum Likelihood Estimation (MLE)
>- MLE solution seeks the solution that best explains the dataset _X_<br>
> \begin{equation}\hat{\theta\;}\_{MLE}\;=\;argmax\_{\theta}p(D\mid \theta)\;=\;argmax\_{\theta}L(\theta)\end{equation}
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/likelihood_example_mle.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Log-Likelihood<br>
>- Likelihood L(&theta;&#8739;D) for n observations is a product of n, <br>
> where each 0 &le; p(x<sub>i</sub>&#8739;&theta;) &le; 1.<br>
<br>
>- As a result, likelihood function will taken on extremely small values: <br>
> _L(&theta;) = &theta;<sup>NH</sup>(1 - &theta;)<sup>NT</sup>_<br>
<br>
>- **log-likelihood function** helps to avoid numerical underflow:
> \begin{equation}l(\theta)\;=\;logL(\theta)\end{equation}
>- Logarithm is a monotonic function, so the logarithm of a function achieves its maximum value at the same points as the function itself.<br>
<br>
>- It is easier to differentiate for **sum of terms** rather than **product of terms**.<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/log-likelihood_example.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

> #### Finding &theta; where Log-Likelihood is maximum - Approach I
>- Compute derivative and solve for parameters.<br>
>-- If possible, compute the **first derivative** of the log-likelihood and set it to 0.<br>
>-- Solve ofr parameters.<br>
>-- Compute partial derivatives when there are multiple unknown parameters.

<br>
<hr>
<br>

> #### Finding &theta; where Log-Likelihood is maximum - Approach II
>- When approach I is not possible (particularly when the model involves many parameters and its PDF is highly non-linear), the use **gradient descent approach**.<br>
>-- Use negative log-likelihood (also referred to as a cost function)<br>
>-- Randomly initialize and then incrementally update our weights by calculating the slope of our objective function.<br>
>-- When applying the cost function, we want to continue updating our weights until the slope of the gradient gets as close to zero as possible.<br>
<br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-14-Parameter_Estimation_and_Max_Likelihood_Estimation/gradient_descent_approach_example.png){:class="img-responsive"}<br>

<br>
<hr>
<br>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
