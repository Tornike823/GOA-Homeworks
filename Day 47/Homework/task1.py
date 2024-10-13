"""სიტყვის რიცხვი ტექსტში
შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში."""

def word_count(text):
   
    words = text.split()
    return len(words)


text = "baro"
print(word_count(text))