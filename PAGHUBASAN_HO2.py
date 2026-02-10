import tkinter as tk

root = tk.Tk()
root.title("Student Profile")
root.geometry("600x600")
root.resizable(False, True)
root.configure(bg="#f7b6c8")

tk.Label(
    root,
    text="Student Profile",
    font=("Arial", 24, "bold"),
    bg="#f7b6c8"
).pack(pady=20)

tk.Label(root, text="Full Name: Angelica Mae V. Borela", font=("Arial", 14), bg="#f7b6c8").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Age: 23 years old", font=("Arial", 14), bg="#f7b6c8").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Course and Section: BSIT - 3A", font=("Arial", 14), bg="#f7b6c8").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Birthday: February 14, 2002", font=("Arial", 14), bg="#f7b6c8").pack(anchor="w", padx=40, pady=5)

tk.Label(
    root,
    text="Personal Motto:",
    font=("Arial", 14, "bold"),
    bg="#f7b6c8"
).pack(anchor="w", padx=40, pady=(