

	/* 
    
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static void levelOrder(Node root) {
      if(root==null){
          return;
      }
      Queue<Node> q = new LinkedList<>(); 
      q.add(root); 
      q.add(null); 
      while(!q.isEmpty()){
        Node curr = q.poll(); 
        if (curr == null) { 
            if (!q.isEmpty()) { 
                q.add(null); 
            } 
        } else { 
            if (curr.left != null) 
                q.add(curr.left); 
    
            if (curr.right != null) 
                q.add(curr.right); 
    
            System.out.print(curr.data+" "); 
        }
      }
    }

