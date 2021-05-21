+++
title = "Java Abstract Class"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Abstract Class]({{< relref "20210123074954-abstract_class" >}})

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)


## Purpose {#purpose}

Establish a basic form for all the derived classes.
To express only the interface, and not a particular implementation.

-   no actual instances


## Abstract Class {#abstract-class}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.5  | 0   | 0        | 2021-01-23T15:52:20Z |

Classes have abstract methods (or not).

```java
abstract class Basic {
    abstract void f();
}
```

Derived classes of abstract classes must implemente abstract methods.
If not, the derived class is still abstract class.

```java
abstract class Base2 extends Basic {
    int f() { return 111; }
    abstract void g();
    // f still not implemented
}
```

Allow almost all [Java Access Control]({{< relref "20210116004947-java_access_control" >}}) modifiers, except `private abstract` (no sense for it);
whereas [Java Interface]({{< relref "20210123074906-java_interface" >}}) only allow public methods.
