""" შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.
"""

def age_category(age):
    if age < 0:
        return "ასაკი არასწორია"
    elif age <= 12:
        return "ბავშვი"
    elif age <= 17:
        return "თინეიჯერი"
    elif age <= 64:
        return "ზრდასრული"
    else:
        return "ხანდაზმული"

age_category(12)