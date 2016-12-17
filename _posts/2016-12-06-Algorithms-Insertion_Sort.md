---
layout: post
section-type: post
title: Insertion Sort
category: Algorithms
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
![Insertion Sort StepByStep]({{site.baseurl}}/assets/img/posts_img/2016-12-06-Algorithms-Insertion_Sort/ITA_Page-18_img_1.png){:class="img-responsive"}
(Image is from the book)
<br>
<br>
![Insertion Sort Gif]({{site.baseurl}}/assets/img/posts_img/2016-12-06-Algorithms-Insertion_Sort/Insertion-sort-example-300px.gif){:class="img-responsive"}
(Gif from wiki)
<br>
<br>

##### Pseudocode:
~~~
for j = 2 to A.length
    key = A[j]
    //Insert A[j] into the sorted sequence A[1..j-1].
    i = j - 1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
~~~

<br>
<br>
> The concept of this algorithm is to imagine that you are actually sorting a bunch of cards.\\
<br>
The unsorted cards (unsorted lsit) is on the TABLE and you will draw a card each time and sort it base on the cards that are in your HAND.
<br>
<br>
The first card that we will start sorting will the second card you DRAW. (You don't need to sort when you have only 1 card in hand).\\
Thus, the loop will start at 2 (2nd card) to n (amounts of cards). However, as I know, the data structure of list in most (or ALL?) programming language implements index from "0" to "n-1". So, when we implement the algorithms, be aware of the bondaries of the loop. In python, we don't need to add "-1" to the right boundary, since the "range()" function will automatically exclude the right boundary.\\
<br>
Now, this is how the outter loop will be. The outter loop is going over each single card on the TABLE, except the first card. Next is the inner loop that will go over each single card in your HAND, except the card that you just draw (the last card).\\
<br>
It is the best to use while loop for the inner loop, due to the reason that we can not foresee when we need to stop until certain conditions are met. The conditions will be two. First, as long as we are not done with the cards on hand, we will keep checking. Then, as long as the cards in hand are bigger than the last card that we draw, we will keep checking (the next card in hand).\\
<br>
These 2 conditions need to be both true and if anyone of them fail, we quit the inner loop and that means we find the right position to place the last draw card.\\
<br>
A[i+1] = A[i], this line is doing the swiching position job\\
i = i - 1, this line is updating the current postion (next card) that we will check.\\
<br>
However, as soon as we exit the inner loop (means we find the right position), we need to insert the card to the right position.\\
Then, A[i+1] = key, this line will insert the card. The reason we do i + 1 is because the previous line (i = i - 1).
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
