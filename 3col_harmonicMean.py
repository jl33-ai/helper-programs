import tkinter as tk
from tkinter import ttk

def triColourMean(c1, c2, c3):
    c1_rgb = (int(c1[:2], 16), int(c1[2:4], 16), int(c1[4:6], 16))
    c2_rgb = (int(c2[:2], 16), int(c2[2:4], 16), int(c2[4:6], 16))
    c3_rgb = (int(c3[:2], 16), int(c3[2:4], 16), int(c3[4:6], 16))

    new_rgb = (round(harmonic_mean(c1_rgb[0], c2_rgb[0], c3_rgb[0]), 2),
               round(harmonic_mean(c1_rgb[1], c2_rgb[1], c3_rgb[1]), 2),
               round(harmonic_mean(c1_rgb[2], c2_rgb[2], c3_rgb[2]), 2))

    return new_rgb

def harmonic_mean(x, y, z):
    return (3 / (1/x + 1/y + 1/z))

def update_color():
    color1 = color1_entry.get()
    color2 = color2_entry.get()
    color3 = color3_entry.get()

    result = triColourMean(color1, color2, color3)
    result_hex = "#{:02x}{:02x}{:02x}".format(int(result[0]), int(result[1]), int(result[2]))

    result_label.config(text="\t\t🎨 Result: " + result_hex)
    canvas_result.config(bg=result_hex)

root = tk.Tk()
root.option_add("*Font", "Courier")
root.title("Hex Colour Averager")

frame_title = ttk.Frame(root)
frame_title.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=1, column=0, sticky=(tk.W, tk.E))

frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=2, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame_title, text="Hex Colour Averager", font=("Courier", 18)).grid(row=0, column=1, sticky=tk.W)

# Add your logo here
original_logo = tk.PhotoImage(file="/Users/justinlee/Documents/Projects & Portfolio/jkhlee/smol.png")  # Replace with your file path

# Downscale the image
scaled_logo = original_logo.subsample(5, 5)  # Downscale by 2x in each dimension

# Add downscaled logo
logo_label = ttk.Label(frame_title, image=scaled_logo)
logo_label.grid(row=0, column=0, sticky=tk.E, padx=15, pady=15)

color1_entry = ttk.Entry(frame_input, width=10)
color1_entry.grid(row=0, column=1)
color1_entry.insert(0, "de213d")

color2_entry = ttk.Entry(frame_input, width=10)
color2_entry.grid(row=0, column=3)
color2_entry.insert(0, "9803f8")

color3_entry = ttk.Entry(frame_input, width=10)
color3_entry.grid(row=0, column=5)
color3_entry.insert(0, "b9fb8c")

ttk.Label(frame_input, text="Colour 1:").grid(row=0, column=0)
ttk.Label(frame_input, text="Colour 2:").grid(row=0, column=2)
ttk.Label(frame_input, text="Colour 3:").grid(row=0, column=4)

calculate_button = ttk.Button(frame_output, text="Calculate", command=update_color)
calculate_button.grid(row=0, column=0, sticky=tk.W)

result_label = ttk.Label(frame_output, text="\t\t🎨 Result: ")
result_label.grid(row=0, column=1, sticky=tk.W)

canvas_result = tk.Canvas(frame_output, width=50, height=50)
canvas_result.grid(row=0, column=2, sticky=tk.E)

root.mainloop()
