from tkinter import *

#defines future click command
def click():
    entered_text=TextEntry.get()
    entered_text = entered_text.lower()
    output.delete(0.0, END)
    try:

        definition = dictionary[entered_text]
    except:
        definition = "You do not wish to know."
    output.insert(END, definition)

#creates window
window = Tk()
window.title("The All Knowing Ape")
window.configure(background="gray")
window.resizable(0,0)
photo1 = PhotoImage(file="GORBA.png")
Label(window, image=photo1, bg="gray") .grid(row=0, column=0, sticky=E)
#provides a label
Label(window, text="THE ALL KNOWING APE.  ", bg="black", fg="white", font="NSimSun 12 bold") .grid(row=1, column=0, sticky=W)


TextEntry = Entry(window, width=20, bg="white", fg="black",font="NSimSun 12 bold",)
TextEntry.grid(row=2, column=0, sticky=W)


Button(window, text="Enter", command=click, width=6) .grid(row=3, column=0, sticky=W)
Label(window, text="\nDefinition.  ", bg="black", fg="white", font="NSimSun 12 bold") .grid(row=4, column=0, sticky=W,)
#gives definition
output = Text(window, width=75, height=6, wrap=WORD, background="white",font="NSimSun 12 bold")
output.grid(row=5, column=0, columnspan=2,sticky=W)
dictionary = {
    "banana": "A banana is an elongated, edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus Musa. In some countries, bananas used for cooking may be called plantains, distinguishing them from dessert bananas.",}



window.mainloop()