

    // Complete the reversePrint function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static void reversePrint(SinglyLinkedListNode head) {

        if(head==null || head.next==null){
        }
        SinglyLinkedListNode previous=null;
        SinglyLinkedListNode current=head;
        SinglyLinkedListNode next=null;
        while(current!=null){
            next=current.next;
            current.next=previous;
            previous=current;
            current=next;
        }

        while(previous!=null){
            System.out.println(previous.data);
            previous=previous.next;
        }
    }

