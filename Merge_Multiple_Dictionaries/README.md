# Merge Multiple Dictionaries and Sum Values

## Background
As part of my college's daily technical coding assessments, I solved the **Merge Multiple Dictionaries and Sum Values** problem. The objective is to combine multiple dictionaries and calculate the total value for keys that appear in more than one dictionary.

## Problem Statement
Given multiple dictionaries containing key-value pairs, merge them into a single dictionary. If the same key appears in multiple dictionaries, sum its values.

### Example

**Input:**
Dictionary 1:
apple 10
banana 15
grape 10
Dictionary 2:
apple 5
banana 5
grape 5

**Output:**
apple 15
banana 20
grape 15


## Approach
* Read multiple dictionaries.
* Traverse each key-value pair.
* Check whether the key already exists in the result dictionary.
* If it exists, add the new value to the existing value.
* Otherwise, add the key with its value.
* Display the merged dictionary.

## Complexity Analysis

| Metric               | Complexity |
| :------------------- | :--------: |
| **Time Complexity**  |    O(n)    |
| **Space Complexity** |    O(n)    |

Where `n` represents the total number of key-value pairs across all dictionaries.

## Concepts Used
* Dictionaries
* Key-Value Pairs
* Dictionary Traversal
* Data Aggregation

## Language
* Python

## Status
✅ Solved

**Topic:** Dictionaries / Data Aggregation
**Language:** Python

> This solution is part of my Data Structures and Algorithms (DSA) practice and my college's daily technical coding assessments.
