import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner ob=new Scanner(System.in);
        int i=1;
        while(ob.hasNext()){
            String str = ob.nextLine();
            System.out.println(i+" "+str);
            i+=1;
        }
    }
}
