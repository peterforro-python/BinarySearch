
def binary_search(nums: "list[int]", element: int) -> bool:
    '''
    Classic iterative binary search algorithm
    '''
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == element:
            return True
        elif nums[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
    return False


def binary_search2(nums: "list[int]", element: int) -> bool:
    '''
    Iterative binary search algorithm with list slicing
    '''
    middle = (len(nums) - 1) // 2
    try:
        if nums[middle] == element:
            return True
        elif nums[middle] < element:
            return binary_search2(nums[middle + 1 : len(nums)], element)
        elif nums[middle] > element:
            return binary_search2(nums[0 : middle], element)
    except IndexError:
        return False


def recursive_binary_search(nums: "list[int]", element: int, start = 0, end = -10) -> bool:
    '''
    Recursive binary search
    '''
    end = len(nums) - 1 if end == -10 else end
    middle = (start + end) // 2
    if (nums[middle] == element):
        return True
    elif start > end:
        return False
    elif nums[middle] < element:
        return recursive_binary_search(nums, element, middle + 1, end)
    else:
        return recursive_binary_search(nums, element, start, middle - 1)



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10]
    for i in range(-5,16,1):
        print(f"{i}.:\t{binary_search2(nums, i)}")