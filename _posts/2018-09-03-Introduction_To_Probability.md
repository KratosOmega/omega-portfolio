---
layout: post
section-type: post
title: Introduction To Probability
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### Essential Elements of a Probability Distribution

- #### Random Experiment:
> Definition: A phenomenon whose outcome is not predictable with certainty, but the set of all possible outcomes is known.
>- ex: coin toss, roll of a dice.

- #### Random variables:
> Definition: A variable whose possible values/state are outcomes of a random phenomenon/experiment. 
>- ex: x is a random variable that capture outcome of a coin toss.

- #### Domain: 
> Definition: dom(x) denotes the set of possible state variable x can take.
>- ex: in the case of a coin toss, dom(c) = {heads, tails}.
>- ex: rolling a dice, dom(d) = {1, 2, 3, 4, 5, 6}

- #### Probability:
> Definition: p(X = s), is the probability of variable x being in state s.<br>
>- p(X = s) = 1, we are certain x is in state s.
>- p(X = s) = 0, we are certain x is NOT in state s.
>- 0 < p(X = s) < 1, represent the degree of certainty of state occupancy.

- #### Kolmogorov Axioms:
>- 1st axiom: probability of variable x in state s lies between 0 and 1:
 \begin{equation}0 \leq p(X = s)  \leq 1\end{equation}
>- 2nd axiom: the summation of the probability over all the states is 1:
\begin{equation}\sum_{X \in dom(X)} = p(X = X) = 1 \;\;\; (or) \;\;\; \sum_{X} = p(X) = 1 \end{equation}
>- 3rd axiom: For mutually exclusive events s1 and s2:
\begin{equation}p(X = s_{1} \; \cup \; X = s_{2}) = p(X = s_{1}) + p(X = s_{2} )\end{equation}

- #### Probability Distribution
>- Given:
>> x is a randome variable.<br>
>> x's domain is dom(x) = {s1, s2, ..., sn}.<br>
>- A **FULL** specificatfion of the **probability values** for **each** of the variable **states**, p(x), is a probability distribution.
>- ex: in other word, list the probabilities of all states<br>
>>* p(x = s1) = 0.1
>>* p(x = s2) = 0.2
>>* ...
>>* p(x = sn) = 0.n

- #### Probability table: can be write as a **VECTOR**, whose component values' sum = 1.
> The order of the components within the vector is arbitrary (not matter).

- #### Interpretation:
>* Frequentist version - _empirical_: Probability is defined w.r.t a potentially infinite repetition of experiments.
<br>
>* Bayesian version - _subjective_: It is a _degree of belief_ that a certain event may occur.

<br>

<hr>

<br>

### Operations

- #### AND (**Joint Probability**):
>- p(x = a and y = b), the shorthand is writen as below: 
>\begin{equation}p(X, \; Y) \equiv p(X \; \cap \; Y) \;\;\; for \;\;\; p(X \; and \; Y)\end{equation}
>- Independence Definition:
>\begin{equation}p(x_{i}, \; y_{i}) = p(x_{i}) * p(y_{i})\end{equation}
>- Some other formulas that we can have for p(X and b):
>\begin{equation}p(X, Y) = p(X\;|\;Y) * P(Y) = p(Y\;|\;X) * P(X)\end{equation}

- #### OR:
>- For specific states, we write:<br>
>\begin{equation}p(X = a \; or \; Y = b) = p(X = a) + p(Y = b) - p(X = a \; and \; Y = b)\end{equation}
>- More generally, we can write:
>\begin{equation}p(X \; or \; Y) \equiv p(X \; \cup \; Y) = p(X) + p(Y) - p(X \; and \; Y)\end{equation}
> NOTE: p(X or Y) is equivalent to p(Y or X).

