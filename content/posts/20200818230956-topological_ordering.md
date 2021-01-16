+++
title = "Topological Ordering"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [Algorithm]({{< relref "20200916235844-algorithm" >}})


Create a graph
    in this process, mark every node's in degree

add all nodes with 0 degree to queue

get one node from queue, add this node to path
    decrease 1 from all adjacency nodes
    if one node's degree becomes 0, add to queue

loop 3 while queue becomes empty
