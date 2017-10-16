class Solution
{
  public:
    unordered_map<int, string> u;
    const string base = "http://tinyurl.com/";

    // Encodes a URL to a shortened URL.
    string encode(string longUrl)
    {
        int hashCode = hash<string>()(longUrl);
        u.insert({hashCode, longUrl});
        return base + to_string(hashCode);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl)
    {
        int hashCode = stoi(shortUrl.substr(19));
        return u[hashCode];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));