import tkinter as tk

window = tk.Tk()

window.title("Register/Log-in Page")
window.geometry("500x200")
window.resizable(False,False)
window.config(bg= "white")



label = tk.Label(window, text =  "Welcome!", font= ("Times New Roman", 15, "bold"), bg= "white")
label.pack (fill="x", anchor="center", padx=10, pady=10)

def click_rbutt():
    rbutt=tk.Toplevel()
    rbutt.title("Register")
    rbutt.geometry("500x200")
    rbutt.config(False,False)

    userlbl = tk.Label(rbutt, text="Register Username and Password")
    userlbl.grid(row=0,column=1,columnspan=3)

def click_lbutt():
    lbutt=tk.Toplevel()
    lbutt.title("Log In")
    lbutt.geometry("500x200")
    lbutt.config(False,False)

rbutt = tk.Button(window, text = "Register", font= ("Times New Roman", 15, "bold"), bg= "blue", command=click_rbutt)
rbutt.pack (fill="y", anchor="center", padx=10, pady=15)

lbutt = tk.Button(window, text = "Log In", font= ("Times New Roman", 15, "bold"), bg= "green", command=click_lbutt)
lbutt.pack (fill="y", anchor="center", padx=10, pady=15)

window.mainloop()
