import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import database as backend

# Global variables to hold user details
full_name_var = None
age_var = None
height_entry = None
weight_entry = None
bmi_output_label = None

# Logic of Classifying the BMI index values
def on_generate_clicked():
    try:
        full_name = full_name_var.get()
        age = age_var.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi_result = backend.calculate_bmi(height, weight)
        bmi_result = float(bmi_result)
        
        if bmi_result < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_result < 24.9:
            category = "Healthy"
        elif 24.9 <= bmi_result < 29.9:
            category = "Overweight"
        elif bmi_result >= 30:
            category = "Obesity"

        backend.insert_data(full_name, age, height, weight, bmi_result)
        bmi_output_label.config(text=f"Your BMI is: {bmi_result} \n Category: {category}")
    except ValueError:
        bmi_output_label.config(text="Error: Invalid input.")

def on_view_graph_clicked():
    backend.create_histogram()

def open_main_app():
    global full_name_var, age_var, height_entry, weight_entry, bmi_output_label

    root = tk.Tk()
    root.title("BMI Calculator")
    root.configure(bg="#f0f0f0")
    root.geometry("640x720")

    canvas = tk.Canvas(root, width=600, height=100, bg="#f0f0f0")
    canvas.grid(columnspan=3, rowspan=1)

    logo = Image.open('Images/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg="#f0f0f0")
    logo_label.image = logo
    logo_label.grid(column=0, row=0, columnspan=2)

    full_name_label = tk.Label(root, text="Enter Full Name:", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black")
    full_name_label.grid(column=0, row=1, padx=5, pady=8, sticky="e")

    full_name_var = tk.StringVar()
    full_name_entry = tk.Entry(root, textvariable=full_name_var, font=("Helvetica", 12, "normal"), width=30, bg="#e6e6e6", fg="black", bd=1, justify='center')
    full_name_entry.grid(column=1, row=1, padx=5, pady=8, sticky="w")

    age_label = tk.Label(root, text="Enter Age:", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black")
    age_label.grid(column=0, row=2, padx=5, pady=8, sticky="e")

    age_var = tk.IntVar()
    age_entry = tk.Entry(root, textvariable=age_var, font=("Helvetica", 12, "normal"), width=10, bg="#e6e6e6", fg="black", bd=1, justify='center')
    age_entry.grid(column=1, row=2, padx=5, pady=8, sticky="w")

    height_label = tk.Label(root, text="Enter Height (cm):", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black")
    height_label.grid(column=0, row=3, padx=5, pady=8, sticky="e")

    height_entry = tk.Entry(root, font=("Helvetica", 12, "normal"), width=10, bg="#e6e6e6", fg="black", bd=1, justify='center')
    height_entry.grid(column=1, row=3, padx=5, pady=8, sticky="w")

    weight_label = tk.Label(root, text="Enter Weight (kg):", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black")
    weight_label.grid(column=0, row=4, padx=5, pady=8, sticky="e")

    weight_entry = tk.Entry(root, font=("Helvetica", 12, "normal"), width=10, bg="#e6e6e6", fg="black", bd=1, justify='center')
    weight_entry.grid(column=1, row=4, padx=5, pady=8, sticky="w")

    submit_btn = tk.Button(root, text="Calculate", font=("Helvetica", 12, "bold"), bg="#ff6f61", fg="white", height=2, width=15, justify="center", command=on_generate_clicked)
    submit_btn.grid(column=0, row=5, columnspan=2, padx=5, pady=10)

    generate_graph_btn = tk.Button(root, text="View Graph", font=("Helvetica", 12, "bold"), bg="#ff6f61", fg="white", height=2, width=15, justify="center", command=on_view_graph_clicked)
    generate_graph_btn.grid(column=0, row=6, columnspan=2, padx=5, pady=10)

    bmi_output_label = tk.Label(root, text="BMI", font=("Helvetica", 14, "normal"), bg="#e6e6e6", fg="black", width=40, height=4, border=2)
    bmi_output_label.grid(column=0, row=7, columnspan=2, padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    open_main_app()
