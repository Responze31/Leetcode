class Solution:
  def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

    arr1.sort()
    ans = []

    for target in arr2:
      for num in arr1:
        if num == target:
          ans.append(num)

    for num in arr1:
      if num not in arr2:
        ans.append(num)

    return ans