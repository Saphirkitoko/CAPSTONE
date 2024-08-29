# Asking the user how many classes they are taking this semester
num_classes = int(input("How many classes are you taking this semester? "))

# Initializing an empty list to store the class names
classes = []

# Loop to get the class names
for i in range(num_classes):
    class_name = input(f"Enter the name of class #{i+1}: ")
    classes.append(class_name)

# Printing the list of classes
print("\nHere are the classes you are taking this semester:")
for class_name in classes:
    print(f"- {class_name}")