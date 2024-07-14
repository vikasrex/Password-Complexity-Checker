import re
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, Checkbutton, IntVar, LEFT, RIGHT

class PasswordChecker:
    def __init__(self, master):
        self.master = master
        master.title("Password Complexity Checker")

        self.frame = Frame(master)
        self.frame.pack(pady=10)

        self.label = Label(self.frame, text="Enter your password:")
        self.label.pack(side=LEFT)

        self.password_var = StringVar()
        self.entry = Entry(self.frame, textvariable=self.password_var, show='*')
        self.entry.pack(side=RIGHT, padx=5)

        self.show_password_var = IntVar()
        self.show_password_check = Checkbutton(master, text="Show Password", variable=self.show_password_var, command=self.toggle_password)
        self.show_password_check.pack()

        self.check_button = Button(master, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=5)

        self.result_label = Label(master, text="", justify=LEFT, wraplength=300)
        self.result_label.pack(pady=5)

    def toggle_password(self):
        if self.show_password_var.get():
            self.entry.config(show='')
        else:
            self.entry.config(show='*')

    def check_password(self):
        password = self.password_var.get()
        complexity, feedback, color = self.evaluate_password(password)
        self.result_label.config(text=f"Complexity: {complexity}\n\nFeedback:\n{feedback}", fg=color)
        self.entry.config(bg=color)

    def evaluate_password(self, password):
        length_criteria = len(password) >= 8
        lowercase_criteria = bool(re.search(r'[a-z]', password))
        uppercase_criteria = bool(re.search(r'[A-Z]', password))
        number_criteria = bool(re.search(r'[0-9]', password))
        special_criteria = bool(re.search(r'[\W_]', password))

        criteria = [length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria]
        score = sum(criteria)

        complexity = "Very Weak"
        feedback = []
        color = "red"

        if length_criteria:
            feedback.append("✔️ Length is sufficient (8+ characters).")
        else:
            feedback.append("❌ Length is insufficient (less than 8 characters).")

        if lowercase_criteria:
            feedback.append("✔️ Contains lowercase letters.")
        else:
            feedback.append("❌ Does not contain lowercase letters.")

        if uppercase_criteria:
            feedback.append("✔️ Contains uppercase letters.")
        else:
            feedback.append("❌ Does not contain uppercase letters.")

        if number_criteria:
            feedback.append("✔️ Contains numbers.")
        else:
            feedback.append("❌ Does not contain numbers.")

        if special_criteria:
            feedback.append("✔️ Contains special characters.")
        else:
            feedback.append("❌ Does not contain special characters.")

        if score == 5:
            complexity = "Very Strong"
            color = "green"
        elif score == 4:
            complexity = "Strong"
            color = "blue"
        elif score == 3:
            complexity = "Moderate"
            color = "orange"
        elif score == 2:
            complexity = "Weak"
            color = "brown"

        feedback = "\n".join(feedback)
        return complexity, feedback, color

if __name__ == "__main__":
    root = Tk()
    password_checker = PasswordChecker(root)
    root.mainloop()
