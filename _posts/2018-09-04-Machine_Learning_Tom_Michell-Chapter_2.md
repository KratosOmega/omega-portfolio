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

> &nbsp;&nbsp;&nbsp;&nbsp;FIND-S Algorithm<br>
> &nbsp;&nbsp;&nbsp;&nbsp;1. Initialize _h_ to the most specific hypothesis in _H_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;2. For each positive training istance _x_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each attribute constraint _a<sub>i</sub>_ in _h_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the constraint _a<sub>i</sub>_ is satisfied by _x_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then do nothing<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Else replace _a<sub>i</sub>_ in _h_ by the next more general constraint that is satisfied by _x_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;3. Output hypothesis _h_<br>

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
> \begin{equation}VS_{H,\;D}\;\equiv\;\\{h\;\in\;H\;|\;Consistent(h,\;D)\\}\end{equation}
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

<br>

> #### 5.3 A More Compact Representation for Version Spaces
<br>
>- The CANDIDATE-ELIMINATION algorithm represents the **version space** by storing ONLY its **most general members** (labeled as _G_), and its **most specific** (labeled as _S_).
>- Given only these two sets _S_ & _G_, it's possible to enumerate all members of the version space as needed by generating the hypotheses that lie between these two sets in the general-to-specific partial ordering over hypotheses.
>- The general and specific boundary sets that delimit the version space within the partially ordered hypothesis space.

> &nbsp;&nbsp;&nbsp;&nbsp;The LIST-THEN-ELIMINATE Algorithm<br>
> &nbsp;&nbsp;&nbsp;&nbsp;1. _VersionSpace &larr;_ a list containing every hypothesis in _H_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;2. For each training example, <x, c(x)><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove from _VersionSpace_ any hypothesis _h_ for which _h(x) &ne; c(x)_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;3. Output the list of hypotheses in _VersionSpace_<br>

