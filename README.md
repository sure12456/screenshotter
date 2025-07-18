﻿# 🖼️ Monitor Screenshot Capture Tool

This Python-based GUI tool allows you to quickly capture and save **cropped screenshots** from any of your connected monitors.

Built with **Tkinter**, **mss**, and **Pillow**, it features a modern interface with real-time monitor previews, cropping controls, and auto-naming using the current day.

---

## ✅ Features

- 🖥️ **Live Monitor Previews**  
  Shows updated, cropped thumbnails of all connected monitors.

- ✂️ **Precise Auto-Cropping**  
  Crop away browser bars, taskbars, and side clutter using custom values.

- 🔄 **One-Click Refresh**  
  Instantly reload monitor previews without restarting the app.

- 💾 **Clean File Naming**  
  Prompts you for a filename and saves it with the current day (e.g., `18-mychart.png`).

- 🎨 **Modern GUI Styling**  
  Uses consistent gray tones, rounded buttons, clean typography, and responsive layout.

---

## 📦 Requirements

Install dependencies:

```bash
pip install pillow mss
```

---

## 🚀 How to Use

1. Run the script:

```bash
python main.py
```

2. The app will open with:
   - Input fields to define crop values (top, bottom, left, right)
   - A refresh button to reload previews
   - Thumbnail previews of each monitor

3. Click a monitor preview:
   - It will save a cropped screenshot
   - You’ll be asked for a file name, and it saves as `DD-name.png` (e.g., `18-summary.png`)

4. Update crop values and hit 🔄 **Refresh** to apply.

---

## 🛠️ Crop Configuration (Dynamic)

No need to edit code! You can enter cropping values inside the GUI:
- **Top**: Removes top margin (e.g., browser tab area)
- **Bottom**: Removes taskbar area
- **Left / Right**: Trim sides if needed

---

## 📁 Output

All screenshots are saved in the **current folder** as `.png` files.

---

## 📌 To-Do / Future Enhancements

- [ ] Auto-append timestamp to filename
- [ ] User-defined save directory
- [ ] Drag-and-crop selection tool
- [ ] Export to `.exe` with custom icon
- [ ] Dark mode toggle

---

## 📄 License

MIT License. Free for personal and commercial use. Modify as you like.

---

## 🙌 Credits

Developed with ❤️ using Tkinter, Pillow, and MSS.
