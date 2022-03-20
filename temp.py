#
# class Solution:
#     def minimalKSum(self, nums: List[int], k: int) -> int:
#         count = 0
#         while True:
#             print()

def main():
    # s1 = Solution()
    nums = []
    k=10
    count = 0
    sum = 0
    set_nums = set(nums)
    i=1
    while True:
        if k==count:
            return sum
        if i not in set_nums:
            sum+= i
            count += 1
        i += 1


if __name__ == '__main__':
    main()