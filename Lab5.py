# Online Food Ordering System

def display_menu(category, items):
    print(f"\n{category} Menu:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item['name']} - Rs {item['price']}")

def main():
    # Food items with prices
    starters = [
        {"name": "Paneer Tikka", "price": 250},
        {"name": "Chicken Wings", "price": 300},
        {"name": "Spring Rolls", "price": 200},
    ]

    main_course = [
        {"name": "Butter Chicken", "price": 400},
        {"name": "Paneer Butter Masala", "price": 350},
        {"name": "Veg Biryani", "price": 300},
    ]

    desserts = [
        {"name": "Gulab Jamun", "price": 150},
        {"name": "Ice Cream", "price": 200},
        {"name": "Brownie", "price": 250},
    ]

    total_bill = 0

    while True:
        print("\nWhat would you like to order?")
        print("1. Starters")
        print("2. Main Course")
        print("3. Desserts")

        try:
            category_choice = int(input("Enter your choice (1-3): "))

            if category_choice == 1:
                display_menu("Starters", starters)
                items = starters
            elif category_choice == 2:
                display_menu("Main Course", main_course)
                items = main_course
            elif category_choice == 3:
                display_menu("Desserts", desserts)
                items = desserts
            else:
                print("Invalid choice. Please try again.")
                continue

            item_choice = int(input("Select an item number: "))

            if 1 <= item_choice <= len(items):
                selected_item = items[item_choice - 1]
                total_bill += selected_item['price']
                print(f"You added {selected_item['name']} to your order. Current bill: Rs {total_bill}")
            else:
                print("Invalid item number. Please try again.")
                continue

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        more = input("Would you like to order more? (yes/no): ").strip().lower()
        if more == 'no':
            break

    print(f"\nYour final bill amount is: Rs {total_bill}")
    print("Thank you for ordering with us!")

if __name__ == "__main__":
    main()