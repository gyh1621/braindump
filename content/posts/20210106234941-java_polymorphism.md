+++
title = "Java Polymorphism"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Java]({{< relref "20210106174605-java" >}}), [Polymorphism]({{< relref "20210106234832-polymorphism" >}})

source
: [stackify-polymorphism-in-java](x-devonthink-item://79F1947B-AE80-4018-86F0-BDA46155E3C2)

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)


## Static Polymorphism {#static-polymorphism}

Or compile time.

[Java Method Overloading]({{<relref "20210114070305-java_overloading.md" >}})


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


### Fields are not polymorphic {#fields-are-not-polymorphic}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 3   | 6.00     | 2021-01-28T20:26:18Z |

When derived class instance upcasting to base class
instance, fields would be base class fields.

```java
class Super {
  public int field = 0;
  public int getField() { return field; }
}

class Sub extends Super {
  public int field = 1;
  @Override
  public int getField() { return field; }
  public int getSuperField() { return super.field; }
}

public class FieldAccess {
  public static void main(String[] args) {
    Super sup = new Sub(); // Upcast
    System.out.println("sup.field = " + sup.field +
      ", sup.getField() = " + sup.getField());
    Sub sub = new Sub();
    System.out.println("sub.field = " +
      sub.field + ", sub.getField() = " +
      sub.getField() +
      ", sub.getSuperField() = " +
      sub.getSuperField());
  }
}
/* Output:
sup.field = 0, sup.getField() = 1
sub.field = 1, sub.getField() = 1, sub.getSuperField()
= 0
*/
```


### Static methods are not polymorphic {#static-methods-are-not-polymorphic}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 2   | 1.00     | 2021-01-23T20:25:17Z |

\#[static]({{< relref "20210108200839-static" >}})

```java
class StaticSuper {
  public static String staticGet() {
    return "Base staticGet()";
  }
  public String dynamicGet() {
    return "Base dynamicGet()";
  }
}

class StaticSub extends StaticSuper {
  public static String staticGet() {
    return "Derived staticGet()";
  }
  @Override
  public String dynamicGet() {
    return "Derived dynamicGet()";
  }
}

public class StaticPolymorphism {
  public static void main(String[] args) {
    StaticSuper sup = new StaticSub(); // Upcast
    System.out.println(sup.staticGet());
    System.out.println(sup.dynamicGet());
  }
}
/* Output:
Base staticGet()
Derived dynamicGet()
*/
```


### Covariant Return Types {#covariant-return-types}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 1   | 0.01     | 2021-01-23T15:07:17Z |

\#[covariant]({{< relref "20210122140132-covariant" >}})

an [overridden]({{< relref "20210118220036-overriding" >}}) method in a [Derived Class]({{<relref "20210106234746-inheritance.md" >}}) can return a type
dertived from the type returned by the base-class method.

```java
class Grain {
  @Override
  public String toString() { return "Grain"; }
}

class Wheat extends Grain {
  @Override
  public String toString() { return "Wheat"; }
}

class Mill {
  Grain process() { return new Grain(); }
}

class WheatMill extends Mill {
  @Override
  Wheat process() { return new Wheat(); }
}

public class CovariantReturn {
  public static void main(String[] args) {
    Mill m = new Mill();
    Grain g = m.process();
    System.out.println(g);
    m = new WheatMill();
    g = m.process();
    System.out.println(g);
  }
}
/* Output:
Grain
Wheat
*/
```
