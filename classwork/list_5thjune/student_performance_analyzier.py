# vidyarthiyon ke marks ki list
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# paas hone wale vidyarthiyon ke marks rakhne ke liye khaali list
passed_students = []

# fail students ki ginti rakhne ke liye variable
failed_count = 0

# shuruaat me pehle mark ko highest maan liya
highest = marks[0]

# shuruaat me pehle mark ko lowest maan liya
lowest = marks[0]

# 75 se jyada marks wale students ke liye khaali list
merit_list = []

# list ke har mark par loop chalega
for mark in marks:

    # agar marks 40 ya usse jyada hain to student pass hai
    if mark >= 40:
        # pass student ke marks list me add karo
        passed_students.append(mark)
    else:
        # warna fail students ki ginti 1 badha do
        failed_count += 1

    # agar current mark highest se bada hai
    if mark > highest:
        # highest ko update kar do
        highest = mark

    # agar current mark lowest se chhota hai
    if mark < lowest:
        # lowest ko update kar do
        lowest = mark

    # agar marks 75 se jyada hain
    if mark > 75:
        # merit list me add kar do
        merit_list.append(mark)

# pass students ki list print karo
print("Passed Students:", passed_students)

# fail students ki sankhya print karo
print("Failed Count:", failed_count)

# sabse adhik marks print karo
print("Highest Marks:", highest)

# sabse kam marks print karo
print("Lowest Marks:", lowest)

# merit list print karo
print("Merit List:", merit_list)
