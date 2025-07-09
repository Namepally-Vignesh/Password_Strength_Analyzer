import tkinter as tk
from tkinter import ttk # For themed widgets if desired
import re # Already imported in analysis logic, but good to have here

# Import your analysis functions
from password_analyzer import analyze_password

class PasswordStrengthCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("600x400") # Adjust size as needed

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Password Label and Entry
        self.password_label = ttk.Label(self.root, text="Enter your Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ttk.Entry(self.root, width=50, show="*") # show="*" hides characters
        self.password_entry.pack(pady=5)
        self.password_entry.bind("<KeyRelease>", self.check_password_strength) # Real-time update

        # Strength Feedback Label
        self.strength_feedback_label = ttk.Label(self.root, text="Strength: -")
        self.strength_feedback_label.pack(pady=10)

        # Suggestions Text Area
        self.suggestions_label = ttk.Label(self.root, text="Suggestions:")
        self.suggestions_label.pack(pady=5)

        self.suggestions_text = tk.Text(self.root, height=8, width=60, wrap=tk.WORD)
        self.suggestions_text.pack(pady=5)
        self.suggestions_text.config(state=tk.DISABLED) # Make it read-only

    def check_password_strength(self, event=None):
        password = self.password_entry.get()
        strength, suggestions = analyze_password(password)

        self.strength_feedback_label.config(text=f"Strength: {strength}")

        # Update suggestions text area
        self.suggestions_text.config(state=tk.NORMAL) # Enable to modify
        self.suggestions_text.delete("1.0", tk.END) # Clear previous content
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                self.suggestions_text.insert(tk.END, f"{i}. {suggestion}\n")
        else:
            self.suggestions_text.insert(tk.END, "Great job! Your password is strong.")
        self.suggestions_text.config(state=tk.DISABLED) # Disable again

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthCheckerApp(root)
    root.mainloop() 