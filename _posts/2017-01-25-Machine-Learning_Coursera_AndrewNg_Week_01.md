---
layout: post
section-type: post
title: Linear Regression Learning Algorithm (Supervised)
category: Artificial_Intelligence
tags: [ 'python', 'algorithm', 'reading', 'machine_learning' ]
comments: true
---

#### Introduction

> 
This is a basic supervised learning algorithm for linear regression which involves only one variable.
<br>
<br>
This algorithm is from Andrew Ng's Coursera course - Machine Learning (Week One) and this post will include some personal understanding and implementation of the algorithm from week one content in python.
<br>

<hr>

<br>

#### Algorithm Analysis:

<br>
![Formulas]({{site.baseurl}}/assets/img/posts_img/2017-01-25-Machine-Learning_Coursera_AndrewNg_Week_01/machine_learning_process.png){:class="img-responsive"}
(Image from the Coursera)
<br>
<br>

>
By feeding the learning algorithm with the training data set, we can get a "hypothesis" which is a function can be used for predication.

<br>

![Formulas]({{site.baseurl}}/assets/img/posts_img/2017-01-25-Machine-Learning_Coursera_AndrewNg_Week_01/Formulas.png){:class="img-responsive"}
(Image from the Coursera)

<br>

>
- The hypothesis is a linear regression function (line) which fits the training data set as much as possible. So that we can use it to predict the output when input is given.
- Our goal is to find the combination of theta0 & theta1 that makes cost function as small as possible.

<br>

![Insertion Sort Gif]({{site.baseurl}}/assets/img/posts_img/2017-01-25-Machine-Learning_Coursera_AndrewNg_Week_01/Gradient_Descent_Derivative.png){:class="img-responsive"}
(Image from the Coursera)

<br>
<br>

>
- In order to do this, we need to use some calculus knowledge (differential equation) to get the partial derivatives in respect of theta0 & theta1.
- The derivatives is used by Gradient Descent to find the local minimum (hopefully the global minimum)
- More details, please check [Machine Learning - Week One](https://www.coursera.org/learn/machine-learning/home/week/1)

<br>

<hr>

<br>
#### Python Implementation:

<br>

~~~ 
#!/usr/bin/env python3
def getDataSet(self):
        """
        :Description: used for loading training dataset from csv file
        :rtype: n-D array (numpy.ndarray)
        """
        return loadtxt('dataSet.csv', delimiter = ',')
~~~

<br>

<br>

~~~ 
#!/usr/bin/env python3
def gradientDescent(self, _lambda, theta, precision = 0.1):
        """
        :Description: used for finding the best linear regression (best combination of theta0 & theta1).
        Ideally, this method should be updated for being able to handle several sets of theta candidates
        :rtype: n x 1 matrix (vector)
        """
        # load data set from csv file
        dataSet = self.getDataSet()

        # set the variables size
        k = theta.size

        # kth column is y
        y = dataSet[:, k-1]

        m = y.size

        # set a "n x 2" matrix for interception data
        X = ones(shape=(m, k))

        for i in range(1, k):
            X[:, i] = dataSet[:, i-1]

        while True:
            predictions = X.dot(theta).flatten()

            precisions = []

            for i in range(k):
                theta[i, 0] = theta[i, 0] - _lambda * (1.0 / m) * (((predictions - y) * X[:, i]).sum())
                precisions.append(abs((1.0 / m) * (((predictions - y) * X[:, i]).sum())))

            # -------------------------------------------------------------------------------------
            # for observation purpose
            display = ''
            for p in precisions:
                display = display + '       ' + str(p)
            print(display)
            # -------------------------------------------------------------------------------------

            # check if both deltas are precisive enough, 
            stop = True
            for p in precisions:
                if p > precision:
                    stop = False
                    break

            if stop:
                break

        return theta
~~~

<br>

<hr>

<br>

#### Summary
>
- Lambda: As Andrew mentioned in his course, the value of lambda is very important and somehow it can be a little be tricky. In different training sets, I have to manually adjust lambda in order to get the good thedas. It can be easily high which causes inifinty loop or low which causes timeout error.
- The value choices for initializing thedas is not that important, but if you can pick a good starting point for thedas, it will definitely save you a lot of time.
- In __[Resources]__, there are 2 data sets for testing purpose, readers can download them for personal use only. After files are download, save the python codes and the data sets under the same directory. Make sure the csv file name reference is same as the file name.
- It is obviously important to pick a good value for lambda (the size of baby step) for our algorithm. However, I think it could be even more important to pick the good thedas. I try different combinations of thedas, and find out if I can plot the scatter first and use it to
guess the "good" values for thedas, it will dramatically improve the calculation time and precision. Since we may have the issue of global minimum vs. local minimum, a good starting point (good thetas) will increase the chance for us to find the global minimum, which will lead us to a more precisive hypothesis solution. Also, it will cut off all the unnecessary calculation time for those "rediculous" theta guesses.
- Thus, IMHO, my suggestion about working on this algorithm is to find 2 data pairs (2 points) in the training set, which a line that pass through them is visually good enough to become our prediction linear regression. Then use it to calculation the theta candidates.

<br>

<hr>

<br>

#### Reference:
[Machine Learning - Week One](https://www.coursera.org/learn/machine-learning/home/week/1)
<br>
<br>
>
Thanks to Marcel Caraciolo's [post](http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html), it helps me a lot by using numpy to implement this algorithm since I was using List of List as my initial data structure.

<br>
<hr>

#### Resources:
[Implementation Source File](https://raw.githubusercontent.com/KratosOmega/omega-portfolio/gh-pages/assets/extra/source_files/machine_learning_andrew_ng/linear_regression_learning_algorithm.py)
<br>
[Training Data Set Sample 0](https://raw.githubusercontent.com/KratosOmega/omega-portfolio/gh-pages/assets/extra/source_files/machine_learning_andrew_ng/dataSet_0.csv)
<br>
[Training Data Set Sample 1](https://raw.githubusercontent.com/KratosOmega/omega-portfolio/gh-pages/assets/extra/source_files/machine_learning_andrew_ng/dataSet_1.csv)
<br>
[Training Data Set Sample 2](https://raw.githubusercontent.com/KratosOmega/omega-portfolio/gh-pages/assets/extra/source_files/machine_learning_andrew_ng/dataSet_2.csv)
<br>
[Training Data Set Sample 3](https://raw.githubusercontent.com/KratosOmega/omega-portfolio/gh-pages/assets/extra/source_files/machine_learning_andrew_ng/dataSet_3.csv)
