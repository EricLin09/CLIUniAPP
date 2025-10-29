import time 
from controller import StudentController, SubjectController, AdminController
from menu import UniversityMenu, StudentMenu, SubjectEnrolmentMenu, AdminMenu
from database import Database


def run_student_system():

    controller = StudentController()
    
    while True:
        choice = StudentMenu.display()
        
        if choice == 'l':
            print("Student Sign In")
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            success, result = controller.login(email, password)
            if success:
                print(f"email and password formats acceptable")
                print(f"Welcome {result.name}!")
                time.sleep(1)  
                run_subject_enrolment_system(result)
            else:
                print(result)
                time.sleep(1) 
        
        elif choice == 'r':

            print("Student Sign Up")
            email = input("Email: ").strip()
            password = input("Password: ").strip()

            if not controller.validate_email(email):
                print("Incorrect email format")
                time.sleep(0.7)
                print("Email format: firstname.lastname@university.com")
                time.sleep(1)
                continue
            
            if not controller.validate_password(password):
                print("Incorrect password format")
                time.sleep(0.7)
                print("Password format: Must start with uppercase letter, contain at least 5 letters, followed by 3+ digits")
                time.sleep(1)
                continue

            if not controller.validate_email(email) and not controller.validate_password(password):
                print("Both email and password formats are invalid.")
                print("Email format: firstname.lastname@university.com")
                print("Password format: Must start with uppercase letter, contain at least 5 letters, followed by 3+ digits")
                time.sleep(1)
                continue

            if controller.database.find_by_email(email):
                print("Student already exists")
                time.sleep(1)
                continue
            
            name = input("Name: ").strip()
            
            success, result = controller.register(name, email, password)
            if success:
                print("email and password formats acceptable")
                time.sleep(0.7)
                print(f"Enrolling Student {name}")
                time.sleep(1.2)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)


def run_subject_enrolment_system(student):

    database = Database()
    controller = SubjectController(database)
    
    while True:
        choice = SubjectEnrolmentMenu.display()
        
        if choice == 'e':

            success, result = controller.enroll_subject(student)
            if success:
                print(f"Enrolling in Subject-{result.id}")
                time.sleep(0.7)
                print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects")
                time.sleep(1) 
            else:
                print(result)
                time.sleep(1) 
        
        elif choice == 'r':

            if not student.subjects:
                print("No subjects enrolled")
                time.sleep(1)  
                continue
                
            subject_id = input("Remove subject by ID: ").strip()
            success = controller.remove_subject(student, subject_id)
            if success:
                print(f"Dropping Subject-{subject_id}")
                time.sleep(0.7)
                print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects")
                time.sleep(1) 
            else:
                print(f"Subject {subject_id} not found")
                time.sleep(1) 
        
        elif choice == 's':

            subjects = controller.show_subjects(student)
            if not subjects:
                print("Showing 0 subjects")
                time.sleep(1)
            else:
                print(f"Showing {len(subjects)} subjects")
                time.sleep(0.5)
                for subject in subjects:
                    print(f"[ Subject::{subject.id} -- mark = {subject.mark} -- grade = {subject.grade} ]")
                    time.sleep(0.5)

        
        elif choice == 'c':

            print("Updating Password")
            new_password = input("New Password: ").strip()
            confirm_password = input("Confirm Password: ").strip()
            
            if new_password != confirm_password:
                print("Password does not match - try again")
                time.sleep(1)
                continue

            if new_password == student.password:
                print("New password cannot be the same as the current password.")
                time.sleep(1)
                continue
            
            success, message = controller.change_password(student, new_password)
            if success:
                print(message)
                time.sleep(1)
            else:
                print(message)
                time.sleep(1) 
        
        elif choice == 'x':
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)


def run_admin_system():

    controller = AdminController()
    
    while True:
        choice = AdminMenu.display()
        
        if choice == 's':

            students = controller.show_all_students()
            if not students:
                print("< Nothing to Display >")
            else:
                print(f"\nStudent List")
                for student in students:
                    print(f"{student.id} :: {student.name} --> Email: {student.email}")
            time.sleep(1)
        
        elif choice == 'g':

            grouped = controller.group_by_grade()
            has_students = any(students for students in grouped.values())
            
            if not has_students:
                print("< Nothing to Display >")
            else:
                print("\nGrade Grouping")
                for grade in ["HD", "D", "C", "P", "Z"]:
                    students = grouped[grade]
                    if students:
                        print(f"\n{grade} --> [", end="")
                        print(", ".join([f"{s.name} :: {s.id} --> GRADE: {grade} - MARK: {s.get_average_mark():.2f}" 
                                       for s in students]), end="")
                        print(" ]")
            time.sleep(1)  
        
        elif choice == 'p':

            passed, failed, NotEnrolled = controller.partition_pass_fail()
            
            if not passed and not failed and not NotEnrolled:
                print("< Nothing to Display >")
                
            else:
                print("\nPASS/FAIL/Not Enrolled Partition")
                
                if passed:
                    print(f"PASS --> [", end="")
                    print(", ".join([f"{s.name} :: {s.id} --> GRADE: {s.get_grade()} - MARK: {s.get_average_mark():.2f}" 
                                   for s in passed]), end="")
                    print(" ]")
                
                if failed:
                    print(f"FAIL --> [", end="")
                    print(", ".join([f"{s.name} :: {s.id} --> GRADE: {s.get_grade()} - MARK: {s.get_average_mark():.2f}" 
                                   for s in failed]), end="")
                    print(" ]")

                if NotEnrolled:

                    print(f"Not Enrolled --> [", end="")
                    print(", ".join([f"{s.name} :: {s.id}"
                                   for s in NotEnrolled]), end="")
                    print(" ]")

            time.sleep(1)
        
        elif choice == 'r':

            student_id = input("Remove by ID: ").strip()
            success = controller.remove_student(student_id)
            if success:
                print(f"Removing Student {student_id} Account")
                time.sleep(1)
            else:
                print(f"Student {student_id} does not exist")
                time.sleep(1)
        
        elif choice == 'c':

            confirm = input("Are you sure you want to clear the database (Y/N)? ").strip().upper()
            if confirm == 'Y':
                controller.clear_database()
                print("Students data cleared")
                time.sleep(1)
            else:
                print("Operation cancelled")
                time.sleep(1)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)


def main():
    print("=" * 50)
    print(" " * 15 + "University Menu")
    print("=" * 50)
    
    while True:
        choice = UniversityMenu.display()
        
        if choice == 'A':
            run_admin_system()
        elif choice == 'S':
            run_student_system()
        elif choice == 'X':
            print("\nThank you!")
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    main()