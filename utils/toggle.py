#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jezhang
#
# Created:     24/09/2013
# Copyright:   (c) jezhang 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from itertools import cycle

def make_toggle(num):
    """利用迭代器和闭包实现，如果不需要设置初始状态，就更简单。
    直接myIterator = cycle([1,0])
    """
    
    if num == 0:
        myIterator = cycle(range(2)[::-1])
        # bools = [True,False]
        # myIterator = cycle(bools)
        def inner():
            return myIterator.next()
        return inner
    else:
        def inner():
            return "please input num=0"
        return inner

def main():
    x = toggle(0)
    for i in range(1000):
        print x()


if __name__ == '__main__':
    main()
