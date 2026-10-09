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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (left == right) return head;
        return partition(head, left, right);
    }

    ListNode partition(ListNode head, int left, int right) {
        ListNode partition1 = head;
        ListNode partition2 = head;
        ListNode temp = head;
        ListNode before = null;

        for (int i = 1; i < right; i++) {
            partition2 = partition2.next;
        }

        temp = partition2.next;
        partition2.next = null;
        partition2 = temp;

        temp = head;

        for (int i = 1; i < left; i++) {
            before = temp;
            temp = temp.next;
        }

        partition1 = temp;

        ListNode reversed = rev(partition1);

        if (before != null) {
            before.next = reversed;
        } else {
            head = reversed;
        }

        partition1.next = partition2;

        return head;
    }

    ListNode rev(ListNode partition) {
        ListNode prev = null;
        ListNode curr = partition;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
