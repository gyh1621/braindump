+++
title = "138. Copy List with Random Pointer"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-08-13 23:25:26


tags
: [LinkedList]({{< relref "20200813223551-linkedlist" >}}), [Recursion]({{< relref "20200813223609-recursive" >}}), [trick]({{< relref "20200722211911-trick" >}})

source
: [leetcode](https://leetcode.com/problems/copy-list-with-random-pointer/)


## Edge Cases {#edge-cases}

nodes can have same value


## Solution 1 - Recursion {#solution-1-recursion}

```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;

        Map<Node, Node> clonedNodes = new HashMap<>();
        return copyRandomListHelper(head, clonedNodes);
    }

    private Node copyRandomListHelper(Node head, Map<Node, Node> clonedNodes) {
        if (head == null) return null;
        if (clonedNodes.containsKey(head)) return clonedNodes.get(head);

        Node newNode = new Node(head.val);
        clonedNodes.put(head, newNode);
        newNode.next = copyRandomListHelper(head.next, clonedNodes);
        newNode.random = copyRandomListHelper(head.random, clonedNodes);

        return newNode;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)


## Solution 2 - HashMap, one pass {#solution-2-hashmap-one-pass}

```java
public class Solution {
  // Visited dictionary to hold old node reference as "key" and new node reference as the "value"
  HashMap<Node, Node> visited = new HashMap<Node, Node>();

  public Node getClonedNode(Node node) {
    // If the node exists then
    if (node != null) {
      // Check if the node is in the visited dictionary
      if (this.visited.containsKey(node)) {
        // If its in the visited dictionary then return the new node reference from the dictionary
        return this.visited.get(node);
      } else {
        // Otherwise create a new node, add to the dictionary and return it
        this.visited.put(node, new Node(node.val, null, null));
        return this.visited.get(node);
      }
    }
    return null;
  }

  public Node copyRandomList(Node head) {

    if (head == null) {
      return null;
    }

    Node oldNode = head;

    // Creating the new head node.
    Node newNode = new Node(oldNode.val);
    this.visited.put(oldNode, newNode);

    // Iterate on the linked list until all nodes are cloned.
    while (oldNode != null) {
      // Get the clones of the nodes referenced by random and next pointers.
      newNode.random = this.getClonedNode(oldNode.random);
      newNode.next = this.getClonedNode(oldNode.next);

      // Move one step ahead in the linked list.
      oldNode = oldNode.next;
      newNode = newNode.next;
    }
    return this.visited.get(head);
  }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)


## Solution 3 - O(1) space {#solution-3-o--1--space}

1.  First pass: create cloned nodes and append to original node

{{< figure src="/ox-hugo/2020-08-13_22-42-29_C31035DE-4640-4D55-9C51-3209B93CF5D9.png" >}}

1.  assign random of cloned nodes
2.  assemble cloned nodes


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)
