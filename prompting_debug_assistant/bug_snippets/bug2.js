import java.util.ArrayList;

public class InventoryManager {
    public static void main(String[] args) {
        ArrayList<Integer> prices = new ArrayList<>();
        prices.add(15);
        prices.add(25);
        prices.add(35);

        int total = 0;
        for (int i = 0; i <= prices.size(); i++) {
            total += prices.get(i);
        }

        double average = total / prices.size();

        if (average > 20) {
            System.out.println("Orta qiymət yüksəkdir: " + average);
        } else if (average = 20) {
            System.out.println("Orta qiymət tamdır.");
        }

        String message = null;
        System.out.println(message.toUpperCase());
    }
}
