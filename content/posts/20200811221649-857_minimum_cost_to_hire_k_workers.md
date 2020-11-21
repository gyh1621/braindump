+++
title = "857. Minimum Cost to Hire K Workers"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:38 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-11 Tue 22:32&gt;</span></span>

tags
: [Greedy]({{< relref "20200811221702-greedy" >}}), [PriorityQueue]({{< relref "20200804222308-priorityqueue" >}})

source
: [leetcode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)


## Edge Cases {#edge-cases}


## Solution 1 - Greedy {#solution-1-greedy}

Iterate every worker
    for every one, compute its ratio
    and then apply this ratio to all other workers, put ones with wage above minimum into an array
    sort the array, get first K


### Complexity {#complexity}

-   time: O(N^2lgN)
-   space: O(N)


## Solution 2 - PriorityQueue {#solution-2-priorityqueue}

iterate based on ratio, suppose current ratio is N, then previous workers should all have satisfying wage,
also, we choose K workers with minmum quality, so current wage sum will be minimum

1.  sort based on ratio
2.  add every quality into queue
3.  if queue reachs K, compute current total wage, pop one with maximum quality

<!--listend-->

```java
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int K) {
        int N = quality.length;
        int workers[][] = new int[N][2];

        for (int i = 0; i < N; i++) {
            workers[i][0] = quality[i];
            workers[i][1] = wage[i];
        }

        Arrays.sort(workers, new Comparator<int[]>() {
            public int compare(int[] w1, int[] w2) {
                double r1 = w1[1] / (double)w1[0];
                double r2 = w2[1] / (double)w2[0];
                return Double.compare(r1, r2);
            }
        });

        double ans = 1e9;
        int curQSum = 0;
        PriorityQueue<Integer> pq = new PriorityQueue();
        for (int i = 0; i < N; i++) {
            pq.add(-workers[i][0]);
            curQSum += workers[i][0];
            if (pq.size() == K) {
                double r = workers[i][1] / (double)workers[i][0];
                ans = Math.min(ans, r * curQSum);
                curQSum += pq.poll();
            }
        }

        return ans;
    }
}
```


### Complexity {#complexity}

-   time: O(NlgN)
-   space: O(N)
