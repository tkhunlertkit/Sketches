import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class StringCount {

    private static List<String> strings = new ArrayList<>();
    private static HashMap<String, Integer> hms = new HashMap<>();

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String input;
        do {
            System.out.print("Enter a phrase: ");
            input = s.nextLine();
            if (!input.equalsIgnoreCase("quit")) {
                int count = countUsingArrayList(input);
                System.out.println(input + " has count of " + count + " return from ArrayList count");
                count = countUsingHashMap(input);
                System.out.println(input + " has count of " + count + " return from HashMap");
            }
        } while (!input.equalsIgnoreCase("quit"));
        s.close();
    }

    private static int countUsingHashMap(String input) {
        input = input.toLowerCase();
        if (hms.containsKey(input)) {
            hms.put(input, hms.get(input) + 1);
        } else {
            hms.put(input, 1);
        }

        return hms.get(input);
    }

    private static int countUsingArrayList(String input) {
        strings.add(input.toLowerCase());
        int count = 0;
        for (String str : strings) {
            if (str.equalsIgnoreCase(input))
                count++;
        }
        return count;
    }
}
