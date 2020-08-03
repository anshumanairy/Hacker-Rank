

    // Complete the removeDuplicates function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode removeDuplicates(SinglyLinkedListNode head) {

        SinglyLinkedListNode current = head;
        while(current.next!=null){
            if(current.data==current.next.data){
                SinglyLinkedListNode temp=current.next;
                current.next=current.next.next;
                temp=null;
            }
            else{
                current=current.next;
            }
        }
        return head;
    }

