+++
title = "42. Trapping Rain Water"
author = ["John Doe"]
draft = false
+++

tags
: [trick]({{< relref "20200722211911-trick" >}}), [two pointers]({{< relref "20200720224430-two_pointers" >}})

source
: [leetcode](https://leetcode.com/problems/trapping-rain-water/)


## Edge Cases {#edge-cases}


## Solution 1 - Memorize {#solution-1-memorize}

For water every position can hold = min(leftMax, rightMax) - height[i]

1.  from left to right, get leftMax[]
2.  from right to left, get rightMax[]
3.  from left to right, add water

<!--listend-->

```java
class Solution {
    public int trap(int[] height) {
        int N = height.length;
        int left[] = new int[N], right[] = new int[N];

        for (int i = 0, leftMax = 0; i < N; i++) {
            left[i] = leftMax;
            leftMax = Math.max(leftMax, height[i]);
        }

        for (int i = N - 1, rightMax = 0; i >= 0; i--) {
            right[i] = rightMax;
            rightMax = Math.max(rightMax, height[i]);
        }

        int sum = 0;
        for (int i = 0; i < N; i++) {
            int cur = Math.min(left[i], right[i]) - height[i];
            sum += Math.max(0, cur);
        }

        return sum;
    }
}
```


### Complexity {#complexity}

-   time: O(n)
-   space: O(n)


## Solution 2 - Two Pointers {#solution-2-two-pointers}

Start from two ends, maintain `leftMax` and `rightMax`
in a position, if `leftMax < rightMax`,
    if current position's height < `leftMax`, then current position can hold water `leftMax - currentHeight`
    if current position's height >= `leftMax` , update `leftMax`
    left pointer move forward
else:
    same as above

```java
class Solution {
    public int trap(int[] height) {
        int sum = 0, leftMax = 0, rightMax = 0;

        int left = 0, right = height.length - 1;
        while (left <= right) {
            if (leftMax < rightMax) {
                if (height[left] >= leftMax) leftMax = height[left];
                else sum += (leftMax - height[left]);
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else sum += (rightMax - height[right]);
                right--;
            }
        }

        return sum;
    }
}
```


### Complexity {#complexity}

-   time: O(n)
-   space: O(1)
