from tkinter import *
from PIL import Image, ImageTk

from Cinemaster.home import load_movie_ui
from BeatVerse.home import load_music_ui
from GameVerse.signin import load_game_ui


def main_desktop():

    root = Tk()
    root.title("My App Desktop")
    root.geometry("950x550+250+150")
    root.configure(bg="#1e1e1e")


    # HEADER (with clickable label)
    header = Frame(root, bg="#2C2C2C", height=60)
    header.pack(fill="x")

    header_label = Label(
        header, text="My App Desktop", fg="white", bg="#2C2C2C",
        font=("Segoe UI", 18, "bold"), cursor="hand2"
    )
    header_label.place(x=20, y=13)


    # MAIN CONTENT AREA
    content = Frame(root, bg="#1e1e1e")
    content.pack(fill="both", expand=True)

    # Clears all widgets from content frame
    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()


    # PAGE LOADERS (Movies / Music / Games)
    def show_movies():
        clear_content()
        ui = load_movie_ui(content)
        ui.pack(fill="both", expand=True)

    def show_music():
        clear_content()
        ui = load_music_ui(content)
        ui.pack(fill="both", expand=True)

    def show_game():
        clear_content()
        ui = load_game_ui(content)
        ui.pack(fill="both", expand=True)


    # IMAGE LOADER UTILITY
    def load_image(path, size=(180, 150)):
        img = Image.open(path).resize(size)
        return ImageTk.PhotoImage(img)


    # MODERN ROUNDED APP CONTAINER
    def create_app_box(parent, title, logo_file, command, x):

        # Rounded frame using Canvas
        rounded = Canvas(parent, width=220, height=260, bg="#1e1e1e",
                         highlightthickness=0)
        rounded.place(x=x, y=80)

        # Draw rounded rectangle
        rounded.create_round_rect = rounded.create_polygon(
            20, 0, 200, 0, 220, 20, 220, 240, 200, 260, 20, 260, 0, 240, 0, 20,
            smooth=True, fill="#2f2f2f"
        )

        # Real container widget placed on top of canvas
        box = Frame(parent, bg="#2f2f2f", width=220, height=260)
        box.place(x=x, y=80)

        # Load logo image from filename
        logo_img = load_image(logo_file)
        logo = Label(box, image=logo_img, bg="#2f2f2f", cursor="hand2")
        logo.image = logo_img
        logo.place(x=20, y=20)

        # App name
        Label(
            box, text=title, fg="white", bg="#2f2f2f",
            font=("Segoe UI", 14, "bold")
        ).place(x=60, y=200)

        # Hover effect
        def on_enter(e):
            box.config(bg="#3a3a3a")
            logo.config(bg="#3a3a3a")

        def on_leave(e):
            box.config(bg="#2f2f2f")
            logo.config(bg="#2f2f2f")

        box.bind("<Enter>", on_enter)
        box.bind("<Leave>", on_leave)

        # Click action
        box.bind("<Button-1>", lambda e: command())
        logo.bind("<Button-1>", lambda e: command())


    # MAIN MENU WITH 3 APP BOXES
    def show_main_menu():
        clear_content()

        create_app_box(content, "Cinemaster", "logo_img.png", show_movies, x=100)
        create_app_box(content, "BeatVerse", "beat_logo.png", show_music, x=365)
        create_app_box(content, "GameVerse", "game_logo.png", show_game, x=630)

    # Click header to return home
    header_label.bind("<Button-1>", lambda e: show_main_menu())

    # Show menu on first load
    show_main_menu()

    root.mainloop()


if __name__ == "__main__":
    main_desktop()
