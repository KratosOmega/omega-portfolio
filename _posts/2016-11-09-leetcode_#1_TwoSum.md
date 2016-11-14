---
layout: post
section-type: post
title: Two Sum
category: python
tags: [ 'python', 'algorithm', 'leetcode' ]
comments: true
---

#### Problem Description

> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
<br><br>
Example:
<br>
Given nums = [2, 7, 11, 15], target = 9,\\
Because nums[0] + nums[1] = 2 + 7 = 9,\\
return [0, 1].

<br>

#### Problem Analysis:

> Well, a O(n&sup2;) solution will be the first one comes to my mind. It will be a brutal force method which uses parallel loops to check every single combination.\\
\\
However, try to always think about whether dictionary can be used to make problem much easier.\\
\\
Thanks to the (key, value) data structure and build-in method, it will be easier to quickly check the combination and quit loop as soon as we find our target.


<br>

#### Solution: O(n&sup2;)

<br>

~~~ 
#!/usr/bin/env python3

"""Two Sum

Usage:
    Practices

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for x in range(length-1):
            for y in range(x+1, length):
                sum = nums[x]+nums[y]
                if sum  == target:
                    print(sum)
                    return [x, y]
~~~

<br>

#### This is another online solution which is a good reference (Better performance): O(n)

<br>

~~~
#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}    #generate a empty dict for searching
        for i, num in enumerate(nums):    #using enumerate() python build-in method to make iterator countable
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i    #*: instead of normal action, make the value as the key,
                               #...and the counter as the value,
                               #...so that the value can be quickly search by using "if...in..."
        return []
~~~

<br>

#### Summary

> The O(n) solution uses "enumerate()", which is a python build-in method to make iterator countable, however, this is not a must-do if you are using other language.\\
Simply using for loop to count from 0 will also do the same thing.\\
\\
There are 2 key points of this method. First one is having a "lookup" dictionary to keep track the non-match data. As long as current data is not matched in current "lookup" dictionary, we put the current data into the "lookup" dictionary as "KEY", but the counter "i" as "VALUE". This is the second key point. This is because we need to use the advantage of dictionary which the key is unique and can be quickly searched.\\
\\
As soon as we find matched key in dictionary, we return the combination to terminate the search.
