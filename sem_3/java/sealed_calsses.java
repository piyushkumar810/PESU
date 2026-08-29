/*
// ============================================================
// SEALED CLASSES IN JAVA
// ============================================================

// A sealed class restricts which classes can inherit from it.
//
// It was finalized in Java 17.
//
// Syntax:
//
// sealed class Parent permits Child1, Child2 {
// }


// ============================================================
// 1. BASIC EXAMPLE
// ============================================================

sealed class Animal permits Dog, Cat {
}

// Only Dog and Cat are allowed to extend Animal.

final class Dog extends Animal {
}

final class Cat extends Animal {
}


// ============================================================
// 2. 'permits' KEYWORD
// ============================================================

// 'permits' specifies which classes are allowed to extend
// or implement the sealed class/interface.
//
// Example:

sealed class Vehicle permits Car, Bike {
}

final class Car extends Vehicle {
}

final class Bike extends Vehicle {
}


// ============================================================
// 3. SUBCLASSES MUST DECLARE THEIR STATUS
// ============================================================

// A direct subclass of a sealed class MUST be one of:
//
// 1. final
// 2. sealed
// 3. non-sealed


// ---------------- final ----------------

// final means nobody can extend the class further.

sealed class Shape permits Circle {
}

final class Circle extends Shape {
}


// ---------------- sealed ----------------

// sealed allows controlled further inheritance.

sealed class A permits B {
}

sealed class B extends A permits C {
}

final class C extends B {
}


// ---------------- non-sealed ----------------

// non-sealed removes the inheritance restriction.
//
// Any class can extend a non-sealed class.

sealed class Parent permits Child {
}

non-sealed class Child extends Parent {
}

// Now other classes can extend Child.

class GrandChild extends Child {
}


// ============================================================
// 4. SEALED INTERFACE
// ============================================================

// Interfaces can also be sealed.

sealed interface Payment permits CreditCard, UPI {
}

final class CreditCard implements Payment {
}

final class UPI implements Payment {
}


// ============================================================
// 5. IMPORTANT RULE
// ============================================================

// A class mentioned in 'permits' must directly extend
// the sealed class or implement the sealed interface.
//
// Example:
//
// sealed class Animal permits Dog { }
//
// final class Dog extends Animal { }
//
// VALID


// ============================================================
// 6. WHY SEALED CLASSES?
// ============================================================

// Sealed classes provide controlled inheritance.
//
// They are useful when you know exactly which classes
// are allowed to be subclasses.
//
// Example:
//
// sealed class Payment permits UPI, CreditCard, Cash {
// }


// ============================================================
// 7. SEALED vs FINAL vs NON-SEALED
// ============================================================

// final:
//     No class can extend it.
//
// sealed:
//     Only permitted classes can extend it.
//
// non-sealed:
//     Removes inheritance restrictions for that subclass.
//
//
// final    → No inheritance
// sealed   → Restricted inheritance
// non-sealed → Open inheritance
*/