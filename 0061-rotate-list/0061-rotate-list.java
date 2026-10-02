class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null) return head;

        int len = size(head);
        k = k % len;

        if(k == 0) return head;

        ListNode temp = head;
        int pos = len - k;
        ListNode tail = head;

        while(tail.next != null){
            tail = tail.next;
        }

        for(int i = 1; i < pos; i++){
            temp = temp.next;
        }

        tail.next = head;
        head = temp.next;
        temp.next = null;

        return head;
    }

    static int size(ListNode head){
        ListNode temp = head;
        int len = 0;
        while(temp != null){
            len++;
            temp = temp.next;
        }
        return len;
    }
}