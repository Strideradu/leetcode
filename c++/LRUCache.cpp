class LRUCache {
private:
    // A list of (key, value) pairs
    list<pair<int, int>> items;
    // Map items to iterators (pointers) to list nodes
    unordered_map<int, list<pair<int, int>>::iterator> cache;
    // The capacity of the list
    int capacity;

public:
    LRUCache(int capacity) : capacity(capacity) {}

    int get(int key) {
        // If key is not found in hash map, return -1
        if (cache.find(key) == cache.end())
            return -1;
        // Move the (key, value) pair to the beginning of the list
        // splice will move the cache[key] position in items to items.begin
        items.splice(items.begin(), items, cache[key]);
        return cache[key]->second;
    }

    void put(int key, int value) {
        // The key is not in the hash table
        if (cache.find(key) == cache.end()) {
            // If the cache is full then delete the least recently
            // used item, which is at the end of the list
            if (items.size() == capacity) {
                cache.erase(items.back().first);
                items.pop_back();
            }
            items.push_front(make_pair(key, value));
            cache[key] = items.begin();
        } 
        else {
            // Update the value associated with the key
            cache[key]->second = value;
            // Move the (key, value) pair to the beginning of the list
            items.splice(items.begin(), items, cache[key]);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */