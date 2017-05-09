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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode root(0), *cur = &root;
        int extra = 0;
        while (l1 || l2 || extra) {
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + extra;
            extra = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
			// if l1 has value, then l1 = l1->next else keep l1(no value)
			l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return root.next;
    }
};