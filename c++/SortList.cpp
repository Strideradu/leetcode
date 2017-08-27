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
    ListNode *sortList(ListNode *head)
    {
        if (head == NULL || head->next == NULL)
            return head;

        ListNode *slow = head;
        ListNode *fast = head->next;

        while (fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        // slow is at the center of list, then divide

        fast = slow->next;
        slow->next = NULL;

        return merge(sortList(head), sortList(fast));
    }

    ListNode *merge(ListNode *l1, ListNode *l2)
    {
        ListNode head = ListNode(0);
        ListNode *cur = &head;

        while (l1 != NULL && l2 != NULL)
        {
            if (l1->val < l2->val)
            {
                cur->next = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                l2 = l2->next;
            }

            cur = cur->next;
        }

        cur->next = l1 ? l1 : l2;

        return head.next;
    }
};