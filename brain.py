from tkinter import Listbox
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
import pandas as pd
import pyperclip

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Comparrow")
        self.geometry(f"{2000}x{1500}+{0}+{0}")
        self.state('zoomed')

        # self.resizable(False, False)
        self.iconbitmap("yin-yang.ico")
        # self.bind("<Double-Shift_L>", lambda x: self.save_text())
        # self.bind("<Double-Shift_R>", lambda x: self.save_text())

        # configure grid layout (3 columns x 2 rows)
        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # create main entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter an idea...", width=220, font=("Calibri Light", 20))
        self.entry.grid(column=0, row=0, pady=(10, 10))
        self.entry.bind("<Return>", lambda x: self.add_idea(self.entry))

        # create slider
        self.slider = customtkinter.CTkSlider(self, from_=0, to=1, number_of_steps=5, state="disabled", button_color="white", width=220)
        self.slider.grid(column=1, row=0, pady=(10, 10))
        self.slider.set(0)

        # create a rerate button
        self.rerate_button = customtkinter.CTkButton(self, text="Rerate", width=1, font=("Calibri Light", 20), command=self.rerate, fg_color="#141414", hover_color="#EC4E20")
        self.rerate_button.grid(column=2, row=0, padx=(10, 10), pady=(10, 10), sticky="e")

        # create save button
        self.save_button = customtkinter.CTkButton(self, text="Save", width=1, font=("Calibri Light", 20), command=self.save, fg_color="#141414", hover_color="#EC4E20")
        self.save_button.grid(column=0, row=3, padx=(10, 10), sticky="w")

        # create listboxes
        self.listbox1 = Listbox(self, activestyle="none", font=("Calibri Light", 20), background="#141414", selectbackground="#EC4E20", foreground="white", height=20, width=60)
        self.listbox2 = Listbox(self, activestyle="none", font=("Calibri Light", 20), background="#141414", selectbackground="#EC4E20", foreground="white", height=20, width=60)
        self.listbox3 = Listbox(self, activestyle="none", font=("Calibri Light", 20), background="#141414", selectbackground="#EC4E20", foreground="white", height=20, width=60)
        self.listbox1.grid(column=0, row=1, sticky="n", padx=(5, 0))
        self.listbox2.grid(column=1, row=1, sticky="n", padx=(5, 5))
        self.listbox3.grid(column=2, row=1, sticky="n", padx=(0, 5))
        self.listbox1.bind("<Return>", lambda x: self.add_idea(self.listbox1))
        self.listbox2.bind("<Return>", lambda x: self.add_idea(self.listbox2))
        self.listbox1.bind("<Double-BackSpace>", lambda x: self.remove_idea(self.listbox1))
        self.listbox2.bind("<Double-BackSpace>", lambda x: self.remove_idea(self.listbox2))
        self.listbox3.bind("<Double-BackSpace>", lambda x: self.remove_idea(self.listbox3))
        self.listbox1.bind("<Left>", lambda x: self.on_left(self.listbox1))
        self.listbox2.bind("<Left>", lambda x: self.on_left(self.listbox2))
        self.listbox3.bind("<Left>", lambda x: self.on_left(self.listbox3))
        self.listbox1.bind("<Right>", lambda x: self.on_right(self.listbox1))
        self.listbox2.bind("<Right>", lambda x: self.on_right(self.listbox2))
        self.listbox3.bind("<Right>", lambda x: self.on_right(self.listbox3))
        self.listbox1.bind("<Double-Button-1>", lambda x: self.copy_idea(self.listbox1))
        self.listbox2.bind("<Double-Button-1>", lambda x: self.copy_idea(self.listbox2))
        self.listbox3.bind("<Double-Button-1>", lambda x: self.copy_idea(self.listbox3))

        # create regular tkinter textboxes
        # self.textbox1 = Text(self, wrap="none", font=("Calibri Light", 15), background="#141414", foreground="white", width=80, height=20, selectbackground="#EC4E20", insertbackground="white")
        # self.textbox2 = Text(self, wrap="none", font=("Calibri Light", 15), background="#141414", foreground="white", width=80, height=20, selectbackground="#EC4E20", insertbackground="white")
        # self.textbox3 = Text(self, wrap="none", font=("Calibri Light", 15), background="#141414", foreground="white", width=80, height=20, selectbackground="#EC4E20", insertbackground="white")
        # self.textbox1.grid(column=0, row=2, sticky="n", padx=(5, 0))
        # self.textbox2.grid(column=1, row=2, sticky="n", padx=(5, 5))
        # self.textbox3.grid(column=2, row=2, sticky="n", padx=(0, 5))

        # seeding
        self.seed()

    def add_idea(self, sender):
        if sender == self.entry:
            idea = sender.get()
            if idea != "":
                self.listbox1.insert(0, idea)
                self.entry.delete(0, "end")
        elif sender == self.listbox1:
            index = sender.curselection()
            if index:
                cost = round(self.slider.get())
                idea = sender.get(index)
                self.listbox2.insert(0, f"{cost}|{idea}")
                self.listbox1.delete(sender.curselection())
                if sender.get(index):
                    self.listbox1.selection_set(index[0])
                else:
                    self.listbox1.selection_set(index[0] - 1)
        elif sender == self.listbox2:
            index = sender.curselection()
            if index:
                parts = sender.get(index).split("|")
                cost = int(parts[0])
                influence = round(self.slider.get())
                idea = parts[1]
                self.listbox3.insert(0, f"{cost}|{influence}|{idea}")
                self.listbox2.delete(sender.curselection())
                if sender.get(index):
                    self.listbox2.selection_set(index[0])
                else:
                    self.listbox2.selection_set(index[0] - 1)
        self.save()
        self.clear()
        self.seed()

    def remove_idea(self, sender):
        if sender == self.listbox1:
            index = sender.curselection()
            if index:
                self.listbox1.delete(index)
                if sender.get(index):
                    self.listbox1.selection_set(index[0])
                else:
                    self.listbox1.selection_set(index[0] - 1)
        elif sender == self.listbox2:
            index = sender.curselection()
            if index:
                self.listbox2.delete(index)
                if sender.get(index):
                    self.listbox2.selection_set(index[0])
                else:
                    self.listbox2.selection_set(index[0] - 1)
        elif sender == self.listbox3:
            index = sender.curselection()
            if index:
                self.listbox3.delete(index)
                if sender.get(index):
                    self.listbox3.selection_set(index[0])
                else:
                    self.listbox3.selection_set(index[0] - 1)
        self.save()
        self.clear()
        self.seed()

    def copy_idea(self, sender):
        index = sender.curselection()
        if index:
            idea = sender.get(index)
            pyperclip.copy(idea)

    def decrement(self, slider):
        current_value = slider.get()
        if current_value > 0:
            slider.set(current_value - 1)

    def increment(self, slider):
        current_value = slider.get()
        if current_value < 5:
            slider.set(current_value + 1)

    def seed(self):
        # listboxes
        list1_df = pd.read_csv("data/list1.csv")
        list2_df = pd.read_csv("data/list2.csv")
        list3_df = pd.read_csv("data/list3.csv")
        for row in range(len(list1_df)):
            idea = list1_df["idea"][row]
            self.listbox1.insert("end", idea)
        for row in range(len(list2_df)):
            cost = list2_df["cost"][row]
            idea = list2_df["idea"][row]
            self.listbox2.insert("end", f"{cost}|{idea}")
        for row in range(len(list3_df)):
            cost = list3_df["cost"][row]
            influence = list3_df["influence"][row]
            idea = list3_df["idea"][row]
            self.listbox3.insert("end", f"{cost}|{influence}|{idea}")
        
        # textboxes
        # text1_df = pd.read_csv("data/text1.csv")
        # text2_df = pd.read_csv("data/text2.csv")
        # text3_df = pd.read_csv("data/text3.csv")
        # for row in range(len(text1_df)):
        #     text = text1_df["text"][row]
        #     self.textbox1.insert("end", text)
        # for row in range(len(text2_df)):
        #     text = text2_df["text"][row]
        #     self.textbox2.insert("end", text)
        # for row in range(len(text3_df)):
        #     text = text3_df["text"][row]
        #     self.textbox3.insert("end", text)

    def save(self):
        list1_df = pd.DataFrame(columns=["idea"])
        list2_df = pd.DataFrame(columns=["cost", "idea"])
        list3_df = pd.DataFrame(columns=["cost", "influence", "idea"])
        for row in range(self.listbox1.size()):
            idea = str(self.listbox1.get(row))
            list1_df.loc[row] = [idea]
        for row in range(self.listbox2.size()):
            parts = self.listbox2.get(row).split("|")
            cost = int(parts[0])
            idea = str(parts[1])
            list2_df.loc[row] = [cost, idea]
        for row in range(self.listbox3.size()):
            parts = self.listbox3.get(row).split("|")
            cost = int(parts[0])
            influence = int(parts[1])
            idea = str(parts[2])
            list3_df.loc[row] = [cost, influence, idea]
        list2_df.sort_values(by=["cost"], ascending=False, inplace=True)
        list3_df.sort_values(by=["cost", "influence"], ascending=[False, False], inplace=True)
        list1_df.to_csv("data/list1.csv", index=False)
        list2_df.to_csv("data/list2.csv", index=False)
        list3_df.to_csv("data/list3.csv", index=False)

        # save text
        # text1_df = pd.DataFrame(columns=["text"])
        # text2_df = pd.DataFrame(columns=["text"])
        # text3_df = pd.DataFrame(columns=["text"])
        # text1_df.loc[0] = [self.textbox1.get("1.0", "end-1c")]
        # text2_df.loc[0] = [self.textbox2.get("1.0", "end-1c")]
        # text3_df.loc[0] = [self.textbox3.get("1.0", "end-1c")]
        # text1_df.to_csv("data/text1.csv", index=False)
        # text2_df.to_csv("data/text2.csv", index=False)
        # text3_df.to_csv("data/text3.csv", index=False)

    def rerate(self):
        # take all the tasks from the 3rd listbox and put them in the 1st listbox without the numbers and pipes at the start of each task: "|" and digits

        # read the 3rd listbox
        list3_df = pd.DataFrame(columns=["cost", "influence", "idea"])
        for row in range(self.listbox3.size()):
            parts = self.listbox3.get(row).split("|")
            cost = int(parts[0])
            influence = int(parts[1])
            idea = str(parts[2])
            list3_df.loc[row] = [cost, influence, idea]
            # put the tasks in the 1st listbox
            self.listbox1.insert("end", idea)

    def clear(self):
        self.listbox1.delete(0, "end")
        self.listbox2.delete(0, "end")
        self.listbox3.delete(0, "end")
        # self.textbox1.delete("1.0", "end")
        # self.textbox2.delete("1.0", "end")
        # self.textbox3.delete("1.0", "end")

    def on_left(self, listbox):
        self.decrement(self.slider)

    def on_right(self, listbox):
        self.after(1, lambda: listbox.xview_scroll(-1, "units"))
        self.increment(self.slider)

    # def save_text(self):
        # cosmetic changes
        # self.textbox1.config(bg="#EC4E20")
        # self.textbox2.config(bg="#EC4E20")
        # self.textbox3.config(bg="#EC4E20")
        # self.after(400, lambda: self.textbox1.config(bg="#141414"))
        # self.after(400, lambda: self.textbox2.config(bg="#141414"))
        # self.after(400, lambda: self.textbox3.config(bg="#141414"))

        # save text
        # self.save()

if __name__ == "__main__":
    app = App() 
    app.mainloop()
