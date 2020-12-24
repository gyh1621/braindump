+++
title = "329. Longest Increasing Path in a Matrix"
author = ["John Doe"]
draft = false
+++

tags
: [DFS]({{< relref "20200817231103-dfs" >}}), [Memoization]({{< relref "20200819235643-memoization" >}}), [Topological Ordering]({{< relref "20200818230956-topological_ordering" >}})

source
: [leetcode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solution/)


## Edge Cases {#edge-cases}


## Solution 1 - Raw DFS {#solution-1-raw-dfs}


### Complexity {#complexity}

-   time: O(2^(M + N))
-   space: O(MN)


## Solution 2 - DFS with Memoization {#solution-2-dfs-with-memoization}

```java
class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int r = matrix.length;
        if (r == 0) return 0;
        int c = matrix[0].length;
        int[][] longest = new int[r][c];
        for (int i = 0; i < r; i++) Arrays.fill(longest[i], -1);

        int maxLen = -1;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int pathLen = findLongestPath(matrix, i, j, longest);
                maxLen = Math.max(maxLen, pathLen);
            }
        }

        return maxLen;
    }

    private int findLongestPath(int[][] matrix, int i, int j, int[][] longest) {
        if (longest[i][j] != -1) return longest[i][j];

        int r = matrix.length, c = matrix[0].length;

        int maxLen = 1;
        if (i + 1 < r && matrix[i + 1][j] > matrix[i][j]) {
            int pathLen = findLongestPath(matrix, i + 1, j, longest);
            maxLen = Math.max(maxLen, pathLen + 1);
        }
        if (i - 1 >= 0 && matrix[i - 1][j] > matrix[i][j]) {
            int pathLen = findLongestPath(matrix, i - 1, j, longest);
            maxLen = Math.max(maxLen, pathLen + 1);
        }
        if (j + 1 < c && matrix[i][j + 1] > matrix[i][j]) {
            int pathLen = findLongestPath(matrix, i, j + 1, longest);
            maxLen = Math.max(maxLen, pathLen + 1);
        }
        if (j - 1 >= 0 && matrix[i][j - 1] > matrix[i][j]) {
            int pathLen = findLongestPath(matrix, i, j - 1, longest);
            maxLen = Math.max(maxLen, pathLen + 1);
        }

        longest[i][j] = maxLen;
        return maxLen;
    }
}
```


### Complexity {#complexity}

-   time: O(MN)
-   space: O(MN)


## Solution 3 - Topological Ordering {#solution-3-topological-ordering}

```java
class Solution {
public int longestIncreasingPath(int[][] matrix) {
        // Corner cases
        if (matrix.length == 0) {
            return 0;
        }

        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int rows = matrix.length, cols = matrix[0].length;

        // indegree[i][j] indicates thee number of adjacent cells bigger than matrix[i][j]
        int[][] indegree = new int[rows][cols];
        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                for (int[] dir: dirs) {
                    int nx = x + dir[0];
                    int ny = y + dir[1];
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                        if (matrix[nx][ny] > matrix[x][y]) {
                            indegree[x][y]++;
                        }
                    }
                }

            }
        }

        // Add each cell with indegree zero to the queue
        Queue<int[]> queue = new LinkedList<>();
        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                if (indegree[x][y] == 0) {
                    queue.offer(new int[]{x, y});
                }
            }
        }

        int length = 0; // The longest path so far
        // BFS implements the Topological Sort
        while(!queue.isEmpty()) {
            int sz = queue.size();
            for (int i = 0; i < sz; i++) {
                int[] cur = queue.poll();
                int x = cur[0];
                int y = cur[1];
                for (int[] dir: dirs) {
                    int nx = x + dir[0];
                    int ny = y + dir[1];
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                        if (matrix[nx][ny] < matrix[x][y]
                            && --indegree[nx][ny] == 0) {
                           queue.offer(new int[]{nx, ny});
                        }
                    }
                }
            }
            length++;
        }

        return length;
    }
}
```


### Complexity {#complexity}

-   time: O(MN)
-   space: O(MN)
