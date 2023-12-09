import csv
import tkinter as tk

class BMICalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BMI Calculator")
        self.window.configure(bg="black")  # Set background color to black

        # Create labels and entry widgets
        tk.Label(self.window, text="Weight (kg):", bg="black", fg="white").pack()
        self.weight_ent = tk.Entry(self.window)
        self.weight_ent.pack()

        tk.Label(self.window, text="Height (m):", bg="black", fg="white").pack()
        self.height_ent = tk.Entry(self.window)
        self.height_ent.pack()

        # Create Calculate button with larger size
        tk.Button(self.window, text="Calculate", command=self.calculate, width=20, height=2).pack()

        # Create result label
        self.result_var = tk.StringVar()
        tk.Label(self.window, textvariable=self.result_var, fg="green", bg="black").pack()

    def calculate(self):
        # Get weight and height from entry widgets
        weight = float(self.weight_ent.get())
        height = float(self.height_ent.get())

        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)

        # Set result label text based on BMI
        if bmi < 18.5:
            result_text = f"Your BMI: {bmi}\nYour Rank: Underweight\nYou need to gain weight"
        elif 18.5 <= bmi < 24.9:
            result_text = f"Your BMI: {bmi}\nYour Rank: Normal\nYou are great!"
        elif 25 <= bmi < 30:
            result_text = f"Your BMI: {bmi}\nYour Rank: Overweight\nYou need to lose weight"
        elif bmi > 30:
            result_text = f"Your BMI: {bmi}\nYour Rank: Obese\nLose some weight"

        self.result_var.set(result_text)

        # Save data in a CSV file
        with open('bmi_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Write column headers if the file is empty
            if file.tell() == 0:
                writer.writerow(['Weight (kg)', 'Height (m)', 'BMI'])

            writer.writerow([weight, height, bmi])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BMICalculator()
    app.run()