---
layout: post
section-type: post
title: Loop Invariant
category: Keypoint
tags: [ 'algorithm', 'reading' ]
comments: true
---

#### What Is It?
> In simple words, a loop invariant is some predicate (condition) that holds for every iteration of the loop.\\
<br>
Loop invariant is essential for helping us understand why an algorithm is correct.\\

#### Something about it that you want to remember:
> There are 3 key things about a loop invariant.\\
1) Initialization: It is true prior to the  first iteration of the loop.\\
2) Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration.\\
3) Termination: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.
