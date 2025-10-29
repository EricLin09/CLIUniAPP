import tkinter as tk
from tkinter import messagebox, ttk
from controller import StudentController, SubjectController
from database import Database


class GUIUniApp:

    def __init__(self, root):
        self.root = root
        self.root.title("GUIUniApp - University System")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        self.current_student = None
        self.student_controller = StudentController()

        self.show_login_window()
    
    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_window(self):
        self.clear_window()
        self.root.configure(bg="#f0f0f0")
        
        title = tk.Label(self.root, text="Student Login",
                        font=("Arial", 20, "bold"), pady=20, bg="#f0f0f0")
        title.pack()

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(x=95, y=100) 

        tk.Label(frame, text="Email:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0,
                                                                sticky="e", padx=10, pady=10)
        self.email_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0,
                                                                    sticky="e", padx=10, pady=10)
        self.password_entry = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_btn = tk.Button(self.root, text="LOGIN", font=("Arial", 14, "bold"),
                            bg="#2196F3", fg="Black", width=18, height=2,
                            command=self.handle_login, cursor="hand2",
                            relief=tk.RAISED, bd=3,
                            activebackground="#1976D2", activeforeground="white")
        login_btn.place(x=200, y=250) 

        hint_frame = tk.Frame(self.root, bg="#f0f0f0", relief=tk.GROOVE, bd=2)
        hint_frame.pack(pady=10, padx=40, fill=tk.BOTH, side=tk.BOTTOM)
        
        tk.Label(hint_frame, text="Email format: firstname.lastname@university.com",
                font=("Arial", 9), bg="#f0f0f0", fg="#555555").pack(pady=5)
        tk.Label(hint_frame, text="Password: Uppercase letter + 5+ letters + 3+ digits",
                font=("Arial", 9), bg="#f0f0f0", fg="#555555").pack(pady=5)
    
    def handle_login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            self.show_exception_window("Empty Fields", 
                                       "Email and password cannot be empty!")
            return

        if not self.student_controller.validate_email(email):
            self.show_exception_window("Invalid Email Format", 
                                       "Email must be in format:\nfirstname.lastname@university.com")
            return

        success, result = self.student_controller.login(email, password)
        
        if success:
            self.current_student = result
            messagebox.showinfo("Login Successful", 
                              f"Welcome {result.name}!\nStudent ID: {result.id}")
            self.show_enrolment_window()
        else:
            self.show_exception_window("Login Failed", result)
    
    def show_enrolment_window(self):

        self.clear_window()

        self.root.configure(bg="#f5f5f5")

        title_frame = tk.Frame(self.root, bg="#1565C0", pady=15)
        title_frame.pack(fill=tk.X)
        
        tk.Label(title_frame, text=f"Welcome, {self.current_student.name}", 
                font=("Arial", 18, "bold"), bg="#1565C0", fg="white").pack()
        tk.Label(title_frame, text=f"Student ID: {self.current_student.id}", 
                font=("Arial", 11), bg="#1565C0", fg="white").pack()
        
  
        info_frame = tk.Frame(self.root, bg="#E3F2FD", pady=10, relief=tk.RIDGE, bd=2)
        info_frame.pack(fill=tk.X, pady=10, padx=20)
        
        enrolled_count = len(self.current_student.subjects)
        tk.Label(info_frame, 
                text=f"Enrolled Subjects: {enrolled_count} / 4", 
                font=("Arial", 13, "bold"), bg="#E3F2FD").pack()

        btn_frame = tk.Frame(self.root, bg="#F5F5F5")
        btn_frame.pack(pady=20)

        enroll_btn = tk.Button(btn_frame, text="Enroll in Subject", 
                              font=("Arial", 12, "bold"), bg="#43A047", fg="black",
                              width=20, height=2, command=self.handle_enroll,
                              cursor="hand2", relief=tk.RAISED, bd=2,
                              activebackground="#388E3C", activeforeground="white")
        enroll_btn.grid(row=0, column=0, padx=10, pady=10)

        view_btn = tk.Button(btn_frame, text="View Subjects", 
                            font=("Arial", 12, "bold"), bg="#1E88E5", fg="black",
                            width=20, height=2, command=self.show_subject_window,
                            cursor="hand2", relief=tk.RAISED, bd=2,
                            activebackground="#1565C0", activeforeground="white")
        view_btn.grid(row=0, column=1, padx=10, pady=10)
        
 
        remove_btn = tk.Button(btn_frame, text="Remove Subject", 
                              font=("Arial", 12, "bold"), bg="#FB8C00", fg="black",
                              width=20, height=2, command=self.handle_remove_subject,
                              cursor="hand2", relief=tk.RAISED, bd=2,
                              activebackground="#F57C00", activeforeground="white")
        remove_btn.grid(row=1, column=0, padx=10, pady=10)
        

        pwd_btn = tk.Button(btn_frame, text="Change Password", 
                           font=("Arial", 12, "bold"), bg="#8E24AA", fg="black",
                           width=20, height=2, command=self.handle_change_password,
                           cursor="hand2", relief=tk.RAISED, bd=2,
                           activebackground="#7B1FA2", activeforeground="white")
        pwd_btn.grid(row=1, column=1, padx=10, pady=10)
        

        logout_btn = tk.Button(self.root, text="LOGOUT", 
                              font=("Arial", 12, "bold"), bg="#E53935", fg="black",
                              width=15, command=self.handle_logout,
                              cursor="hand2", relief=tk.RAISED, bd=2,
                              activebackground="#C62828", activeforeground="white")
        logout_btn.pack(pady=20)
    
    def handle_enroll(self):
        
        if len(self.current_student.subjects) >= 4:
            self.show_exception_window("Enrollment Limit Reached", 
                                       "Students are allowed to enrol in 4 subjects only!\n" +
                                       f"You are currently enrolled in {len(self.current_student.subjects)} subjects.")
            return
        
        subject_controller = SubjectController(Database())
        success, result = subject_controller.enroll_subject(self.current_student)
        
        if success:
            messagebox.showinfo("Enrollment Successful", 
                              f"Enrolled in Subject {result.id}\n" +
                              f"Mark: {result.mark}\n" +
                              f"Grade: {result.grade}\n" +
                              f"Current Average: {self.current_student.get_average_mark():.2f}")
            self.show_enrolment_window()  
        else:
            self.show_exception_window("Enrollment Failed", result)
    

    def show_subject_window(self):
   
        if not self.current_student.subjects:
            messagebox.showinfo("No Subjects", "You are not enrolled in any subjects yet.")
            return

        subject_window = tk.Toplevel(self.root)
        subject_window.title("Enrolled Subjects")
        subject_window.geometry("700x600")
        subject_window.resizable(False, False)
        subject_window.configure(bg="#f5f5f5")

        tk.Label(subject_window, text="Your Enrolled Subjects", 
                font=("Arial", 16, "bold"), pady=15, bg="#f5f5f5").pack()

        frame = tk.Frame(subject_window, bg="#f5f5f5")
        frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview.Heading", background="#1565C0", foreground="white", font=("Arial", 11, "bold"))
        style.configure("Treeview", background="white", foreground="black", rowheight=25, font=("Arial", 10))
        style.map("Treeview", background=[('selected', '#E3F2FD')])

        columns = ("Subject ID", "Mark", "Grade")
        tree = ttk.Treeview(frame, columns=columns, show="headings", 
                           yscrollcommand=scrollbar.set, height=12)
        
        tree.heading("Subject ID", text="Subject ID")
        tree.heading("Mark", text="Mark")
        tree.heading("Grade", text="Grade")
        
        tree.column("Subject ID", width=150, anchor="center")
        tree.column("Mark", width=150, anchor="center")
        tree.column("Grade", width=150, anchor="center")

        for subject in self.current_student.subjects:
            tree.insert("", tk.END, values=(subject.id, subject.mark, subject.grade))
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=tree.yview)

        avg_frame = tk.Frame(subject_window, bg="#C8E6C9", pady=10, relief=tk.RIDGE, bd=2)
        avg_frame.pack(fill=tk.X, padx=20, pady=10)

        avg_mark = self.current_student.get_average_mark()
        grade = self.current_student.get_grade()
        status = self.current_student.get_enrollment_status()
        
        tk.Label(avg_frame, text=f"Average Mark: {avg_mark:.2f}", 
                font=("Arial", 12, "bold"), bg="#C8E6C9").pack()
        tk.Label(avg_frame, text=f"Overall Grade: {grade}", 
                font=("Arial", 12), bg="#C8E6C9").pack()
        tk.Label(avg_frame, text=f"Status: {status}", 
                font=("Arial", 12, "bold"), bg="#C8E6C9",
                fg="#2E7D32" if status == "PASS" else "#C62828").pack()
        

        tk.Button(subject_window, text="CLOSE", font=("Arial", 11, "bold"),
                 command=subject_window.destroy, width=15,
                 bg="#757575", fg="black", cursor="hand2",
                 activebackground="#616161", activeforeground="white").pack(pady=10)


    def handle_remove_subject(self):
       
        if not self.current_student.subjects:
            messagebox.showinfo("No Subjects", "You have no subjects to remove.")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Remove Subject")
        dialog.geometry("400x250")
        dialog.resizable(False, False)
        dialog.configure(bg="#f5f5f5")
        
        tk.Label(dialog, text="Remove Subject", 
                font=("Arial", 16, "bold"), pady=20, bg="#f5f5f5").pack()
        
        tk.Label(dialog, text="Enter Subject ID to remove:", 
                font=("Arial", 11), bg="#f5f5f5").pack(pady=10)
        
        subject_id_entry = tk.Entry(dialog, font=("Arial", 12), width=20)
        subject_id_entry.pack(pady=10)
        
        def confirm_remove():
            subject_id = subject_id_entry.get().strip()
            if not subject_id:
                messagebox.showwarning("Empty Field", "Please enter a subject ID")
                return
            
            subject_controller = SubjectController(Database())
            success = subject_controller.remove_subject(self.current_student, subject_id)
            
            if success:
                messagebox.showinfo("Success", f"Subject {subject_id} removed successfully!")
                dialog.destroy()
                self.show_enrolment_window()  
            else:
                messagebox.showerror("Error", f"Subject {subject_id} not found!")
        
        btn_frame = tk.Frame(dialog, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="REMOVE", font=("Arial", 11, "bold"),
                 bg="#E53935", fg="black", width=12, cursor="hand2",
                 command=confirm_remove,
                 activebackground="#C62828", activeforeground="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="CANCEL", font=("Arial", 11, "bold"),
                 width=12, bg="#757575", fg="black", cursor="hand2",
                 command=dialog.destroy,
                 activebackground="#616161", activeforeground="white").pack(side=tk.LEFT, padx=5)
    
    def handle_change_password(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Change Password")
        dialog.geometry("450x300")
        dialog.resizable(False, False)
        dialog.configure(bg="#f5f5f5")
        
        tk.Label(dialog, text="Change Password", 
                font=("Arial", 16, "bold"), pady=20, bg="#f5f5f5").pack()
        
        frame = tk.Frame(dialog, bg="#f5f5f5")
        frame.pack(pady=20)
        
        tk.Label(frame, text="New Password:", font=("Arial", 11), bg="#f5f5f5").grid(row=0, column=0, 
                                                                        sticky="e", padx=10, pady=10)
        new_pwd_entry = tk.Entry(frame, font=("Arial", 11), width=20, show="*")
        new_pwd_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(frame, text="Confirm Password:", font=("Arial", 11), bg="#f5f5f5").grid(row=1, column=0, 
                                                                            sticky="e", padx=10, pady=10)
        confirm_pwd_entry = tk.Entry(frame, font=("Arial", 11), width=20, show="*")
        confirm_pwd_entry.grid(row=1, column=1, padx=10, pady=10)
        
        def confirm_change():
            new_pwd = new_pwd_entry.get().strip()
            confirm_pwd = confirm_pwd_entry.get().strip()
            
            if not new_pwd or not confirm_pwd:
                messagebox.showwarning("Empty Fields", "Please fill in all fields")
                return
            
            if new_pwd != confirm_pwd:
                messagebox.showerror("Mismatch", "Passwords do not match!")
                return

            if new_pwd == self.current_student.password:
                messagebox.showerror("Invalid Password", "New password cannot be the same as current password!")
                return
            
            subject_controller = SubjectController(Database())
            success, message = subject_controller.change_password(self.current_student, new_pwd)
            
            if success:
                messagebox.showinfo("Success", "Password updated successfully!")
                dialog.destroy()
            else:
                messagebox.showerror("Error", message)
        
        btn_frame = tk.Frame(dialog, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="CHANGE PASSWORD", font=("Arial", 11, "bold"),
                 bg="#43A047", fg="black", width=16, cursor="hand2",
                 command=confirm_change,
                 activebackground="#388E3C", activeforeground="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="CANCEL", font=("Arial", 11, "bold"),
                 width=10, bg="#757575", fg="black", cursor="hand2",
                 command=dialog.destroy,
                 activebackground="#616161", activeforeground="white").pack(side=tk.LEFT, padx=5)

        hint_frame = tk.Frame(dialog, bg="#f5f5f5", relief=tk.GROOVE, bd=2)
        hint_frame.pack(pady=5, padx=10, fill=tk.X)
        
        tk.Label(hint_frame, text="Password must start with uppercase letter,",
                font=("Arial", 9), bg="#f5f5f5", fg="#000000").pack()
        tk.Label(hint_frame, text="contain at least 5 letters, followed by 3+ digits",
                font=("Arial", 9), bg="#f5f5f5", fg="#000000").pack()
    
    def handle_logout(self):

        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.current_student = None
            self.show_login_window()

    def show_exception_window(self, title, message):
        error_window = tk.Toplevel(self.root)
        error_window.title(title)
        error_window.geometry("400x200")
        error_window.resizable(False, False)
        error_window.configure(bg="#fff")

        tk.Label(error_window, text="⚠️", font=("Arial", 40), bg="#fff").pack(pady=20)

        tk.Label(error_window, text=title, 
                font=("Arial", 14, "bold"), bg="#fff").pack()
        tk.Label(error_window, text=message, 
                font=("Arial", 10), wraplength=350, justify=tk.CENTER, bg="#fff").pack(pady=10)

    def show_exception_window(self, title, message):
            error_window = tk.Toplevel(self.root)
            error_window.title(title)
            error_window.geometry("400x200")
            error_window.resizable(False, False)
            error_window.configure(bg="#fff")
            tk.Label(error_window, text="⚠️", font=("Arial", 40), bg="#fff").pack(pady=20)
            tk.Label(error_window, text=title,
                    font=("Arial", 14, "bold"), bg="#fff").pack()
            tk.Label(error_window, text=message,
                    font=("Arial", 10), wraplength=350, justify=tk.CENTER, bg="#fff").pack(pady=10)
            tk.Button(error_window, text="OK", font=("Arial", 11),
            bg="#f0f0f0", fg="black", width=10, cursor="hand2",
            command=error_window.destroy,
            relief=tk.RAISED, bd=1,
            activebackground="#f0f0f0", activeforeground="black").pack(pady=5)

def main():
    root = tk.Tk()
    app = GUIUniApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()