// https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie {
 private:
  class TrieNode {
   public:
    TrieNode* children[26];
    bool isWord;
    TrieNode() {
      for (int i = 0; i < 26; i++) {
        children[i] = NULL;
      }
      isWord = false;
    }
  };

  TrieNode* root;

 public:
  /** Initialize your data structure here. */
  Trie() { root = new TrieNode(); }

  /** Inserts a word into the trie. */
  void insert(string word) {
    TrieNode* node = root;
    for (int i = 0; i < word.size(); i++) {
      int idx = word[i] - 'a';
      if (node->children[idx] == NULL) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->isWord = true;
  }

  /** Returns if the word is in the trie. */
  bool search(string word) {
    TrieNode* node = root;
    for (int i = 0; i < word.size(); i++) {
      int idx = word[i] - 'a';
      if (node->children[idx] == NULL) {
        return false;
      }
      node = node->children[idx];
    }
    return node->isWord;
  }

  /** Returns if there is any word in the trie that starts with the given
   * prefix. */
  bool startsWith(string prefix) {
    TrieNode* node = root;
    for (int i = 0; i < prefix.size(); i++) {
      int idx = prefix[i] - 'a';
      if (node->children[idx] == NULL) {
        return false;
      }
      node = node->children[idx];
    }
    return true;
  }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */