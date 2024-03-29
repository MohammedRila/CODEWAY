import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number is not allowed."
    return math.sqrt(x)

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation_var.get()

        if choice in ('1', '2', '3', '4', '5'):
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
        elif choice == '6':
            result = sqrt(num1)
        else:
            result = "Invalid input! Please enter a valid choice."

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Invalid input! Please enter valid numbers.")
    except Exception as e:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, str(e))

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")

# Create frames
frame_input = tk.Frame(root)
frame_input.pack(pady=10)
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

# Labels and Entry widgets for input
label_num1 = tk.Label(frame_input, text="Number 1:")
label_num1.grid(row=0, column=0, padx=5)
entry_num1 = tk.Entry(frame_input)
entry_num1.grid(row=0, column=1, padx=5)

label_num2 = tk.Label(frame_input, text="Number 2:")
label_num2.grid(row=1, column=0, padx=5)
entry_num2 = tk.Entry(frame_input)
entry_num2.grid(row=1, column=1, padx=5)

# Radio buttons for operation selection
operation_var = tk.StringVar()
operation_var.set('1')  # Default choice (Addition)

radio_add = tk.Radiobutton(frame_buttons, text="Addition", variable=operation_var, value='1')
radio_add.grid(row=0, column=0, padx=5)
radio_subtract = tk.Radiobutton(frame_buttons, text="Subtraction", variable=operation_var, value='2')
radio_subtract.grid(row=0, column=1, padx=5)
radio_multiply = tk.Radiobutton(frame_buttons, text="Multiplication", variable=operation_var, value='3')
radio_multiply.grid(row=0, column=2, padx=5)
radio_divide = tk.Radiobutton(frame_buttons, text="Division", variable=operation_var, value='4')
radio_divide.grid(row=1, column=0, padx=5)
radio_power = tk.Radiobutton(frame_buttons, text="Power", variable=operation_var, value='5')
radio_power.grid(row=1, column=1, padx=5)
radio_sqrt = tk.Radiobutton(frame_buttons, text="Square Root", variable=operation_var, value='6')
radio_sqrt.grid(row=1, column=2, padx=5)

# Calculate Button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

# Result Entry
entry_result = tk.Entry(root, width=40)
entry_result.pack(pady=10)

# Run the application
root.mainloop()
