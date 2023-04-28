#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(nums):
    # Handle the base cases for empty and single-element lists
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    # Divide the list into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    # Check if the middle element is a peak
    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        return nums[mid]

    # If not, recurse on the half with the larger neighboring element
    elif nums[mid - 1] > nums[mid + 1]:
        return find_peak(left_half)
    else:
        return find_peak(right_half)
