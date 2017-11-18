/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        map<int, vector<int>> m;
        int off = 0;
        // need use BFS, other wise cannot make sure the upper levle node will appear fierst
        queue<pair<TreeNode *, int>> q;        
        vector<vector<int>> output;
        
        q.push(make_pair(root, 0));
        
        while (!q.empty()){
            TreeNode * curr = q.front().first;
            int pos = q.front().second;
            q.pop();
            
            if (curr == nullptr){
                continue;
            }
            
            m[pos].push_back(curr->val);
            q.push(make_pair(curr->left, pos-1));
            q.push(make_pair(curr->right, pos+1));
        }
                    
        for(auto v : m){
            output.push_back(v.second);
        }
        return output;
    }
};