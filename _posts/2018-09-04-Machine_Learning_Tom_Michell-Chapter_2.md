---
layout: post
section-type: post
title: ML - Concept Learning & the General-to-Specific Ordering
category: Machine_Learning
tags: [ 'machine_learning', 'ai', 'reading' ]
comments: true
---

<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/javascript" src="http://www.hostmath.com/Math/MathJax.js?config=OK"></script>
</head>

### 1. Introduction
<br>
>- **Concept Learning** is acquiring the definition of general category given a sample of positive and negative training examples of the category.
>- **Concept Learning** is formulated as a problem of _searching_ through a predefined space of potential _hypotheses_ (a general-to-specific ordering of hypotheses) for the hypothesis that _best fits_ the traing examples.
>- The "concept" can be viewd as describing some subset of objects or events defined over a larger set (e.g., the subset of animals that constitue birds) and can be thought of as a **boolean-valued** function defined over this larger set (e.g., a function defined over all animals, whose value is _true_ for birds and _false_ for other animals).

<br>
<hr>
<br>

### 2. A Concept Learning Task
<br>
>- In general, any concept learning task can be described by:<br>
> -- the _set of instances_ over which the target function is defined,<br>
> -- the target function,<br>
> -- the set of candidate hypotheses considered by the learner,<br>
> -- and the set of available training examples.<br>

<br>

> #### 2.1 Notation
<br>
>- The **set of instances**, denoted by **X**: the set of items over which the concept is defined.
>- The **target concept**, denoted by **c**: the concept or function to be learned.
> -- In general, _c_ can be any boolean-valued function defined over the instances _X_ (_c:X &rarr; {0, 1}_).
>- The **set of training examples**: each consisting of an instance _x_ from _X_, along with its target concept value _c(x)_.
>- Instances for which _c(x)_ = 1 are called **positive examples**, or **members** of the target concept.
>- Instances for which _c(x)_ = 0 are called **negative examples**, or **nonmembers** of the target concept.
>- Using the ordered pair _&lt;x, c(x)&gt;_ to describe the training example consisting of the instance _x_ and its target concept value _c(x)_.
>- The **set of available training examples** are denoted as **D**.
>- The **set of all possible hypotheses** are denoted as **H**: that the learner used to _hypothesize, or estimate_, c and may consider regarding the identity of the target concept.
>- Each hypothesis **h** in _H_ represents a boolean-valued function defined over _X_ (_h:X &rarr; {0, 1}_).
>- The goal of the learner is to find a hypothesis _h_ such that _h(x) = c(x)_ for all _x_ in _X_.

<br>

> #### 2.2 The Inductive Learning Hypothesis
<br>
>- With the only information available about _c_ is its value over the training examples, the inductive learning algorithms can at best guarantee that the output hypothesis fits the target concept over the training data. 
>- The _fundamental assumption_ of **inductive learning**: Lacking any further information other than _c_, our assumption is that the best hypothesis regarding unseen instances is the hypothesis that best fits the observed training data.
>- **The inductive learning hypothesis**: Any hypothesis found to approximate the target function well over a sufficiently large set of training examples will also approximate the target function well over other unobserved examples.

<br>
<hr>
<br>

### 3. Concept Learning as Search
<br>
>- **Concept learning** can be viewd as the task of searching through a large space of hypotheses implicitly defined by the hypothesis representation.
>- The **goal** of this concept learning searching is to find the hypothesis that best fits the training examples.
>- It's important to note that by selecting a hypothesis representation, the designer of the learning algorithm implicitly defines the space of all hypotheses that the program can ever represent and therefore can ever learn.

<br>

