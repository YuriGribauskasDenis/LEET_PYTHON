#26.RemoveDuplicatesFromSortedArray.py
def removeDuplicates(nums):
    p_put = 1
    for p_scn in range(1, len(nums)):
        if nums[p_scn - 1] != nums[p_scn]:
            nums[p_put] = nums[p_scn]
            p_put += 1
    return p_put


print(removeDuplicates([1,1,2])) # 2, [1,2,_]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]