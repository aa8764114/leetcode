/*
 * @lc app=leetcode id=146 lang=cpp
 */
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// @lc code=start
class LRUCache {
public:
    LRUCache(int capacity) {
        
    }
    
    int get(int key) {
        
    }
    
    void put(int key, int value) {
        
    }
};
// @lc code=end

int main() {
    cout << "Testing LRUCache..." << endl;
    // Example 1 從題目來的測試流程
    LRUCache lRUCache(2);
    lRUCache.put(1, 1); // 快取是 {1=1}
    lRUCache.put(2, 2); // 快取是 {1=1, 2=2}
    int res1 = lRUCache.get(1);    // 回傳 1
    cout << "get(1): " << res1 << " | Expected: 1 | " << (res1 == 1 ? "✅ PASS" : "❌ FAIL") << endl;
    lRUCache.put(3, 3); // 該操作會使得關鍵字 2 作廢，快取是 {1=1, 3=3}
    int res2 = lRUCache.get(2);    // 回傳 -1 (未找到)
    cout << "get(2): " << res2 << " | Expected: -1 | " << (res2 == -1 ? "✅ PASS" : "❌ FAIL") << endl;
    lRUCache.put(4, 4); // 該操作會使得關鍵字 1 作廢，快取是 {4=4, 3=3}
    int res3 = lRUCache.get(1);    // 回傳 -1 (未找到)
    cout << "get(1): " << res3 << " | Expected: -1 | " << (res3 == -1 ? "✅ PASS" : "❌ FAIL") << endl;
    return 0;
}
