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
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> starts, ends;
        for (auto interval: intervals){
            starts.push_back(interval.start);
            ends.push_back(interval.end);
        }
        sort(starts.begin(),starts.end());
        sort(ends.begin(),ends.end());
        int e = 0;
        int rooms = 0;
        int available = 0;
        int room = 0;
        for (auto start:starts){
            
            while(ends[e] <= start){
                e++;
                available++;
            }
            if (available > 0){
                available--;
            }
            else{
                room++;
            }
        }
        return room;
    }
};