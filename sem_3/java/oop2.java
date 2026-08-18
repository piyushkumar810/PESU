class OOP2 {

    public static void main(String[] args) {

        // Creating objects
        Dog d1 = new Dog("Tommy", 5, "Labrador");
        Dog d2 = new Dog("Rocky", 3, "German Shepherd");

        // Display objects
        d1.display1();
        d2.display2();

        // Using setter
        d1.setAge(6);

        System.out.println("\nAfter changing Tommy's age:");
        d1.display1();
    }
}


class Dog {

    // Private data members
    private String name;
    private int age;
    private String breed;

    // Constructor
    Dog(String name, int age, String breed) {
        this.name = name;
        this.age = age;
        this.breed = breed;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for age
    public int getAge() {
        return age;
    }

    // Setter for age
    public void setAge(int age) {
        this.age = age;
    }

    // Getter for breed
    public String getBreed() {
        return breed;
    }

    // Setter for breed
    public void setBreed(String breed) {
        this.breed = breed;
    }

    // Display method for first object
    public void display1() {
        System.out.println("Dog 1");
        System.out.println("Name  : " + getName());
        System.out.println("Age   : " + getAge());
        System.out.println("Breed : " + getBreed());
    }

    // Display method for second object
    public void display2() {
        System.out.println("\nDog 2");
        System.out.println("Name  : " + getName());
        System.out.println("Age   : " + getAge());
        System.out.println("Breed : " + getBreed());
    }
}