// https://leetcode.com/problems/implement-trie-prefix-tree/

type Trie struct {
    children [26]*Trie
    isWord bool
}


/** Initialize your data structure here. */
func Constructor() Trie {
    return Trie{}
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
    node := this
    for _, v := range word {
        idx := v-'a'
        if node.children[idx] == nil {
            node.children[idx] = &Trie{}
        }
        node = node.children[idx]
    }
    node.isWord = true
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    node := this
    for _, v := range word {
        idx := v-'a'
        if node.children[idx] == nil {
            return false
        }
        node = node.children[idx]
    }
    return node.isWord
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    node := this
    for _, v := range prefix {
        idx := v-'a'
        if node.children[idx] == nil {
            return false
        }
        node = node.children[idx]
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */