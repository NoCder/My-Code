import math
from tkinter import messagebox
from customtkinter import *
from CTkTable import *
import dictionary as dic

#Krāsas:
#Default customtkinker  BG:     #242424
#                       Frame:  #2b2b2b
#Custom                 FG:     #222222
#                       Green:  #00bc8c
#                       Red:    #e74c3c           

#Window Configure
app = CTk()
app.minsize(1000, 600); app.maxsize(1000, 600)
app.iconbitmap(default="book_icon.ico")
app.title("Book Managment System")


#Variables
add_open = False
edit_open = False
table_head = [["Title", "Author", "ISBN", "Price", "Quanity in stock"]]
page = 1
nr_pages = 0
table_list = None
selected_book = None
filtered_data = []


#Update dictionary [Overwritting]
def update_dic():
    with open("dictionary.py", "w", encoding="utf-8") as file:
        file.write("book = [\n")
        for item in dic.book:
            file.write(f"   {item},\n")
        file.write("]\n")      

#Open a frame where can add/register a book
def open_addFrame():
    global add_open
    if add_open:
        add_fr.place_configure(relx=1)
        add_open = False
    else:
        add_fr.place_configure(relx=0)
        add_open = True

#Open a frame where can edit a selected book
def open_editFrame(cellInfo):
    row = cellInfo["row"]
    column = cellInfo["column"]
    global selected_book, filtered_data

    # Check if there is any filtered data, if yes, then takes list from filtered_data instead dictionary
    if filtered_data:
        if row >= 0 and row < len(filtered_data) and column >= 0 and column < 5:
            try:
                selected_book = filtered_data[row + (10 * (page - 1))]
            except Exception as e:
                print(f"An error occurred: {e}")
                return
    else:
        if row >= 0 and row < len(dic.book) and column >= 0 and column < 5:
            try:
                selected_book = dic.book[row + (10 * (page - 1))]
            except Exception as e:
                print(f"An error occurred: {e}")
                return

    # Clear the edit frame fields
    edit_title_inp.delete(0, "end")
    edit_author_inp.delete(0, "end")
    edit_isbn_inp.delete(0, "end")
    edit_price_inp.delete(0, "end")
    edit_quantity_inp.delete(0, "end")

    # Update the edit frame fields with book data
    edit_title_inp.insert(0, selected_book[0])
    edit_author_inp.insert(0, selected_book[1])
    edit_isbn_inp.insert(0, selected_book[2])
    edit_price_inp.insert(0, selected_book[3])
    edit_quantity_inp.insert(0, selected_book[4])

    # Display the edit book frame
    edit_fr.place_configure(relx=0)

#Close a edit frame
def close_editFrame():
    edit_fr.place_configure(relx=1)
    edit_error_msg.configure(text=" ")
    global selected_book; selected_book = None

# Function to divide dictionary and return a list of books based on page
def divide_dic(page, filtered_books=None):
    global nr_pages
    if filtered_books is not None:
        nr_pages = math.ceil(len(filtered_books) / 10)

        start_idx = (page - 1) * 10
        end_idx = start_idx + 10

        return filtered_books[start_idx:end_idx]
    else:
        nr_pages = math.ceil(len(dic.book) / 10)

        start_idx = (page - 1) * 10
        end_idx = start_idx + 10

        return dic.book[start_idx:end_idx]

# Bottom bar buttons (Previous and Next)
def go_previous():
    global page, filtered_data
    if page > 1:
        page -= 1
        create_tableView(page, filtered_data if filtered_data else None)

def go_next():
    global page, filtered_data
    if page < nr_pages:
        page += 1
        create_tableView(page, filtered_data if filtered_data else None)

# Function for searching then update table view
def search_books():
    global page, filtered_books
    search_text = src_bar.get()
    filter_type = src_fltr.get()

    if not search_text.strip():
        reset_table()
        return
        
    if filter_type == "Title":
        filtered_books = [book for book in dic.book if search_text.lower() in book[0].lower()]
    elif filter_type == "Author":
        filtered_books = [book for book in dic.book if search_text.lower() in book[1].lower()]
    elif filter_type == "ISBN":
        filtered_books = [book for book in dic.book if search_text.lower() in book[2].lower()]

    if not filtered_books:
        messagebox.showerror("Error", f"There is no book you searched by {filter_type}")
        return

    create_tableView(1, filtered_books)  # Always start from page 1 with filtered data
    reset_bt.configure(state="normal")  # Enable the reset button
    page = 1  # Reset to page 1

