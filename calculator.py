from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title("CALCULATOR")
calculator.resizable(0, 1)  # remove or change this in order to get different screen sizes

calculator.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\123.ico')

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    def calculateExpression(self):  # python's calculate function
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

    def clearText(self):  # clears input on pressing C on Calculator
        self.replaceText("0")

    def createWidgets(self):
        # Set the background color for the calculator
        self.configure(bg="#2E2E2E")

        # Display Entry
        self.display = Entry(self, font=("Helvetica", 24), borderwidth=0, relief=RAISED, justify=RIGHT, bg="#4B4B4B", fg="white")
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        # Button configuration
        button_font = ("Helvetica", 18)
        button_padx = 20
        button_pady = 20
        button_bg = "#3C3C3C"
        button_fg = "white"

        # This is the First Row
        self.sevenButton = Button(self, font=button_font, text="7", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=button_font, text="8", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=button_font, text="9", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

        self.timesButton = Button(self, font=button_font, text="*", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

        self.clearButton = Button(self, font=button_font, text="C", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")

        # This is the Second Row
        self.fourButton = Button(self, font=button_font, text="4", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")

        self.fiveButton = Button(self, font=button_font, text="5", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")

        self.sixButton = Button(self, font=button_font, text="6", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")

        self.divideButton = Button(self, font=button_font, text="/", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")

        self.percentageButton = Button(self, font=button_font, text="%", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE")

        # This is the Third Row
        self.oneButton = Button(self, font=button_font, text="1", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0, sticky="NWNESWSE")

        self.twoButton = Button(self, font=button_font, text="2", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1, sticky="NWNESWSE")

        self.threeButton = Button(self, font=button_font, text="3", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2, sticky="NWNESWSE")

        self.minusButton = Button(self, font=button_font, text="-", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")

        self.equalsButton = Button(self, font=button_font, text="=", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)

        # This is the Fourth Row
        self.zeroButton = Button(self, font=button_font, text="0", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="NWNESWSE")

        self.dotButton = Button(self, font=button_font, text=".", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4, column=2, sticky="NWNESWSE")

        self.plusButton = Button(self, font=button_font, text="+", borderwidth=0, padx=button_padx, pady=button_pady, bg=button_bg, fg=button_fg, command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")

app = Application(calculator).grid()
calculator.mainloop()
