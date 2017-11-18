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
    bool isValidBST(TreeNode* root) {
        
        return isValidRange(root, nullptr, nullptr);
    }
    
    bool isValidRange(TreeNode* cur, TreeNode* minNode, TreeNode* maxNode){
        if (cur == nullptr) return true;
        if (maxNode&&cur->val>=maxNode->val) return false;
        if (minNode&&cur->val<=minNode->val) return false;
        
        bool leftvalid = true;
        bool rightvalid = true;
        if(cur->left){
            leftvalid = isValidRange(cur->left,minNode, cur);
        }
        if(cur->right){
                rightvalid = isValidRange(cur->right, cur, maxNode);
        }
        return leftvalid&&rightvalid;
    }
};