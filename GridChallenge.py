def gridChallenge(grid):
    ans = []
    temp = ''
    text = ''
    for i in range(t):
        for j in range(0, n):
            grid[j] = sorted(grid[j])
            grid[j] = "".join(grid[j])

    for x in range(n):
        column = []
        for y in grid:
            column.append(y[x])

        text = "".join(column)
        sorted_text = sorted(text)
        sorted_text = "".join(sorted_text)

        if text == sorted_text:
            ans.append("YES")
        else:
            ans.append("NO")

    if "NO" in ans:
        print("NO")
    else:
        print("YES")

t = int(input())

for t_itr in range(t):
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    gridChallenge(grid)