{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ebecc73-d7ad-41f7-9454-6351600777ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#BMI Calculator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "76c111f0-143d-4b9c-9ae1-a4abd032a79b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9f9a64b7d7744e58a90ea7ca121332c3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Text(value='', description='Name:', placeholder='Enter your name')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4d9ee601f4e040059fec4d898f455e0e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Text(value='', description='Weight (kg):', placeholder='Enter weight')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0e725a16b3e543d48274d6eb1f08deb0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Text(value='', description='Height (ft):', placeholder=\"e.g., 5'4\")"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7dd7e9d96878400a8a181eb7a5530390",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(button_style='info', description='Calculate BMI', style=ButtonStyle())"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "464f354a9f854d52a7bad233f18faa23",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display, clear_output\n",
    "\n",
    "name = widgets.Text(description=\"Name:\", placeholder=\"Enter your name\")\n",
    "weight = widgets.Text(description=\"Weight (kg):\", placeholder=\"Enter weight\")\n",
    "height = widgets.Text(description=\"Height (ft):\", placeholder=\"e.g., 5'4\")\n",
    "button = widgets.Button(description=\"Calculate BMI\", button_style='info')\n",
    "\n",
    "output = widgets.Output()\n",
    "\n",
    "def calculate_bmi(b):\n",
    "    with output:\n",
    "        clear_output()\n",
    "        try:\n",
    "            w = float(weight.value)\n",
    "            h_str = height.value.strip()\n",
    "\n",
    "            if \"'\" in h_str:\n",
    "                feet, inches = h_str.split(\"'\")\n",
    "                feet = float(feet)\n",
    "                inches = float(inches)\n",
    "            else:\n",
    "                print(\"⚠️ Please enter height in format like 5'4\")\n",
    "                return\n",
    "\n",
    "            h_m = (feet * 0.3048) + (inches * 0.0254)\n",
    "            bmi = w / (h_m ** 2)\n",
    "\n",
    "            if bmi < 18.5:\n",
    "                category = \"Underweight\"\n",
    "                feedback = \"Eat more nutritious food and protein to gain healthy weight.\"\n",
    "            elif 18.5 <= bmi <= 24.9:\n",
    "                category = \"Normal Weight\"\n",
    "                feedback = \"Great job! You're maintaining a healthy weight. Keep it up!\"\n",
    "            elif 25 <= bmi <= 29.9:\n",
    "                category = \"Overweight\"\n",
    "                feedback = \"Try exercising regularly and watch your diet.\"\n",
    "            else:\n",
    "                category = \"Obese\"\n",
    "                feedback = \"Exercise daily and focus on healthier meals.\"\n",
    "\n",
    "            print(f\"{name.value} has a BMI of {round(bmi, 2)} ({category})\")\n",
    "            print(f\"Feedback: {feedback}\")\n",
    "\n",
    "        except Exception as e:\n",
    "            print(f\"⚠️ Error: {e}\")\n",
    "\n",
    "button.on_click(calculate_bmi)\n",
    "\n",
    "display(name, weight, height, button, output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4821ed5a-1e5d-47f1-b71b-7815c77beae4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "238a4e44-c1c9-48e8-beef-957b302a06e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
