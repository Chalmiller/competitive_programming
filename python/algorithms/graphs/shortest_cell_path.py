from typing import *
import collections

def shortestCellPath(grid, sr, sc, tr, tc):
  queue = collections.deque()
  queue.append((sr, sc, 0))

  seen = set()
  seen.add((sr, sc))

  while queue:
    (r, c, count) = queue.popleft()
    if r == tr and c == tc: return count

    for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
      if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1 and (nr, nc) not in seen:
        queue.append((nr,nc, count + 1))
        seen.add((nr, nc))

  return -1


