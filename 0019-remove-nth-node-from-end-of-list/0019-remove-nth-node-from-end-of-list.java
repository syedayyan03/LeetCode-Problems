/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = size(head);
        if (n == length) {
            return head.next;
        }
        ListNode temp = head;
        int totalTraverse = length - n;
        int count = 0;
        while(temp != null){
            count++;
            if(count == totalTraverse){
                temp.next = temp.next.next;
                break;
            }
            
            temp = temp.next;
        }
        return head;
    }
    static int size(ListNode head){
        int length = 0;
        ListNode temp = head;
        while(temp != null){
            length += 1;
            temp = temp.next;
        }
        return length;
    }
}