"""PS No. 28 - Student Attendance Manager."""

DATA_FILE = "attendance.txt"
MINIMUM_PERCENTAGE = 75


def load_students_from_file():
    student_list = []
    try:
        with open(DATA_FILE, encoding="utf-8") as data_file:
            for file_line in data_file:
                fields = file_line.strip().split("|")
                if len(fields) == 4 and fields[2].isdigit() and fields[3].isdigit():
                    student_list.append({"roll": fields[0], "name": fields[1],
                                         "held": int(fields[2]), "attended": int(fields[3])})
    except FileNotFoundError:
        pass                                # first run: no file yet, start with an empty list
    return student_list


def save_students_to_file(student_list):
    with open(DATA_FILE, "w", encoding="utf-8") as data_file:
        for student in student_list:
            data_file.write(f"{student['roll']}|{student['name']}|"
                            f"{student['held']}|{student['attended']}\n")


def find_student_by_roll(student_list, roll_number):
    for student in student_list:
        if student["roll"] == roll_number:
            return student
    return None


def calculate_percentage(student):
    if student["held"] == 0:                # avoid dividing by zero
        return 0.0
    return student["attended"] / student["held"] * 100


def add_new_student(student_list):
    roll_number = input("Roll: ").strip()
    student_name = input("Name: ").strip()
    if not roll_number or not student_name:
        print("Roll and name cannot be empty.")
    elif find_student_by_roll(student_list, roll_number):
        print(f"Roll number {roll_number} already exists.")
    else:
        student_list.append({"roll": roll_number, "name": student_name,
                             "held": 0, "attended": 0})
        save_students_to_file(student_list)
        print(f"Student added: {roll_number} | {student_name} | Held: 0 | Attended: 0")


def mark_student_attendance(student_list):
    roll_number = input("Roll: ").strip()
    student = find_student_by_roll(student_list, roll_number)
    if student is None:
        print(f"Roll number {roll_number} not found.")
        return
    attendance_status = input("Status (P/A): ").strip().upper()
    if attendance_status not in ("P", "A"):
        print("Invalid status. Enter P or A.")
        return
    student["held"] += 1
    if attendance_status == "P":
        student["attended"] += 1
    save_students_to_file(student_list)
    print("Attendance marked.")


def show_student_percentage(student_list):
    roll_number = input("Roll: ").strip()
    student = find_student_by_roll(student_list, roll_number)
    if student is None:
        print(f"Roll number {roll_number} not found.")
    elif student["held"] == 0:
        print(f"{student['name']}: Attendance 0.00% (no classes held yet)")
    else:
        print(f"{student['name']}: Attendance {calculate_percentage(student):.2f}%")


def show_shortage_list(student_list):
    for student in student_list:            # students below the requirement first
        attendance_percentage = calculate_percentage(student)
        if attendance_percentage < MINIMUM_PERCENTAGE:
            print(f"Below {MINIMUM_PERCENTAGE}%: {student['roll']} | "
                  f"{student['name']} | {attendance_percentage:.2f}%")
    for student in student_list:            # then the students who meet it
        attendance_percentage = calculate_percentage(student)
        if attendance_percentage >= MINIMUM_PERCENTAGE:
            print(f"{student['name']} ({attendance_percentage:.2f}%) meets the requirement.")


def main():
    student_list = load_students_from_file()
    program_running = True
    while program_running:
        print("\n1. Add student\n2. Mark attendance\n3. Percentage\n4. Shortage list\n0. Exit")
        menu_choice = input("Choose: ").strip()
        if menu_choice == "1":
            add_new_student(student_list)
        elif menu_choice == "2":
            mark_student_attendance(student_list)
        elif menu_choice == "3":
            show_student_percentage(student_list)
        elif menu_choice == "4":
            show_shortage_list(student_list)
        elif menu_choice == "0":
            program_running = False
        else:
            print("Invalid option.")


main()
