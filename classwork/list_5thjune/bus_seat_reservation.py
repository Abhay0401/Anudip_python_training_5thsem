seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# 1. Count booked and available seats
booked_seats = seats.count(1)
available_seats = seats.count(0)

# 2. Find the first available seat
first_available = -1
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1  # Seat numbers start from 1
        break

# 3. Create a list of all available seat numbers
available_seat_numbers = []
for i in range(len(seats)):
    if seats[i] == 0:
        available_seat_numbers.append(i + 1)

# 4. Determine whether the bus is more than 70% occupied
occupancy = (booked_seats / len(seats)) * 100

print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", int(occupancy), "%")

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
