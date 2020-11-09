//Calculate the an % b where a, b and n are all 32bit non-negative integers.
// https://www.youtube.com/watch?v=EHUgNLN8F1Y

public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        if (n == 0) {
            return 1%b;
        }
        if (n == 1) {
            return a%b;
        }
        long power = fastPower(a, b, n/2);
        power = (power*power) % b;
        if (n % 2 == 1) {
            power = (power*a) % b;
        }
        return (int) power;
    }
}