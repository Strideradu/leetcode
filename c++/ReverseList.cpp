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
        ListNode* last= NULL;
        while(head) {
            ListNode* cur = head;
            head = head->next;
            cur -> next = last;
            last = cur;
        }
        return last;
    }
};