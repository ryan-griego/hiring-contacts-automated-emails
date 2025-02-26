from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Define an empty list to track the numbers
        my_list = []

         # Loop through the values in list
        for i in range(len(nums)):
            #Check to see if the value in i exists in my_list
            if nums[i] in my_list:
                print("the value exists in my list", my_list)

                print(my_list)
                return True
            my_list.append(nums[i])
        print(my_list)
        return False

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))  # Expected output: True
print(solution.hasDuplicate([1, 2, 3, 4]))  # Expected output: False
