+++
title = "CN-09. Implement queue by stack"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-08-29 14:41:44


tags
: [Stack]({{< relref "20200825212600-stack" >}}), [Queue]({{< relref "20200825212611-queue" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)


## Edge Cases {#edge-cases}


## Solution {#solution}

two stacks

NOTE
`Stack` is implemented by `Array` which is slow when expanding size
so we use `LinkedList` here, which inherents `Deque` interface and can act like `Stack`

```java
class CQueue {

    LinkedList<Integer> s1, s2;

    public CQueue() {
        s1 = new LinkedList<>();
        s2 = new LinkedList<>();
    }

    public void appendTail(int value) {
        s1.push(value);
    }

    public int deleteHead() {
        if (s2.size() != 0) return s2.pop();
        if (s1.size() == 0) return -1;

        while (s1.size() > 0) {
            s2.push(s1.pop());
        }

        return s2.pop();
    }
}
```


### Complexity {#complexity}

-   time:
-   space:
