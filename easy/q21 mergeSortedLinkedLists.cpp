/*

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        ListNode* newList;
        
        if (l1 == NULL) {
            newList = l2;
            return newList;
        }
        else if (l2 == NULL) {
            newList = l1;
            return newList;
        }
        
        else if (l1->val < l2->val) {
            newList = new ListNode(l1->val);
            l1 = l1->next;
        }
        else {
            newList = new ListNode(l2->val);
            l2 = l2->next;
        }
        
        ListNode* head = newList;
        
        while ((l1 != NULL) && (l2 != NULL)) {
            
            if (l1->val < l2->val)  {
                cout << "l1 is smaller" << endl;
                newList->next = new ListNode(l1->val);
                l1 = l1->next;
            }
 
            else {
                cout << "l2 is smaller" << endl;
                newList->next = new ListNode(l2->val);
                l2 = l2->next;
            } 
            
            newList = newList->next;
        }
        
        if (l1 == NULL) {
            while (l2 != NULL) {
                newList->next = new ListNode(l2->val);
                newList = newList->next;
                l2 = l2->next;
            }
        }
        else {
            while (l1 != NULL) {
                newList->next = new ListNode(l1->val);
                newList = newList->next;
                l1 = l1->next;
            }
        }
        
        return head;
    }
};