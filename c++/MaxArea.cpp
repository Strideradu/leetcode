class Solution
{
  public:
    int maxArea(vector<int> &height)
    {
        int area = 0;
        int i = 0, j = height.size() - 1;
        while (i < j)
        {
            int h = min(height[i], height[j]);
            area = max(area, h * (j - i));
            while (height[j] <= h && i < j)
                j--;
            while (height[i] <= h && i < j)
                i++;
        }

        return area;
    }
};