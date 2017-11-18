class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int mx = 0, mxCount = 0;
        vector<int> count(26, 0); 
        for (auto t:tasks){
            count[t - 'A']++;
        }
        sort(count.begin(), count.end());
        mx = count[25];
        for (int i = 0; i < 25; i ++){
            if (count[25-i] == mx){
                mxCount++;
            }
        }
        int taskSlot = (mx - 1) * (n + 1 - mxCount);
        int mxTaskSize = mx * mxCount;
        int taskLeft = tasks.size() - mxTaskSize;
        int extra = std::max(0, taskLeft - taskSlot );
        return mxTaskSize + taskSlot + extra;
    }
};