# Function to reset the table view to the full list [to dictionary]
def reset_table():
    global page
    create_tableView(1)  # Always start from page 1 with the full list
    reset_bt.configure(state="disabled")  # Disable the reset button
    page = 1  # Reset to page 1

#Starter window GUI design
#Top bar frame
top_fr = CTkFrame(app, corner_radius=0)
top_fr.place(relwidth=1, relheight=0.1)

src_bar = CTkEntry(top_fr, corner_radius=0, placeholder_text="Search...")
src_bar.place(anchor="w", relx=0.01, rely=0.5, relwidth=0.25)

src_fltr = CTkComboBox(top_fr, corner_radius=0, values=["Title", "Author", "ISBN"], state="readonly", justify="center")
src_fltr.set("Title")
src_fltr.place(anchor="w", relx=0.26, rely=0.5, relwidth=0.1)

src_bt = CTkButton(top_fr, corner_radius=0, text="Search", fg_color="transparent", border_color="gray", border_width=2, hover_color="#222222", command=search_books)
src_bt.place(anchor="w", relx=0.37, rely=0.5, relwidth=0.07)

reset_bt = CTkButton(top_fr, corner_radius=0, text="Reset", fg_color="transparent", border_color="gray", border_width=2, hover_color="#222222", state="disabled", command=reset_table)
reset_bt.place(anchor="w", relx=0.45, rely=0.5, relwidth=0.07)

add_bt = CTkButton(top_fr, corner_radius=0, text="ADD", fg_color="transparent", border_color="#00bc8c", border_width=2, hover_color="#222222", command=open_addFrame)
add_bt.place(anchor="e", relx=0.99, rely=0.5, relwidth=0.07)


#Table list frames (List and bottom buttons)
lst_fr = CTkFrame(app, corner_radius=0, fg_color="#242424")
lst_fr.place(rely=0.1, relwidth=1, relheight=0.8)

table_top = CTkTable(master=lst_fr, corner_radius=0, row=1, column=5, color_phase="horizontal", header_color="#242424", values=table_head, font=("default", 15, "bold"), )
table_top.pack(fill="x", anchor="s", pady=5)

bottom_fr = CTkFrame(app, corner_radius=0)
bottom_fr.place(rely=0.9, relwidth=1, relheight=0.1)

page_nr = CTkLabel(bottom_fr, corner_radius=0, text="1/1")
prev_bt = CTkButton(bottom_fr, corner_radius=0, text="Previous", fg_color="transparent", border_color="#e74c3c", border_width=2, hover_color="#222222", state="disabled", command=go_previous)
next_bt = CTkButton(bottom_fr, corner_radius=0, text="Next", fg_color="transparent", border_color="#00bc8c", border_width=2, hover_color="#222222", command=go_next)

page_nr.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.1)
prev_bt.place(anchor="e", relx=0.4, rely=0.5, relwidth=0.1)
next_bt.place(anchor="w", relx=0.6, rely=0.5, relwidth=0.1)


# Function to create a table view of books based on the current page and {if} filtered
def create_tableView(page, filtered_books=None):
    global table_list, filtered_data
    if table_list:
        table_list.destroy()  # Destroy the existing table

    # Get a list of books for the current page
    if filtered_books is not None:
        books = divide_dic(page, filtered_books)
        filtered_data = filtered_books  # Update the filtered data
        num_pages = int(len(books) / 10) + 1 
    else:
        books = divide_dic(page)  # Use the original data for pagination
        filtered_data = []  # Clear the filtered data
        num_pages = int(len(dic.book) / 10) + 1 

    # Create a new table for the current page
    table_list = CTkTable(master=lst_fr, corner_radius=0, row=10, column=5, color_phase="horizontal", values=books, hover_color="#222222", command=open_editFrame)
    table_list.pack(expand=True, fill="both", pady=10)
    
    # Update the page number label
    page_nr.configure(text=f"{page}/{num_pages}")
    
    #Update Next/Previous Buttons
    prev_bt.configure(state="disabled" if page == 1 else "normal", border_color="#e74c3c" if page == 1 else "#00bc8c")
    next_bt.configure(state="disabled" if page >= nr_pages or nr_pages == 1 else "normal", border_color="#e74c3c" if page >= nr_pages else "#00bc8c")
    
create_tableView(1) #Start as first page of dicionary list

