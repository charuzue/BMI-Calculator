import streamlit as st

st.title("🏋️ BMI Calculator")


name = st.text_input("Name", placeholder="Enter your name")
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height_ft = st.text_input("Height (ft)", placeholder="e.g., 5'4")

if st.button("Calculate BMI"):
    try:
        if "'" in height_ft:
            feet, inches = height_ft.split("'")
            feet = float(feet)
            inches = float(inches)
        else:
            st.warning("⚠️ Please enter height in format like 5'4")
            st.stop()

        h_m = (feet * 0.3048) + (inches * 0.0254)
        bmi = weight / (h_m ** 2)

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

        
        st.success(f"{name} has a BMI of {round(bmi, 2)} ({category})")
        st.info(f"Feedback: {feedback}")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
