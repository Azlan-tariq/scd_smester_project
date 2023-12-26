import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("900x400")  # Increased window size
        self.root.configure(bg="aqua")  # Set background color

        self.employees = []
        self.selected_employee = None

        # Search
        self.label_search = tk.Label(root, text="Search:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_search = tk.Entry(root)
        self.button_search = tk.Button(root, text="Search", command=self.search_employee, bg="aqua", font=('Arial', 10, 'bold'))

        # GUI components
        self.label_name = tk.Label(root, text="Name:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_name = tk.Entry(root, bg="lightgoldenrodyellow")

        self.label_position = tk.Label(root, text="Position:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_position = tk.Entry(root, bg="lightgoldenrodyellow")

        self.label_id = tk.Label(root, text="ID:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_id = tk.Entry(root, bg="lightgoldenrodyellow")

        self.label_address = tk.Label(root, text="Address:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_address = tk.Entry(root, bg="lightgoldenrodyellow")

        self.label_department = tk.Label(root, text="Department:", bg="aqua", font=('Arial', 10, 'bold'))
        self.entry_department = tk.Entry(root, bg="lightgoldenrodyellow")

        self.label_listbox = tk.Label(root, text="Employee List:", bg="aqua", font=('Arial', 12, 'bold'))

        # Table
        self.tree = ttk.Treeview(root, columns=("Name", "Position", "ID", "Address", "Department"), show="headings", selectmode='browse')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Position", text="Position")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Department", text="Department")

        self.tree.column("Name", width=150, anchor='center')
        self.tree.column("Position", width=150, anchor='center')
        self.tree.column("ID", width=100, anchor='center')
        self.tree.column("Address", width=200, anchor='center')
        self.tree.column("Department", width=150, anchor='center')

        self.tree.grid(row=2, column=2, padx=10, pady=10, rowspan=4, columnspan=2)

        # Detail Frame
        self.detail_frame = tk.Frame(root, bg="lightblue", bd=5)  # Change background color here
        self.detail_frame.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.4)

        self.label_detail = tk.Label(self.detail_frame, text="Employee Details:", bg="lightblue", font=('Arial', 12, 'bold'))
        self.label_detail.pack()

        self.label_detail_name = tk.Label(self.detail_frame, text="", font=('Arial', 10))
        self.label_detail_name.pack()

        self.label_detail_position = tk.Label(self.detail_frame, text="", font=('Arial', 10))
        self.label_detail_position.pack()

        self.label_detail_id = tk.Label(self.detail_frame, text="", font=('Arial', 10))
        self.label_detail_id.pack()

        self.label_detail_address = tk.Label(self.detail_frame, text="", font=('Arial', 10))
        self.label_detail_address.pack()

        self.label_detail_department = tk.Label(self.detail_frame, text="", font=('Arial', 10))
        self.label_detail_department.pack()

        # Buttons
        self.button_add = tk.Button(root, text="Add", command=self.add_employee, bg="green", fg="white", font=('Arial', 10, 'bold'))
        self.button_update = tk.Button(root, text="Update", command=self.update_employee, bg="blue", fg="white", font=('Arial', 10, 'bold'))
        self.button_delete = tk.Button(root, text="Delete", command=self.delete_employee, bg="red", fg="white", font=('Arial', 10, 'bold'))

        # Pack components
        self.label_search.grid(row=0, column=0, padx=10, pady=10)
        self.entry_search.grid(row=0, column=1, padx=10, pady=10)
        self.button_search.grid(row=0, column=2, padx=10, pady=10)

        self.label_name.grid(row=1, column=0, padx=10, pady=10)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_position.grid(row=2, column=0, padx=10, pady=10)
        self.entry_position.grid(row=2, column=1, padx=10, pady=10)

        self.label_id.grid(row=3, column=0, padx=10, pady=10)
        self.entry_id.grid(row=3, column=1, padx=10, pady=10)

        self.label_address.grid(row=4, column=0, padx=10, pady=10)
        self.entry_address.grid(row=4, column=1, padx=10, pady=10)

        self.label_department.grid(row=5, column=0, padx=10, pady=10)
        self.entry_department.grid(row=5, column=1, padx=10, pady=10)

        self.label_listbox.grid(row=1, column=2, padx=10, pady=10, rowspan=5)

        self.button_add.grid(row=1, column=4, padx=10, pady=10, sticky="ew")
        self.button_update.grid(row=2, column=4, padx=10, pady=10, sticky="ew")
        self.button_delete.grid(row=3, column=4, padx=10, pady=10, sticky="ew")

        # Initialize employee listbox
        self.update_listbox()

        # Bind the on_select method to the Treeview
        self.tree.bind("<ButtonRelease-1>", self.on_select)

    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            index = selection[0]
            self.selected_employee = self.employees[index]
            self.display_selected_employee()

    def display_selected_employee(self):
        if self.selected_employee:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, self.selected_employee.get('name', ''))

            self.entry_position.delete(0, tk.END)
            self.entry_position.insert(0, self.selected_employee.get('position', ''))

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, self.selected_employee.get('id', ''))

            self.entry_address.delete(0, tk.END)
            self.entry_address.insert(0, self.selected_employee.get('address', ''))

            self.entry_department.delete(0, tk.END)
            self.entry_department.insert(0, self.selected_employee.get('department', ''))

            # Update detail labels
            self.label_detail_name.config(text=f"Name: {self.selected_employee.get('name', '')}")
            self.label_detail_position.config(text=f"Position: {self.selected_employee.get('position', '')}")
            self.label_detail_id.config(text=f"ID: {self.selected_employee.get('id', '')}")
            self.label_detail_address.config(text=f"Address: {self.selected_employee.get('address', '')}")
            self.label_detail_department.config(text=f"Department: {self.selected_employee.get('department', '')}")

    def add_employee(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        employee_id = self.entry_id.get()
        address = self.entry_address.get()
        department = self.entry_department.get()

        if name and position and employee_id and address and department:
            employee = {'name': name, 'position': position, 'id': employee_id, 'address': address, 'department': department}
            self.employees.append(employee)

            self.update_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please enter all details.")

    def update_employee(self):
        if self.selected_employee:
            name = self.entry_name.get()
            position = self.entry_position.get()
            employee_id = self.entry_id.get()
            address = self.entry_address.get()
            department = self.entry_department.get()

            if name and position and employee_id and address and department:
                self.selected_employee['name'] = name
                self.selected_employee['position'] = position
                self.selected_employee['id'] = employee_id
                self.selected_employee['address'] = address
                self.selected_employee['department'] = department

                self.update_listbox()
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "Please enter all details.")
        else:
            messagebox.showwarning("Warning", "Select an employee to update.")

    def delete_employee(self):
        if self.selected_employee:
            self.employees.remove(self.selected_employee)
            self.selected_employee = None

            self.update_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Select an employee to delete.")

    def search_employee(self):
        query = self.entry_search.get().lower()
        if query:
            matching_employees = [employee for employee in self.employees if query in str(employee).lower()]
            self.display_search_results(matching_employees)
        else:
            self.update_listbox()

    def display_search_results(self, results):
        self.tree.delete(*self.tree.get_children())
        for employee in results:
            self.tree.insert("", "end", values=(employee.get('name', ''), employee.get('position', ''), employee.get('id', ''),
                                                employee.get('address', ''), employee.get('department', '')))

    def update_listbox(self):
        self.tree.delete(*self.tree.get_children())
        for employee in self.employees:
            self.tree.insert("", "end", values=(employee.get('name', ''), employee.get('position', ''), employee.get('id', ''),
                                                employee.get('address', ''), employee.get('department', '')))

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_department.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
