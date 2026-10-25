import collections

class ExpenseAgent:
    def __init__(self):
        # Define keywords for automatic categorization, simulating the agent's 'learning'
        self.category_keywords = {
            "Food": ["coffee", "restaurant", "groceries", "supermarket", "lunch", "dinner", "breakfast"],
            "Transport": ["bus", "train", "taxi", "uber", "fuel", "gas", "subway"],
            "Entertainment": ["movie", "concert", "game", "bar", "club", "streaming"],
            "Utilities": ["rent", "electricity", "water", "internet", "phone bill"],
            "Shopping": ["clothes", "shoes", "electronics", "book", "store"],
            "Health": ["pharmacy", "doctor", "hospital", "gym"]
        }
        self.expenses = []

    def add_expense(self, description, amount):
        """Adds an expense and attempts to categorize it, mimicking the agent's data intake and initial processing."""
        category = "Uncategorized"
        description_lower = description.lower()
        for cat, keywords in self.category_keywords.items():
            if any(keyword in description_lower for keyword in keywords):
                category = cat
                break
        self.expenses.append({"description": description, "amount": amount, "category": category})
        print(f"Added: {description} (${amount:.2f}) -> Category: {category}") # Agent's immediate feedback

    def analyze_spending(self):
        """Analyzes total spending per category, simulating the agent's analytical capabilities."""
        category_totals = collections.defaultdict(float)
        total_spending = 0.0
        for expense in self.expenses:
            category_totals[expense["category"]] += expense["amount"]
            total_spending += expense["amount"]

        print("\n--- Spending Analysis ---")
        if not self.expenses:
            print("No expenses to analyze yet.")
            return {}, 0.0

        for category, total in sorted(category_totals.items()):
            percentage = (total / total_spending) * 100 if total_spending > 0 else 0
            print(f"{category}: ${total:.2f} ({percentage:.1f}%)")
        print(f"Total Spending: ${total_spending:.2f}")
        return category_totals, total_spending

    def generate_recommendations(self, category_totals, total_spending):
        """Generates smart agent recommendations based on spending patterns, providing 'guidance'."""
        print("\n--- Smart Agent Recommendations ---")
        if not category_totals:
            print("Add some expenses to get recommendations!")
            return

        high_spending_threshold_percent = 25 # If a category exceeds this, it's flagged for review
        high_spending_categories = []

        for category, total in category_totals.items():
            percentage = (total / total_spending) * 100 if total_spending > 0 else 0
            if percentage > high_spending_threshold_percent:
                high_spending_categories.append((category, percentage))

        if high_spending_categories:
            high_spending_categories.sort(key=lambda x: x[1], reverse=True)
            print(f"💡 Alert: You are spending a significant amount in '{high_spending_categories[0][0]}' ({high_spending_categories[0][1]:.1f}% of total).")
            print(f"Consider reviewing your '{high_spending_categories[0][0]}' habits to find potential savings.")
        else:
            print("Your spending seems well-distributed. Keep up the good work!")

        # Example of a specific recommendation based on a common high-spend item
        if any("coffee" in e["description"].lower() for e in self.expenses) and category_totals.get("Food", 0) > 50:
             print("☕ Tip: Frequent coffee purchases can add up. Try making coffee at home a few days a week.")

        if category_totals.get("Entertainment", 0) > 100:
            print("🎉 Suggestion: Look for free or low-cost entertainment options this month to balance your budget.")

        if category_totals.get("Uncategorized", 0) > 0:
            print("❓ Action: You have uncategorized expenses. Providing more detailed descriptions can help the agent learn better!")


# --- Main execution ---
if __name__ == "__main__":
    print("Orcha: Your Smart Expense Agent Simulation")
    agent = ExpenseAgent()

    # Simulate adding expenses for the agent to process
    print("\n--- Scenario 1: Diverse Spending ---")
    agent.add_expense("Morning coffee at Starbucks", 5.50)
    agent.add_expense("Groceries from local supermarket", 75.20)
    agent.add_expense("Monthly internet bill", 60.00)
    agent.add_expense("Dinner at Italian restaurant", 45.00)
    agent.add_expense("Bus ticket", 2.75)
    agent.add_expense("New book from Amazon", 18.99)
    agent.add_expense("Movie tickets for two", 24.00)
    agent.add_expense("Gym membership", 35.00)
    agent.add_expense("Lunch with colleagues", 15.00)
    agent.add_expense("Taxi ride home", 12.50)
    agent.add_expense("Concert tickets", 80.00) # High entertainment expense

    # Agent analyzes and provides insights
    category_totals, total_spending = agent.analyze_spending()

    # Agent generates personalized recommendations
    agent.generate_recommendations(category_totals, total_spending)

    print("\n--- Scenario 2: High Shopping & Utilities ---")
    agent_v2 = ExpenseAgent()
    agent_v2.add_expense("Rent payment", 1200.00)
    agent_v2.add_expense("Electricity bill", 80.00)
    agent_v2.add_expense("Weekly groceries", 120.00)
    agent_v2.add_expense("New laptop from electronics store", 900.00) # High shopping expense
    agent_v2.add_expense("Dinner out", 60.00)
    agent_v2.add_expense("Bus fare", 3.00)

    category_totals_v2, total_spending_v2 = agent_v2.analyze_spending()
    agent_v2.generate_recommendations(category_totals_v2, total_spending_v2)
