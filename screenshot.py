import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import mss
import datetime

PREVIEW_WIDTH = 300  # Thumbnail width for monitor previews

# Cropping function
def crop_image(image, top, bottom, left, right):
    width, height = image.size
    return image.crop((left, top, width - right, height - bottom))

# Save with DD prefix
def ask_and_save(image):
    today_day = datetime.datetime.now().strftime("%d")
    name = simpledialog.askstring("Save Screenshot", f"Enter name (will be saved as {today_day}-<your_input>.png):")
    if not name:
        return
    filename = f"{today_day}-{name}.png"
    image.save(filename)

# Reload monitor thumbnails
def reload_monitor_previews(container, top_var, bottom_var, left_var, right_var):
    for widget in container.winfo_children():
        widget.destroy()

    top = top_var.get()
    bottom = bottom_var.get()
    left = left_var.get()
    right = right_var.get()

    with mss.mss() as sct:
        monitors = sct.monitors[1:]

        for i, monitor in enumerate(monitors):
            screenshot = sct.grab(monitor)
            image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            cropped = crop_image(image, top, bottom, left, right)

            thumb_height = int(cropped.height * (PREVIEW_WIDTH / cropped.width))
            image_thumb = cropped.resize((PREVIEW_WIDTH, thumb_height))
            image_tk = ImageTk.PhotoImage(image_thumb)

            def on_click(img=cropped):
                ask_and_save(img)

            frame = tk.Frame(container, bg="#f8f8f8", bd=1, relief="solid", padx=8, pady=8)
            frame.grid(row=0, column=i, padx=10, pady=10)

            label = tk.Label(frame, text=f"Monitor {i+1}", font=('Segoe UI', 10, 'bold'), bg="#f8f8f8", fg="#444")
            label.pack()

            btn = tk.Button(frame, image=image_tk, command=on_click, bd=0, relief="flat",
                            bg="#eeeeee", activebackground="#dddddd", cursor="hand2",
                            highlightthickness=0)
            btn.image = image_tk
            btn.pack(pady=(2, 0))

# Main GUI
def display_monitor_selection():
    root = tk.Tk()
    root.title("📸 ScreenShot Capturer")
    root.configure(bg="#f2f2f2")
    root.resizable(True, True)

    # Crop variables
    top_var = tk.IntVar(value=150)
    bottom_var = tk.IntVar(value=80)
    left_var = tk.IntVar(value=0)
    right_var = tk.IntVar(value=0)

    # ------------------- Header -------------------
    header_frame = tk.Frame(root, bg="#f2f2f2")
    header_frame.pack(fill="x", padx=10, pady=10)

    tk.Label(header_frame, text="Cropping (px):", font=("Segoe UI", 10, "bold"), bg="#f2f2f2", fg="#222").pack(side="left", padx=(0, 10))

    def crop_input(label_text, var):
        lbl = tk.Label(header_frame, text=label_text, bg="#f2f2f2", fg="#333", font=("Segoe UI", 10))
        lbl.pack(side="left")
        entry = tk.Entry(header_frame, textvariable=var, width=5,
                         font=("Segoe UI", 10), relief="flat", justify="center",
                         bg="#ffffff", fg="#222", highlightthickness=1, highlightbackground="#cccccc", highlightcolor="#aaaaaa", bd=1)
        entry.pack(side="left", padx=(2, 12))

    crop_input("Top", top_var)
    crop_input("Bottom", bottom_var)
    crop_input("Left", left_var)
    crop_input("Right", right_var)

    # Rounded-style Refresh Button
    refresh_btn = tk.Button(
        header_frame, text="🔄 Refresh", font=("Segoe UI", 10, "bold"),
        bg="#2741d8", fg="#ffffff", activebackground="#6ac7ca", activeforeground="#ffffff",
        relief="flat", padx=14, pady=4, cursor="hand2",
        command=lambda: reload_monitor_previews(content_frame, top_var, bottom_var, left_var, right_var),
        bd=0,
        highlightthickness=0
    )
    refresh_btn.pack(side="right", padx=5)

    # ------------------- Preview Grid -------------------
    global content_frame
    content_frame = tk.Frame(root, bg="#f2f2f2")
    content_frame.pack(fill="both", expand=True, padx=10, pady=5)
    content_frame.pack_propagate(True)

    reload_monitor_previews(content_frame, top_var, bottom_var, left_var, right_var)
    root.mainloop()

if __name__ == "__main__":
    display_monitor_selection()
