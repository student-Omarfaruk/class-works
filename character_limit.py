name= input("Enter your name: ")
if len(name)<5:
    print('name must be more than 5 character.')
elif len(name)>50:
    print("name shouldn't more than 50 character")
else:
    print('its a good name')