- #### Marginalization:
>- **Marginal Probability Distribution** is a probabilisty distribution of a _subset_ of variable.
>- Given a joint distribution, p(X, Y) is the marginal distribution of x is computed as:
>\begin{equation}p(X) = \sum_{Y} p(X, \; Y)\end{equation}
> and
>\begin{equation}p(Y) = \sum_{X} p(X, \; Y)\end{equation}
> which can also be understanded as:
>\begin{equation}p(X = x) = \sum_{y} p(X = x, \; Y = y)\end{equation}
> and
>\begin{equation}p(Y = y) = \sum_{x} p(X = x, \; Y = y)\end{equation}
>which "x" & "y" is the sum of all Xs & Ys.
>- ex: calculate p(row = a) of p(row, col), p(row = a) = p(row = a, col = Sum(cols))
>- More generally, a process called **marginalizing**:
>\begin{equation}p(x_{1}, \; ..., \; x_{i-1}, \; x_{i+1}, \; ..., \; x_{n}) = \sum_{x_{i}} p(x_{1}, \; ..., \; x_{n})\end{equation}
> **Marginalized Out**:
>\begin{equation}x_{i}\end{equation}
> , which is excluded from Xs.
>- **Marginal variables** are:
>\begin{equation}x_{1}, \; ..., \; x_{i-1}, \; x_{i+1}, \; ..., \; x_{n}\end{equation}
> It's easy to see that xi is not on the list.
>- Another note-worthy operation on marginalization:
>\begin{equation}\sum_{X} \frac{p(X, \; Y, \; Z)}{p(Z)} = \frac{\sum_{X} p(X, \; Y, \; Z)}{p(Z)}\end{equation}
> which means that marginalization only takes effect on the relevant probability, e.g., mariginalization on X only affects p(X, Y, Z), but not p(Z).

- #### Conditional Probability & Bayes' Rule:
>- The probability of event x conditioned on knowing event y (or more shortly, the probability of x given y) is defined as:
>\begin{equation}p(x\;|\;y) \equiv \frac{p(x, \;y)}{p(y)} = \frac{p(y\;|\;x)p(x)}{p(y)} \;\;\; (Bayes' Rule)\end{equation}
> where
>\begin{equation}p(y) = \sum_{x} p(x)p(y\;|\;x) = \int p(x,\;y)dx = \int p(x)p(y\;|\;x)dx\end{equation}

- #### Probability Tables:
>- Large numbers of variables
>- Exchangeability:
> A probability distribut assigns a value to each of the joint state of the variables, thus:
>\begin{equation}p(T, \; J, \; R, \; S) = p(J, \; S, \; R, \; T)\end{equation}
>- In each case the join setting of the variables is simply a different index to the same probability table.
>- Not to be confused with function f(x, y)

<br>

<hr>

<br>

### Independence

- #### Independence
>- Variables x and y are **independent** if knowing one event gives no extra information about the other event.
>- Mathematically, this is expressed by:
>\begin{equation}p(X,\;Y) = p(X)p(Y)\end{equation}
>- Independence of x and y is equivalent to:
>\begin{equation}p(X\;|\;Y) = p(X), \;\;\; p(Y\;|\;X) = p(Y)\end{equation}
>- If p(x|y) = p(x) for **all states of x and y** (p(X|Y) = p(X)), then the variables x and y are said to be independent, and write as:
>\begin{equation}X \unicode{x2AEB} Y\end{equation}
<br><br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-03-Introduction_To_Probability/independence_vs_mutually_exclusive.png){:class="img-responsive"}<br>
<br>
>- Interpretaion: ?
>- Factorisation: ?

