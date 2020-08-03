

    // Complete the insertNodeAtPosition function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode insertNodeAtPosition(SinglyLinkedListNode head, int data, int position) {
        SinglyLinkedListNode newNode = new SinglyLinkedListNode(data);
        if(head==null){
            head=newNode;
            return head;
        }
        SinglyLinkedListNode current=head;
        SinglyLinkedListNode previous=null;
        int i=0;
        while(i<position){
            previous=current;
            current=current.next;
            if(current==null){
                break;
            }
            i=i+1;
        }
        newNode.next=current;
        previous.next=newNode;
        return head;
    }

