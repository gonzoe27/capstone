list_classes = []

amount_of_classes = int(input("How many classes are you taking this semester?: "))


while len(list_classes) < amount_of_classes:
    class_name = input("What is the name of your class?: ")
    list_classes.append(class_name)

for class_name in list_classes:
    print(class_name)
    