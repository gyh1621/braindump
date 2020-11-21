+++
title = "LoRaWAN Clock Synchronization"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:05:12 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-07-26 Sun 01:51&gt;</span></span>


## Intro {#intro}

synchronize the clock of devices to the network's GPS clock with ****second**** accuracy

-   Default port: 202

-   All messages are transported as application layer messages
    -   **unicast:** encrypted by AppSKey
    -   **multicast:** encrypted by McAppSKey

-   Useful for devices without access to accurate time source

-   Devices should not use this package
    -   devices use LoRaWAN 1.1 or above should use `DeviceTimeReq` MAC command
    -   Class B devices should use network beacon to synchronize time

-   Use Cases
    -   get all devices of a [multicast]({{< relref "20200625153941-lorawan_multicast" >}}) group switching to classC temporarily and synchronously at the beginning of the slot
    -   Get many sensors to synchronously perform a measurement
        get water meter reading of all meters at midnight every day for example
    -   Enabling end-devices to transmit time-stamped events with a unified clock
        the door was opened this morning at 8:00AM
