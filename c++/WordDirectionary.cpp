class TrieNode {
public:
    bool isEnd;
    TrieNode* children[26];

    TrieNode() {
        isEnd = false;
        memset(children, 0, sizeof(children));
    }
};


class WordDictionary {
private:
    TrieNode* root;
    
    bool searchNode(string word, TrieNode* node){
        TrieNode* cur = node;
        int n = word.size();
        for (int i =0; i < n; i ++){
            
            if (cur&&word[i] == '.'){
                for(int j = 0; j < 26; j ++){
                    bool res = searchNode(word.substr(i+1), cur->children[j]);
                    if (res) return true;
                }
                return false;
            }
            else if(cur){
                cur = cur->children[word[i] - 'a'];
            }
            else{
                return false;
            }
            
        }
        return cur&&cur->isEnd;
    }
    
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode* cur = root;
        int n = word.size();
        
        for ( int i = 0; i < n; i ++){
            if (cur->children[word[i] - 'a'] == nullptr){
                cur->children[word[i] - 'a'] = new TrieNode();
            }
            cur = cur->children[word[i] - 'a'];
        }
        cur ->isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return searchNode(word, root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */