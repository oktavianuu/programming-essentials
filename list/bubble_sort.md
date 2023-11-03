### The Bubble Short
There are many sorting algorithm to sort elements of a list. Different algorithms different speed and effectiveness. 
One of them are bubble sort. Let's assume that list can be sorted in two ways:
* Increasing (or more precisely -non-decreasing)-if in every pair of adjacent elements, the former element is not greater than the latter.
* Decreasing (or more precisely -non-decreasing)-if in every pair of adjacent elements, the former is not less than the latter.

Here is an example, we're going to use increasing method with the following list:
```python
the_list = [1, 2, 3, 4, 5, 6]
```
We'll try to use the following approach: we'll take the first and the second elements and compare them; if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; if their order is valid, we'll do nothing. A glance at our list confirms the latter - the elements 01 and 02 are in the proper order, as in 8 < 10.



