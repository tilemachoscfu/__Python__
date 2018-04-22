from random import randint
import numpy as np
from scipy import stats


def makelist(count):
    return [randint(1, 100) for _ in range(count)]

def main():
    random_integer = randint(50,50)  # generate a random integer 
    unsorted_list = makelist(count = random_integer)  # make a list
    sorted_list = sorted(unsorted_list)  # sort the list
    print ('Mean:',np.average(sorted_list),'|Range:', np.ptp(sorted_list),
    	   '|Median:', np.median(sorted_list),'|Mode:', stats.mode(sorted_list))
  
main()