class Solution {
    public ListNode middleNode(ListNode head) {
        int length = size(head);
        ListNode temp = head;
        ListNode dummy = new ListNode(0);

        if(length % 2 == 0){
            for(int i = 0; i < length/2; i++){
                temp = temp.next;
            }
            dummy.next = temp;
        }
        else{
            for(int i = 0; i < length/2; i++){
                temp = temp.next;
            }
            dummy.next = temp;
        }

        return dummy.next;
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