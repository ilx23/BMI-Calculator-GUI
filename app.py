import math
from tkinter import *
from tkinter import messagebox

# Function to calculate BMI based on weight and height entered by the user
def bmi_calculator():
    # Get user input for weight and height
    weight = weight_entry.get()
    height = height_entry.get()
    bmi_status = ''

    # Check if both weight and height are provided
    if weight == '' or height == '':
        messagebox.showerror("Error", "Please fill all input")
    else:
        try:
            # Convert input strings to float
            float_weight = float(weight)
            float_height = float(height)

            # Convert height from centimeters to meters if greater than 100
            if float_height > 100:
                float_height = float_height / 100

            # Calculate BMI
            bmi = round(float_weight / (float_height ** 2), 2)

            # Determine BMI status
            if bmi < 18.5:
                bmi_status = 'Underweight'
            elif 18.5 < bmi < 24.9:
                bmi_status = 'Normal'
            elif 25 < bmi < 29.9:
                bmi_status = 'Overweight'
            else:
                bmi_status = "Obese"

            # Display BMI result and status
            messagebox.showinfo("BMI", f"Your BMI is {bmi}. \nYou are {bmi_status}")

        # Handle input errors
        except ValueError:
            messagebox.showerror("Error", "Please Enter number not string")


# GUI setup
app = Tk()
app.title("BMI Calculator")
app.geometry("400x300")
app.config(padx=10, pady=10)

# Labels and Entry fields for weight and height
app_title = Label(app, text="BMI Calculator", font=("nectar bold", 18))
app_title.pack()

weight_label = Label(app, text="Enter your weight(KG)", font=("aria", 12))
weight_label.pack(pady=15)

weight_entry = Entry(app, borderwidth=2, relief=GROOVE, font='aria')
weight_entry.pack()

height_label = Label(app, text="Enter your height(M & CM)", font=("aria", 12))
height_label.pack(pady=15)

height_entry = Entry(app, borderwidth=2, relief=GROOVE, font='aria')
height_entry.pack()

# Button to trigger BMI calculation
calculate_button = Button(app, text="Calculate", font=('aria', 12), borderwidth=2, relief=GROOVE,
                          command=bmi_calculator)
calculate_button.pack(pady=10)

# Developer label
developer_label = Label(app, text="Made by Ilia keshavarz", font=("nectar bold", 10), fg='#212121')
developer_label.pack(pady=10)

# Start the GUI event loop
app.mainloop()
