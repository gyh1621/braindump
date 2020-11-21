+++
title = "Topological Ordering"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:02 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-18 Tue 23:15&gt;</span></span>

tags
: [Algorithm]({{< relref "20200916235844-algorithm" >}})


Create a graph
    in this process, mark every node's in degree

add all nodes with 0 degree to queue

get one node from queue, add this node to path
    decrease 1 from all adjacency nodes
    if one node's degree becomes 0, add to queue

loop 3 while queue becomes empty
