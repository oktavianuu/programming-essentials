### The Bubble Short
There are many sorting algorithm to sort elements of a list. Different algorithms different speed and effectiveness. 
One of them are bubble sort. Let's assume that list can be sorted in two ways:
* Increasing (or more precisely -non-decreasing)-if in every pair of adjacent elements, the former element is not greater than the latter.
* Decreasing (or more precisely -non-decreasing)-if in every pair of adjacent elements, the former is not less than the latter.

Here is an example, we're going to use increasing method with the following list:
```python
the_list = [8, 10, 6, 2, 4]
```
We'll try to use the following approach: we'll take the first and the second elements and compare them; if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; if their order is valid, we'll do nothing. A glance at our list confirms the latter - the elements 01 and 02 are in the proper order, as in 8 < 10.

Now look at the second and the third elements. They're in the wrong positions so we have to swap them:
```python
the_list = [8, 6, 10, 2, 4]
```
We go further, and look at the third and the fourth elements. Again, this is not what it's supposed to be like. We have to swap them:
```python
the_list = [8, 6, 2, 10, 4]
```
Now we check the fourth and the fifth elements. Yes, they too are in the wrong positions. Another swap occurs:
```python
the_list = [8, 6, 2, 4, 10]
```
The first pass through the list is already finished. We're still far from finishing our job, but something curious has happened in the meantime. The largest element, 10, has already gone to the end of the list. Note that this is the desired place for it. All the remaining elements form a picturesque mess, but this one is already in place.

Now we start with the second pass through the list. We look at the first and second elements - a swap is necessary:
```python
the_list = [6, 8, 2, 4, 10]
```
Time for the second and third elements: we have to swap them too:
```python
the_list = [6, 2, 8, 4, 10]
```
Now the third and fourth elements, and the second pass is finished, as 8 is already in place:
```python
the_list = [6, 2, 4, 8, 10]
```
We start the next pass immediately. Watch the first and the second elements carefully - another swap is needed:
```python
the_list = [2, 6, 4, 8, 10]
```
Now ```6``` needs to go into place. We swap the second and the third elements:
```python
the_list = [2, 4, 6, 8, 10]
```
The list is already sorted. We have nothing more to do. This is exactly what we want.

As you can see, the essence of this algorithm is simple: we compare the adjacent elements, and by swapping some of them, we achieve our goal.

Let's code in Python all the actions performed during a single pass through the list, and then we'll consider how many passes we actually need to perform it. We haven't explained this so far, and we'll do that a little later.