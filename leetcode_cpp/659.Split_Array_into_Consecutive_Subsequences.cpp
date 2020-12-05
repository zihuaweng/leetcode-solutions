// has valid prev path
// 1 X 2 X X 3 [4]  X X 5 X X X 6
// It is safe to link with 123, so as 5, 6.
// The gist is to link as many number as possible

// do not have valid prev path
// 1 X 2 X X 3 [5]  X X 6 X X X 7
// 5 can only link to numbers behind. return false if 6 or 7 is absent

// 1 1 2 2 2 3 3 4
// seq[3] = 3
// add 4:
// seq[3] -= 1
// seq[4] += 1

class Solution {
 public:
  bool isPossible(vector<int>& nums) {
    // key: number, val: count of seqs end with key
    unordered_map<int, int> seq;
    // key: number, val: count of key
    unordered_map<int, int> count;  

    for (auto x : nums) count[x] += 1;

    for (auto x : nums) {
      if (count[x] == 0) continue;
      if (seq[x - 1] > 0) {
        seq[x - 1] -= 1;
        seq[x] += 1;
        count[x] -= 1;
      } else {
        if (count[x + 1] == 0 || count[x + 2] == 0) return false;

        count[x] -= 1;
        count[x + 1] -= 1;
        count[x + 2] -= 1;
        seq[x + 2] += 1;
      }
    }

    return true;
  }
};