import streamlit as st

col_title1, col_title2 = st.columns([2, 1])
with col_title1:
    st.markdown("## 🏋️ BMI Calculator")
with col_title2:
    st.markdown("## Reference")

st.write("Made by Charles Edquila")

col1, col2 = st.columns([2, 1])

with col1:
    name = st.text_input("Name", placeholder="Enter your name")
    weight_str = st.text_input("Weight (kg)", placeholder="Enter your weight")
    height_ft = st.text_input("Height (ft)", placeholder="e.g., 5'4")

    if st.button("Calculate BMI"):
        try:
            if not weight_str:
                st.warning("⚠️ Please enter your weight")
                st.stop()
            weight = float(weight_str)

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

with col2:
    st.markdown("### BMI Reference Guide")
    st.markdown("""
| Category        | BMI Range (kg/m²) |
|-----------------|-----------------|
| Underweight     | < 18.5          |
| Normal Weight   | 18.5 – 24.9     |
| Overweight      | 25 – 29.9       |
| Obese           | ≥ 30            |
""")
