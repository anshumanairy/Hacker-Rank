

    // Complete the findMergeNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static int findMergeNode(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        SinglyLinkedListNode current1=head1;
        SinglyLinkedListNode current2=head2;
        while(current1!=null){
            while(current2!=null){
                if(current1==current2){
                    return current1.data;
                }
                current2=current2.next;
            }
            current1=current1.next;
            current2=head2;
        }
    return 0;
    }

