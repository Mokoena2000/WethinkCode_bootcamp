def count_words(my_string):
    return(f"your string has {count} words")

my_string = "hsnsdnnd"

count = 0

for char in my_string:
    count +=1 

print(count_words(my_string))