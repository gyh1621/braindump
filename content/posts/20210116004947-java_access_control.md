+++
title = "Java Access Control"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Java]({{< relref "20210106174605-java" >}}), [Access Control]({{< relref "20210106173814-access_control" >}})

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)

Determine who can use the definitions that follow.

When comes to determine whether elements accessible,
see whether the current scope meets the access requirement.


## Default {#default}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 3   | 6.00     | 2021-01-28T20:29:09Z |

Also called **package-private access**.

Don't need to import package-private classes in the same package.

Package-private members (fields and methods) in any cases, inherited or inside public classes,
remains ****package-private****.

If [Java Class]({{< relref "20210114095654-java_class" >}}) is package-private, it's invisible outside of the package.

Files in the same directory are implicitly part of the "default package" for that directory.


## Public {#public}

The element is available to everyone


## Private {#private}

No one can access that element except the creator.

Anyone trying to access this kind of elements illegally gets [compile time error]({{< relref "20210106175817-compile_time_error" >}}).


## Protected {#protected}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 3   | 6.00     | 2021-01-28T20:26:42Z |

-   Like **private**, but inheriting classes (same package or not) may access **protected** members
-   Also gives package access - other classes in the same package can access protected elements
-   It's best to define fields private to always preserve right to change the underlying implementation

<!--listend-->

```java
package package1;

public class Class1 {
    public void tryMePublic() {
    }

    protected void tryMeProtected() {
    }

    public static void main(String[] args) {
        Class1 c = new Class1();
        c.tryMeProtected(); // no error
    }
}


package package2;

import package1.Class1;

public class Class2 extends Class1 {
    doNow() {
        Class1 c = new Class1();
        c.tryMeProtected(); // ERROR: tryMeProtected() has protected access in Class1
        tryMeProtected();  // No error
    }
}
```


## Java Class Access Control {#java-class-access-control}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 1   | 0.01     | 2021-01-18T17:00:43Z |

\#[Java Class]({{< relref "20210114095654-java_class" >}})


### Java Class can only be Default or Public {#java-class-can-only-be-default-or-public}

-   Private would make the class inaccessible to anyone, which make the Class meaningless
-   [Java Inner Class]({{< relref "20210117230439-java_inner_class" >}}) is an exception


### Public members in a package access class {#public-members-in-a-package-access-class}

-   for usage outside of the package
    e.g., [Use package private class instances outside of the package](https://stackoverflow.com/a/41282060)

<!--listend-->

```java
package pkg1;

public class A {
    public void publicPrint() {System.out.println("Public print from A");}
}

class AA extends A {
    @Override
    public void publicPrint() { System.out.println("Public print from AA"); }
}

public class B {
    public A makeAA() {return new AA();}
    // need upcasting here
    // otherwise if return AA, it cannot use outside of the package
    // e.g., in class C:
    // new B().makeAA().publicPrint() will cause error
}

package pkg2;

public class C {
    public static void main(String[] args){
        B b = new B();
        A aa = b.makeAA();
        aa.publicPrint();
    }
}

/* Output
Public print from AA
*/
```

-   for usage in [Derived Class]({{<relref "20210106234746-inheritance.md" >}}) outside of the package

<!--listend-->

```java
package pkg1;

class Base {
    void packagePrint() { System.out.println("Package print from Base"); }
    public void publicPrint() { System.out.println("Public print from Base"); }
}

public class A extends Base{ }

package pkg2;

import pkg1.A;

public class C extends A {
    public static void main(String[] args){
        C c = new C();
        c.publicPrint();
    }
}

/* Output
Public print from Base
*/
```
