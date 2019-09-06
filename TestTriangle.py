# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #***Right Triangle Tests***

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testIsoscelesRightTriangle(self):
        self.assertEqual(classifyTriangle(1,1,math.sqrt(2)),'InvalidInput','Can only have integers')

    #***Equilateral Triangle Tests***

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #***Isosceles Triangle Tests***

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5,5,4),'Isosceles', '5,5,4 is Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4,5,5),'Isosceles', '4,5,5 is Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(5,4,5),'Isosceles', '5,4,5 is Isosceles')

    #***Scalene Triangle Tests***

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7,12,15),'Scalene', '7,12,15 is Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(12,7,15),'Scalene', '12,7,15 is Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(15,7,12),'Scalene', '15,7,12 is Scalene')

    #***Testing Bad Inputs***

    def testInvalidInputHigh(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 is not within range')

    def testInvalidInputHighB(self):
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201,1,1 is not within range')

    def testInvalidInputHighC(self):
        self.assertEqual(classifyTriangle(1,201,1),'InvalidInput','1,201,1 is not within range')

    def testInvalidInputHighD(self):
        self.assertEqual(classifyTriangle(1,1,201),'InvalidInput','1,1,201 is not within range')

    def testInvalidInputLow(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is not within range')

    def testInvalidInputLowB(self):
        self.assertEqual(classifyTriangle(0,3,3),'InvalidInput','0,3,3 is not within range')

    def testInvalidInputLowC(self):
        self.assertEqual(classifyTriangle(3,0,3),'InvalidInput','3,0,3 is not within range')

    def testInvalidInputLowD(self):
        self.assertEqual(classifyTriangle(3,3,0),'InvalidInput','3,3,0 is not within range')

    def testInvalidInputType(self):
        self.assertEqual(classifyTriangle(2.1,2,3),'InvalidInput', '2.1 is not an integer')

    def testInvalidInputTypeString(self):
        self.assertEqual(classifyTriangle('a',3,3), 'InvalidInput', 'a is not an integer')

    #***Testing Impossible Triangles***

    def testImpossibleTriangle(self):
        self.assertEqual(classifyTriangle(1,10,12), 'NotATriangle','1,10,12 are not compatible lengths for sides of a triangle')

    def testImpossibleTriangleB(self):
        self.assertEqual(classifyTriangle(12,1,10), 'NotATriangle','12,1,10 are not compatible lengths for sides of a triangle')

    def testImpossibleTriangleC(self):
        self.assertEqual(classifyTriangle(10,1,12), 'NotATriangle','10,1,12 are not compatible lengths for sides of a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
