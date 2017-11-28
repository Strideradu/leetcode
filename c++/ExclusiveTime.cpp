struct Log {
    int id;
    string status;
    int timestamp;
};

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> result(n, 0);
        stack<Log> st;
        for (string log: logs){
            stringstream ss(log);
            string temp, temp2, temp3;
            getline(ss, temp, ':');
            getline(ss, temp2, ':');
            getline(ss, temp3, ':');
            
            Log item = {stoi(temp), temp2, stoi(temp3)};
            if(item.status == "start") {
                st.push(item);
            }
            else{
                int time_added = item.timestamp - st.top().timestamp + 1;
                result[item.id] += time_added;
                st.pop();
                
                if(!st.empty()) {
                    result[st.top().id] -= time_added;
                }
            }
        }
        
        return result;
    }
};