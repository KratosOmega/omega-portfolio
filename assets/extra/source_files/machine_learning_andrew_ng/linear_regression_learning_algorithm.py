#!/usr/bin/env python3

import csv
import numpy
from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour

""" Learning Algorithm for Linear Regression (Coursera - Machine Learning by Andrew Ng)

    This is an implementation of the Algorithm in Coursera - Machine Learning by Andrew Ng's Week 1.

    This implementation uses "numpy", which is a python library for scientific computing and it will
    be frequently used for the further more implementations for the later courses.

    "pylab" (Matplotlib) is used for visualizing the data set patterns & verifying the prediction.

    Data will be imported through "csv" file.

    This implementation is designed for multi-variables linear regression. Simply add more variables in "def main()",
    by adding rows to the theta with values.

    EX: 3 variables will be theta[0, 0] = val0, theta[1, 0] = val1, theta[2, 0] = val2.

    Thanks to Marcel Caraciolo's post [http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html],
    it helps me a lot by using numpy to implement this algorithm since I was using List of List as my initial data structure.
"""

###################################################################################################

# Performance: %

class LinearRegression(object):

    def main(self):
        """
        :Description: used for assemblying linear regression equation & output predications
        :_lambda: used for set "baby step", a good value need to be picked for it
        :precision: used for determine how precisive the hypothesis will be
        :lb: left boundary of the data plot
        :rb: right boundary of the data plot        
        :theta: coefficient matrix (vector) of the hypothesis 
        """
        _lambda = 0.0000001
        precision = 0.1
        lb = 1945
        rb = 1965
        theta = zeros(shape=(2, 1))
        theta[0, 0] = -77860
        theta[1, 0] = 40

        # run the Grandient Descent process
        theta = self.gradientDescent(_lambda, theta, precision)

        print('------------------------------------------------------------------------')
        print('h(x) = ', theta[0, 0], ' + ', theta[1, 0], ' * x')
        print('------------------------------------------------------------------------')

        # plot the training set & prediction
        self.plotData(theta, lb, rb)

        # testing, press Ctrl+C to quit
        while True:
            print('------------------------------------------------------------------------')
            _input = float(input('_>: '))
            print(theta[0, 0] + theta[1, 0] * _input)


    def getDataSet(self):
        """
        :Description: used for loading training dataset from csv file
        :rtype: n-D array (numpy.ndarray)
        """
        return loadtxt('dataSet.csv', delimiter = ',')


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


    def plotData(self, theta, lb, rb):
        # load dataset from csv file
        dataSet = self.getDataSet()

        # plot the dataset
        scatter(dataSet[:, 0], dataSet[:, 1], marker='o', c='b')

        # plot the prediction (hypothesis)
        x = numpy.arange(lb, rb)
        h = theta[0, 0] + theta[1, 0] * x
        S = zeros(shape=(x.size, 2))
        S[:, 0] = x
        S[:, 1] = h

        scatter(S[:, 0], S[:, 1], marker='x', c='r')

        title('Training Set vs. Prediction Distribution')
        xlabel('X')
        ylabel('Y')
        show()


    def compute_cost(self, X, y, theta):
        """
        :Description: used for computing the cost function value for linear regression (current theda)
        """
        m = y.size
        predictions = X.dot(theta).flatten()
        sqErrors = (predictions - y) ** 2
        J = (1.0 / (2 * m)) * sqErrors.sum()

        return J


###################################################################################################
if __name__ == '__main__':
    LR = LinearRegression()
    LR.main()

###################################################################################################

'''
It is obviously import to pick a good value for lambda (the size of baby step) for our algorithm,
however, I think it could be even more import to pick the good thedas.

I try different combinations of thedas, and find out if I can plot the scatter first and use it to
guess the possible value for thedas, it will dramatically improve the calculation time and precision.

Since we may have global minimum vs local minimum issue, a good starting point will increase the chance 
for us to find the global minimum, which leads to a more precisive prediction.

Also, it will cut off all the unnecessary calculation time for those "rediculous" theta guesses.

Thus, IMHO, my suggestion about working on this algorithm is to find 2 data pairs (2 points) in the training set,
which a line that pass through them is visually good enough to become our prediction linear regression. Then use it 
to calculation the theta candidates.
'''
