/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* prev = nullptr;
    
        while(cur){
            ListNode* tmp = cur;
            // Noticed move cur to cur->next first, otherwise when change tmp->next the cur also changes!
            cur = cur->next;
            tmp->next = prev;            
            prev = tmp;
        }
        return prev;
    }
};