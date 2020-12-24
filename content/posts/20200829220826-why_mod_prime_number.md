+++
title = "Why Mod Prime Number"
author = ["John Doe"]
draft = false
+++

tags
: [Mod]({{< relref "20200829220845-mod" >}})

source
: [DEVONThink](x-devonthink-item://824B5705-3239-43B4-B3B5-AFB23C88FE32)

1000000007 is a prime which fits inside an integer value. Now many problems require you to have arithmetic operations on them(division, addition, multiplication or subtraction). Now, so that the result after the arithmetic operation also fits inside an integer and it is also unique, a prime number is used. It is unique because a prime number has only 1 and itself as its factors, so neither a nor b can have common factors with m (as a, b < m). Example where the multiplication results as non-unique: 4 \* 6 mod 12 and 9 \* 8 mod 12 both equal 0.

By unique, I meant that the results of the modulo will have range over integer between 0 and m-1 and no integer will be skipped. That is why in hashing a prime number is used as mentioned by Namit Sinha.
