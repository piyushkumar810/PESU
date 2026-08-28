// class wrapper{
//     public static void main(String[] args) {
//         Object x="a";
//         System.out.println(x.getClass().getName());
//         Integer a=5,b=10;
//         System.out.println(a+b);
//     }
// }



/*
class wrapper{
    public static void main(String[] args) {
        Integer a=5,b=5;
        System.out.println(a==b);  // True
    }
}

class wrapper{
    public static void main(String[] args) {
        Integer a=500,b=500;
        System.out.println(a==b);   // false  ,because of cached integer object
    }
}   


class wrapper{
    public static void main(String[] args) {
        Integer a=128,b=128;
        System.out.println(a.equals(b));
    }
}
*/


class wrapper{
    public static void main(String[] args) {
        Integer a=10;  //autobox
        int b =a+20; //unbox
        System.out.println(b);
    }
}