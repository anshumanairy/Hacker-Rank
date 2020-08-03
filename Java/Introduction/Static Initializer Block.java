

    Scanner ob=new Scanner(System.in);
    public static int B=0;
    public static int H=0;
    public static boolean flag=false;
    private static int initializeClassVariable() {
        Scanner ob=new Scanner(System.in);
        B=ob.nextInt();
        H=ob.nextInt();
        if(B>0 && H>0){
            flag=true;
        }
        else{
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        return 0;
    }
    public static int myVar = initializeClassVariable();
