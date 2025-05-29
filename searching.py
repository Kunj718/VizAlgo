import tkinter as tk
from tkinter import messagebox
import time

def linear_search(self , data , root , code_display, step_by_step):

    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        # self.running = False
        return

    code_display.highlight_line(1)
    root.after(t)

    n = len(data)

    code_display.highlight_line(2)
    root.after(t)
    
    for i in range(n):
        
        code_display.highlight_line(2)
        root.after(t)

        if not self.running:
            break
        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)
        
        code_display.highlight_line(3)
        root.after(t)
        
        code_display.highlight_line(4)
        root.after(t)
        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])

            code_display.highlight_line(4)
            root.after(t)    
            return
        
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()
        if i == n-1 and self.target_value!=data[i]:
            messagebox.showinfo("Result", "Value not found in the array.")

    # messagebox.showinfo("Result", "Value not found in the array.")
    # self.update_plot(data, ["yellow" if x == i else "blue" for x in range(n)])

def binary_search(self , data , root , code_display, step_by_step):
    
    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))
    low, high = 0, len(data) - 1

    if step_by_step:
        self.step_event.clear()
        self.step_event.wait()

    code_display.highlight_line(1)
    root.after(t)

    while low <= high and self.running:

        code_display.highlight_line(1)
        root.after(t)
        
        code_display.highlight_line(2)
        root.after(t)

        mid = (low + high) // 2
        
        self.update_plot(data, ["red" if x == mid else "blue" for x in range(len(data))])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(3)
        root.after(t)

        if data[mid] == self.target_value:
            
            code_display.highlight_line(4)
            root.after(t)

            self.update_plot(data, ["green" if x == mid else "blue" for x in range(len(data))])
            return

        code_display.highlight_line(5)
        root.after(t)

        if data[mid] < self.target_value:
            
            code_display.highlight_line(6)
            root.after(t)

            low = mid + 1
        
        code_display.highlight_line(7)
        root.after(t)

        if data[mid] > self.target_value:
            
            code_display.highlight_line(8)
            root.after(t)
            high = mid - 1
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()
    # if low==high and data[mid] != self.target_value:
    if self.running:
        messagebox.showinfo("Result", "Value not found in the array.")

def jump_search(self , data , root , code_display, step_by_step):

    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))
    if step_by_step:
        self.step_event.clear()
        self.step_event.wait()

    n = len(data)

    code_display.highlight_line(1)
    root.after(t)

    step = int(n**0.5)

    code_display.highlight_line(2)
    root.after(t)
    
    prev = 0

    code_display.highlight_line(3)
    root.after(t)

    while data[min(step, n) - 1] < self.target_value and self.running:

        code_display.highlight_line(3)
        root.after(t)

        self.update_plot(data, ["red" if x >= prev and x < min(step, n) else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(4)
        root.after(t)

        prev = step

        code_display.highlight_line(5)
        root.after(t)

        step += int(n**0.5)

        code_display.highlight_line(6)
        root.after(t)

        if prev >= n:
            messagebox.showinfo("Result", "Value not found in the array.")

            code_display.highlight_line(7)
            root.after(t)

            return
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()
    
    code_display.highlight_line(8)
    root.after(t)
 
    for i in range(prev, min(step, n)):

        if not self.running:
            break
        code_display.highlight_line(8)
        root.after(t)

        code_display.highlight_line(9)
        root.after(t)
        code_display.highlight_line(10)
        root.after(t)

        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(12)
        root.after(t)

        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])
            
            code_display.highlight_line(13)
            root.after(t)
            return
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()                      

        if data[i] != self.target_value and i==(min(step,n)-1):
            messagebox.showinfo("Result", "Value not found in the array.")
    code_display.highlight_line(11)
    root.after(t)

