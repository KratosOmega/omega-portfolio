---
layout: post
section-type: post
title: Add Two Numbers
category: Leetcode
tags: [ 'python', 'algorithm', 'leetcode' ]
comments: true
---

#### Problem Description

> You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.\\
\\
Example:\\
\\
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)\\
Output: 7 -> 0 -> 8

<br>

#### Problem Analysis:

> 

<br>

#### Solution: O(n)

<br>

~~~ 
#!/usr/bin/env python3

"""Add Two Numbesr

Usage:

    You are given two linked lists representing two non-negative numbers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None: return l2
        if l2 is None: return l1

        sum =  ListNode(0)
        head = sum
        carryOver = 0

        while l1 is not None or l2 is not None or carryOver == 1:
            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val

            head.next = ListNode((v1 + v2 + carryOver)%10)
            carryOver = (v1 + v2 + carryOver) / 10

            head = head.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return sum.next
~~~

<br>

#### This is another online solution which is a good reference (Better performance): O(n) ?

<br>

~~~
#!/usr/bin/env python3

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0); p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next; l2 = l2.next; p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next; p = p.next
        if flag == 1: p.next = ListNode(1)
        return dummy.next
~~~

<br>

#### Summary

> 
