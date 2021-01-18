+++
title = "Java Garbage Collector"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Java]({{< relref "20210106174605-java" >}}), [Programming Language Concept]({{< relref "20210106173919-programming_language_concept" >}})

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)


## Facts easily got mistaken {#facts-easily-got-mistaken}

-   objects might not get garbage collected
-   garbage collection is not destruction
-   garbage collection is only about memory


## Use [Heap]({{<relref "20210108151044-where_storage_lives.md" >}}) != Slow Speed {#use-heap--20210108151044-where-storage-lives-dot-md--slow-speed}

-   think C++ use heap as a yard -> search the whole yard when finding an object
-   think Java use heap as an stack -> JVM implementation


## Technique {#technique}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 1   | 0.01     | 2021-01-17T18:35:08Z |


### Reference Counting {#reference-counting}

-   each object contains a reference
    -   a reference attached, count + 1
    -   a reference goes out of scope or is set to null, count - 1
-   the collector moves along the list of objects, release ones whose counting is 0


#### Circular Reference {#circular-reference}

One problem is that when objects circularly refer to each other,
their counting will never be zero while still being garbage.


### Adaptive Scheme {#adaptive-scheme}


#### Finding starts from references {#finding-starts-from-references}

General Idea: Any non-dead object must ultimately be traceable back to
a reference that lives either on the stack or in static storage.

-   start in the stack and in the static storage and walk through all references
-   for each object found, follow references in that object

No Circular Reference issue.


#### Stop and Copy {#stop-and-copy}

After finding the objects:

-   each live object is copied from one heap to another, leaving behind all garbage
-   all reference (stack, static storage, inside objects) updated

Issues:

1.  have two heaps, maintaining twice as much memory as needed
2.  when the process become stable, less garbage generated, copying process seems wasteful


#### Mark and Sweep {#mark-and-sweep}

Slow, but when little new garbage generated, it's fast. (?)

Also stops the process.

After finding the objects:

-   set a flag - the object isn't collected yet
-   after all objects found, sweep begins:
    -   dead objects are released

Issue:

-   cause fragmented heap


#### Adaptive Way {#adaptive-way}

When all objects are long-lived, JVM switches to use mark-and-sweep;
when the heap starts to become fragmented, JVM switches to use stop-and-copy.
