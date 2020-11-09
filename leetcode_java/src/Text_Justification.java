package com.leetcode;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        List<String> temp = new ArrayList<>();
        int wordLength = 0;
        for (String w: words) {
            if (wordLength + w.length() + temp.size() <= maxWidth) {
                temp.add(w);
                wordLength += w.length();
            } else {
                int space = maxWidth - wordLength;
                int length = (temp.size() > 1)? temp.size()-1 : 1;
                for (int i=0; i<space; i++) {
                    int idx = i % length;
                    temp.set(idx, temp.get(idx) + " ");
                }
                res.add(String.join("", temp));
                temp = new ArrayList<String>();
                temp.add(w);
                wordLength = w.length();
            }
        }
        res.add(String.format("%-" + maxWidth + "s", String.join(" ", temp)));

        return res;
    }
}
