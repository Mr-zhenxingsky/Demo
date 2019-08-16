import math
def longest_side(a,b):
    """
    function to find the length of longest side of a right triangle
    :arg a: side a of the triangle
    :arg b: side b of the triangle

    :return: length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)# use to show the doc
    print(longest_side(4,5))

# def fun() use to define a function
# """  """ use to annotation
#__name__ == '__main__' as main function entry

