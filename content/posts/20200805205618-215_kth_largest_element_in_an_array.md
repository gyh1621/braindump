+++
title = "215. Kth Largest Element in an Array"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:51 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-05 Wed 21:00&gt;</span></span>

tags
: [PriorityQueue]({{< relref "20200804222308-priorityqueue" >}}), [QuickSelect]({{< relref "20200805205651-quickselect" >}})

source
: [leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/)


## Edge Cases {#edge-cases}


## Solution 1 - PriorityQueue {#solution-1-priorityqueue}

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < nums.length; i++) {
            pq.add(nums[i]);
            if (pq.size() > k) pq.poll();
        }

        return pq.poll();
    }
}
```


### Complexity {#complexity}

-   time: O(NlgK)
-   space: O(K)


## Solution 2 - QuickSelect {#solution-2-quickselect}

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int left = 0, right = nums.length - 1;
        return quickSelect(nums, left, right, nums.length - k);
    }

    private int quickSelect(int[] nums, int left, int right, int target) {
        int pivotIndex = (left + right) >> 1;
        pivotIndex = partition(nums, left, right, pivotIndex);

        if (pivotIndex == target) return nums[pivotIndex];
        else if (pivotIndex < target) return quickSelect(nums, pivotIndex + 1, right, target);
        else return quickSelect(nums, left, pivotIndex - 1, target);
    }

    private int partition(int[] nums, int left, int right, int pivotIndex) {
        if (left == right) return left;

        int pivot = nums[pivotIndex];
        swap(nums, right, pivotIndex);  // must be right, or the cur in swap before right can exceed boundary

        int cur = left;
        for (int i = left; i <= right; i++) {
            if (nums[i] < pivot) {
                if (cur != i) swap(nums, cur, i);
                cur++;
            }
        }

        swap(nums, cur, right);
        return cur;
    }

    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}
```


### Complexity {#complexity}

-   time: average O(N)
-   space: O(1)
