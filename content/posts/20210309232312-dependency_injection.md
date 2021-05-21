+++
title = "Dependency Injection"
author = ["Yuhang Guo"]
draft = false
+++

source
: [Guice Motivation](https://github.com/google/guice/wiki/Motivation)


## Dependency Injection is a [Design Pattern]({{< relref "20210118055021-design_pattern" >}}) {#dependency-injection-is-a-design-pattern--20210118055021-design-pattern-dot-md}


## Advantages {#advantages}

1.  Easy to write tests
    -   e.g.: classes with database instances
2.  Dependency is exposed by **API signature**, not **hidden in the code**
    -   after adding a new dependency
        -   no need to manually check the tests to find out which ones will fail
        -   no need to worry about forgot initializing the new dependency in the code
