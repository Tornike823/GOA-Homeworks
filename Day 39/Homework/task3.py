"""3)შექმენით ფუნქცია is_even(num), რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი, თუ ლუწია, აბრუნებს True, სხვა შემთხვევაში False."""

def is_even(num):
    if num == num[::-1]:
        print(True)
    else:
        print(False)
    is_even(10)
