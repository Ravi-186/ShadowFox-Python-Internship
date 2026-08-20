import csv

# 1. Open the CSV file in read mode
with open("student_marks.csv", "r") as file:

    # 2. Create dictionaries from the CSV data
    reader = csv.DictReader(file)

    students = []

    for row in reader:

        # Calculate total marks
        total_marks = (
            int(row["Maths"] or 0) +
            int(row["Physics"] or 0) +
            int(row["Chemistry"] or 0) +
            int(row["English"] or 0) +
            int(row["Biology"] or 0) +
            int(row["Economics"] or 0) +
            int(row["History"] or 0) +
            int(row["Civics"] or 0)
        )

        # 3. Add total_marks field
        row["total_marks"] = total_marks

        # 4. Add Average field
        row["Average"] = total_marks / 8

        # Store the dictionary
        students.append(row)


# 5. Create a new file and write the information
with open("student_marks_updated.csv", "w", newline="") as file:

    # Get all dictionary keys as column names
    fieldnames = students[0].keys()

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write column names
    writer.writeheader()

    # Write all student dictionaries
    writer.writerows(students)


print("Student marks processed successfully!")
print("New file created: student_marks_updated.csv")
