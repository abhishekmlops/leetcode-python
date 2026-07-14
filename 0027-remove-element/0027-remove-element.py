class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Remove all occurrences of val in-place.
        Return the number of remaining elements.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow
        