# Function to add a book and then update the dictionary in real-time
def create_book():
    title = add_title_inp.get()
    author = add_author_inp.get()
    isbn = add_isbn_inp.get()
    price = add_price_inp.get()
    quantity = add_quantity_inp.get()

    # Check if all fields are filled
    if isbn:
        # Set default values if not provided
        title = title if title else "Unknown Title"
        author = author if author else "Unknown Author"
        price = price if price else "0.00"
        quantity = quantity if quantity else "1"

        # Check if ISBN is a 13-digit integer
        if not ((isbn.isdigit() and len(isbn) == 13)):
            # Display an error message and change border color for ISBN input
            add_error_msg.configure(text="ISBN must be a 13-digit long numbers.")
            add_isbn_inp.configure(border_color="#e74c3c")
            return  # Exit the function without adding the book

        try:
            price = f'{float(price):.2f}'
        except ValueError:
            add_error_msg.configure(text="Price must be a numbers.")
            add_price_inp.configure(border_color="#e74c3c")
            return
        add_price_inp.configure(border_color="grey")
        
        try:
            quantity = int(quantity)
        except ValueError:
            add_error_msg.configure(text="Quantity must be a whole number.")
            add_quantity_inp.configure(border_color="#e74c3c")
            return
        add_quantity_inp.configure(border_color="grey")
        
        # Check if a book with the same ISBN already exists
        for book in dic.book:
            if book[2] == isbn:
                # Display an error message and change border color
                add_error_msg.configure(text="ISBN already exists.")
                add_isbn_inp.configure(border_color="#e74c3c")
                return  # Exit the function without adding the book

        new_book = [title, author, isbn, price, quantity]
        dic.book.append(new_book)
        update_dic()  # Update the dictionary file in real-time
        create_tableView(page)  # Refresh the table view
        open_addFrame()  # Close the add book frame
        
        #Correct state
        add_isbn_inp.configure(border_color="grey")
        add_error_msg.configure(text=" ")
    else:
        # Display an error message or handle the incomplete input
        add_error_msg.configure(text="Please fill in ISBN field. ISBN must be a 13-digit long numbers.")
        add_isbn_inp.configure(border_color="#e74c3c")

# Function to edit a book and then update the dictionary in real-time
def edit_book():
    title = edit_title_inp.get()
    author = edit_author_inp.get()
    new_isbn = edit_isbn_inp.get()
    price = edit_price_inp.get()
    quantity = edit_quantity_inp.get()

    # Check if all fields are filled
    if title and author and new_isbn:
        # Check if the new ISBN is different from the original ISBN
        if new_isbn != selected_book[2]:
            # Check if the new ISBN already exists
            for book in dic.book:
                if book[2] == new_isbn:
                    edit_error_msg.configure(text="ISBN already exists.")
                    return

        try:
            price = f'{float(price):.2f}'
        except ValueError:
            edit_error_msg.configure(text="Price must be a numbers.")
            edit_price_inp.configure(border_color="#e74c3c")
            return
        edit_price_inp.configure(border_color="grey")
        
        try:
            quantity = int(quantity)
        except ValueError:
            edit_error_msg.configure(text="Quantity must be a whole number.")
            edit_quantity_inp.configure(border_color="#e74c3c")
            return
        edit_quantity_inp.configure(border_color="grey")
        
        # Update the book data
        selected_book[0] = title
        selected_book[1] = author
        selected_book[2] = new_isbn
        selected_book[3] = price
        selected_book[4] = quantity

        # Update the dictionary file in real-time
        update_dic()

        # Refresh the table view
        create_tableView(page)

        # Close the edit book frame
        close_editFrame()
        add_error_msg.configure(text=" ")
    else:
        # Display an error message or handle incomplete input
        edit_error_msg.configure(text="Please fill in the Title, Author, and ISBN fields.")

#Function to delete a selected book from dictionary
def delete_book():
    global selected_book
    result = messagebox.askyesno("Delete Book", "Are you sure you want to delete this book?")
    if result:
        dic.book.remove(selected_book)
        update_dic()  # Update the dictionary file in real-time
        create_tableView(page)  # Refresh the table view
        close_editFrame()

#Add book frame GUI Design (Toggable by open_addFrame)
add_fr = CTkFrame(app, corner_radius=0)
add_fr.place(relwidth=1, relheight=1, relx=1)

inp_fr = CTkFrame(add_fr, corner_radius=0, width=500, height=300, bg_color="#242424")
inp_fr.place(anchor="center", relx=0.5, rely=0.5)

top_lbl = CTkLabel(inp_fr, text="Add a book", font=("default", 20), anchor="w")
top_lbl.place(anchor="n", rely=0.05, relx=0.5, relwidth=0.9)

