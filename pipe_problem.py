def pipe_fix(nums):
    new_list = []
    first_ele = nums[0]
    last_ele = nums[len(nums)-1]
    print(first_ele, last_ele)
    while first_ele <= last_ele:
        new_list.append(first_ele)
        first_ele += 1
    print(new_list)
    return new_list

pipe_fix([6, 9])