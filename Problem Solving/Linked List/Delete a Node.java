

    // Complete the deleteNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode deleteNode(SinglyLinkedListNode head, int position) {
        SinglyLinkedListNode current=head;
        SinglyLinkedListNode previous=null;
        if(position==0){
            head=head.next;
            return head;
        }
        else
        {
            int i=0;
            while(i<position){
                previous=current;
                current=current.next;
                i=i+1;
            }
            previous.next=current.next;
            current=null;
        }
        return head;
    }

