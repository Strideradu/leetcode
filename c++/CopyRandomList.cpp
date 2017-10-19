/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution
{
  public:
    RandomListNode *copyRandomList(RandomListNode *head)
    {
        RandomListNode *cur = head;
        RandomListNode *next;
        while (cur)
        {
            next = cur->next;
            cur->next = new RandomListNode(cur->label);
            cur->next->next = next;
            cur = next;
        }

        cur = head;
        while (cur)
        {
            if (cur->random)
            {
                cur->next->random = cur->random->next;
            }

            cur = cur->next->next;
        }

        cur = head;
        RandomListNode *head_cp = new RandomListNode(0);
        RandomListNode *cur_cp = head_cp;
        while (cur)
        {
            next = cur->next->next;
            cur_cp->next = cur->next;
            cur_cp = cur->next;
            cur->next = next;
            cur = cur->next;
        }

        return head_cp->next;
    }
};