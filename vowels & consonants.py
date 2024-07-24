def count_vowels(string):
    
    vowels = ["a", "e", "i", "o", "u"]

    count = 0

    for i in string:
        if i in vowels: 
            count += 1

        return(f"your name has {count} vowels")

string = input("Enter your name: ")

print(count_vowels(string))