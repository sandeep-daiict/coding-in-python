
// Java Program to print Bottom View of Binary Tree
import java.util.LinkedList;
import java.util.Queue;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.HashMap;
import java.io.*;
import java.util.*;
 
// Tree node class
class Node
{
    int data; //data of the node
    int hd; //horizontal distance of the node
    Node left, right; //left and right references
 
    // Constructor of tree node
    public Node(int key)
    {
        data = key;
        hd = Integer.MAX_VALUE;
        left = right = null;
    }
}
 
	
class BottomView
{
	// driver function to test the above functions
    public static void main(String args[])
    {
		
        // Input the number of test cases you want to run
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
		//Node root=null;
        while (t > 0)
        {
            HashMap<Integer, Node> m = new HashMap<Integer, Node> ();
            int n = sc.nextInt();
            Node root=null;
            while (n > 0)
            {
                int n1 = sc.nextInt();
                int n2 = sc.nextInt();
                char lr = sc.next().charAt(0);
                //  cout << n1 << " " << n2 << " " << (char)lr << endl;
                Node parent = m.get(n1);
                if (parent == null)
                {
                    parent = new Node(n1);
                    m.put(n1, parent);
                    if (root == null)
                        root = parent;
                }
                Node child = new Node(n2);
                if (lr == 'L')
                    parent.left = child;
                else
                    parent.right = child;
                m.put(n2, child);
                n--;
            }
		
            GfG g = new GfG();
            
			//g.leftView(root);
			g.bottomView(root);
			
			System.out.println();
         t--;			
        }
    }
}

}

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* Tree node class
class Node {
    int data; //data of the node
    int hd; //horizontal distance of the node
    Node left, right; //left and right references
    public Node(int key)
    {
        data = key;
        hd = Integer.MAX_VALUE;
        left = right = null;
    }
}*/
class GfG
{
    // Should print bottom view of tree with given root
    TreeMap<Integer, Integer> map = new TreeMap<>();
    public void bottomView(Node root)
    {
        // Your code here
        bottomViewUtil(root, 0);
        for(Map.Entry<Integer,Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            System.out.print(value + " ");
        }
    }
    public void bottomViewUtil(Node root, int val)
    {
        if(root==null)
            {return;}
        map.put( val, root.data);
        if(root.left !=null)
            {bottomViewUtil( root.left, val - 1);}
        if(root.right !=null)
            {bottomViewUtil( root.right, val + 1);}
        
    }
}
