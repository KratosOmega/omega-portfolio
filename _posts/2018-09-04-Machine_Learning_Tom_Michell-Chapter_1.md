---
layout: post
section-type: post
title: Machine Learning - Introduction
category: Machine Learning
tags: [ 'machine_learning', 'ai', 'reading' ]
comments: true
---

<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### 1. Well-Posed Learning Problems
<br>
- #### Disciplines and examples of their influence on Machine Learning:
>- **Artificial Intelligence**: Learning symbolic representations of concepts. Machine learning as a search problem. Learning as an approach to improving problem solving. Using prior knowledge together with training data to guide learning.
>- **Bayesian Methods**: Bayes' theorem as the basis for calculating probabilities of hypotheses. The naive Bayes classifier. Algorithms for estimating values of unobserved variables.
>- **Computational Complexity Theory**: Theoretical bounds on the inherent complexity of different learning tasks, measured in terms of the computational effort, number of training examples, number of mistakes, etc. required in order to learn.
>- **Control Theory**: Procedures that learn to control processes in order to optimize predefined objectives and that learn to predict the next state of the process they are controlling.
>- **Information Theory**: Measures of entropy and information content. Minimum description length approaches to learning. Optimal codes and their relationship to optimal training sequences for encoding a hypothesis.
>- **Philosophy**: Occam's razor, suggesting that the simplest hypothesis is the best. Analysis of the justificaiton for generalizing beyond observed data.
>- **Psychology and neurobiology**: The power law of practice, which states that over a very broad range of learning problems, people's response time improves with practice according to a power law. Neurobiological studies motivating artificial neural network models of learning.
>- **Statistics**: Characterization of errors (e.g., bias and variance) that occur when estimating the accuracy of a hypothesis based on a limited smaple of data. Confidence intervals, statistical tests.

<br>

- #### What is learning problem?
>- Definition: A computer program is said to **learn** from experience _E_ with respect to some class of taks _T_ and performance measure _P_, if its performance at tasks in _T_, as measured by _P_, improves with experience _E_.<br>
<br>
>- **3 features** for a well-defined learning problem:<br>
> -- **Task** _T_: the class of tasks.
> -- **Performance measure** _P_: the measure of performance.
> -- **Training experience** _E_: the source of experience.

<br>
<hr>
<br>

### 2. Designing a Learning System
<br>
- #### 2.1 Choosing the Training Experience
>- The **first** design choice is to choose the type of training experience from which our system will learn.<br>
<br>
>- THREE important **attributes** to consider when choosing training experience:
> -- 1. whether the training experience provides _direct_ or _indirect_ **feedback** regarding the choices made by the performance system.<br>
> -- 2. the degree to which the learner _controls_ the sequence of training examples.<br>
> -- 3. how well it represents the distribution of examples over which the final system performance _P_ must be measured. (In general, learning is most reliable when the **training examples** follow a distribution similar to that of future **test examples**.)

<br>

- #### 2.2 Choosing the Target Function
>- The **second** design choice is to determine exactly _what type of knowledge will be learned_ and _how this will be used_ by the performance program.<br>
<br> 
>- Operational Description vs. Nonoperational Description<br>
> -- Operational description; a description that can be used by the evaluation function to evaluate performance.<br>
<br>
>- Function Approximation is also called **the process of learning the target function**<br>

<br>

- #### 2.3 Choosing a Representation for the Target Function
>- The **third** design choice is to choose a representation that the learning program will use to describe the learning function.<br>
<br>
>- In general, the choice of representation involves a crucial tradeoff:<br>
> -- On one hand, we wish to pick a very expressive representation to all representing as close an approximation as possible to the ideal target function.<br>
> -- On the other hand, the more expressive the representation, the more training data the program will require in order t ochoose among the alternative hypotheses it can represent.<br>
<br>
>- Partial design of learning program:<br>
> -1. Task _T_<br>
> -2. Performance measure _P_<br>
> -3. Training experience _E_<br>
> -4. Target function _V_<br>
> -5. Target function representation _V'_ = w_0 + w_1 * x_1 + w_2 * x_2 + ... + w_i * x_i<br>
<br>
> -* The first 3 items (1-3) above correspond to the specification of the learning task.<br>
<br>
> -* The final 2 items (4-5) constitue design choices for the implementation of the learning program.<br>
<br>
> -*The net effect of this set of design choices is to reduce the problem of learning a task to the problem of learning values ofr the coefficients w_0 throught w_n in the target function representation.<br>

<br>

- #### 2.4 Choosing a Function Approximation Algorithm
>- To learn the target function representation _V'_, we require a set of training examples, each describing a specific training input _t_ and the training value _V(t)_ for _t_. 
>- In other words, each training example is an ordered pair of the form _(t, V(t))_.
>- ex: ((x_1 = 1, x_2 = 0, ..., x_i = 5), 100)<br>
><br>
> ##### 2.4.1 Estimating Training Values<br>
> ...
<br>
<br>
> ##### 2.4.2 Adjusting The Weights<br>
> \begin{equation}E\;\equiv\;\sum_{(t,\;V(t))\;\in\;training\;examples}(V(t)\;-\;V'(t))^{2}\end{equation}<br>
> The goal is to find the weights, or equivalently the _V'_, that minimize E for the observed training examples.<br>
<br>
> There are several algorithms for finding weights of a linear function that minimize _E_. One of them is called the _least mean squares_ or _LMS training rule_.<br>
<br>
> **LMS weight update rule**:<br>
> For each training example _(t, V(t))_<br>
> -- Use the current weights to calculate _V'(t)_<br>
> -- For each weight w_i, update it as:
> \begin{equation}w_{i}\;:=\;w\_{i}\;+\;\eta\;*\;(V(t)\;-\;V'(t))\;\*\;x\_{i}\end{equation}
> _n_ is a small constant that moderates the size of the weight update.

<br>

- #### 2.5 The Final Design
>- The final design can be described by 4 distinct program modules, which represent the central components in many learning systems:<br>
<br>
> 1) The **Performance System** is the module that must solve the given performance task by using the _learned target function(s)_. It takes an instance of a new problem as input and produces a trace of its solution as output.<br>
<br>
> 2) The **Critic** takes as input the history or trace of task and produces as output a set of training examples of the target function.<br>
<br>
> 3) The **Generalizer** takes as input the training examples and produces an output hypothesis that is its estimate of the target function. It generalizes from the specific training examples, hypothesizing a general function that covers these examples and other cases beyond the training examples.<br>
<br>
> 4) The **Experiment Generator** takes as input the current hypothesis (currently learned function) and outputs a new problem for the _Performance System_ to explore. Its _role_ is to pick new practice problems that will maximize the learning rate of the overall system.<br>

<br>
<hr>
<br>

### 3. Perspectives and Issues in Machine Learning
<br>
>- One useful perspective on machine learning is that: it involves **searching** a very large space of possible hypotheses to determine one that best fits the observed data and any prior knowledge held by the learner.<br>
<br>
- #### 3.1 Issues in Machine Learning<br>
...

<br>

<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s [Machine Learning](https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077)
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s authorization.
<br>
