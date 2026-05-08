function greetUser(name) {
    console.log("Hello, " + name.toUpperCase() + "!");
}

// Test case with null (causes bug)
greetUser(null);
