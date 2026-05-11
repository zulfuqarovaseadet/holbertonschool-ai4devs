class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_history = [100, -50, 200]

    def display_transactions(self):
        print(f"Hörmətli {self.owner}, son əməliyyatlar:")
        for i in range(len(self.transaction_history) + 1):
            print(f"Əməliyyat {i+1}: {self.transaction_history[i]} AZN")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Balans artırıldı: {amount} AZN")
            print("Yeni balans: " + self.balance)
        else:
            print("Məbləğ düzgün deyil.")

    def withdraw(self, amount):
        print(f"Çıxarılacaq məbləğ: {amount}")
        
        limit = 500
        if amount > "500":
            print("Xəta: Gündəlik limit aşıldı.")
            is_over_limit = True

        if is_over_limit:
            print("Əməliyyat rədd edildi.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print("Vəsait çıxarıldı.")

    def calculate_interest(self, months):
        print("Faiz hesabı aparılır...")
        print("Müştəri məlumatları yoxlanılır...")
        print("Mərkəzi bankla əlaqə qurulur...")
        
        interest_rate = 0.05
        if months > 0:
            total_interest = self.balance * interest_rate * months
        
        print("Gözlənilən faiz gəliri: " + total_interest)

    def close_account(self):
        confirm = "Bəli"
        if confirm = "Bəli":
            print("Hesab uğurla bağlandı.")
        
        print("Sistem mesajı: Çıxış edilir...")
        print("Loglar yadda saxlanılır...")
        print("Sessiya bitdi.")
        return True

user_acc = BankAccount("Zülfüqar", 1000)
user_acc.display_transactions()
user_acc.deposit(50)
user_acc.withdraw(100)
user_acc.calculate_interest(12)
user_acc.close_account()
