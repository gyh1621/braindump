+++
title = "849. Maximize Distance to Closest Person"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:52 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-03 Mon 23:41&gt;</span></span>

tags
: [subarray]({{< relref "20200716205913-subarray" >}}), [two pointers]({{< relref "20200720224430-two_pointers" >}})

source
: [leetcode](https://leetcode.com/problems/maximize-distance-to-closest-person/)


## Edge Cases {#edge-cases}


## Solution 1 - divide by situations {#solution-1-divide-by-situations}

1.  start is 0 -> max dis: number of 0
2.  end is 0 -> max dis: number of 0
3.  group of 0 between 1 -> max dis: (number of 0 + 1) / 2

<!--listend-->

```java
class Solution {
    public int maxDistToClosest(int[] seats) {
        int zero = 0, maxDis = 0;

        for (int i = 0; i < seats.length && seats[i] == 0; i++) zero++;
        maxDis = zero;

        zero = 0;
        for (int i = seats.length - 1; i >= 0 && seats[i] == 0; i--) zero++;
        maxDis = Math.max(zero, maxDis);

        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 1) {
                zero = 0;
            } else {
                zero++;
                maxDis = Math.max((zero + 1) / 2, maxDis);
            }
        }

        return maxDis;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)


## Solution 2 - two pinters {#solution-2-two-pinters}

`left` is distance of current seat to left 1
`right` is distance of current seat to right 1

```java
class Solution {
    public int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int prev = -1, future = 0;
        int ans = 0;

        for (int i = 0; i < N; ++i) {
            if (seats[i] == 1) {
                prev = i;
            } else {
                while (future < N && seats[future] == 0 || future < i)
                    future++;

                int left = prev == -1 ? N : i - prev;
                int right = future == N ? N : future - i;
                ans = Math.max(ans, Math.min(left, right));
            }
        }

        return ans;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)
