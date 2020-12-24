+++
title = "CN-350. Intersect of two arrays"
author = ["John Doe"]
draft = false
+++

tags
: [two pointers]({{< relref "20200720224430-two_pointers" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)


## Edge Cases {#edge-cases}


## Solution 1 - hashset {#solution-1-hashset}

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersect(nums2, nums1);
        }

        Map<Integer, Integer> numbers = new HashMap<>();
        for (int num: nums1) {
            numbers.put(num, numbers.getOrDefault(num, 0) + 1);
        }

        int[] res = new int[Math.min(nums1.length, nums2.length)];
        int r = 0;
        for (int i = 0; i < nums2.length; i++) {
            int num = nums2[i];
            if (numbers.getOrDefault(num, 0) != 0) {
                numbers.put(num, numbers.get(num) - 1);
                res[r++] = num;
            }
        }

        return Arrays.copyOfRange(res, 0, r);
    }
}
```


### Complexity {#complexity}

-   time: O(N + M)
-   space: O(min(N, M))


## Solution 2 - two pointers {#solution-2-two-pointers}

sort first

```nil
if (nums1[p1] == nums2[p2]) add;
if (nums1[p1] < nums2[p2]) p1++;
else p2++;

if p1 invalid or p2 invalid, break;
```


### Complexity {#complexity}

-   time: O(N + M)
-   space: O(min(N, M))
