+++
title = "LoRaWAN Fragmentation"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:05:25 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-07-26 Sun 13:31&gt;</span></span>


## Intro {#intro}

-   Default port: 201

-   All messages are transported as application layer messages
    -   **unicast:** encrypted by AppSKey
    -   **multicast:** encrypted by McAppSKey

-   Use cases
    -   firmware update ([multicast]({{< relref "20200625153941-lorawan_multicast" >}}) group or unicast)
    -   device send large data file to the server


## Thoughts {#thoughts}

-   ensure integrity
    -   check CRC
    -   transport some data fragments more than once
    -   Forward Error Correction

-   authentication
    -   use certificate
    -   use unicast to send one more message contains HASH of the data
