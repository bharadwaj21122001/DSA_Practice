# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
        num_set = set(nums)
        count = 0

        for i in num_set:
            if i - 1 not in num_set:
                current = i
                current_count = 1
                
                while current + 1 in num_set:
                    current += 1
                    current_count += 1
                count = max(count, current_count)
        return count

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))