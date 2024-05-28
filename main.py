#This creates a simple calculator
import tkinter as tk

#This is to show numbers / result on display/lable
value, first_value, second_value,active_syms ='',0,0,''

def update_value(text):
    nums = ["0","1","2","3","4","5","6","7","8","9","."]
    syms = ["+","-","*","/"]
    fns = ["=","ac"]
    global value,first_value, second_value,active_syms
    global label
    if text in nums:
        value += text

        if not active_syms:
            first_value = float(value)
        else:
            second_value =float(value)


    elif text in syms:

        if first_value and second_value and active_syms:
            val = calculate(first_value,active_syms,second_value)
            if val == 'err':
                value=val
            elif val<1:
                value=val
            else:
                value=round(val)
            active_syms = text
            first_value = value
        else:
            active_syms = text
            value = ''

    elif text in fns:
        if text == "ac":
            first_value,second_value,active_syms,value =0,0,'',''
        elif text == "=":
            if not first_value:
                first_value,second_value,active_syms,value =0,0,'',0
            elif first_value and not active_syms:
                value = first_value
                first_value,second_value,active_syms,=0,0,''
            else:
                val = calculate(first_value,active_syms,second_value)
                if val == 'err':
                    value=val
                elif val<1:
                    value=val
                else:
                    value=round(val)
                # print(value)
        else:
            pass
    else:
        pass
   
    label.config(text=value)



#this calculates 
def calculate(f_val,sym,s_val):
    
    if sym == "+":
        if not s_val: s_val = 0
        return f_val + s_val
    elif sym == "-":
        if not s_val: s_val = 0
        return f_val -s_val
    elif sym == "*":
        if not s_val: s_val = 1
        return f_val * s_val
    elif sym == "/":
        if not s_val: return "err"
        return f_val /s_val

window = tk.Tk()
window.title("Calculator")
window.geometry("276x316")

# this creates the display
label = tk.Label(
    window,
    text=value,
    height=1,
    width=15,
    font=("Arial", 24),
    anchor="e",
    background="white",
    borderwidth=2,
    relief="solid",
)
label.grid(row=0, column=0, columnspan=4) 


#this lays down button
space1 = tk.Label(window,text='').grid(row=2, column=0, columnspan=4)

button_7 = tk.Button(text="7", command=lambda: update_value("7")).grid(row=3, column=0)
button_8 = tk.Button(text="8", command=lambda: update_value("8")).grid(row=3, column=1)
button_9 = tk.Button(text="9", command=lambda: update_value("9")).grid(row=3, column=2)
button_m = tk.Button(text="*", command=lambda: update_value("*")).grid(row=3, column=3)

space2= tk.Label(window,text='').grid(row=4, column=0, columnspan=4)
button_4 = tk.Button(text="4", command=lambda: update_value("4")).grid(row=5, column=0)
button_5 = tk.Button(text="5", command=lambda: update_value("5")).grid(row=5, column=1)
button_6 = tk.Button(text="6", command=lambda: update_value("6")).grid(row=5, column=2)
button_s = tk.Button(text="-", command=lambda: update_value("-")).grid(row=5, column=3)

space3= tk.Label(window,text='').grid(row=6, column=0, columnspan=4)
button_1 = tk.Button(text="1", command=lambda: update_value("1")).grid(row=7, column=0)
button_2 = tk.Button(text="2", command=lambda: update_value("2")).grid(row=7, column=1)
button_3 = tk.Button(text="3", command=lambda: update_value("3")).grid(row=7, column=2)
button_a = tk.Button(text="+", command=lambda: update_value("+")).grid(row=7, column=3)

space4= tk.Label(window,text='').grid(row=8, column=0, columnspan=4)
button_ac = tk.Button(text="AC", command=lambda: update_value("ac")).grid(row=9, column=0)
button_0 = tk.Button(text="0", command=lambda: update_value("0")).grid(row=9, column=1)
button_p = tk.Button(text=".", command=lambda: update_value(".")).grid(row=9, column=2)
button_d = tk.Button(text="/", command=lambda: update_value("/")).grid(row=9, column=3)

space5= tk.Label(window,text='').grid(row=10, column=0, columnspan=4)
button_eq = tk.Button(text="=", command=lambda: update_value("=")).grid(row=11,columnspan=4)


# Add the remaining buttons for your calculator

tk.mainloop()
