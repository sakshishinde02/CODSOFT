import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Labels and entry widgets for contact information
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Address:").grid(row=3, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1)

        # Text widget to display contacts
        self.contacts_text = tk.Text(self.master, height=10, width=40)
        self.contacts_text.grid(row=4, column=0, columnspan=2, pady=10)

        # Buttons for actions
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="View Contacts", command=self.view_contacts).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Search Contact", command=self.search_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Update Contact", command=self.update_contact).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact).grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.update_contacts_text()
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contacts_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            self.contacts_text.delete(1.0, tk.END)
            self.contacts_text.insert(tk.END, contacts_list)
        else:
            self.contacts_text.delete(1.0, tk.END)
            self.contacts_text.insert(tk.END, "No contacts available.")

    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            results = [contact for contact in self.contacts if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']]
            if results:
                result_str = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in results])
                self.contacts_text.delete(1.0, tk.END)
                self.contacts_text.insert(tk.END, result_str)
            else:
                self.contacts_text.delete(1.0, tk.END)
                self.contacts_text.insert(tk.END, "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search query.")

    def update_contact(self):
        contact_name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        
        if contact_name:
            matching_contacts = [contact for contact in self.contacts if contact_name.lower() == contact['Name'].lower()]

            if matching_contacts:
                selected_contact = matching_contacts[0]

                field_to_update = simpledialog.askstring("Update Contact", "Enter the field to update (Name, Phone, Email, Address):")
                if field_to_update:
                    field_to_update = field_to_update.capitalize()  # Capitalize the input for consistency

                    if field_to_update in selected_contact:
                        new_value = simpledialog.askstring("Update Contact", f"Enter the new value for {field_to_update}:")
                        if new_value is not None:
                            selected_contact[field_to_update] = new_value

                            self.update_contacts_text()
                            messagebox.showinfo("Success", f"{field_to_update} updated successfully for {contact_name}.")
                            self.clear_entries()
                        else:
                            messagebox.showerror("Error", "Invalid new value. Update canceled.")
                    else:
                        messagebox.showerror("Error", "Invalid field. Update canceled.")
                else:
                    messagebox.showerror("Error", "Field not specified. Update canceled.")
            else:
                messagebox.showerror("Error", f"No contact found with the name '{contact_name}'.")
        else:
            messagebox.showerror("Error", "Please enter the name of the contact to update.")
            
    def delete_contact(self):
        contact_to_delete = simpledialog.askstring("Delete Contact", "Enter the name or phone number of the contact to delete:")

        if contact_to_delete:
            matching_contacts = [contact for contact in self.contacts if
                                contact_to_delete.lower() in contact['Name'].lower() or contact_to_delete in contact['Phone']]
            if matching_contacts:
                # Assuming there is only one matching contact for simplicity
                selected_contact = matching_contacts[0]

                self.contacts.remove(selected_contact)
                self.update_contacts_text()
                messagebox.showinfo("Success", f"Contact '{selected_contact['Name']}: {selected_contact['Phone']}' deleted successfully.")
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"No contact found with the name or phone number '{contact_to_delete}'.")
        else:
            messagebox.showerror("Error", "Please enter the name or phone number of the contact to delete.")


    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def update_contacts_text(self):
        self.view_contacts()  # Refresh the contacts text widget

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