> #### 3.1 General-to-Specific Ordering of Hypotheses
>- General-to-Specific ordering structure of hypotheses is very useful for concept learning algorithms to organize the search through the hypothesis space.
>- G-t-S structure is used on hypothesis space allows algorithms that exhaustively search even inifinite hypothesis spaces without explicitly enumerating every hypothesis.
>- "more general than" relationship:<br>
<br>
> -- First, for any instance _x_ in _X_ and hypothesis _h_ in _H_, we say that _x_ satisfies _h_ **if and only** if _h(x) = 1_.<br>
<br>
> -- We now define the more-general-than-or-equal-to relation in terms of the sets of instances that satisfy the two hypotheses: Given hypotheses h<sub>j</sub> and h<sub>k</sub>, h<sub>j</sub> is more-general-than-or-equal-to h<sub>k</sub> if and only if any instance that satisfies h<sub>k</sub> also satisfies h<sub>j</sub>.<br>
<br>
> -- **Definition**: Let h<sub>j</sub> and h<sub>k</sub> be boolean-valued functions defined over _X_,<br>
> &nbsp;&nbsp;* Then h<sub>j</sub> is **more_general_than_or_equal_to** h<sub>k</sub> (written h<sub>j</sub> &ge;<sub>g</sub> h<sub>k</sub>) if and only if:
> \begin{equation}(\forall x \in X)[(h_{k}(x)\;=\;1)\;\rightarrow\;(h_{j}(x)\;=\;1)]\end{equation}
> &nbsp;&nbsp;* Then h<sub>j</sub> is (strictly) **more_general_than** h<sub>k</sub> (written h<sub>j</sub> ><sub>g</sub> h<sub>k</sub>) if and only if:
> \begin{equation}(h_{j}\;\geq_{g}\;h_{k})\wedge(h_{j}\;\ngeq_{g}\;h_{k})\end{equation}
> &nbsp;&nbsp;* we can say it inversely like h<sub>k</sub> is **more_specific_than_or_equal_to** h<sub>j</sub> or h<sub>k</sub> is **more_specific_than** h<sub>j</sub><br>
<br>
> -- **&ge;<sub>g</sub> relation** is important for providing a useful structure over the hypothesis space _H_ for _any_ concept learning problem.

<br>
<hr>
<br>

### 4. FIND-S: Finding a Maximally Specific Hypothesis
>- To use the _more_general_than_ partial ordering to organize the search for a hypothesis consistent with the observed training example:<br>
> -- start with the **most specific possible** hypothesis in _H_,<br>
> -- then generalize this hypothesis each time it fails to cover an observed positive training example.<br>

> FIND-S Algorithm<br>
> 1. Initialize _h_ to the most specific hypothesis in _H_<br>
> 2. For each positive training istance _x_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;For each attribute constraint _a<sub>i</sub>_ in _h_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the constraint _a<sub>i</sub>_ is satisfied by _x_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then do nothing<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Else replace _a<sub>i</sub>_ in _h_ by the next more general constraint that is satisfied by _x_<br>
> 3. Output hypothesis _h_<br>

>- In the general case, as long as we assume that the hypothesis space _H_ contains a hypothesis that describes the true target concept _x_ and that the training data contains no errors, then the current hypothesis _h_ can never require a revision in response to a negative example.<br>
<br>
>- **FIND-S algorithm** illustrate that the **more_general_than** partial ordering can be used to organize the search for an _acceptable hypothesis_.<br>
<br>
>- The **key property** of the FIND-S algorithm is:<br>
> -- for hypothesis spaces described by conjunctions of attribute constraints, FIND-S is **guaranteed** to output the **most specific hypothesis** within _H_ that is consistent with the positive training examples.<br>
> -- Its final hypothesis will also be consistent with the negative examples provided the correct target concept is contained in _H_, and provided the training examples are correct.<br>

<br>
<hr>
<br>

### 5. Version Spaces and the CANDIDATE-ELIMINATION Algorithm
<br>
>- The **key idea** of CANDIDATE-ELIMINATION algorithm is to output a description of the set of _all hypotheses consistent with the training examples_.
>- "more_general_than" partial ordering plays a big part in the CANDIDATE-ELIMINATION algorithm.
>- Both FIND-S & CANDIDATE-ELIMINATION algorithms perform **poorly** when given noisy training data.

<br>

