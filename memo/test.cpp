#include "list"
#include "unordered_map"
#include "utility"
using namespace std;

class LRUCache {
  int max;
  list<pair<int, int>> data;
  unordered_map<int, list<pair<int, int>>::iterator> map;

public:
  LRUCache(int size) { max = size; }
  int get(int key) {
    if (map.find(key) == map.end())
      return -1;
    auto pos = map[key];
    data.splice(data.begin(), data, pos);
    return pos->second;
  }
  void put(int key, int value) {
    if (map.find(key) != map.end()) {
      auto pos = map[key];
      pos->second = value;
      data.splice(data.begin(), data, pos);
      return;
    }
    if (data.size() == max) {
      int lastkey = data.back().first;
      map.erase(lastkey);
      data.pop_back();
    }
    data.push_front({key, value});
    map[key] = data.begin();
  }
};
