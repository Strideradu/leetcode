/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        // preorder print tree
        string result = "";
        result = serializeHelper(root);
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return deserializeHelper(data, pos);
        
    }

private:
    string serializeHelper(TreeNode* root){
        string result = "";
        if (root == nullptr){
            result = "#,";
        }
        else{
            result = to_string(root->val) + ",";
            result += serializeHelper(root->left);
            result += serializeHelper(root->right);
        }  
        return result;
        
    }
    
    TreeNode* deserializeHelper(string& data,int& pos){
        if (pos < data.size() && data[pos] == '#'){
            pos += 2;
            return nullptr;
        }
        else{
            int sep_pos = data.find(',', pos);
            int val = stoi(data.substr(pos, sep_pos - pos));
            TreeNode* root = new TreeNode(val);
            pos += sep_pos - pos + 1;
            root->left = deserializeHelper(data, pos);
            root->right = deserializeHelper(data, pos);
            return root;
        }
        
    }

};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));