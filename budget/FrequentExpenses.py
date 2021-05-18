
import collections
import matplotlib.pyplot as plt
from budget.Expense import *


expenses = Expenses()
expenses.read_expenses("c:\Tasks365_New\ML\pyworks\python-collections-budget\data\spending_data.csv")

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
categories, count = zip(*top5)
fig, ax = plt.subplots()  #initialize
ax.bar(categories, count)
ax.set_title("# of purchases by category")
plt.show()

