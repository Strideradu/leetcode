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
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        intervals.push_back(newInterval);
        sort(intervals.begin(), intervals.end(), compare);
        int n = intervals.size();
        vector<Interval> result;
        result.push_back(intervals[0]);
        bool inserted = false;
        for (int i = 1; i < n; i ++){
            if (intervals[i].start<=result.back().end){
                result.back().end = max(intervals[i].end, result.back().end);
            }
            else{
                result.push_back(intervals[i]);
            }
            
        }
        return result;
    }
    
    static bool compare(Interval iv1, Interval iv2){
        return iv1.start<iv2.start;
    }
};