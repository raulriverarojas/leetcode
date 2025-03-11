package leetcode

import (
	"reflect"
	"testing"
)

func TestRomanToInt(t *testing.T) {
	// Table-driven tests
	testCases := []struct {
		name     string
		input    []int
		target   int
		expected int
	}{
		{
			name:     "Example 1",
			input:    []int{1, 3, 5, 6},
			target:   5,
			expected: 2,
		},
		{
			name:     "Example 2",
			input:    []int{1, 3, 5, 6},
			target:   2,
			expected: 1,
		},
		{
			name:     "Example 3",
			input:    []int{1, 3, 5, 6},
			target:   7,
			expected: 4,
		},
		// Add more test cases as needed
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := searchInsertPosition(tc.input, tc.target)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("searchInsertPosition(%v, %v) = %v; want %v",
					tc.input, tc.target, result, tc.expected)
			}
		})
	}
}
