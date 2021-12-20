### 2D Array

```
char[][] board = new char[3][3];

for (int i = 0; i < 3; i++)
{
  for (int j = 0; j < 3; j++)
  {
    board[i][j] = '-';
  }
}

System.out.println(Arrays.deepToString(board));
```
Because it's a 2D Array we use deepToString instead of toString

returns:

[[-, -, -], [-, -, -], [-, -, -]]

