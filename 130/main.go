package leetcode

// Your solution function
func romanToInt(input string) int {
	table := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	result := 0
	length := len(input)
	for i := 0; i < length; i++ {
		curr := input[i]
		if (i+1 < length) && (table[curr] < table[input[i+1]]) {
			result = result - (table[curr])
		} else {
			result = result + (table[curr])
		}
	}
	return result
}
