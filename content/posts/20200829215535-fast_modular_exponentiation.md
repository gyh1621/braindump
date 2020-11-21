+++
title = "Fast Modular Exponentiation"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:14 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-10-24 Sat 09:18&gt;</span></span>

tags
: [Mod]({{< relref "20200829220845-mod" >}}), [Algorithm]({{< relref "20200916235844-algorithm" >}})

source
: [DEVONThink](//5C203F39-E8D5-4AC0-98BF-87372FFEDBDE)

<!--listend-->

```java
long pow(long base, int num){
    long res = 1;
    while(num > 0){
        if((num & 1) == 1){
            res *= base;
            res %= mod;
        }
        base *= base;
        base %= mod;
        num >>= 1;
    }
    return res;
}
```
