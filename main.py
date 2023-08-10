import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.geometry("200x200")

def bmi_calculate():
    weight = entry_weight.get()
    height = entry_height.get()
    if weight == "" or height == "":
        tkinter.messagebox.showwarning(title="Warning", message="Please Enter Your Weight and Height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            if bmi <= 18.4:
                result_label.config(text=f"Your BMI is {bmi:.2f}, You are Underweight")
            elif bmi > 18.4 and bmi <= 24.9:
                result_label.config(text=f"Your BMI is {bmi:.2f}, You are Normal")
            elif bmi > 24.9 and bmi <= 39.9:
                result_label.config(text=f"Your BMI is {bmi:.2f}, You are Overweight")
            elif bmi > 39.9:
                result_label.config(text=f"Your BMI is {bmi:.2f}, You are Obese")
        except:
            tkinter.messagebox.showwarning(title="Warning", message="Please Enter Valid Number")

label_weight = Label(root, text="Weight (kg):")
label_weight.pack()

entry_weight = Entry(root, width=12)
entry_weight.pack()

label_height = Label(root, text="Height (cm):")
label_height.pack()

entry_height = Entry(root, width=12)
entry_height.pack()

calculate_button = Button(root, text="Calculate", command=bmi_calculate)
calculate_button.pack()

result_label = Label(root)
result_label.pack()

root.mainloop()