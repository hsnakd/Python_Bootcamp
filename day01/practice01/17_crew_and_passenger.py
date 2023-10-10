"""

17. Create a python file named crew_and_passenger,
    Given a number of people on the ship, determine how many need to be crew members and how many can be passengers.
    Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""

total_people = int(input("Enter the total number of people on the ship: "))

if total_people == 50 or total_people == 75 or total_people == 100:
    if total_people == 50:
        num_crew = 20
        num_passengers = 30
    elif total_people == 75:
        num_crew = 25
        num_passengers = 50
    elif total_people == 100:
        num_crew = 30
        num_passengers = 70
    print(f"Total: {total_people} ===> {num_crew} crew, {num_passengers} passengers")
else:
    print('Any other number of people on the ship is not valid')

