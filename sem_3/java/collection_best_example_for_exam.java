// 🏆 ONE CODE TO REMEMBER FOR EXAM
// If you remember only one general-purpose collection program, remember this:

import java.util.*;

class collection_best_example_for_exam {

    public static void main(String[] args) {

        // =========================
        // ARRAYLIST
        // =========================
        ArrayList<Integer> list = new ArrayList<>();

        list.add(10);
        list.add(20);
        list.add(30);

        System.out.println("ArrayList: " + list);
        System.out.println("First: " + list.get(0));


        // =========================
        // HASHSET
        // =========================
        HashSet<Integer> set = new HashSet<>();

        set.add(10);
        set.add(20);
        set.add(10);       // Duplicate ignored

        System.out.println("HashSet: " + set);


        // =========================
        // TREESET
        // =========================
        TreeSet<Integer> tree = new TreeSet<>();

        tree.add(30);
        tree.add(10);
        tree.add(20);

        System.out.println("TreeSet: " + tree);


        // =========================
        // HASHMAP
        // =========================
        HashMap<String, Integer> map = new HashMap<>();

        map.put("Java", 90);
        map.put("Python", 85);
        map.put("SQL", 95);

        System.out.println("Java marks: " + map.get("Java"));

        for (Map.Entry<String, Integer> entry
                : map.entrySet()) {

            System.out.println(
                entry.getKey() + " = " + entry.getValue()
            );
        }


        // =========================
        // PRIORITY QUEUE
        // =========================
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.add(30);
        pq.add(10);
        pq.add(20);

        System.out.println("Smallest: " + pq.peek());
        System.out.println("Removed: " + pq.poll());


        // =========================
        // COLLECTIONS METHODS
        // =========================
        Collections.sort(list);

        System.out.println("Sorted: " + list);
        System.out.println("Maximum: " + Collections.max(list));
        System.out.println("Minimum: " + Collections.min(list));
    }
}