>- The **general boundary** _G_, with respect to hypothesis space _H_ and training data _D_, is the set of maximally general members of _H_ consistent with _D_.
> \begin{equation}G\;\equiv\;\\{g\;\in\;H\;|\;Consistent(g,\;D)\wedge(\urcorner\exists g'\;\in\;H)[(g'\;>_{g}\;g)\wedge Consistent(g',\;D)]\\}\end{equation}
>- The **specific boundary** _S_, with respect to hypothesis space _H_ and training data _D_, is the set of minimally general (i.e., maximally specific) members of _H_ consistent with _D_.
> \begin{equation}S\;\equiv\;\\{s\;\in\;H\;|\;Consistent(s,\;D)\wedge(\urcorner\exists s'\;\in\;H)[(s'\;>_{g}\;s)\wedge Consistent(s',\;D)]\\}\end{equation}
>- **Version space representation theorem**. Let _X_ be an arbitrary set of instances and let _H_ be a set of boolean-valued hypotheses defined over _X_. Let _c : X &rarr; {O,1)_ be an arbitrary target concept defined over _X_, and let _D_ be an arbitrary set of training examples _{<x,c(x)>}_. For all _X_, _H_, _c_, and _C_ such that _S_ and _G_ are well defined,
> \begin{equation}VS_{H,\;D}\;=\;\\{h\;\in\;H\;|\;(\exists s\;\in\;S)(\exists g\;\in\;G)(g\;\geq_{g}\;h\;\geq_{g}\;s)\\}\end{equation}

<br>

> #### 5.4 CANDIDATE-ELIMINATION Learning Algorithm
<br>
>- The CANDIDATE-ELIMINATION algorithm computes the version space containing all hypotheses from _h_ that are consistent with an observed sequence of training examples.<br>
<br>
>- The algorithm begins by initializing the version space to the set of all hypotheses in _H_:<br>
> -- initializing the _G_ boundary set to contain **the most general** hypthesis in _H_ as _G<sub>0</sub>_.<br>
> -- initializing the _S_ boundary set to contain **the most specific (least general)** hypthesis in _H_ as _S<sub>0</sub>_.<br>
<br>
> These 2 boundary sets delimit the entire hypothesis spaces, because every other hypothesis in _H_ is bothe more general than _S<sub>0</sub>_ and more specific than _G<sub>0</sub>_.<br>
<br>
>- As each training example is considered, the _S_ and _G_ boundary sets are generalized ans specialized to eliminate from the version space any hypotheses found inconsistent with the new training example. After all examples have been proessed, the computed version space contains all the hypotheses consistent with the training examples and only these hyptheses.

> &nbsp;&nbsp;&nbsp;&nbsp;The CANDIDATE-ELIMINATION Algorithm<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Initialize _G_ to the set of maximally general hypotheses in _H_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Initialize _S_ to the set of maximally specific hypotheses in _H_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;For each training example _d_, do:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;* If _d_ is a positive example:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove from _G_ any hypothesis inconsistent with _d_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* For each hypothesis _s_ in _S_ that is not consistent with _d_:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove _s_ from _S_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Add to _S_ all minimal generalizations _h_ of _s_ such that:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* _h_ is consistent with _d_, and some member of _G_ is more general than _h_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove from _S_ any hypothesis that is more genreal than another hypothesis in _S_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;* If _d_ is a negative example:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove from _S_ any hypothesis inconsistent with _d_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* For each hypothesis _g_ in _G_ that is not consistent with _d_:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove _g_ from _G_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Add to _G_ all minimal generalizations _h_ of _g_ such that:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* _h_ is consistent with _d_, and some member of _S_ is more specific than _h_<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Remove from _G_ any hypothesis that is less genreal than another hypothesis in _G_<br>

> #### 5.5 An Illustrative Example
<br>
>- The _S_ boundary of the version space forms a summary of the previously encountered positive examples that can be used to determine whether any given hypothesis is consistent with these examples. Any hypothesis more general than _S_ will, by definition, cover any example that _S_ covers and thus will cover any past positive example.

<br>
<hr>
<br>

### 6. Remarks on Version Spaces and CANDIDATE-ELIMINATION
<br>
> #### 6.1 Will the CANDIDATE-ELIMINATION Algorithm Converge to the Correct Hypothesis?
<br>
>- The version space learned by the CANDIDATE-ELIMINATION algorithm will converge toward the hypothesis that correctly describes the target concept, provided:<br>
> -1) there are NO errors in the training examples.<br>
> -2) theere is some hypothesis in _H_ that correctly describes the target concept.<br>
<br>
>- The target concept is exactly learned when the _S_ and _G_ boundary sets coverge to a _single, identical,_ hypothesis.<br>

>- Given sufficient (incorrect) training data, the learner will eventually detect an inconsistency by noticing that the _S_ and _G_ boundary sets eventually converge to an **empty** version space. The empty VS indicates that there is **no** hypothesis in _H_ consistent with all observed training examples. A similar symptom will appear when the training examples are correct, but the target concept cannot be described in the hypthesis representation.

<br>
> #### 6.2 What Training Example Should the Learner Request Next?
>- **Query** is used to refer to the instances constructed by the learner, which are then classified by an external oracle.
> e.g.: learner may conduct experiments in nature, like build new bridges and then allow nature to classify them as stable or unstable.
>- Learner uses _query_ to request the next training examples, choose an instance that would be classified positive by some ofthese hypotheses, but negative by others.
>- The optimal query strategy for a concept learner is to generate instances that satisfy exactly **half** the hypotheses in the current version space. ==> the size of the version space is reduced by half with each new example, and the correct target concept can therefore be found with only &#9484;log<sub>2</sub>\|VS\|&#9488; experiments.

<br>

> #### 6.3 How Can Partially Learned Concepts Be Used?
<br>
>- Suppose that no additional training examples are available beyond what we have, but that the learner is now required to classify new instances that it has not yet observed. Even though the version space at this point multiple hypotheses, indicating that the target concept has not yet been fully learned, it is possible to classify certain examples with the same degree of confidence as if the target concept had been uniquely identified.

<br>
<hr>
<br>

### 7. Inductive Bias
<br>
>As discussed above, the CANDIDATE-ELIMINATION Algorithm will converge toward the true target concept provided it is given accurate training examples and provided its initial hypothesis space contains the target concept. 
>- What if the target concept is not contained in the hypothesis space? 
>- Can we avoid this difficulty by using a hypothesis space that includes every possible hypothesis? 
>- How does the size of this hypothesis space influence the ability of the algorithm to generalize to unobserved instances? 
>- How does the size of the hypothesis space influence the number of training examples that must be observed? 

> These are fundamental questions for inductive inference in general. As we shall see, though, the conclusions we draw from this analysis will apply to any concept learning system that outputs any hypothesis consistent with the training data.

> #### 7.1 A Biased Hypothesis Space
<br>
>- Suppose we wish to assure that the hypothesis space contains the unknown target concept. The obvious solution is to enrich the hypothesis space to include _every possible_ hypothesis.
> e.g.: Since we restricted the hypothesis space to include only **conjunctions** of attribute values, the hypothesis space is unable to represent even simple **disjunctive** target concepts.


> #### 7.2 An Unbiased Learner
<br>
>- The obvious solution to the problem of assuring that the target concept is in the hypothesis space _H_ is to provide a hypothesis space capable of representing **every teachable concept**; that is, it is capable of representing **every possible subset** of the instances _X_. In general, the set of all subsets of a set _X_ is called the **power set** of _X_. 
>- How many possible concepts can be defined over the set of instances? (how large is the power set of _X_?) In general, the number of distinct subsets that can be defined over a set _X_ containing |_X_| elementt is 2<sup>|_X_|</sup>.

> #### 7.3 The Futility of Bias-Free Learning
<br>
>- **Fundamental property** of inductive inderence: a learner that makes no a priori assumptions regarding the identity of the target concept has no rational basis for classifying any unseen instances.<br>
<br>
> The only reason that the CANDIDATE-ELIMINATION algorithm was able to generalize beyond the observed training examples is that it was biased by the implicit assumption that the target concept could be represented by a conjunction of attribute values.<br>
<br>
> In cases where this assumption is correct (and the training examples are error-free), its classification of new instances wil lalso be correct.<br>
<br>
> If this assumption is incorrect, however, it is certain that the CANDIDATE-ELIMINATION algorithm wil lmisclassify at least some instances from _X_.<br>

>- Because inductive learning requires some form of **prior assumptions** (a.k.a. inductive bias), it's useful to characterize different learning approaches by the inductive bias they employ.
>- The key idea we wish to capture here is the policy by which the learner generalizes beyond the observed training data, to infer the classification of new instances. Therefore, consider the general setting in which an arbitrary learning algorithm _L_ is provided an arbitrary set of training data _D<sub>c</sub>_ = _{<x, c(x)}_ of some arbitrary target concept _x_. After training, _L_ is asked to classify a new instance _x<sub>i</sub>_. Let _L(x<sub>i</sub>, D<sub>c</sub>)_ denote the classificiation (e.g., positive or negative) that _L_ assigns to x<sub>i</sub> after learning from the training data _D<sub>c</sub>_. We can describe this inductive inference step performed by _L_ as follow:
> \begin{equation}(D_{c} \wedge x_{i})\succ L(x_{i}, D_{c})\end{equation}
> where the notation _y &#8881; z_ indicates that _z_ is inductively inferred from _y_.
<br><br>
>- Because _L_ is an inductive learning algorithm, the result _L(x<sub>i</sub>, D<sub>c</sub>)_ that it infers  will not in general be provably correct; that is, the classification _L(x<sub>i</sub>, D<sub>c</sub>)_ need not follow deductively from the training data _D<sub>c</sub>_ and the description of the new instance _x<sub>i</sub>_. However, it is interesting to ask what additional assumptions could be added to _D<sub>c</sub> &#8896; x<sub>i</sub>_ so that _L(x<sub>i</sub>, D<sub>c</sub>)_ would follow deductively. We define the inductive bias of _L_ as this set of additional assumptions. More precisely, we define the inductive bias of _L_ to be the set of assumptions _B_ such that for all new instances _x<sub>i</sub>_
> \begin{equation}(B\;\wedge\;D_{c}\;\wedge\;x_{i})\;\vdash\;L(x_{i},\;D_{c})\end{equation}
> where the notation _y &#8866; z_ indicates that _z_ follows deductively from _y_ (i.e., that z is provable from y). Thus, we define the inductive bias of a learner as the set of additional assumptions _B_ sufficient to justify its inductive inderences as deductive inferences.

> To summarize:
<br>
> Definition: Consider a concept learning algorithm _L_ for the set of instances _X_. Let _c_ be an arbitrary concept defined over _X_, and let _D<sub>c</sub> = {<x, c(x)}_ be an arbitrary set of training examples of _c_. Let _L(x<sub>i</sub>, D<sub>c</sub>)_ denote the classification assigned to the instance _x<sub>i</sub>_ by _L_ after training on the data _D<sub>c</sub>_. The **inductive bias** of _L_ is any minimal set of asserttions _B_ such that for any target concept _x_ and corresponding training examples _D<sub>c</sub>_
> \begin{equation}(\forall x_{i}\;\in\;X)[(B\;\wedge\;D_{c}\;\wedge\;x_{i})\;\vdash\;L(x_{i},\;D_{c})]\end{equation}

>- What is the inductive bias of the CANDIDATE-ELIMINATION algorithm?
<br>
> To answer this, let us specify _L(x<sub>i</sub>, D<sub>c</sub>)_ exactly for this algorithm: given a set of data _D<sub>c</sub>_, the CANDIDATE-ELIMINATION algorithm will first compute the version space _VS<sub>H,D<sub>c</sub></sub>_, then classify the new instance _x<sub>i</sub>_ by a vote among hypotheses in this version space. Here let us assume that it will output a classification for _x<sub>i</sub>_ only if this vote among version space hypotheses is unanimously positive or negative and that it will not output a classificaiton otherwise. Given this definition of _L(x<sub>i</sub>, D<sub>c</sub>)_ for the CANDIDATE-ELIMINATION algorithm, what is its inductive bias? It is simply the assumptoin _c &isin; H_. Given this assumption, each inductive inference performed by the CANDIDATE-ELIMINATION algorithm can be justified deductively.

>- To see why the classification _L(x<sub>i</sub>, D<sub>c</sub>)_ follows deductively from _B = {c &isin; H}_, together with teh data _D<sub>c</sub>_ and description of the instance _x<sub>i</sub>_, consider the following argument.
<br>
> -- First, notice that if we assume _c &isin; H_ then it follows deductively that _c &isin; VS<sub>H,D<sub>c</sub></sub>_. This follows form _c &isin; H_, from the definition of the version space _VS<sub>H,D<sub>c</sub></sub>_ as the set of all hypotheses in _H_ that are consistent with _D<sub>c</sub>_, and from our definition of _D<sub>c</sub> = {<x, c(x)}_ as training data consistent with the target concept _c_.<br>
> -- Second, recall that we defined the classification _L(x<sub>i</sub>, D<sub>c</sub>)_ to be the unanimous vote of all hypotheses in the version space. Thus, if _L_ outputs the classification _L(x<sub>i</sub>, D<sub>c</sub>)_, it must be the case the every hypothesis in _VS<sub>H,D<sub>c</sub></sub>_ also produces this classification, including the hypothesis _c &isin; VS<sub>H,D<sub>c</sub></sub>_. Therefore _c(x<sub>i</sub>) = L(x<sub>i</sub>, D<sub>c</sub>)_.

>- To summarize, the CANDIDATE-ELIMINATION algorithm defined in this fashion can be characterized by the following bias:<br>
> **Inductive bias of CANDIDATE-ELIMINATION algorithm**: The target concept _c_ is contained in the given hypothesis space _H_.

<br>

![Modeling inductive system by equivalent deductive system]({{site.baseurl}}/assets/img/posts_img/2018-09-04-Machine_Learning_Tom_Michell-Chapter_2/Inductive_system-Deductive_system.png){:class="img-responsive"}
([Figure 1: Modeling inductive systems by equivalent deductive system]())

<br>

> In **Figure 1**, The input-output behavior of the CANDIDATE-ELIMINATION algorithm using a hypothesis space _H_ is identical to that of a deductive theorem prover utilizing the assertion "_H_ contains the target concept." This assertion is therefore called the _inductive bias_ of the CANDIDATE-ELIMINATION algorithm. Characterizing inductive systems by their inductive bias allows modeling them by their equivalent deductive systems. This provides a way to compare inductive systems according to their policies for generalizing beyond the observed training data.

>- Advantages of viewing inductive inference systems in terms of their inductive bias:<br>
> -- 1) It provides a nonprocedural means of characterizing their policy for generalizing beyond the observed data.<br>
> -- 2) It allows comparison of different learners according to the strength of the inductive bias they employ.

