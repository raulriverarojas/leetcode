package leetcode

import (
	"reflect"
	"testing"
)

func TestRomanToInt(t *testing.T) {
	// Table-driven tests
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "Example 1",
			input:    "III",
			expected: 3,
		},
		{
			name:     "Example 2",
			input:    "LVIII",
			expected: 58,
		},
		{
			name:     "Example 3",
			input:    "MCMXCIV",
			expected: 1994,
		},
		// Add more test cases as needed
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := romanToInt(tc.input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("romanToInt(%v) = %v; want %v",
					tc.input, result, tc.expected)
			}
		})
	}
}
