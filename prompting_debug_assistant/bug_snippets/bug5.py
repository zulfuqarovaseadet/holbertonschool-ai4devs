import time

class StoreSystem:
    def __init__(self):
        self.inventory = {
            "Laptop": 1200,
            "Smartphone": 800,
            "Headphones": 150,
            "Monitor": 300
        }
        self.categories = {
            "Laptop": "Electronics",
            "Smartphone": "Electronics",
            "Headphones": "Accessories"
        }

    def apply_discount(self, product, discount_map):
        print(f"Checking discount for {product}...")
        # Bug 1: KeyError - 'Monitor' is not in self.categories
        category = self.categories[product]
        rate = discount_map.get(category, 0)
        return self.inventory[product] * (1 - rate)

    def process_checkout(self, cart):
        print("\n--- Checkout Started ---")
        for item in cart:
            if item in self.inventory:
                price = self.inventory[item]
                if price > 500:
                    # Bug 2: UnboundLocalError (variable scope)
                    promo_msg = "Premium Discount!"
                print(f"Item: {item} | Status: {promo_msg}")

    def validate_shipping(self, total):
        # Bug 3: Logical Error (using '=' instead of '==')
        if total = 0:
            return "Empty"
        return "Shipped"

if __name__ == "__main__":
    store = StoreSystem()
    try:
        store.apply_discount("Monitor", {"Electronics": 0.1})
    except Exception as e:
        print(f"Error 1: {e}")
    
    try:
        store.process_checkout(["Headphones", "Laptop"])
    except Exception as e:
        print(f"Error 2: {e}")
