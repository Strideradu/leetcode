class Solution
{
  public:
    int numIslands(vector<vector<char>> &grid)
    {
        if (grid.size() == 0 || grid[0].size() == 0)
        {
            return 0;
        }

        int count = 0;

        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == '1')
                {
                    count += 1;
                    DFS(grid, i, j);
                }
            }
        }

        return count;
    }

    void DFS(vector<vector<char>> &grid, int x, int y)
    {
        grid[x][y] = '0';
        if (x > 0 && grid[x - 1][y] == '1')
        {
            DFS(grid, x - 1, y);
        }
        if (x < grid.size() - 1 && grid[x + 1][y] == '1')
        {
            DFS(grid, x + 1, y);
        }
        if (y > 0 && grid[x][y - 1] == '1')
        {
            DFS(grid, x, y - 1);
        }
        if (y < grid[0].size() - 1 && grid[x][y + 1] == '1')
        {
            DFS(grid, x, y + 1);
        }
    }
};