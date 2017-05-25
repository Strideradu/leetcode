class MinStack {
private:
    vector<int> q;
    vector<int> min;
public:
    void push(int x) {
        q.push_back(x);
        if(min.size()==0)
            min.push_back(x);
        else
        {
            int curMin = getMin();
            if(x<curMin)
                curMin = x;
            min.push_back(curMin);
        }
    }

    void pop() {
        q.pop_back();
        min.pop_back();
    }

    int top() {
        return q.back();
    }

    int getMin() {
        return min.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */