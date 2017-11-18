/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        buildStack(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !(st.empty());
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* top = st.top();
        st.pop();
        buildStack(top->right);
        return top->val;
    }
private:
    
    void buildStack(TreeNode* root){
        if (root!=nullptr){
            st.push(root);
            buildStack(root->left);
        }
       
    }
    
    stack<TreeNode*> st;
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */