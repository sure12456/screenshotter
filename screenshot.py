import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import mss
import datetime

PREVIEW_WIDTH = 300  # Small preview size to fit all monitors
TOP_CROP = 150
BOTTOM_CROP = 80
LEFT_CROP = 0
RIGHT_CROP = 0

# Global reference to main window so we can refresh it
root = None

# Cropping function
def crop_image(image):
    width, height = image.size
    return image.crop((LEFT_CROP, TOP_CROP, width - RIGHT_CROP, height - BOTTOM_CROP))

# Save the image directly with DD- prefix
def ask_and_save(image):
    today_day = datetime.datetime.now().strftime("%d")
    name = simpledialog.askstring("Save Screenshot", f"Enter name (will be saved as {today_day}-<your_input>.png):")
    if not name:
        return
    filename = f"{today_day}-{name}.png"
    image.save(filename)

# Refresh and reload all previews
def reload_monitor_previews(container):
    for widget in container.winfo_children():
        widget.destroy()

    with mss.mss() as sct:
        monitors = sct.monitors[1:]

        for i, monitor in enumerate(monitors):
            screenshot = sct.grab(monitor)
            image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            cropped = crop_image(image)

            thumb_height = int(cropped.height * (PREVIEW_WIDTH / cropped.width))
            image_thumb = cropped.resize((PREVIEW_WIDTH, thumb_height))
            image_tk = ImageTk.PhotoImage(image_thumb)

            def on_click(img=cropped):
                ask_and_save(img)

            frame = tk.Frame(container, borderwidth=2, relief="ridge", padx=5, pady=5)
            frame.grid(row=0, column=i, padx=5, pady=5)

            label = tk.Label(frame, text=f"Monitor {i+1}", font=('Arial', 10))
            label.pack()

            btn = tk.Button(frame, image=image_tk, command=on_click)
            btn.image = image_tk  # hold reference
            btn.pack()

# Main GUI
def display_monitor_selection():
    global root
    root = tk.Tk()
    root.title("Select Monitor to Capture")

    # Refresh button
    refresh_btn = tk.Button(root, text="🔄 Refresh", font=("Arial", 10, "bold"),
                            command=lambda: reload_monitor_previews(content_frame))
    refresh_btn.pack(anchor="ne", padx=10, pady=5)

    # Content area
    global content_frame
    content_frame = tk.Frame(root)
    content_frame.pack()

    reload_monitor_previews(content_frame)
    root.mainloop()

if __name__ == "__main__":
    display_monitor_selection()
