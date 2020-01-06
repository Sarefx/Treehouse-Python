my_name = "Ashley"
for letter in my_name:
    print(letter)

groceries = ["beef","cucumbers","lettuce"]

index = 1
for item in groceries:
    print(f'{index}. {item}')
    index+=1

for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')


