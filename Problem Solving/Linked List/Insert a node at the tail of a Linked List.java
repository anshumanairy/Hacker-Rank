

    // Complete the insertNodeAtTail function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
        SinglyLinkedListNode newNode = new SinglyLinkedListNode(data);

        if(head==null){
            head=newNode;
            return head;
        }
        SinglyLinkedListNode current=head;
        while(current.next!=null){
            current=current.next;
        }
        current.next=newNode;
        return head;
    }

