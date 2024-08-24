from typing import List

def shrinkable_sliding_window(nums: List[int], k: int) -> float:
    start = 0
    current_sum = 0
    max_result = float('-inf')

    for end in range(len(nums)):
        current_sum += nums[end]

        # Shrink the window as needed
        while end - start + 1 > k:  # Window exceeds size k
            current_sum -= nums[start]  # Remove the element at the start
            start += 1  # Move the start pointer forward

        # Process the window if its size is exactly k
        if end - start + 1 == k:
            result = current_sum
            max_result = max(max_result, result)

    return max_result

# Example usage
nums = [1, 2, 3, 4, 5]
k = 3
result = shrinkable_sliding_window(nums, k)
print(f"The maximum sum of any subarray of size {k} is: {result}")