add_title_inp = CTkEntry(inp_fr, corner_radius=0, placeholder_text="Title", border_color="grey")
add_title_inp.place(relx=0.05, rely=0.2, relwidth=0.425)

add_author_inp = CTkEntry(inp_fr, corner_radius=0, placeholder_text="Author", border_color="grey")
add_author_inp.place(relx=0.525, rely=0.2, relwidth=0.425)

add_isbn_inp = CTkEntry(inp_fr, corner_radius=0, placeholder_text="ISBN Code", border_color="grey")
add_isbn_inp.place(relx=0.05, rely=0.35, relwidth=0.425)

add_price_inp = CTkEntry(inp_fr, corner_radius=0, placeholder_text="Price", border_color="grey")
add_price_inp.place(relx=0.525, rely=0.35, relwidth=0.2)

add_quantity_inp = CTkEntry(inp_fr, corner_radius=0, placeholder_text="Quanity", border_color="grey")
add_quantity_inp.place(relx=0.75, rely=0.35, relwidth=0.2)

add_create_bt = CTkButton(inp_fr, corner_radius=0, text="Add", fg_color="transparent", border_color="#00bc8c", border_width=2, hover_color="#222222", command=create_book)
add_create_bt.place(relx=0.525, rely=0.5, relwidth=0.2)

add_cancel_bt = CTkButton(inp_fr, corner_radius=0, text="Cancel", fg_color="transparent", border_color="#e74c3c", border_width=2, hover_color="#222222", command=open_addFrame)
add_cancel_bt.place(relx=0.75, rely=0.5, relwidth=0.2)

add_error_msg = CTkLabel(inp_fr, corner_radius=0, text=" ", fg_color="transparent", text_color="#e74c3c")
add_error_msg.place(relx=0.05, rely=0.65, relwidth=0.9)

#Edit book frame GUI Design (Toggable by open_editFrame, close_editFrame)
edit_fr = CTkFrame(app, corner_radius=0)
edit_fr.place(relwidth=1, relheight=1, relx=1)

inp_fr2 = CTkFrame(edit_fr, corner_radius=0, width=500, height=300, bg_color="#242424")
inp_fr2.place(anchor="center", relx=0.5, rely=0.5)

top_lbl = CTkLabel(inp_fr2, text="Edit a book", font=("default", 20), anchor="w")
top_lbl.place(anchor="n", rely=0.05, relx=0.5, relwidth=0.9)

edit_title_inp = CTkEntry(inp_fr2, corner_radius=0, placeholder_text="Title", border_color="grey")
edit_title_inp.place(relx=0.05, rely=0.2, relwidth=0.425)

edit_author_inp = CTkEntry(inp_fr2, corner_radius=0, placeholder_text="Author", border_color="grey")
edit_author_inp.place(relx=0.525, rely=0.2, relwidth=0.425)

edit_isbn_inp = CTkEntry(inp_fr2, corner_radius=0, placeholder_text="ISBN Code", border_color="grey")
edit_isbn_inp.place(relx=0.05, rely=0.35, relwidth=0.425)

edit_price_inp = CTkEntry(inp_fr2, corner_radius=0, placeholder_text="Price", border_color="grey")
edit_price_inp.place(relx=0.525, rely=0.35, relwidth=0.2)

edit_quantity_inp = CTkEntry(inp_fr2, corner_radius=0, placeholder_text="Quanity", border_color="grey")
edit_quantity_inp.place(relx=0.75, rely=0.35, relwidth=0.2)

edit_edit_bt = CTkButton(inp_fr2, corner_radius=0, text="Edit", fg_color="transparent", border_color="#00bc8c", border_width=2, hover_color="#222222", command=edit_book)
edit_edit_bt.place(relx=0.525, rely=0.5, relwidth=0.2)

edit_cancel_bt = CTkButton(inp_fr2, corner_radius=0, text="Cancel", fg_color="transparent", border_color="#e74c3c", border_width=2, hover_color="#222222", command=close_editFrame)
edit_cancel_bt.place(relx=0.75, rely=0.5, relwidth=0.2)

edit_delete_bt = CTkButton(inp_fr2, corner_radius=0, text="Delete", fg_color="transparent", border_color="#e74c3c", border_width=2, command=delete_book)
edit_delete_bt.place(relx=0.75, rely=0.65, relwidth=0.2)

edit_error_msg = CTkLabel(inp_fr2, corner_radius=0, text=" ", fg_color="transparent", text_color="#e74c3c")
edit_error_msg.place(relx=0.05, rely=0.8, relwidth=0.9)

#Run in loop until closed
app.mainloop()