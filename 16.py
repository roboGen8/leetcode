class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # naive solution: nC3 == O(n3)
        # sort -> nlogn , hashmap -> space O(n) 
        # -4, -1, 1, 2, 4  target = 1 
        # pivot for loop O(n)
        # left and right pointer
        nums.sort()
        print(nums)
        min_sum = 99999999999999999999
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            print(left, right)
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    if abs(target - curr_sum) < abs(target - min_sum):
                        min_sum = curr_sum
                    left += 1
                else:
                    if abs(target - curr_sum) < abs(target - min_sum):
                        min_sum = curr_sum
                    right -= 1
                    
                
                
        return min_sum