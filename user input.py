name = input("How would you like to be adressed?" ) 
print(f"Nice to meet you, {name}.")
your_input = input("Please enter some text: ")
print(your_input)
your_input = input("Please enter some text, starting it with the letter P: ")
if your_input[0].lower() != "p":
    print("This text should start with the letter p.")
print(your_input)
try:
    your_input = input("Please enter some text beginning with the letter p: ")
    if your_input[0].lower() != "p":
        print("This text should start with the letter p.")
except IndexError:
    print("No text entered.")

print(your_input)
need_input = True
while need_input:
    try:
         your_input = input("Please enter some text beginning with the letter p: ")
         if your_input[0].lower() == "p":
            need_input = False
    except IndexError:
        print("No text entered.")
print(your_input)

a = int(input("Think of a number: "))
if a>5:
    print("Wow. That's a big number...")
if a<5:
    print("That's a small number...")
else:
    print("I knew you'd pick 5...")
