import tkinter as tk
from tkinter import messagebox

# ---------------------- DATA ------------------------------
movies = [
    {"name": "3 Idiots", "timing": "6:00 PM", "price": 150, "audi": 1},
    {"name": "Interstellar", "timing": "9:00 PM", "price": 200, "audi": 2},
    {"name": "Yeh Jawaani Hai Deewani", "timing": "3:00 PM", "price": 120, "audi": 3}
]

seats = {0: [False]*6, 1: [False]*6, 2: [False]*6}
bookings = []
username = ""

# ---------------------- WINDOWS ------------------------------

def reset_system():
    global seats, bookings
    seats = {0: [False]*6, 1: [False]*6, 2: [False]*6}
    bookings = []
    messagebox.showinfo("Reset", "System reset successful!")
    show_movie_selection()

def show_seat_window(movie_idx):
    seat_win = tk.Toplevel(root)
    seat_win.title("Select Seats")

    tk.Label(seat_win,
             text=f"Select Seats for {movies[movie_idx]['name']}",
             font=('Arial', 12)).pack(pady=5)

    seat_buttons = []

    def select_seat(seat_num):
        if seats[movie_idx][seat_num]:
            messagebox.showinfo("Already Booked", "This seat is already booked!")
        else:
            seats[movie_idx][seat_num] = True
            bookings.append((movie_idx, seat_num))
            seat_buttons[seat_num].config(bg='red')
            messagebox.showinfo("Success", f"Seat {seat_num+1} booked!")

    seat_frame = tk.Frame(seat_win)
    seat_frame.pack(pady=10)

    for i in range(len(seats[movie_idx])):
        btn = tk.Button(
            seat_frame,
            text=f"Seat {i+1}",
            width=8,
            bg='green' if not seats[movie_idx][i] else 'red',
            command=lambda i=i: select_seat(i)
        )
        btn.grid(row=0, column=i, padx=5)
        seat_buttons.append(btn)

def show_my_bookings():
    booking_win = tk.Toplevel(root)
    booking_win.title("My Bookings")

    if not bookings:
        tk.Label(booking_win, text="No bookings yet.").pack()
        return

    tk.Label(booking_win, text=f"Bookings for {username}", font=('Arial', 12)).pack(pady=5)

    total_price = 0

    for movie_idx, seat_num in bookings:
        m = movies[movie_idx]
        total_price += m['price']
        info = (
            f"Movie: {m['name']}\n"
            f"Seat: {seat_num + 1}\n"
            f"Time: {m['timing']} | Audi: {m['audi']}\n"
            f"Price: Rs.{m['price']}\n"
        )
        tk.Label(booking_win, text=info, justify='left', relief='ridge', padx=8).pack(pady=4)

    tk.Label(booking_win, text=f"Total Price: Rs.{total_price}", font=('Arial', 12, 'bold')).pack(pady=10)

def show_movie_selection():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome, {username}!", font=('Arial', 14)).pack(pady=10)
    tk.Label(root, text="Choose Your Movie:", font=('Arial', 12)).pack()

    for idx, m in enumerate(movies):
        movie_text = f"{m['name']} | {m['timing']} | Rs.{m['price']} | Audi {m['audi']}"
        tk.Button(root, text=movie_text, width=45,
                  command=lambda idx=idx: show_seat_window(idx)).pack(pady=4)

    tk.Button(root, text="My Bookings", command=show_my_bookings, bg='blue', fg='white').pack(pady=6)
    tk.Button(root, text="Reset System", command=reset_system, bg='red', fg='white').pack(pady=6)

# ---------------------- USERNAME SCREEN ------------------------------

def enter_system():
    global username
    username = entry_name.get().strip()

    if username == "":
        messagebox.showwarning("Error", "Please enter your name!")
    else:
        show_movie_selection()

def show_welcome_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Movie Ticket Booking System", font=('Arial', 16)).pack(pady=10)
    tk.Label(root, text="Enter your name to continue:").pack(pady=5)

    global entry_name
    entry_name = tk.Entry(root)
    entry_name.pack(pady=5)

    tk.Button(root, text="Enter", command=enter_system, width=15).pack(pady=10)

# ---------------------- MAIN ------------------------------

root = tk.Tk()
root.title("Movie Ticket Booking System")
root.geometry("480x320")

show_welcome_screen()

root.mainloop()
