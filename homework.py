print("    Welcome to Holiday Planner!     ")

print("Step 1: Pick your holiday type")
print("  1 - Beach Holiday")
print("  2 - snowy Holiday")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    print("Step 2: Pick your beach activity")
    print("  1 - Snorkeling")
    print("  2 - Sandcastle Building")
    print()
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked  : Snorkeling")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Sandcastle Building")
        print("Best time   : Evening")
        print("Remember    : Carry a bucket and shovel")
 
elif choice==2:
    print("Step 2: Pick your snowy activity")
    print("  1 - skiing")
    print("  2 - sledding")
    print()
 
    mountain_activity = int(input("Enter 1 or 2: "))
    print()
 
    if mountain_activity == 1:
        print("You picked  : skiing")
        print("Best for    : going around fast")
        print("Remember    : Wear skiing shoes")
    else:
        print("You picked  : sledding")
        print("Best for    : having fun")
        print("Remember    : Carry a sled")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday or 2 for Mountain Holiday.")
 

print("   Your holiday plan is ready!      ")
print("   Enjoy your trip!                 ")
