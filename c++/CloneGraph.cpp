/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        map<UndirectedGraphNode*, UndirectedGraphNode*> nodes;
        if (node == nullptr) return nullptr;
        UndirectedGraphNode* copy = new UndirectedGraphNode(node -> label);
        nodes[node] = copy;
        queue<UndirectedGraphNode*> q;
        q.push(node);
        while(!q.empty()){
            UndirectedGraphNode* cur = q.front();
            q.pop();
            //int n = cur->neighbors.size();
            for (auto neighbor :cur->neighbors ){
                if (nodes.find(neighbor)== nodes.end()){
                    UndirectedGraphNode* neigh_copy = new UndirectedGraphNode(neighbor -> label);
                    nodes[neighbor] = neigh_copy;
                    q.push(neighbor);
                }
                nodes[cur]->neighbors.push_back(nodes[neighbor]);
            }
        }
        
        return copy;
    }
};