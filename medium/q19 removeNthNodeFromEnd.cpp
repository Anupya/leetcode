/* Given a linked list, remove the n-th node from the end of list and
    return its head.
 
 Given linked list: 1->2->3->4->5, and n = 2.
 After removing the second node from the end, the linked list becomes 1->2->3->5.
 */
 
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 1;
        ListNode* curNode = head;
        
        // PASS 1: Find length of linked list
        while (curNode->next != NULL) {
            curNode = curNode->next;
            len++;
        }
        
        int actualLen = len;
        // PASS 2: Find node to be removed
        cout << len << endl;
        ListNode* nodeRemoved;
        
        // if removing head
        if (actualLen == n) {
            nodeRemoved = head;
            head = nodeRemoved->next;
        }
         
        // if not removing the head
        else {
            curNode = head;
            while (len > (n+1)) {
                curNode = curNode->next;
                len--;
            }

            nodeRemoved = curNode->next;
            ListNode* nodeJoined = curNode->next->next;
            curNode->next = nodeJoined;
            nodeRemoved->next = NULL;
        }

        delete nodeRemoved;
        return head;
    }
};
