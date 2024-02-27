# Python program to create a simple GUI 
# weight converter using Tkinter
from tkinter import *

# Create a GUI window
window = Tk()
window.title("Weight Converter")

# Function to convert weight given in kg to grams, pounds, and ounces
def from_kg():
    # Get the value from the entry widget
    kg_value = float(entry_kg.get())

    # Convert to grams, pounds, and ounces
    grams_value = kg_value * 1000
    pounds_value = kg_value * 2.20462
    ounces_value = kg_value * 35.274

    # Update the text in the result labels
    label_grams.config(text=f"Grams: {grams_value:.2f}")
    label_pounds.config(text=f"Pounds: {pounds_value:.2f}")
    label_ounces.config(text=f"Ounces: {ounces_value:.2f}")

# Create labels, entry widget, and button
label_kg = Label(window, text="Enter Weight in Kg:")
entry_kg = Entry(window)
label_grams = Label(window, text="Grams:")
label_pounds = Label(window, text="Pounds:")
label_ounces = Label(window, text="Ounces:")
button_convert = Button(window, text="Convert", command=from_kg)

# Grid layout to place widgets in table-like structure
label_kg.grid(row=0, column=0, padx=10, pady=10)
entry_kg.grid(row=0, column=1, padx=10, pady=10)
label_grams.grid(row=1, column=0, padx=10, pady=10)
label_pounds.grid(row=1, column=1, padx=10, pady=10)
label_ounces.grid(row=1, column=2, padx=10, pady=10)
button_convert.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
