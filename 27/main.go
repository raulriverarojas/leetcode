package leetcode

import ()

// Your solution function
func removeElementUnoptomized(nums []int, val int) int {
	length := len(nums)
	end_pointer := len(nums) - 1
	i := 0
	for i < length {
		if nums[i] == val {
			for k := end_pointer; i < k; k-- {
				if nums[k] != val {
					nums[i] = nums[end_pointer]
					nums[end_pointer] = val
					break
				}
				length -= 1
				end_pointer -= 1
			}
			length -= 1
			end_pointer -= 1
		}
		i++
	}
	return length

}
func removeElement(nums []int, val int) int {
	writePos := 0
	for readPos := 0; readPos < len(nums); readPos++ {
		if nums[readPos] != val {
			nums[writePos] = nums[readPos]
			writePos++
		}
	}
	return writePos
}
