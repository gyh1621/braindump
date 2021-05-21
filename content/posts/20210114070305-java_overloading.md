+++
title = "Java Overloading"
author = ["Yuhang Guo"]
draft = false
+++

tag
: [Java]({{< relref "20210106174605-java" >}}), [overloading]({{< relref "20210114064351-overload" >}})

source
: [DT-On Java 8](x-devonthink-item://199347D4-709D-41DF-84EA-B02E4E11ACEE)

source
: [stackify-polymorphism-in-java](x-devonthink-item://79F1947B-AE80-4018-86F0-BDA46155E3C2)


## Methods {#methods}

| position | ease | box | interval | due                  |
|----------|------|-----|----------|----------------------|
| front    | 2.50 | 3   | 6.00     | 2021-01-26T23:34:06Z |

Multiple methods with the same name in the same class
Meet one of the requirements below:

-   Different number of parameters
-   Different types of parameters
-   Different order of parameters

Why not distinguish between methods based on return values:

-   compile can not determine which method to call when **calling a method for its side effect**
    -   call a method and ignore the return value: `int f(int x)` called with `f(x)`


### Primitive Arguments {#primitive-arguments}

[Primitive Types]({{<relref "20210106174853-java_grammar.md" >}})


#### Widening Conversion {#widening-conversion}

[boolean not support casting]({{< relref "20210106174853-java_grammar" >}})

-   constant value is treated as int
-   for all primitive types supporting narrowing, they would be
    casted to the function with the next larger type
    -   `void f(short x)`, `void f(int x)`, `void f(long x)`
    -   a variable `byte b = 0`, call function `f(b)`
    -   `void f(short x)` would actually be called
-   char is an exception: if it doesn't find an exact char match, it is promoted to int


#### Narrowing Conversion {#narrowing-conversion}

If an argument is wider than what the method expects, explicit narrowing
conversion must be performed.
