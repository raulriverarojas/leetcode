package leetcode

import ()

// Your solution function
func searchInsertPosition(input []int, target int) int {
	low := 0
	high := len(input) - 1
	mid := 0
	for low <= high {
		mid = low + ((high - low) / 2)
		if input[mid] == target {
			return mid
		}
		if input[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	if input[mid] > target {
		return mid
	} else {
		return mid + 1
	}
}
