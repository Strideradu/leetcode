/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        int n = intervals.size();
        vector<Interval> res;
        if (n == 0) return res;
        vector<int> starts, ends;
        for (int i = 0; i < n; i ++){
            starts.push_back(intervals[i].start);
            ends.push_back(intervals[i].end);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        res.push_back(Interval(starts[0], ends[0]));
        for (int i = 1; i < n; i++){
            if (res.back().end < starts[i]){
                res.push_back(Interval(starts[i], ends[i]));
            }
            else{
                res.back().end = ends[i];
            }
        }
        
        return res;
    }
};