import ipywidgets as widgets
from IPython.display import display, clear_output

name = widgets.Text(description="Name:", placeholder="Enter your name")
weight = widgets.Text(description="Weight (kg):", placeholder="Enter weight")
height = widgets.Text(description="Height (ft):", placeholder="e.g., 5'4")
button = widgets.Button(description="Calculate BMI", button_style='info')

output = widgets.Output()

def calculate_bmi(b):
    with output:
        clear_output()
        try:
            w = float(weight.value)
            h_str = height.value.strip()

            if "'" in h_str:
                feet, inches = h_str.split("'")
                feet = float(feet)
                inches = float(inches)
            else:
                print("⚠️ Please enter height in format like 5'4")
                return

            h_m = (feet * 0.3048) + (inches * 0.0254)
            bmi = w / (h_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
                feedback = "Eat more nutritious food and protein to gain healthy weight."
            elif 18.5 <= bmi <= 24.9:
                category = "Normal Weight"
                feedback = "Great job! You're maintaining a healthy weight. Keep it up!"
            elif 25 <= bmi <= 29.9:
                category = "Overweight"
                feedback = "Try exercising regularly and watch your diet."
            else:
                category = "Obese"
                feedback = "Exercise daily and focus on healthier meals."

            print(f"{name.value} has a BMI of {round(bmi, 2)} ({category})")
            print(f"Feedback: {feedback}")

        except Exception as e:
            print(f"⚠️ Error: {e}")

button.on_click(calculate_bmi)

display(name, weight, height, button, output)