> #### 5.1 Representation
>Some basic definition before defining CANDIDATE-ELIMINATION algorithm:
>- **Consistent**: A hypothesis _h_ is consistent with a set of training examples D if and only if _h(x) = c(x)_ for each example _&lt;x, c(x)&gt;_ in _D_ (correctly classifies the training examples).
> \begin{equation}Consistent(h,\;D)\;\equiv\;(\forall \langle x,\;c(x)\rangle \in D)\;h(x)\;=\;c(x)\end{equation}
> Note: the key difference between **consistent** & **satisfies**.<br>
> _Training example X_ is said to satisfy hypothesis _h_ when _h(x) = 1_, **regardless of** whether _x_ is a posistive or negative example of the target concept.<br>
> _Training example X_ is consistent with _h_ depends on the target concept, and in particular, whether _h(x) = c(x)_.<br>
<br>
>- **Version Space**: is denoted as _VS<sub>H, D</sub>_, with respect to hypothesis space _H_ and training examples _D_, is the subset of hypotheses from _H_ consistent with the training examples in _D_.
> \begin{equation}VS_{H,\;D}\;\equiv\;{h\;\in\;H\;|\;Consistent(h,\;D)}\end{equation}
> The set of _all_ describable hypotheses that CANDIDATE-ELIMINATION algorithm finds (represents), are _consistent_ with thef observed training examples, with respect to the hypothesis space _H_ and the training examples _D_, because it contains all plausible versions of the target concept.

<br>

> #### 5.2 The LIST-THEN-ELIMINATE Algorithm
>- LIST-THEN-ELIMINATE algorithm using version space to simply list all of its members.
>- LIST-THEN-ELIMINATE algorithm:<br>
> -- first initializes the version space to contain all hypotheses in _H_,<br>
> -- then eliminates any hypothesis found inconsistent with any training example. 
> -- The version space of candidate hypotheses thus shrinks as more examples are observed, until ideally just one hypothesis remains that is consistent with all the observed examples. This, presumably, is the desired target concept. If insufficient data is available to narrow the version space to a single hypothesis, then the algorithm can output the entire set of hypotheses consistent with the observed data.<br>
>- LIST-THEN-ELIMINATE algorithm can be applied **whenever** the hypothesis space _H_ is **finite**.
>- Advantage of L-T-E is guaranteed to output all hypotheses consistent with the training data.
>- Disadvantage of L-T-E is that it requires exhaustively enumerating all hypotheses in _H_.

> The LIST-THEN-ELIMINATE Algorithm<br>
> 1. _VersionSpace &larr;_ a list containing every hypothesis in _H_<br>
> 2. For each training example, <x, c(x)><br>
> &nbsp;&nbsp;&nbsp;&nbsp;remove from _VersionSpace_ any hypothesis _h_ for which _h(x) &ne; c(x)_
> 3. Output the list of hypotheses in _VersionSpace_<br>
<br>

> #### 5.3 A More Compact Representation for Version Spaces

> #### 5.4 CANDIDATE-ELIMINATION Learning Algorithm

> #### 5.5 An Illustrative Example

<br>
<hr>
<br>

### 6. Remarks on Version Spaces and CANDIDATE-ELIMINATION
<br>
> #### 6.1 Will the CANDIDATE-ELIMINATION Algorithm Converge to the Correct Hypothesis?

> #### 6.2 What Training Example Should the Learner Request Next?

> #### 6.3 How Can Partially Learned Concepts Be Used?

<br>
<hr>
<br>

### 7. Inductive Bias
<br>
> #### 7.1 A Biased Hypothesis Space

> #### 7.2 An Unbiased Learner

> #### 7.3 The Futility of Bias-Free Learning

<br>
<hr>
<br>

### 8. Summary
> 3 approach to concept learning:
>- FIND-S Algorithm
>- CANDIDATE-ELIMINATION Algorithm
>- 
<br>
> ...
>- ...
>- ...

> ...

> ...

> ...













<br>

<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s [Machine Learning](https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077)
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s authorization.
<br>
