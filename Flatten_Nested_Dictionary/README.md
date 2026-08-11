# Flatten a Nested Dictionary

## Background
As part of my college's daily technical coding assessments, I solved the **Flatten a Nested Dictionary** problem. This solution focuses on converting a nested dictionary into a single-level dictionary using dot notation for the keys.

## Problem Statement
Given a nested dictionary, flatten it so that nested keys are combined using `.` notation.

## Approach
The solution traverses the dictionary and:
- Checks whether the value is another dictionary.
- If it is a nested dictionary, recursively processes its contents.
- Combines parent and child keys using `.`.
- Stores the final key-value pairs in a single-level dictionary.

## Concepts Used
- Dictionaries
- Recursion
- Key-Value Pairs
- Nested Data Structures
- String Manipulation

## Complexity Analysis
| Metric | Complexity |
| :--- | :---: |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) |

Where `n` represents the number of key-value pairs processed.

## Language
- Python

## Status
✅ Solved

**Topic:** Dictionary / Recursion  
**Language:** Python

> This solution is part of my Data Structures and Algorithms (DSA) practice and my college's daily technical coding assessments.
