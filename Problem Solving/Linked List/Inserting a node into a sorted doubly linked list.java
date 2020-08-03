

    // Complete the sortedInsert function below.

    /*
     * For your reference:
     *
     * DoublyLinkedListNode {
     *     int data;
     *     DoublyLinkedListNode next;
     *     DoublyLinkedListNode prev;
     * }
     *
     */
    static DoublyLinkedListNode sortedInsert(DoublyLinkedListNode head, int data) {
        DoublyLinkedListNode current=head;
        DoublyLinkedListNode newNode= new DoublyLinkedListNode(data);
        if(data<=head.data){
            current.prev=newNode;
            newNode.next=current;
            newNode.prev=null;
            return newNode;
        }
        while (current.next != null && current.next.data < newNode.data)  
            current = current.next; 

        newNode.next = current.next; 

        if (current.next != null)  
            newNode.next.prev = newNode;  

        current.next = newNode;  
        newNode.prev = current;
        return head;
    }

