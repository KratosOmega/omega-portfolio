---
layout: post
section-type: post
title: Linear Regression Learning Algorithm (Supervied)
category: Artificial Intelligence
tags: [ 'python', 'algorithm', 'reading', 'machine learning' ]
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
- Hypothesis is a linear regression function (line) which fits the training data set as much as possible. So that we can use it to predict the output when input is given.
- Our goal is to find the theta0 & theta1 that make cost function as small as possible.

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
<br>
#### Python Implementation:

<br>

~~~ 
#!/usr/bin/env python3
import csv

"""Learning Algorithm for Linear Regression (Coursera - Machine Learning by Andrew Ng)

    This is an implementation of the Algorithm in Coursera - Machine Learning by Andrew Ng's Week 1
"""
##############################################################################################
class LinearRegression(object):
    """
    :Description: initialize class variables
    :type _trainingSet: list(list(string))
    :type _theta0: float
    :type _theta1: float    
    :type _lambda: float
    """
    _trainingSet = []
    _theta0 = 7.0
    _theta1 = 7.0
    # a good value need to be picked for _lambda
    # too small will take forever to find the deltas
    # too big will error out
    _lambda = 0.001


    def prepare(self):
        """
        :Description: used for preparing training set, read a csv file
        and prepare the _trainingSet as a list of list of string 
        (need inline covertion of string to float)
        """
        # Set up 
        with open('dataSet.csv') as _file:
            csvReader = csv.reader(_file)
            dataSet = list(csvReader)
        return dataSet


    def gradientDescent(self, _trainingSet, _theta0, _theta1, _lambda):
        """
        :Description: used for finding the best linear regression (best combination of theta0 & theta1)
        :type _trainingSet: list(tuples(int))
        :rtype: tuple
        """
        m = len(_trainingSet)
        print(m)

        while True:
            sigma0 = 0
            sigma1 = 0
            # calculate Sigma part
            for xy in _trainingSet:
                sigma0 = sigma0 + ((_theta0 + _theta1 * float(xy[0])) - float(xy[1]))
            for xy in _trainingSet:
                sigma1 = sigma1 + ((_theta0 + _theta1 * float(xy[0])) - float(xy[1])) * float(xy[0])
            # calculate delta part
            delta0 = (1 / m) * sigma0
            delta1 = (1 / m) * sigma1
            # calculate theta part
            _theta0 = _theta0 - _lambda * delta0
            _theta1 = _theta1 - _lambda * delta1

            # for visualization purpose, not necessary code
            print(delta0, ' - ', delta1)

            # check if both deltas are small enough, 
            # how small the deltas should be depends on accuracy requirement
            if abs(delta0) < 0.1 and abs(delta1) < 0.1:
                break

        return (_theta0, _theta1)


    def predication(self):
        """
        :Description: used for assemblying linear regression equation & output predications
        """
        # prepare the _trainingSet
        self._trainingSet = self.prepare()
        # prepare the hypothesis formula
        _thetas = self.gradientDescent(self._trainingSet, self._theta0, self._theta1, self._lambda)
        # press Ctrl+C to quit
        while True:
            print('##########################')
            _input = float(input('_>: '))
            print(_thetas[0] + _thetas[1] * _input)


##############################################################################################
# Script Section --- Testing Zone
if __name__ == '__main__':
#    unittest.main()
    LR = LinearRegression()
    LR.predication()
##############################################################################################
~~~

<br>

#### Summary
>
- Lambda: As Andrew mentioned in his course, the value choice of lambda is very important and somehow it can be a little be tricky. In different training set, I have to manually adjust lambda in order to get the good thedas. It can be easily high to cause inifinty loop or low to cause timeout error.
- The value choices for initializing thedas is not that important, but if you can pick a good starting point, it will definitely help.
- In __[Resources]__, there are 2 data set for testing purpose, reader can downloads them for personal use only. After files are download, save the python codes and the data sets under the same directory. Make sure the csv file name reference as same as the file name.

<hr>

#### Reference:
[Machine Learning - Week One](https://www.coursera.org/learn/machine-learning/home/week/1)

<br>
<hr>

#### Resources:
[Training Data Set Sample One](https://github.com/KratosOmega/KratosOmega.github.io/raw/master/assets/extra/resources/dataSet_1.csv)
<br>
[Training Data Set Sample Two](https://github.com/KratosOmega/KratosOmega.github.io/raw/master/assets/extra/resources/dataSet_2.csv)
