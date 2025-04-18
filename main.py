from pet import Pet

# Create a pet
my_pet = Pet("Buddy")
# Check initial status
my_pet.get_status()

# Perform some actions
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.get_status()

# Bonus: Training
my_pet.train("roll over")
my_pet.train("fetch")
my_pet.train("sit")
my_pet.show_tricks()

# Play again to see energy go down
my_pet.play()
my_pet.get_status()
