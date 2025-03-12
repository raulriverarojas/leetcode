package leetcode

import ()

func lengthOfLastWord(s string) int {
	p1 := 0
	p2 := 0
	for i := 0; i < len(s); i++ {
		if s[i] != ' ' {
			if i == 0 || s[i-1] == ' ' {
				p1 = i
				p2 = p1
			} else {
				p2++
			}
		}
	}
	return p2 - p1 + 1
}
