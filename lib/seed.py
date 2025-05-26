#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie, session, reset_database

# Reset and seed the database
reset_database()

# Create companies
google = Company(name="Google", founding_year=1998)
amazon = Company(name="Amazon", founding_year=1994)

# Create developers
annie = Dev(name="Annie")
faith = Dev(name="Faith")
charlie = Dev(name="Charlie")

# Add all to session
session.add_all([google, amazon, annie, faith, charlie])
session.commit()

# Create freebies
f1 = Freebie(item_name="T-shirt", value=20, company=google, dev=annie)
f2 = Freebie(item_name="Sticker", value=5, company=google, dev=faith)
f3 = Freebie(item_name="Mug", value=15, company=amazon, dev=annie)
f4 = Freebie(item_name="Backpack", value=50, company=amazon, dev=charlie)

session.add_all([f1, f2, f3, f4])
session.commit()

# ---- Optional: test methods directly here ----
print("Companies for Annie:", [c.name for c in annie.companies])
print("Does Annie have a Mug?", annie.received_one("Mug"))
print("Oldest company:", Company.oldest_company().name)

# Give a new freebie
google.give_freebie(faith, "Laptop Sleeve", 30)

# Print all freebies
print("\nFreebie Details:")
for freebie in session.query(Freebie).all():
    print(freebie.print_details())

# Test give_away
print("\nTesting give_away...")
mug = session.query(Freebie).filter_by(item_name="Mug").first()
annie.give_away(faith, mug)

print("After giveaway, Bob has:", [f.item_name for f in faith.freebies])

