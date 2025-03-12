package leetcode

import (
	"reflect"
	"testing"
)

func TestRemoveElement(t *testing.T) {
	// Table-driven tests
	testCases := []struct {
		name          string
		input         []int
		target        int
		expected      int
		nums_expected []int
	}{
		{
			name:          "Example 1",
			input:         []int{3, 2, 2, 3},
			target:        3,
			expected:      2,
			nums_expected: []int{2, 2, 2, 3},
		},
		// Add more test cases as needed
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := removeElement(tc.input, tc.target)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("removeElement(%v, %v) = %v; want %v",
					tc.input, tc.target, result, tc.expected)
			}
			if !reflect.DeepEqual(tc.input, tc.nums_expected) {
				t.Errorf("removeElement(%v, %v); input %v want %v",
					tc.input, tc.target, tc.input, tc.nums_expected)
			}
		})
	}
}
