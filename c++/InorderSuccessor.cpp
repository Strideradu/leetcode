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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* cur = root;
        TreeNode* r = nullptr;
        while(cur!=nullptr){
            if (p->val==cur->val){
                if (cur->right){
                    cur = cur->right;
                    while(cur->left){
                        cur =cur->left;
                    }
                    return cur;
                }
                else if (r!= nullptr){
                    return r;
                }
                else{
                    return nullptr;
                }
            }
            else if (p->val>cur->val){
                cur =cur->right;
            }
            else{
                r = cur;
                cur = cur->left;
            }
        }
        return nullptr;
    }
};