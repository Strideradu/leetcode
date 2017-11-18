/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
    stack<NestedInteger> nl;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        int n = nestedList.size();
        for (int i =n-1; i >= 0; i--){
            nl.push(nestedList[i]);
        }
    }

    int next() {
        int result = nl.top().getInteger();
        nl.pop();
        return result;
    }

    bool hasNext() {
        while(!nl.empty()){
            NestedInteger curr = nl.top();
            if (curr.isInteger()){
                return true;
            }
            nl.pop();
            
            vector<NestedInteger> & newList = curr.getList();
            int n = newList.size();
            for (int i =n-1; i >= 0; i--){
                nl.push(newList[i]);
            }
            
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */