

    // Complete the compareLists function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static boolean compareLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {

        SinglyLinkedListNode current1 = head1;
        SinglyLinkedListNode current2 = head2;
        int check=1;
        while(current1!=null || current2!=null){
            if(current1.data!=current2.data){
                check=0;
            }
            current1=current1.next;
            current2=current2.next;
            if(current1==null && current2!=null){
                check=0;
                break;
            }
            if(current1!=null && current2==null){
                check=0;
                break;
            }
            if(current1==null && current2==null){
                break;
            }
        }
        if(check==0){
            return false;
        }else{
            return true;
        }
    }

