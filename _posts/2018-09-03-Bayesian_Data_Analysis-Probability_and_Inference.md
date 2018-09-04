---
layout: post
section-type: post
title: Probability and Inference
category: Probability
tags: [ 'probability', 'reading' ]
comments: true
---
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### 1.1 The three steps of Bayesian data analysis
<br>
>- The essential characteristic of Bayesian methods is their explicit **use of probability** for **quantifying uncertainty** in **inferences** **based on statistical data analysis**.<br><br>
>- The _process_ of Bayesian data analysis:<br>
>&nbsp;&nbsp;1. Setting up a full probability model - a _joint probability distribution_ for all **observable and unobservable** quantities in a problem.<br>
>&nbsp;&nbsp;2. Conditioning on observed data: calculating and interpreting the appropriate _posterior distribution_ - the conditional probability distribution of the unobserved quantities of ultimate interest, given the observed data.<br>
>&nbsp;&nbsp;3. Evaluating the fit of the model and the implications of the resulting posterior distribution: how well does the model fit the data, are the substantive conclusions reasonable, and how sensitive arethe results to the modeling assumptions in step 1?<br><br>
>- The **Central feature** of Bayesian inference: is the direct quantification of uncertainty, means that there is no impediment in principle to fitting models with many parameters and complicated multilayered probability specifications.<br>

<br>
<hr>
<br>

### 1.2 General notation for statistical inference
<br>
>- **Statistical inference** is concerned with drawing conclusions, from numerical data, about quantities that are **not observed**.<br><br>
>- **Causal inference** is the comparison between the observed outcome in each patient and the patient's unobserved outcome if exposed to the other treatment.<br><br>
>- 2 kinds of **Estimands** (the unobserved quantities for which statistical inference are made):<br>
>&nbsp;&nbsp;1. potentially observable quantities.<br>
>&nbsp;&nbsp;2. quantities that are not directly observable.<br>

<hr>

##### Parameters, data, and predictions
<br>
>- Unobservable vector quantities or population _parameters_ of interest is denoted as:
>\begin{equation}\theta\end{equation}
>- The observed data is denoted as:
>\begin{equation}y\end{equation}
>- The unknown, but potentially observable, quantities is denoted as:
>\begin{equation}\widetilde{y}\end{equation}
>- Generally, using:<br>
>&nbsp;&nbsp; * Greek letters &rarr; paramenters<br>
>&nbsp;&nbsp; * lower case Roman letters &rarr; observed or observable scalars and vectors (or matrices)<br>
>&nbsp;&nbsp; * upper case Roman letters &rarr; observed or observable matrices<br>

<hr>

##### Observational units and variables
>- Data are gathered on each of a set of _n_ objects or _units_ is writen as a vector:
>\begin{equation}y = (y_{1},...,\;y_{n})\end{equation}

<hr>

##### Exchangeability
>- The usual starting point of a statistical analysis is the assumption that the _n_ values _yi_ may be regarded as _exchangeable_.<br><br>
>- **Exchangeable** means that we express uncertainty as a _joint probability density_ p(y1,..., yn) that is invariant to permutations of the indexes.<br><br>
>- A **nonexchangeable** model would be appropriate if inofrmation relevant t othe outcome were conveyed in the unit indexes rather than by explanatory variables.<br><br>
>- Commonly modeling data from an _exchangeable distribution_ as _independently and identically distributed_ (**iid**) given some unknow parameter vector &theta; with distribution p(&theta;).

<hr>

##### Explanatory variables
>- **Explanatory variables (or covariates)** are observations on each unit that we do not bother to model as _random_, and corresponding notations as following:
>\begin{equation}x \;\;\; \text{explanatory variables}\end{equation}
>\begin{equation}X \;\;\; \text{entire set of explanatory variables for all n units}\end{equation}
> _X_ is a matrix with _n_ rows and _k_ columns, if there are _k_ explanatory variables.

<hr>

##### Hierarchical modeling
>- **Hierarchical model** (a.k.a. multilevel models) are used wen information is availabel on several different levels of observational units.<br>

<br>
<hr>
<br>

### 1.3 Bayesian inference




<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/) CS6035 (Learning Probabilistic Model) course in University of Cincinnati.
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Atluri](http://homepages.uc.edu/~atlurigm/)'s authorization.
<br>
