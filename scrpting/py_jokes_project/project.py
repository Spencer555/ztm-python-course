import pyjokes
import tkinter as tk


def get_a_joke():
    return pyjokes.get_joke()


def get_a_group_of_jokes():
    for _ in pyjokes.get_jokes():
        print(_)

    return


# tkinter gui
root = tk.Tk()
root.title("Py Jokes")
# Entry field
entry = tk.Entry(root, width=70, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)


def click_button():
    entry.delete(0, tk.END)
    entry.insert(0, get_a_joke())


def clear_entry():
    entry.delete(0, tk.END)











if __name__ == '__main__':
    


    button = tk.Button(root, text='Get Joke', width=35, height=2, command=click_button)
    button.grid(row=4, column=1)


    # Special case for the clear button
    clear_button = tk.Button(root, text="Clear", width=35, height=2, command=clear_entry)
    clear_button.grid(row=4, column=2)
    root.mainloop()
