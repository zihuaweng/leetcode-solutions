// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
  boolean isWord;
  TrieNode[] children = new TrieNode[26];
}

class Trie {
  private TrieNode trie;

  /** Initialize your data structure here. */
  public Trie() {
    this.trie = new TrieNode();
  }

  /** Inserts a word into the trie. */
  public void insert(String word) {
    TrieNode node = trie;
    for (int i = 0; i < word.length(); i++) {
      int j = word.charAt(i) - 'a';
      if (node.children[j] == null) {
        node.children[j] = new TrieNode();
      }
      node = node.children[j];
    }
    node.isWord = true;
  }

  /** Returns if the word is in the trie. */
  public boolean search(String word) {
    TrieNode node = trie;
    for (int i = 0; i < word.length(); i++) {
      int j = word.charAt(i) - 'a';
      if (node.children[j] == null) {
        return false;
      }
      node = node.children[j];
    }
    return node.isWord;
  }

  /**
   * Returns if there is any word in the trie that starts with the given prefix.
   */
  public boolean startsWith(String prefix) {
    TrieNode node = trie;
    for (int i = 0; i < prefix.length(); i++) {
      int j = prefix.charAt(i) - 'a';
      if (node.children[j] == null) {
        return false;
      }
      node = node.children[j];
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such: Trie obj = new
 * Trie(); obj.insert(word); boolean param_2 = obj.search(word); boolean param_3
 * = obj.startsWith(prefix);
 */