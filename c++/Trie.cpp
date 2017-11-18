class TrieNode {
public:
    bool isEnd;
    TrieNode* children[26];

    TrieNode() {
        isEnd = false;
        memset(children, 0, sizeof(children));
    }
};


class Trie {
private:
    TrieNode* root;
    
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* curr = root;
        for(int i=0; i<word.size(); i++) {
            int id = word[i] - 'a';
            if(curr->children[id]==nullptr) {
                curr->children[id] = new TrieNode();
            }
            curr = curr->children[id];
        }
        curr->isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* curr = root;
        int i=0, n = word.size();
        while(i<n) {
            int id = word[i] - 'a';
            curr=curr->children[id];
            if(curr == nullptr) return false;
            
            i++;
        }
        return curr->isEnd;
}
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        int i=0, n = prefix.size();
        while(i<n) {
            int id = prefix[i] - 'a';
            curr=curr->children[id];
            if(curr == nullptr) return false;
            
            i++;
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */