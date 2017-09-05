/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
  public:
    ListNode *oddEvenList(ListNode *head)
    {
        if (!head)
        {
            return NULL;
        }
        ListNode *odd = head;
        ListNode *even_first = head->next;
        ListNode *even = head->next;
        while (even != NULL && even->next != NULL)
        {
            odd->next = odd->next->next;
            even->next = even->next->next;
            odd = odd->next;
            even = even->next;
        }
        odd->next = even_first;

        return head;
    }
};