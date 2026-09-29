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
    public ListNode reverseList(ListNode head) {

        // Long Process

        // int size = listSize(head);
        // if (size == 0) return null;

        // int[] arr = new int[size];
        // ListNode temp = head;
        // int k = 0;

        // while (temp != null) {
        //     arr[k++] = temp.val;
        //     temp = temp.next;
        // }

        // for (int i = 0; i < size / 2; i++) {
        //     int temp1 = arr[i];
        //     arr[i] = arr[size - i - 1];
        //     arr[size - i - 1] = temp1;
        // }

        // ListNode ans = new ListNode(arr[0]);
        // ListNode current = ans;

        // for (int i = 1; i < size; i++) {
        //     current.next = new ListNode(arr[i]);
        //     current = current.next;
        // }

        // return ans;

        // Optimal
        ListNode curr = head;
        ListNode prev = null;

        while(curr != null){
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    // Long Process
    // public static int listSize(ListNode head) {
    //     ListNode temp = head;
    //     int count = 0;

    //     while (temp != null) {
    //         count += 1;
    //         temp = temp.next;
    //     }

    //     return count;
    // }
}