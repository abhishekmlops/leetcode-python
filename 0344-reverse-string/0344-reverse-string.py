class Solution:
    def reverseString(self, chars: List[str]) -> None:
        """
    Reverse the list of characters in-place.

    Args:
        chars: List of characters to be reversed.

    Returns:
        None. The input list is modified in-place.

    Time Complexity:
        O(n)
        - The pointers together traverse the array only once.

    Space Complexity:
        O(1)
        - Only two pointer variables are used.
    """
        
        left = 0 
        right = len(chars) - 1

        while left < right:

            chars[left], chars[right] = chars[right], chars[left]
            
            left += 1
            right -= 1