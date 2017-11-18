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
    bool canAttendMeetings(vector<Interval>& intervals) {
        int n = intervals.size();
        if (n == 0) return true;
        
        sort(intervals.begin(), intervals.end(), compare);
        for (int i = 0; i < n-1; i ++){
            if (intervals[i].end > intervals[i+1].start){
                return false;
            }
        }
        return true;
    }
    
private:
    // must have static for used by sort?
    static bool compare(Interval& iv1, Interval& iv2){
        return iv1.start < iv2.start;
    }
};