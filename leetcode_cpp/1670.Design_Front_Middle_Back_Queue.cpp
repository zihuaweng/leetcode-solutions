// Method 1:
// If there is not much number, we can use vector
// time O(n)

class FrontMiddleBackQueue {
  vector<int> q;

 public:
  FrontMiddleBackQueue() {}

  void pushFront(int val) { q.insert(q.begin(), val); }

  void pushMiddle(int val) { q.insert(q.begin() + q.size() / 2, val); }

  void pushBack(int val) { q.push_back(val); }

  int popFront() {
    if (q.empty()) return -1;
    int res = q.front();
    q.erase(q.begin());
    return res;
  }

  int popMiddle() {
    if (q.empty()) return -1;
    int res = q[(q.size() - 1) / 2];
    q.erase(q.begin() + (q.size() - 1) / 2);
    return res;
  }

  int popBack() {
    if (q.empty()) return -1;
    int res = q.back();
    q.pop_back();
    return res;
  }
};

// method 2 linked list
// time O(1)
class FrontMiddleBackQueue {
  list<int> l;
  list<int>::iterator mid;
  int n = 0;

 public:
  FrontMiddleBackQueue() {}

  // O X O O -> Y O X O O, mid -> X
  // O X O -> Y O X O, mid -> X--
  // empty -> O, mid -> O
  void pushFront(int val) {
    l.push_front(val);
    if (n == 0)
      mid = l.begin();
    else if (n % 2 == 1)
      mid--;
    n++;
  }

  // O X O O -> O X Y O O, mid -> Y
  // O X O -> O Y X O, mid -> Y
  // empty -> O, mid -> O
  void pushMiddle(int val) {
    if (n == 0) {
      l.push_back(val);
      mid = l.begin();
    } else if (n % 2 == 0) {
      l.insert(next(mid), val);
      mid++;
    } else {
      l.insert(mid, val);
      mid--;
    }

    n++;
  }

  // O X O O -> O X O O Y, mid -> X++
  // O X O -> O X O Y, mid -> X
  // empty -> O, mid -> O
  void pushBack(int val) {
    l.push_back(val);
    if (n == 0)
      mid = l.begin();
    else if (n % 2 == 0)
      mid++;
    n++;
  }

  // O X O O -> X O O, mid -> X++
  // O X O -> X O, mid -> X
  // empty -> return -1
  int popFront() {
    if (n == 0) return -1;
    int res = l.front();
    if (n % 2 == 0) mid++;
    l.pop_front();
    n--;
    return res;
  }

  // O X O O -> O O O, mid -> X++
  // O X O -> O O, mid -> X--
  // empty -> O, return -1
  int popMiddle() {
    if (n == 0) return -1;
    int res = *mid;
    list<int>::iterator new_mid;
    if (n % 2 == 0)
      new_mid = next(mid);
    else
      new_mid = prev(mid);
    l.erase(mid);
    mid = new_mid;
    n--;
    return res;
  }

  // O X O O -> O X O, mid -> X
  // O X O -> O X, mid -> X--
  // empty -> O, return -1
  int popBack() {
    if (n == 0) return -1;
    int res = l.back();
    if (n % 2 == 1) mid--;
    l.pop_back();
    n--;
    return res;
  }
};