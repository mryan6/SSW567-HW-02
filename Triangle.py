# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(first_side, second_side, third_side):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    # 8 defects found by initial testing
    # Moving this check up fixes fatal error
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(first_side, int) and isinstance(second_side, int)
           and isinstance(third_side, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <=
    if first_side > 200 or second_side > 200 or third_side > 200:
        return 'InvalidInput'
    #*here is where our InvalidInput error most likely came from
    if first_side <= 0 or second_side <= 0 or third_side <= 0:
        return 'InvalidInput'



    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # statement contained a bug, causing incorrect classifications
    # statement was updated to reflect logic above
    if (((first_side + second_side) < third_side)
            or ((first_side + second_side) < third_side)
            or ((second_side + third_side) < first_side)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    #*For equilateral, we must check all three sides
    if first_side == second_side and second_side == third_side:
        return 'Equilateral'
    # (a*2) is not equal to a^2, should be a**2
    # statemnt was updated to check for different parameter order
    elif ((((first_side ** 2) + (second_side ** 2)) == (third_side ** 2))
          or (((second_side ** 2) + (third_side ** 2)) == (first_side ** 2))
          or (((first_side ** 2) + (third_side ** 2)) == (second_side ** 2))):
        return 'Right'
    # *need to check all three sides
    elif (first_side != second_side) and (second_side != third_side) and (first_side != third_side):
        return 'Scalene'
    else:
        return 'Isosceles'
