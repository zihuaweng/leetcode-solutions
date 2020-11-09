package com.leetcode;

// https://leetcode.com/problems/integer-to-english-words/
// 273. Integer to English Words


class Solution {
    private final String[] to19 = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private final String[] tens = {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private final String[] upper = {"Thousand", "Million", "Billion"};

    public String numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }
        return String.join(" ", words(num));
    }

    private String words(int n) {
        if (n < 20) {
            return to19[n - 1];
        }
        if (n < 100) {
            if (n % 10 == 0) {
                return tens[n / 10 - 2];
            } else {
                return tens[n / 10 - 2] + " " + words(n % 10);
            }
        }
        if (n < 1000) {
            if (n % 100 == 0) {
                return to19[n / 100 - 1] + " Hundred";
            } else {
                return to19[n / 100 - 1] + " Hundred " + words(n % 100);
            }
        }
        for (int i = 1; i <= upper.length; i++) {
            if (n < Math.pow(1000, i + 1)) {
                int temp1 = (int) Math.pow(1000, i);
                if (n % temp1 == 0) {
                    return words(n / temp1) + " " + upper[i - 1];
                } else {
                    return words(n / temp1) + " " + upper[i - 1] + " " + words(n % temp1);
                }
            }
        }
        return "";
    }
}
