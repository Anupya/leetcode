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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        // if either list is empty
        if (l1 == NULL) {
            return l2;
        }
        if (l2 == NULL) {
            return l1;
        }
        
        ListNode* result;
        int newVal = l1->val + l2->val;
        int carry = 0;
        
        if (newVal > 9) {
            result = new ListNode(newVal%10);
            carry = 1;
        }
        else {
            result = new ListNode(newVal);  
        }
        
        ListNode* head = result;
        ListNode* p1 = l1->next;
        ListNode* p2 = l2->next;
        
        while ((p1 != NULL) && (p2!=NULL)) {
            int newVal = p1->val + p2->val;
            if ((newVal > 9) && (carry)) {
                result->next = new ListNode((newVal+1) % 10);
                carry = 1;
            }
            else if (newVal > 9) {
                result->next = new ListNode(newVal%10);
                carry = 1;
            }
            else {
                if ((carry) && (newVal < 9)) {
                    newVal++;
                    carry = 0;
                }
                else if ((carry) && (newVal == 9)) {
                    newVal = 0;
                    carry = 1;
                }
                result->next = new ListNode(newVal);  
            }
            result = result->next;
            p1 = p1->next;
            p2 = p2->next;
        }
         
        // if first list is shorter than second list
        if (p1 == NULL) {
            while (p2 != NULL) {
                if ((carry) && (p2->val < 9)) {
                    result->next = new ListNode(p2->val+1);
                    carry = 0;
                }
                else if (carry) {
                    result->next = new ListNode((p2->val+1) %10);
                    carry = 1;
                }
                else {
                    result->next = new ListNode(p2->val);
                }
                p2 = p2->next;
                result = result->next;
            }
        }
             
        // if second list is shorter than first list
        if (p2 == NULL) {
            while (p1 != NULL) {
                if ((carry) && (p1->val < 9)) {
                    result->next = new ListNode(p1->val+1);
                    carry = 0;
                }
                else if (carry) {
                    result->next = new ListNode((p1->val+1) %10);
                    carry = 1;
                }
                else {
                    result->next = new ListNode(p1->val);
                }
                p1 = p1->next;
                result = result->next;
            }
        }
        
        // if same length lists
        if (carry) {
            if (result->next) {
                result->next->val++;
            }
            else {
                result->next = new ListNode(1);
            }
        }
        return head;
    }
};