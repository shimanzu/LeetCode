class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_finder = {}
        for i in nums:
            if i not in num_finder.keys():
                num_finder[i] = 1
            else:
                num_finder[i] += 1

        for i in nums:
            if (target - i) in num_finder.keys():
                if i == (target - i):
                    if num_finder[i] > 1:
                        solution = [nums.index(i), nums.index(i, nums.index(i)+1)]
                        break
                    else:
                        continue
                else:
                    solution = [nums.index(i), nums.index(target-i)]
                    break
        return solution