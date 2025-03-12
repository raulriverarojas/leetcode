package leetcode

import (
	"reflect"
	"testing"
)

func TestRemoveElement(t *testing.T) {
	// Table-driven tests
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "Example 1",
			input:    "Hello World",
			expected: 5,
		},
		// Add more test cases as needed
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := lengthOfLastWord(tc.input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("removeElement(%v) = %v; want %v",
					tc.input, result, tc.expected)
			}
		})
	}
}
