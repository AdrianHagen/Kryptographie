import tkinter as tk

def count_letters():
    text = inputbox.get().lower()

    buchstaben_dict = {}

    for char in text:
        if char.isalpha():
            if char in buchstaben_dict:
                buchstaben_dict[char] += 1
            else:
                buchstaben_dict[char] = 1

    outputbox_list.delete("1.0", tk.END)
    outputbox_list.insert(tk.END, "Buchstaben im Text:\n")
    sorted_buchstaben_dict = dict(sorted(buchstaben_dict.items(), key=lambda x:x[1], reverse=True))
    
    total_number_letters = len(text.replace(" ", ""))
    index_of_coincidence = 0
    
    for buchstabe, anzahl in sorted_buchstaben_dict.items():
        outputbox_list.insert(tk.END, buchstabe + " : " + str(anzahl) + "\n")
        index_of_coincidence += (anzahl/total_number_letters) ** 2

    outputbox_idx.insert(tk.END, "Koinzidenzindex = " + str(index_of_coincidence))    

fenster = tk.Tk()
fenster.title("Buchstaben zählen")

inputbox = tk.Entry(fenster, width=50)
inputbox.pack(padx=10, pady=10)

button = tk.Button(fenster, text="Zähle Buchstaben", command=count_letters)
button.pack(padx=10, pady=5)

outputbox_list = tk.Text(fenster, width=50, height=20)
outputbox_list.pack(padx=50, pady=50)

outputbox_idx = tk.Text(fenster, width=50, height=1)
outputbox_idx.pack(padx=10, pady=10)

fenster.mainloop()