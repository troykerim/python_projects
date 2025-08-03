def getConcatenation(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans

nums = [1,4,1,2]
print(getConcatenation(nums))