> Consider the following 3 learning algorithms, listed from weakest to strongest bias:
>- **ROTE-LEARNER algorithm**: L:earning corresponds simply to storing each observed training example in memory. Subsequent instances are classified by looking them up in memory. If the instance is found in memory, the stored classification is returned. Otherwise, the system refuses to classify the new instance.<br>
<br>
> The ROTE-LEARNER has **no inductive bias**. The classifications it provides for new instances follow deductively from the observed training examples, with no additional assumptions required.<br>
<br>
>- **CANDIDATE-ELIMINATION algorithm**: New instances are classified only in the case where all members of the current version space agree on the classification. Otherwise, the system refuses to classify the new instance.<br>
<br>
> The CANDIDATE-ELIMINATION algorithm has a **stronger inductive bias**: that the target concept can be represented in its hypothesis space. Because it has a stronger bias, it will classify some instances that the ROTE-LEARNER will not. Of course the correctness of such classifications will depend completely on the correctness of this inductive bias.<br>
<br>
>- **FIND-S algorithm**: This algorithm, described earlier, finds the most specific hypothesis consistent with the training examples. It then uses this hypothesis to classify all subsequent instances.<br>
<br>
> The FIND-S algorithm has an **even stronger inductive bias**. In addition to the assumption that the target concept can be descirbed in its hypothesis space, it has an additional inductive bias assumption: that all instances are negative instances unless the opposite is entailed by its other knowledge.<br>
<br>
>- It's useful to keep in mind the means of characterizing the inductive inference methods and the strength of their inductive bias. More strongly biased methos make more inductive leaps, classifying a greater proportion of unseen instances.<br>
> -- Some inductive biases correspond to categorical assumptions that completely rule out certain concepts, such as the bias "the hypothesis space _H_ includes the target concept."<br>
> --  Other inductive biases merely rank order the hypotheses by stating preferences such as "more specific hypotheses are preferred over more general hypotheses."<br>
> -- Some biases are implicit in the learner and are unchangeable by the learner.<br>

