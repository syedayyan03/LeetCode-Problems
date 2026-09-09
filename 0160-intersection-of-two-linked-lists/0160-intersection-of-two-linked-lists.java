public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        int n = size(headA);
        int m = size(headB);

        ListNode h1 = headA;
        ListNode h2 = headB;
        if (m > n) {
            for (int i = 0; i < m - n; i++) {
                h2 = h2.next;
            }
        } 
        else {
            for (int i = 0; i < n - m; i++) {
                h1 = h1.next;
            }
        }

        while (h1 != h2) {
            h1 = h1.next;
            h2 = h2.next;
        }

        return h1;
    }

    static int size(ListNode head) {
        ListNode temp = head;
        int count = 0;

        while (temp != null) {
            count++;
            temp = temp.next;
        }

        return count;
    }
}