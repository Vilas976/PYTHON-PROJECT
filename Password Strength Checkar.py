import re
import requests
import hashlib
import tkinter as tk
from tkinter import messagebox, filedialog

def check_password_strength(password):
    """Assess the strength of a password."""
    feedback = []
    score = 0

    # Length check
    if len(password) < 8:
        feedback.append("Password is too short. Consider using at least 8 characters.")
    else:
        score += 1

    # Check for character variety
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for better security.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for better security.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include numbers to make your password stronger.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Use special characters to enhance password strength.")

    # Common patterns check
    common_patterns = ["123", "password", "qwerty", "abc"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like '123' or 'password'.")

    # Score-based assessment
    strength = "Weak"
    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"

    return strength, feedback

def check_breach(password):
    """Check if the password has been exposed in a data breach."""
    # Compute SHA-1 hash of the password
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    try:
        # Query the API with the hash prefix
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        response.raise_for_status()
        hashes = (line.split(':') for line in response.text.splitlines())
        # Check if the suffix is in the response
        if any(suffix == h[0] for h in hashes):
            return True
    except requests.RequestException:
        return None
    return False

def save_report(password, strength, feedback):
    """Save password strength feedback to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(f"Password: {password}\n")
            file.write(f"Strength: {strength}\n")
            file.write("Feedback:\n")
            for tip in feedback:
                file.write(f"- {tip}\n")
        messagebox.showinfo("Success", "Report saved successfully!")

def update_strength(event):
    password = password_entry.get()
    if password:
        strength, feedback = check_password_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg=("green" if strength == "Strong" else "black" if strength == "Moderate" else "red"))
        feedback_text.delete(1.0, tk.END)
        for tip in feedback:
            feedback_text.insert(tk.END, f"- {tip}\n")

def evaluate_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    # Check strength
    strength, feedback = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength}", fg=("green" if strength == "Strong" else "orange" if strength == "Moderate" else "red"))
    feedback_text.delete(1.0, tk.END)
    for tip in feedback:
        feedback_text.insert(tk.END, f"- {tip}\n")

    # Check breaches
    breached = check_breach(password)
    if breached is None:
        breach_label.config(text="Breach Check: Unable to check.", fg="blue")
    elif breached:
        breach_label.config(text="Breach Check: Password found in breaches!", fg="red")
    else:
        breach_label.config(text="Breach Check: Password is safe.", fg="Blue")

def create_gui():
    global password_entry, strength_label, feedback_text, breach_label

    root = tk.Tk()
    root.title("Password Strength Checker")

    tk.Label(root, text="Enter Password :").pack(pady=10)
    password_entry = tk.Entry(root, width=60, show="*")
    password_entry.pack(pady=5)
    password_entry.bind("<KeyRelease>", update_strength)

    tk.Button(root, text="Check Password", command=evaluate_password).pack(pady=5)

    strength_label = tk.Label(root, text="Strength: ", font=("Arial", 14))
    strength_label.pack(pady=5)

    breach_label = tk.Label(root, text="Breach Check: ", font=("Arial", 14))
    breach_label.pack(pady=5)

    tk.Label(root, text="Feedback:").pack(pady=5)
    feedback_text = tk.Text(root, height=15, width=80)
    feedback_text.pack(pady=5)

    tk.Button(root, text="Save Report", command=lambda: save_report(password_entry.get(), strength_label.cget("text"), feedback_text.get(1.0, tk.END).splitlines())).pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    create_gui()