- #### Conditional Independence
>- Two sets of variables X and Y are independent of each other given the state of the set of variable Z, write as follow:
>\begin{equation}X \; \unicode{x2AEB} \; Y \; | \; Z\end{equation}
> It means that:
> \begin{equation}p(X,\;Y\;|\;Z) = p(X\;|\;Z)p(Y\;|\;Z)\;\;\; and \;\;\;p(X\;|\;Y,\;Z) = p(X\;|\;Z)\end{equation}
> for all states of X, Y, Z.
>- In case the conditioning set is empty, we write:
>\begin{equation}X \unicode{x2AEB} Y \;\;\; for \;\;\; X \unicode{x2AEB} Y|\emptyset\end{equation}
> in which case X is (unconditionally)  independent of Y.
>- By given:<br>
>-* three variables X, Y, Z<br>
>-* their joint probability p(X, Y, Z)<br>
>-* and X \independent Y | Z<br>
> \begin{equation}p(X,\;Y) = \sum_{Z}\underbrace{p(X\;|\;Z)p(Y\;|\;Z)p(Z)}\_{\text{cond. indep.}}\;\neq\;\sum_{Z}\underbrace{p(X\;|\;Z)p(Z)}\_{p(X)}\sum_{Z}\underbrace{p(Y\;|\;Z)p(Z)}\_{p(Y)}\end{equation}
>- If X and Y are not conditionally independent, they are conditionally dependent, which written as:
> \begin{equation}X\;\unicode{x2AEA}\;Y\;|\;Z\end{equation}
>- And we also have:
> \begin{equation}p(X,\;Y) = \sum_{Z}p(X,\; Y\;|\;Z)p(Z) = \sum_{Z}p(X\;|\;Z)p(Y\;|\;Z)p(Z)\end{equation}
> this also indicates:
> \begin{equation}\text{while} \;\;\; X\;\unicode{x2AEB}\;Y\;|\;Z, \;\;\; \text{it is not true that} \;\;\; X\;\unicode{x2AEB}\;Y\end{equation}
<br>
<br>

<hr>

<br>

### Reasoning

- #### Probabilistic Reasoning:
>- Inspector Clouseau Example ?
- #### Scientific Inference:
>- Much of science deals with problems of the form: **tell me something about the variable &Theta; (which we want to know, but we actually don't) given that I have observed data _D_ (which we have already known) and have some knowledge of the underlying data generating mechanism.**<br>
>Our interest is then the quantity:
>\begin{equation}p(\theta\;|\;D) = \frac{p(D\;|\;\theta)p(\theta)}{p(D)} = \frac{p(D\;|\;\theta)p(\theta)}{\int_{\theta}p(D\;|\;\theta)p(\theta)}\end{equation}
<br><br>
> ![]({{site.baseurl}}/assets/img/posts_img/2018-09-03-Introduction_To_Probability/scientific_inference.png){:class="img-responsive"}<br>
<br>
>- Generative model of the dataset:
>\begin{equation}p(D\;|\;\theta)\;\;\;a.k.a\;\;\;(\text{likelihood, or sampling distribution})\end{equation}
> it works well with physical model of the world which typically postulate how to generate observed phenomena, assuming we know the model.
>- Prior belief about which variable values are appropriate:
>\begin{equation}p(\theta)\;\;\;a.k.a\;\;\;(\text{prior distribution})\end{equation}
>- Infereed posterior distribution of the variable in light of the observed data:
>\begin{equation}p(\theta\;|\;D)\;\;\;a.k.a\;\;\;(\text{posterior distribution})\end{equation}
>- Unknown but observable dataset:
>\begin{equation}p(D)\;\;\;a.k.a\;\;\;(\text{evidence or marginal likelihood})\end{equation}
>- The term _likelihood_ is used for the probability that a model generates observed data.
>- More fully, if we condition on the model _M_, we have:
>\begin{equation}p(\theta\;|\;D,\;M) = \frac{p(D\;|\;\theta,\;M)p(\theta\;|\;M)}{p(D\;|\;M)}\end{equation}
> where we see the role of the likelihood p(D|&Theta;, M) and marginal likelihood p(D|M). Thus, the _marginal likelihood_ is also called the _model likelihood_.<br>
>- Note:<br>
>&nbsp;&nbsp; * **prior**: means it is not conditional on a previous observation of the process.<br>
>&nbsp;&nbsp; * **posterior**: means it is conditional on a previous observation of the process.<br>
>&nbsp;&nbsp; * **predictive**: means it is the distribution for a quantity that is observable.<br>
<br>
>- Prior: We actually have the data **prior (or before)** our observation.
>- Posterior: **After** we **observed** ("given"), we know something about the object as it is **post (or after)** the **observation**.
>- Evidence: We **witness** the data, thus it's an evidence to us.
>- Likelihood: ...

<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
