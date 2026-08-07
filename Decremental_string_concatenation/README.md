# Decremental String Concatenation

## Background
This problem was assigned as part of my college's daily technical coding assessment. It is included in my **My Learning Journey** repository to document my progress in problem-solving and Data Structures & Algorithms (DSA).

## Problem Statement
Given an array of strings, concatenate the strings sequentially. If the last character of the current string matches the first character of the next string, concatenate the next string excluding its first character. Otherwise, concatenate the complete string.

The objective is to determine the length of the final concatenated string.

## Approach
- Start with the first string as the initial result.
- Compare the last character of the current result with the first character of the next string.
- If they match, append the next string excluding its first character.
- Otherwise, append the complete next string.
- Print the length of the final string.

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| **Time Complexity** | O(n × m) |
| **Space Complexity** | O(n × m) |

Where `n` is the number of strings and `m` is the average length of the strings.

## Concepts Covered
- Strings
- Arrays / Lists
- String Concatenation
- Functions
- Conditional Statements
- Input Parsing

## Files
solution.py – Python implementation
README.md – Problem description, approach, and complexity analysis

## Status
✅ Solved

*This solution is part of my **My Learning Journey** repository, documenting problems solved through college technical assessments and personal DSA practice.*
