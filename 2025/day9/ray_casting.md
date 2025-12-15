The **Even-Odd Rule** (often called the Ray Casting algorithm) is a simple way to determine if a specific point is **inside** or **outside** a shape.

In the context of your code—specifically `create_boundary`—it is the logic you need to correctly "fill" the solid parts of your map without filling the empty voids.

### 1\. The Core Concept

Imagine you are standing at a point and you shoot a laser beam (a ray) in a straight line all the way to infinity.

  * **Count** how many times your laser hits a wall.
  * If you hit an **ODD** number of walls (1, 3, 5...), you must have started **INSIDE** the shape.
  * If you hit an **EVEN** number of walls (0, 2, 4...), you must have started **OUTSIDE** the shape.

### 2\. How This Applies to Your Code (Scanlines)

You are processing your map one row (y-coordinate) at a time. This is called a **Scanline**. When you sort the x-coordinates of the walls for a specific `y`, you get a list like this:
`[2, 5, 10, 15]`

This list represents the **edges** of your walls.

  * **2 to 5:** This is the **1st** interval. 1 is odd. **INSIDE** (Solid).
  * **5 to 10:** This is the **2nd** interval. 2 is even. **OUTSIDE** (Empty Gap).
  * **10 to 15:** This is the **3rd** interval. 3 is odd. **INSIDE** (Solid).

**Your Bug:**
Your previous code connected `2` to `5`, then `5` to `10`, then `10` to `15`. You filled the "outside" gap (5-10) because you didn't respect the Even-Odd rule.

### 3\. The Fix for `create_boundary`

You must process the sorted list in **pairs**. The first number is the *start* of a wall, the second is the *end*. The third is the *start* of the next wall, and so on.

```python
def create_boundary():
    global vertex_dict_y, allowed_tiles_y
    
    for y, l in vertex_dict_y.items():
        l = sorted(list(l)) # e.g., [2, 5, 10, 15]
        allowed_tiles_y[y] = set()
        
        # STEP BY 2: Take indices 0, 2, 4...
        for i in range(0, len(l), 2): 
            # Pair i with i+1 (e.g., 2 with 5, then 10 with 15)
            # CAREFUL: Ensure i+1 exists to avoid index errors
            if i + 1 < len(l):
                start_x = l[i]
                end_x = l[i+1]
                
                # Fill the range between this pair ONLY
                for j in range(start_x, end_x + 1):
                    allowed_tiles_y[y].add(j)
```

**Why this works:**

  * `i=0`: Connects `l[0]` to `l[1]`. (Odd interval: Inside)
  * Loop steps by 2, so `i` becomes 2.
  * `i=2`: Connects `l[2]` to `l[3]`. (Odd interval: Inside)
  * The gap between `l[1]` and `l[2]` is skipped automatically.

This implementation assumes your input polygons are closed and "clean" (every row has an even number of wall edges). If a row has an odd number of edges (e.g., `[2, 5, 10]`), it implies an error in the geometry or a ray grazing a vertex, which requires more complex handling, but for Advent of Code style inputs, the "Pair" assumption usually holds true.

[Scan line polygon filling algorithm](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DS2zX-y94lD4)
The video explains the scan line polygon filling algorithm which uses the even-odd rule to determine which pixels to fill between edges.