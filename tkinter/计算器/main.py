import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("汐光计算器")
root.geometry("295x280+100+100")

root.attributes("-alpha",0.9)
# root["background"] = "#ffffff"
font = ("宋体",20)
font_16 = ("宋体",16)

result_num = tk.StringVar()
result_num.set("")

tk.Label(root,
         textvariable=result_num,font=font,height=2
         ).grid(row=1,column=1)

now_num = []

def Input(num):
    result_num.set(result_num.get() + num)
    
def result():
    # equation = f"print({result_num.get()})"
    # print(equation)
    result_num.set(eval(result_num.get()))

# def button_clicked():
#     tk.messagebox.showinfo("massage","hello,world")

def event():
    pass

# btn_width = 10

btn_clear = tk.Button(root,text="C",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_back = tk.Button(root,text="←",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_addition = tk.Button(root,text="+",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_subtraction = tk.Button(root,text="-",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_multiplication = tk.Button(root,text="×",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_division = tk.Button(root,text="÷",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_power = tk.Button(root,text="^",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")
btn_num_0 = tk.Button(root,text="0",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_1 = tk.Button(root,text="1",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_2 = tk.Button(root,text="2",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_3 = tk.Button(root,text="3",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_4 = tk.Button(root,text="4",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_5 = tk.Button(root,text="5",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_6 = tk.Button(root,text="6",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_7 = tk.Button(root,text="7",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_8 = tk.Button(root,text="8",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_num_9 = tk.Button(root,text="9",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_point = tk.Button(root,text=".",width=5,font=font_16,relief=tk.FLAT,bg="#eacda1")
btn_return = tk.Button(root,text="=",width=5,font=font_16,relief=tk.FLAT,bg="#b1b2b2")

btn_clear.grid(row=2,column=1,padx=4,pady=2)
btn_back.grid(row=2,column=2,padx=4,pady=2)
btn_addition.grid(row=5,column=4,padx=4,pady=2)
btn_subtraction.grid(row=4,column=4,padx=4,pady=2)
btn_division.grid(row=2,column=4,padx=4,pady=2)
btn_multiplication.grid(row=3,column=4,padx=4,pady=2)
btn_power.grid(row=2,column=3,padx=4,pady=2)
btn_num_1.grid(row=5,column=1,padx=4,pady=2)
btn_num_2.grid(row=5,column=2,padx=4,pady=2)
btn_num_3.grid(row=5,column=3,padx=4,pady=2)
btn_num_4.grid(row=4,column=1,padx=4,pady=2)
btn_num_5.grid(row=4,column=2,padx=4,pady=2)
btn_num_6.grid(row=4,column=3,padx=4,pady=2)
btn_num_7.grid(row=3,column=1,padx=4,pady=2)
btn_num_8.grid(row=3,column=2,padx=4,pady=2)
btn_num_9.grid(row=3,column=3,padx=4,pady=2)
# btn_num_0.grid(row=6,column=1,padx=4,pady=2)
btn_num_0.grid(row=6,column=2,padx=4,pady=2)
btn_point.grid(row=6,column=3,padx=4,pady=2)
btn_return.grid(row=6,column=4)

btn_addition.config(command=lambda: Input("+"))
btn_subtraction.config(command=lambda: Input("-"))
btn_multiplication.config(command=lambda: Input("×"))
btn_division.config(command=lambda: Input("÷"))
btn_power.config(command=lambda: Input("^"))
btn_num_0.config(command=lambda: Input("0"))
btn_num_1.config(command=lambda: Input("1"))
btn_num_2.config(command=lambda: Input("2"))
btn_num_3.config(command=lambda: Input("3"))
btn_num_4.config(command=lambda: Input("4"))
btn_num_5.config(command=lambda: Input("5"))
btn_num_6.config(command=lambda: Input("6"))
btn_num_7.config(command=lambda: Input("7"))
btn_num_8.config(command=lambda: Input("8"))
btn_num_9.config(command=lambda: Input("9"))
btn_point.config(command=lambda: Input("."))
btn_return.config(command=lambda: result())






# while True:
#     Input(input())

root.mainloop()

