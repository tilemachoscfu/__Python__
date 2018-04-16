
def quick_sort(array):
    array_len = len(array)
    if( array_len <= 1):
        return array
    else:
        pivot = array[0]
        greater = [ element for element in array[1:] if element > pivot ] # list comprehension
        less = [ element for element in array[1:] if element <= pivot ]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
print( quick_sort(unsorted) )