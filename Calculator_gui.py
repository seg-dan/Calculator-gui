# A simple calculator application using tkinter

import tkinter 

# Button layout - each inner list represents a row of buttons
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
# Group buttons by their function for easier styling and handling
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]


row_count = len(button_values) #5
column_count = len(button_values[0]) #4

# Color palette
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False) #Prevent resizing the window
window.attributes('-topmost', True) # Keep the window on top of other windows

frame = tkinter.Frame(window)

# Display label — shows current number, right-aligned like a real calculator
label = tkinter.Label(frame, text="0", anchor="e", bg=color_black, fg=color_white, font=("Arial", 35), width= column_count)

label.grid( row = 0, column = 0 , columnspan = column_count, sticky="we") #columnspan to make the label span across all columns

# --- Build Buttons Dynamically ---
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 20),
                                width = column_count-1, height = 1,
                                command=lambda value=value: button_click(value))
        # Apply color to button type
        if value in top_symbols:
            button.config(bg=color_light_gray, fg=color_black)
        elif value in right_symbols:
            button.config(bg=color_orange, fg=color_white)
        else:
            button.config(bg=color_dark_gray, fg=color_white)

        button.grid(row=row+1, column=column) #row+1 because the row 0 is occupied by the label
                            
frame.pack()

# A+B, A-B, A*B, A/B
A = "0"
B = None
operator = None

# Reset the calculator state
def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None

# Remove unnecessary decimal point for whole numbers
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return num
    
# Handle button clicks
def button_click(value):
    global top_symbols, right_symbols, labels, A, B, operator

    if value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        if value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = str(result)

        if value == "%":
            result = float(label["text"]) / 100
            label["text"] = str(result) 

    elif value == "√":
        result = float(label["text"]) ** 0.5
        label["text"] = str(result)

    elif value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decimal(numA / numB)

                clear_all() #reset A, B, operator after calculation

            
        elif value in "+-×÷": # Store current number as A and wait for second operand
            if operator is not None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            else:
            # Store A on the first operator press too
                A = label["text"]
                label["text"] = "0"
            operator = value

    else: #digits and dot
        if value == ".":
            if value not in label["text"]:
                label["text"] += value #append the dot to the existing number
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace zero with the new digit
            else:
                label["text"] += value #append the new digit to the existing number


#center the window
window.update() #update the window to a new style dimension
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position to place window at center of screen
window_x = (screen_width // 2) - (window_width // 2)
window_y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}" )

window.mainloop()