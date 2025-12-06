class Solution:
    #Solution #1 (My original Approach)
    def hasDuplicate(self, nums: List[int]) -> bool:
        initial_len = len(nums)
        no_duplicated_set = set(nums)
        final_len = len(no_duplicated_set)
        if final_len<initial_len:
            return True
        else:
            return False
    #Solution #2 (Cleaner approach)
    # This is a more concise approach that directly returns the
    # boolean result of comparing the list and set lengths.
    def hasDuplicate_Opt(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)
