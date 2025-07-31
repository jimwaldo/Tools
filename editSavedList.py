#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 8/1/23

@author waldo
A simple program that allows editing of a list that has been saved as a pickle file. The main use for this is to
add or delete names from a list of names that has been created from a Canvas roster. The program assumes that the
list is a list of strings, and that the strings are names of the form "Firstname Lastname". The program will display
the list of names, one per line, and allow highlighting of names to be deleted. It will also allow the addition of
items in a text box. Once the list has been changed, it can be saved to the same filename.
"""
import sys
import tkinter as tk
import tkinter.filedialog as filedialog
import pickle


class ListEditor:
    """
    A class that implements a simple list editor. The list is assumed to be a list of strings. The fields are initialized
    with a root window, which is assumed to be a tk.Tk() object. The list is loaded from a file, which is selected by
    a call to load_file.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("List Editor")

        self.listbox = tk.Listbox(root, width = 30, selectmode=tk.MULTIPLE)
        self.listbox.pack(padx=40, pady=5)

        self.new_item_entry = tk.Entry(root)
        self.new_item_entry.pack(padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add", command=self.add_item)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_items)
        self.delete_button.pack(pady=5)

        self.write_button = tk.Button(root, text="Write", command=self.write_list)
        self.write_button.pack(pady=5)

        self.done_button = tk.Button(root, text="Done", command=root.quit)
        self.done_button.pack(pady=5)

        self.load_file()

    def load_file(self):
        """
        Load a file from the file system. The file is assumed to be a pickle file, and the list is assumed to be a list
        of strings. The file is selected by a call to filedialog.askopenfilename. When the file is selected, the name of
        the file is stored in the field self.file_name, which is the name of the file that will be written when the
        user selects the "write" button.
        :return: None
        """
        file_path = filedialog.askopenfilename()
        try:
            with open(file_path, "rb") as file:
                self.items = pickle.load(file)
            self.display_items()
        except FileNotFoundError:
            print(f"File '{file_path}' not found!")
            self.items = []
        except pickle.UnpicklingError:
            print(f"Invalid pickle file: '{file_path}'")
            self.items = []
        self.file_name = file_path
        self.display_items()
        return None

    def display_items(self):
        """
        Display the items in the listbox. This is called whenever the list is changed.
        :return: None
        """
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)
        return None
    def delete_items(self):
        """
        Delete the items that are highlighted in the listbox.
        :return: None
        """
        selected_indices = self.listbox.curselection()
        selected_items = [self.items[index] for index in selected_indices]
        self.items = [item for item in self.items if item not in selected_items]
        self.display_items()
        return None

    def add_item(self):
        """
        Add the item in the new_item_entry field to the list.
        :return: None
        """
        new_item = self.new_item_entry.get()
        if new_item:
            self.items.append(new_item)
            self.new_item_entry.delete(0, tk.END)
            self.display_items()
        return None

    def write_list(self):
        """
        Write the list to the file that was loaded. This will over-write the previous contents of the file.
        :return: None
        """
        try:
            with open(self.file_name, "wb") as file:
                pickle.dump(self.items, file)
            print("List saved successfully!")
        except Exception as e:
            print(f"Error occurred while writing the file: {str(e)}")
        return None


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    editor = ListEditor(root)
    root.mainloop()
