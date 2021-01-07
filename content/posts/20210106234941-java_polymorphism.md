+++
title = "Java Polymorphism"
author = ["John Doe"]
draft = false
+++

tags
: [On Java 8]({{< relref "20210106162054-on_java_8" >}}), [Java]({{< relref "20210106174605-java" >}}), [Polymorphism]({{< relref "20210106234832-polymorphism" >}})

additional source
: [stackify-polymorphism-in-java](x-devonthink-item://79F1947B-AE80-4018-86F0-BDA46155E3C2)


## Static Polymorphism {#static-polymorphism}

Or compile time.

Multiple methods with the same name in the same class - ****Overloading****
Meet one of the requirments below:

-   Different number of parameters
-   Different types of parameters
-   Different order of parameters


## Dynamic Polymorphism {#dynamic-polymorphism}

A derived class override methods(same name and parameters) of its base class.

One advantage is that when types belongs to a general type needed to be operated by
the same way. Objects can defined as the general type instead of specific types, so
when a new type is added, the operation code doesn't need to change.

Using a general type to operate derived types is called ****Upcasting****.

```java
void doSomething(Shape shape) {
    shape.erase();
    // ...
    shape.draw();
}

Circle circle = new Circle();
Triangle tri = new Triangle();
doSomething(circle);
doSomething(tri);
```
