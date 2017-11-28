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
    // If the current (sub)tree contains both p and q, then the function result is their LCA. 
    // If only one of them is in that subtree, then the result is that one of them. 
    // If neither are in that subtree, the result is null/None/nil.
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) return root;
        TreeNode* r = lowestCommonAncestor(root->right, p, q);
        TreeNode* l = lowestCommonAncestor(root->left, p, q);
        if (l&&r){
            return root;
        }
        else {
            if (l) return l;
            else if (r) return r;
            else return nullptr;
        }
    }
};