

    // Complete the getNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static int getNode(SinglyLinkedListNode head, int positionFromTail) {
        int i=0;
        SinglyLinkedListNode current=head;
        SinglyLinkedListNode parse=head;
        while(current!=null){
            current=current.next;
            if(i++>positionFromTail){
                parse=parse.next;
            }
        }
        return(parse.data);
    }

