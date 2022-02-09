import random
#Part A
weeks = 16
print("weeks, integer")
classes = 5
print("classes, integer")
tuition = 6000
print("tuition, integer")
classes_per_week = classes * 3
print("classes_per_week, float")
cost_per_week = ((tuition / classes) / weeks)
print("cost_per_week, float")
print("Cost per week:", cost_per_week)
cost_per_class = cost_per_week / classes_per_week
print("This is how much is being payed per class: ", cost_per_class)
print("cost_per_class, float")


#Part B
mylist = [70, "Grey", 5.5, "Michelle", "Water"]
mylist_rand = random.choice(mylist)
print(mylist_rand)