+++
title = "Where Storage Lives"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Programming Language Concept]({{< relref "20210106173919-programming_language_concept" >}})

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)


## Registers {#registers}

-   fastest: inside CPU
-   limited Numbers
-   typically no direct control over register allocation


## Stack {#stack}

-   lives in genral random-access memory (RAM)
-   direct support from the processor via stack pointer
-   fast and efficient way to allocate storage


## Heap {#heap}

-   pool of memory, also lives in RAM
-   technically slower than stack when allocating and releasing memory


## Constant storage {#constant-storage}

-   placed directly in the program code -> safe
-   in some special cases, some constants can be placed in other special locations
    -   string literals in Java


## Non-RAM storage {#non-ram-storage}

Turn objects into something exist on the other medium,
and yet be resurrected into a regular RAM-based object when necessary.

-   serialized objects  #[serialization]({{< relref "20210108155912-serialization" >}})
    turn objects intio streams of bytes, usually used when sending objects to another machine

-   persistent objects
    place objects on disk
