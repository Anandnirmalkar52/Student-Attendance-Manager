# Student Attendance Manager

A menu-driven console application in Python 3 to add students, mark daily attendance as present or absent, view each student's attendance percentage, and list the students below the 75% requirement. All data is saved in a text file.

**University:** Rungta International Skills University
**School:** School of Computer Science and Engineering
**Course:** Bachelor of Technology, Computer Science and Engineering

---

## What I Used

| Item | Details |
|------|---------|
| Language | Python 3 |
| Libraries | None. Only built-in Python features, so nothing needs to be installed |
| Concepts | Lists, Dictionaries, Functions, File Handling |
| Interface | Console (terminal) menu |
| Storage | Plain text file `attendance.txt` |
| Code size | One file: `student_attendance_manager.py` |

### How each concept is used

- **List:** all students are kept in one list called `student_list`.
- **Dictionary:** each student is a dictionary with the keys `roll`, `name`, `held`, `attended`.
- **Functions:** each feature is its own function (`add_new_student`, `mark_student_attendance`, `show_student_percentage`, `show_shortage_list`), plus helpers (`find_student_by_roll`, `calculate_percentage`, `load_students_from_file`, `save_students_to_file`).
- **File handling:** data is read from `attendance.txt` when the program starts and written back after every change.

---

## Features

1. **Add student:** enter a roll number and a name. The roll number must be unique.
2. **Mark attendance:** enter a roll number and a status (`P` for present, `A` for absent).
3. **Percentage:** shows the attendance percentage of one student.
4. **Shortage list:** shows students below 75% and students who meet the requirement.
0. **Exit:** closes the program.

### Rules and validation

- Minimum required attendance is **75%**. Exactly 75% meets the requirement.
- Percentage = attended / held x 100.
- If no classes are held, the percentage is shown as 0.00% (no division by zero).
- An unknown roll number gives an error message.
- Any status other than P or A is rejected.
- Duplicate roll numbers and empty names or rolls are rejected.

---

## How to Run

1. Install Python 3 from python.org if you do not have it.
2. Put `student_attendance_manager.py` in a folder.
3. Open a terminal in that folder and run:

```
python student_attendance_manager.py
```

The file `attendance.txt` is created in the same folder when you add your first student. Always run the program from the same folder so it finds the same data file.

---

## Data File Format

`attendance.txt` stores one student per line, with fields separated by `|`:

```
roll|name|held|attended
```

Example:

```
101|Aman|4|3
102|Riya|4|2
```

---

## Test Cases

| # | Input | Expected output |
|---|-------|-----------------|
| 1. Normal input | Option 1, Roll `101`, Name `Aman` | `Student added: 101 \| Aman \| Held: 0 \| Attended: 0` |
| 2. Boundary input | Option 3, Roll `101` (no classes held) | `Aman: Attendance 0.00% (no classes held yet)` |
| 3a. Invalid roll | Option 2, Roll `999` | `Roll number 999 not found.` |
| 3b. Invalid status | Option 2, Roll `101`, Status `X` | `Invalid status. Enter P or A.` |
| 4. Different valid scenario | Records: 101 Aman (4 held, 3 attended), 102 Riya (4 held, 2 attended). Option 4 | `Below 75%: 102 \| Riya \| 50.00%` and `Aman (75.00%) meets the requirement.` |

The test cases run in order on the same records.

---

## Project Files

```
student_attendance_manager.py     the whole program
attendance.txt     saved data (created automatically)
README.md          this file
summary.md         how the program runs and problems faced
```

---

## Limitations

- Attendance is stored only as totals (held and attended), not per date, so a single mark cannot be undone or edited.
- There is no option to edit or delete a student.
- It is a console program, with no graphical interface.
