---
layout: post
section-type: post
title: Two Sum
category: python
tags: [ 'python', 'algorithm', 'leetcode' ]
comments: true
---

#### Problem Description

> ###### Given an array of integers, return indices of the two numbers such that they add up to a specific target.
###### You may assume that each input would have exactly one solution.
<br> 
###### Example:
> Given nums = [2, 7, 11, 15], target = 9,\\
> Because nums[0] + nums[1] = 2 + 7 = 9,\\
return [0, 1].

<br>

#### Problem Analysis:

> ###### Here

<br>

#### Solution

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

#### This is another online solution which is a good reference (Better performance)

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

#### Summary
> ###### Summary goes here
