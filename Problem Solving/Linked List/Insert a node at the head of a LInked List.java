static SinglyLinkedListNode insertNodeAtHead(SinglyLinkedListNode llist, int data) {
        SinglyLinkedListNode newNode=new SinglyLinkedListNode(data);
        if(llist==null){
            llist=newNode;
            return llist;
        }
        else{
            newNode.next=llist;
            return newNode;
        }
    }