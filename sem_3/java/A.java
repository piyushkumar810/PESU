// public class A {
//     public static void main(String[] args) {
//         System.out.println("this is my mmfirst java program");
//     } 
// }
// A a=new A()
// a.main()

public class A {

    public static void main(String[] args) {

        System.out.println("This is my first Java program");

        A a = new A();
        a.display();
    }

    void display() {
        System.out.println("Hello from display method");
    }
}