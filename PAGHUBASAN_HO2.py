import tkinter as tk

root = tk.Tk()
root.title("Student Profile")
root.geometry("600x600")
root.resizable(False, True)
root.configure(bg="white")

tk.Label(root, text="Student Profile", font=("Arial", 24, "bold"), bg="white").pack(pady=20)

tk.Label(root, text="Full Name: Neil M. Paghubasan.", font=("Arial", 14), bg="white").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Age: 18 years old", font=("Arial", 14), bg="white").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Course and Section: BSIT - 1C", font=("Arial", 14), bg="white").pack(anchor="w", padx=40, pady=5)
tk.Label(root, text="Birthday: September 1, 2007", font=("Arial", 14), bg="white").pack(anchor="w", padx=40, pady=5)

tk.Label(root, text="Personal Motto:", font=("Arial", 14, "bold"), bg="white").pack(anchor="w", padx=40, pady=(20, 5))

tk.Label(
    root,
    text="If you do something,\nYou'll accomplish a thing.",
    font=("Arial", 13, "italic"),
    bg="white",
    justify="center"
).pack(anchor="w", padx=60)

root.mainloop()