<br>
<hr>
<br>

### 8. Summary
<br>
>- Concept learning can be cast as a problem of searching through a large predefined space of potential hypotheses.
>- The general-to-specific partial ordering of hypotheses, which can be defined for any concept learning problem, provides a useful structure for organizing the search through the hypothesis space.
>- The FIND-S algorithm utilizes this general-to-specific ordering, performing a specific-to-general search through the hypothesis space along one branch of the partial ordering, to find the most specific hypothesis consistent with the training examples.
>- The CANDIDATE-ELIMINATION algorithm  utilizes this general-to-specific ordering to compute the version space (the set of all hypotheses consistent with the training data) by incrementally computing the sets of maximally specific (S) and maximally general (G) hypotheses.
>- Because the S and G sets delimit the entire set of hypotheses consistent with the data, they provide the learner with a description of its uncertainty regarding the exact identity of the target concept. This version space of alternative hypotheses can be examined to determine whether the learner has converged to the target concept, to determine when the training data are inconsistent, to generate informative queries to further refine the version space, and to determine which unseen instances can be unambiguously classified based on the partially learned concept.
>- Version spaces and the CANDIDATE-ELIMINATION algorithm provide a useful conceptual framework for studying concept learning. However, this learning algorithm is not robust to noisy data or to situations in which the unknown target concept is not expressible in the provided hypothesis space.
>- Inductive learning algorithms are able to classify unseen examples only because of their implicit inductive bias for selecting one consistent hypothesis over another. The bias associated with the CANDIDATE-ELIMINATION algorithm is that the target concept can be found in the provided hypothesis space (__c &isin; H_). The output hypotheses and classifications of subsequent instances follow _deductively_ from this assumption together with the observed training data.
>- If the hypothesis space is enriched to the point where there is a hypothesis corresponding to every possible subset of instances (the power set of the instances), this will remove any inductive bias from the CANDIDATE-ELIMINATION algorithm. Unfortunately, this also removes the ability to classify any instance beyond the observed training examples. An unbiased learner cannot make inductive leaps to classify unseen examples.











<br>

<br>

<hr>

#### Resources:
This post is derived from [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s [Machine Learning](https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077)
<br><br>
This post should ONLY be used for course reference and self-studying. It should NEVER be used for any business purpose without [Ph.D. Mitchell](http://www.cs.cmu.edu/~tom//)'s authorization.
<br>
