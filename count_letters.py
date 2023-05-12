import tkinter as tk

def zaehle_buchstaben():
    text = eingabefeld.get()

    buchstaben_dict = {}

    for char in text:
        if char.isalpha():
            if char in buchstaben_dict:
                buchstaben_dict[char] += 1
            else:
                buchstaben_dict[char] = 1

    ausgabefeld.delete("1.0", tk.END)
    ausgabefeld.insert(tk.END, "Buchstaben im Text:\n")
    sorted_buchstaben_dict = dict(sorted(buchstaben_dict.items(), key=lambda x:x[1], reverse=True))
    for buchstabe, anzahl in sorted_buchstaben_dict.items():
        ausgabefeld.insert(tk.END, buchstabe + " : " + str(anzahl) + "\n")

# GUI erstellen
fenster = tk.Tk()
fenster.title("Buchstaben zählen")

# Eingabefeld erstellen
eingabefeld = tk.Entry(fenster, width=50)
eingabefeld.pack(padx=10, pady=10)

# Button erstellen
button = tk.Button(fenster, text="Zähle Buchstaben", command=zaehle_buchstaben)
button.pack(padx=10, pady=5)

# Ausgabefeld erstellen
ausgabefeld = tk.Text(fenster, width=50, height=10)
ausgabefeld.pack(padx=50, pady=50)

# GUI starten
fenster.mainloop()