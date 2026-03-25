import random

quotes = [
    "Stay consistent.",
    "Discipline beats motivation.",
    "Small steps every day.",
    "Focus on progress, not perfection.",
    "Success is built in silence."
]

while True:
    print("\n1. Get Quote")
    print("2. Add Your Own Quote")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("\nQuote:", random.choice(quotes))

    elif choice == "2":
        new_quote = input("Enter your quote: ")
        quotes.append(new_quote)
        print("Quote added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
