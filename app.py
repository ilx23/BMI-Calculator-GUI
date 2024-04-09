import math
from tkinter import *
from tkinter import messagebox


def bmi_calculator():
    weight = weight_entry.get()
    height = height_entry.get()
    bmi_status = ''
    if weight == '' or height == '':
        messagebox.showerror("Error", "Please fill all input")
    else:
        try:
            float_weight = float(weight)
            float_height = float(height)

            if float_height > 100:
                float_height = float_height / 100

            bmi = round(float_weight / (float_height ** 2), 2)

            if bmi < 18.5:
                bmi_status = 'Underweight'
            elif 18.5 < bmi < 24.9:
                bmi_status = 'Normal'
            elif 25 < bmi < 29.9:
                bmi_status = 'Overweight'
            else:
                bmi_status = "Obese"

            messagebox.showinfo("BMI", f"Your BMI is {bmi}. \n you are {bmi_status}")

        except ValueError:
            messagebox.showerror("Error", "Please Enter number not string")


app = Tk()
app.title("BMI Calculator")
app.geometry("400x300")
app.config(padx=10, pady=10)

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

calculate_button = Button(app, text="Calculate", font=('aria', 12), borderwidth=2, relief=GROOVE,
                          command=bmi_calculator)
calculate_button.pack(pady=10)

developer_label = Label(app, text="Made by Ilia keshavarz", font=("nectar bold", 10), fg='#212121')
developer_label.pack(pady=10)

app.mainloop()
