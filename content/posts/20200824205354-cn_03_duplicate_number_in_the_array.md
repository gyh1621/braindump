+++
title = "CN-03.Duplicate number in the array"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-09-08 19:41:31


tags
: [trick]({{< relref "20200722211911-trick" >}}), [Sort]({{< relref "20200824205520-sort" >}}),[ BinarySearch]({{< relref "20200819231114-binarysearch" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)


## Edge Cases {#edge-cases}


## Solution 1 {#solution-1}

Change Original Array

Sort and compare neighbor


### Complexity {#complexity}

-   time: O(NlgN)
-   space: O(1)


## Solution 2 {#solution-2}

Change Original Array

Swap elements to the "sorted" position, if the "sorted" position is already has the element, it's a duplicate number

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (i != nums[i]) {
                int correctIndex = nums[i];
                if (nums[correctIndex] == nums[i]) {
                    // already has one correct number
                    return nums[i];
                }
                int tmp = nums[correctIndex];
                nums[correctIndex] = nums[i];
                nums[i] = tmp;
            }
        }
        return -1;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)


## Solution 3 {#solution-3}

Not Change Original Array

HashSet


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)


## Solution 4 {#solution-4}

Not Change Original Array

Additional array, put elements into new array

****NOTE****

-   this should be faster than HashSet: no hanlding of hash conflict, true O(1)
-   this should cost less space than HashSet: HashSet usually has additional space left, and internal implementation is a tree


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)


## Solution 5 - if change description to "the array's length is bigger than possible numbers in the array" {#solution-5-if-change-description-to-the-array-s-length-is-bigger-than-possible-numbers-in-the-array}

Not Change Original Array

Binary Search

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (count(nums, left, mid) > (mid - left + 1)) {
                right = mid;
            } else if (count(nums, mid + 1, right) > (right - mid)) {
                left = mid + 1;
            }
        }

        return left;
    }

    private int count(int[] nums, int min, int max) {
        int count = 0;
        for (int i = 0; i <= nums.length - 1; i++) {
            if (nums[i] >= min && nums[i] <= max) count++;
        }
        return count;
    }
}
```
