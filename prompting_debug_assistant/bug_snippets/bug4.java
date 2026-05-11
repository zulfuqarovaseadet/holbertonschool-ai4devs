import java.util.ArrayList;
import java.util.List;

public class UserRegistration {
    private String username;
    private Integer age;
    private String role;
    private List<String> permissions;

    public UserRegistration(String username, Integer age, String role) {
        this.username = username;
        this.age = age;
        this.role = role;
        this.permissions = new ArrayList<>();
    }

    public void setupPermissions() {
        // Bug 1: String comparison with '==' instead of .equals()
        if (this.role == "ADMIN") {
            permissions.add("DELETE_USER");
            permissions.add("VIEW_REPORTS");
        } else {
            permissions.add("VIEW_SELF");
        }
    }

    public void validateProfile() {
        System.out.println("Checking profile for: " + username.toUpperCase());

        // Bug 2: NullPointerException 
        // If age is null (from constructor), .intValue() will crash the program
        if (this.age.intValue() < 13) {
            System.out.println("Error: User too young for social features.");
        } else if (this.age > 100) {
            System.out.println("Error: Invalid age provided.");
        }
    }

    public void displayDashboard() {
        System.out.println("--- User Dashboard ---");
        
        // Bug 3: IndexOutOfBoundsException
        // Trying to access an index that doesn't exist if permissions is empty
        System.out.println("Primary Permission: " + permissions.get(0));

        // Bug 4: Logical loop error
        for (int i = 0; i <= permissions.size(); i++) {
            System.out.println("Access level " + i + ": " + permissions.get(i));
        }
    }

    public static void main(String[] args) {
        // We create a user with NULL age to trigger Bug 2
        UserRegistration user1 = new UserRegistration("zulfugar_99", null, "ADMIN");

        try {
            // This might crash because setupPermissions uses '==' 
            // and role might not match "ADMIN" correctly in memory
            user1.setupPermissions(); 
            user1.validateProfile();
            user1.displayDashboard();
        } catch (Exception e) {
            System.out.println("CRITICAL SYSTEM ERROR: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
