# Project Summary: Student Attendance Manager (PS No. 28)

## 1. What the program does

It is a console program that manages student attendance. The user picks options from a menu to add students, mark each day as present or absent, see a student's attendance percentage, and see who is below the 75% requirement. Data stays saved in `attendance.txt` between runs.

## 2. How the program executes

1. **Start:** `main()` runs and calls `load_students_from_file()`.
2. **Load data:** the program opens `attendance.txt` and reads each line (`roll|name|held|attended`). Each line becomes a dictionary and is added to the `student_list`. If the file does not exist yet, the list starts empty.
3. **Show the menu:** a `while True` loop prints the options (1 Add, 2 Mark, 3 Percentage, 4 Shortage list, 0 Exit) and reads the user's choice.
4. **Run the chosen option:**
   - **Add student:** reads roll and name, checks they are not empty and the roll is not already used, creates a dictionary with `held = 0` and `attended = 0`, adds it to the list, and saves the file.
   - **Mark attendance:** reads the roll and looks the student up with `find_student_by_roll()`. If not found, it prints an error. Otherwise it reads the status. If the status is not P or A, it prints an error. If valid, `held` goes up by 1, and `attended` also goes up by 1 when the status is P. The file is saved.
   - **Percentage:** finds the student. If `held` is 0, it prints 0.00% with the no-classes message. Otherwise it prints attended / held x 100 with two decimals.
   - **Shortage list:** goes through every student, first printing those below 75%, then printing those who meet the requirement.
5. **Save after every change:** `save_students_to_file()` rewrites the whole file each time data changes, so nothing is lost if the program is closed.
6. **Exit:** choosing 0 breaks the loop and the program ends.

### Flow

```
Start -> load attendance.txt -> show menu -> user chooses option
   ^                                              |
   |            add / mark / percentage / shortage list
   |                                              |
   +------- save file (if data changed) <---------+
                         |
                      0 = Exit
```

## 3. Difficulties faced and how they were solved

- **Program crashed on the first run.** Opening `attendance.txt` when it did not exist gave a `FileNotFoundError`. I fixed it with `try/except FileNotFoundError`, so a missing file simply means an empty student list.
- **Data was lost when the program closed.** At first the students lived only in the list, so everything disappeared on exit. I added `save_students_to_file()` and call it after every change, and `load_students_from_file()` when the program starts.
- **Division by zero.** A new student has 0 classes held, so `attended / held` crashed. I added a check: if `held` is 0, the percentage is 0.00% and the message "no classes held yet" is shown.
- **Roll number not found even when it existed.** Typing `101` and having `101` in the list still failed at times. The cause was extra spaces in the input and mixing numbers with text. I used `.strip()` on every input and store the roll number as text everywhere, so the comparison always matches.
- **Lowercase status was rejected.** Typing `p` instead of `P` gave "Invalid status". I used `.upper()` on the input before checking it.
- **Duplicate roll numbers.** The same roll could be added twice, which made percentage and attendance wrong for that student. I search the list with `find_student_by_roll()` before adding and reject a roll that already exists.
- **Reading the file back.** A blank line or a damaged line in the file made the loading code crash. I split each line on `|`, check there are exactly four parts, and check that held and attended are digits. Lines that do not fit are skipped.
- **Saving with the wrong file mode.** Opening the file with `"a"` (append) made students appear many times, because every save added all the students again. I switched to `"w"` (write), which rewrites the whole file each time.
- **A name containing the `|` symbol.** Because `|` separates the fields, a name with that symbol would break the line when it is read back. It is a known limit of this simple format, and the fix would be a different separator or the `csv` module.
- **Wrong output order in the shortage list.** The expected output prints students below 75% first, then those who meet it. A single loop printed them in file order, so I used two loops, one for each group.
- **Running from a different folder.** The program starts with empty data when it is run from another folder, because `attendance.txt` is created in the folder where the program is run. The fix is to always run it from the same folder.

## 4. Result

The program passes all 4 test cases from the project sheet and meets the bare minimum requirements: it runs from the console as one `.py` file, stores each student as a dictionary with a unique roll number, validates roll and status, avoids dividing by zero, and loads and saves data in `attendance.txt`.
