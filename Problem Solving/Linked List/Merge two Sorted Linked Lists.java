

    // Complete the mergeLists function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode mergeLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        if(head1==null && head2==null){
            return null;
        }
        if(head1==null){
            return head2;
        }
        if(head2==null){
            return head1;
        }
        // SinglyLinkedListNode current1=head1;
        // SinglyLinkedListNode current2=head1;
        // while(current1.next!=null){
        //     current1=current1.next;
        // }
        // current1.next=head2;
        if(head1.data<=head2.data){
            head1.next=mergeLists(head1.next,head2);
        }else{
            SinglyLinkedListNode temp=head2;
            head2=head2.next;
            temp.next=head1;
            head1=temp;
            head1.next=mergeLists(head1.next,head2);
        }
        return head1;
    }

