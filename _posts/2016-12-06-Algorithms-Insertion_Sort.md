---
layout: post
section-type: post
title: Insertion Sort
category: python
tags: [ 'python', 'algorithm', 'reading' ]
comments: true
---

#### Introduction

> WHEN to use:\\
Insertion sorting is an efficient algorithm for sorting a small number of elements.
<br>
It has time complexity of O(n&sup2;), and as the size of elements increase, it will be less efficient and it is better to use other sorting algorithm such as merge sorting.

<hr>

#### Algorithm Analysis:

<br>
![Analysis Diagram]({{site.baseurl}}/assets/img/posts_img/ITA_Page-18_img_1.png){:class="img-responsive"}
<br>
(Image is from the book)
<br>
<br>

##### Pseudocode:
for j = 2 to A.length\\
&nbsp;&nbsp;&nbsp;&nbsp;key = A[j]\\
&nbsp;&nbsp;&nbsp;&nbsp;//Insert A[j] into the sorted sequence A[1..j-1].\\
&nbsp;&nbsp;&nbsp;&nbsp;i = j - 1\\
&nbsp;&nbsp;&nbsp;&nbsp;while i > 0 and A[i] > key\\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A[i+1] = A[i]\\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i = i - 1\\
&nbsp;&nbsp;&nbsp;&nbsp;A[i+1] = key

<br>

<hr>

#### Python Implementation: O(n&sup2;)

<br>

~~~ 
#!/usr/bin/env python3
import unittest

"""Insertion Sort

Usage:
    Algorithm Implementation

"""
##############################################################################################
# Performance: ?%

class Solution(object):
    def insertionSort(self, input):
        """
        :type input: List[int]
        :rtype: List[int]
        """

        for n in range(1, len(input)):
            check = input[n]
            m = n - 1
            while m >= 0 and input[m] > check:
                input[m+1] = input[m]
                m = m - 1
            input[m+1] = check
        return input
##############################################################################################
# Test Case
class UnitTest(unittest.TestCase):
    def test_check(self):
        omega = Solution()

        # TC-1
        # Arrange
        arg_1 = [5,2,4,6,1,3]
        expected = [1,2,3,4,5,6]
        # Act
        actual = omega.maxArea(arg_1)
        # Assert
        self.assertEqual(actual, expected) # ---------------------------> TC-1
##############################################################################################
# Script Section - Call Test Cases
if __name__ == '__main__':
    unittest.main()
##############################################################################################
~~~

<br>

#### Summary

<hr>

#### Reference:
[Introduction To Algorithms, 3rd Edition]
