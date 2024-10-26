import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Paths
mods_source_folder = r"C:\Users\krish\AppData\Roaming\.minecraft\mods\backup"  # Folder where all mods are stored
mods_folder = r"C:\Users\krish\AppData\Roaming\.minecraft\mods"                 # TLauncher mods folder
backup_folder = r"C:\Users\krish\AppData\Roaming\.minecraft\mods\fault"          # Backup folder for faulty mods

# Mod dependencies list (key = mod, value = list of dependent mods)
mod_dependencies = {
    "ModA.jar": ["DependencyA1.jar", "DependencyA2.jar"],
    "ModB.jar": ["DependencyB1.jar"],
}

# List to store faulty mods
faulty_mods = []

def move_mod_to_folder(mod_file):
    """Move a mod and its dependencies (if any) to the mods folder."""
    src = os.path.join(mods_source_folder, mod_file)
    dest = os.path.join(mods_folder, mod_file)
    shutil.copy(src, dest)

    if mod_file in mod_dependencies:
        dependencies = mod_dependencies[mod_file]
        for dep in dependencies:
            dep_src = os.path.join(mods_source_folder, dep)
            dep_dest = os.path.join(mods_folder, dep)
            shutil.copy(dep_src, dep_dest)

def move_mod_back_to_backup(mod_file):
    """Move faulty mod back to the backup folder."""
    src = os.path.join(mods_folder, mod_file)
    dest = os.path.join(backup_folder, mod_file)
    shutil.move(src, dest)
    faulty_mods.append(mod_file)

def test_mod(mod_file, status_label, yes_button, no_button, root):
    """Test a single mod by copying it to the mods folder and asking user if it works."""
    # Clear the mods folder only when testing the first mod
    if not os.listdir(mods_folder):  # Only clear if mods folder is empty
        clear_mods_folder()  # Clear the mods folder of all mods before testing

    move_mod_to_folder(mod_file)

    status_label.config(text=f"Testing mod: {mod_file}. Please start the game and check if it runs.")
    yes_button.config(state="normal")
    no_button.config(state="normal")
    root.update()

def clear_mods_folder():
    """Clear the mods folder of all mods before testing."""
    for filename in os.listdir(mods_folder):
        file_path = os.path.join(mods_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

def start_testing(all_mods, status_label, yes_button, no_button, progress, root, user_input):
    """Start testing all mods one by one."""
    total_mods = len(all_mods)
    for idx, mod in enumerate(all_mods):
        progress['value'] = (idx + 1) / total_mods * 100
        test_mod(mod, status_label, yes_button, no_button, root)
        
        # Wait for user input (yes or no) to proceed
        yes_button.wait_variable(user_input)
        if user_input.get() == "yes":
            # Copy the working mod to the mods folder
            src = os.path.join(mods_source_folder, mod)
            dest = os.path.join(mods_folder, mod)
            shutil.copy(src, dest)
            status_label.config(text=f"Mod '{mod}' is working fine. Copied to mods folder.", fg="green")
        else:
            status_label.config(text=f"Mod '{mod}' caused an error and was moved back to backup.", fg="red")
            move_mod_back_to_backup(mod)

        # Reset buttons for the next mod
        yes_button.config(state="disabled")
        no_button.config(state="disabled")
        root.update()

    messagebox.showinfo("Testing Complete", "All mods have been tested!")

def on_yes_click(user_input):
    """Handle the 'Yes' button click (mod works)."""
    user_input.set("yes")

def on_no_click(user_input):
    """Handle the 'No' button click (mod failed)."""
    user_input.set("no")

def run_gui():
    """Run the GUI application for testing mods."""
    root = tk.Tk()
    root.title("Minecraft Mod Tester")

    # Create UI elements
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    title_label = tk.Label(frame, text="Minecraft Mod Tester", font=("Arial", 16))
    title_label.pack()

    status_label = tk.Label(frame, text="Waiting to start...", font=("Arial", 12))
    status_label.pack(pady=10)

    progress = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    yes_button = tk.Button(frame, text="Yes (It works)", state="disabled", command=lambda: on_yes_click(user_input))
    yes_button.pack(side="left", padx=10)

    no_button = tk.Button(frame, text="No (It failed)", state="disabled", command=lambda: on_no_click(user_input))
    no_button.pack(side="right", padx=10)

    start_button = tk.Button(frame, text="Start Testing", command=lambda: start_testing(all_mods, status_label, yes_button, no_button, progress, root, user_input))
    start_button.pack(pady=20)

    # Get list of all mods in the source folder
    global all_mods
    all_mods = [f for f in os.listdir(mods_source_folder) if f.endswith(".jar")]

    global user_input  # Declare user_input here to make it a global variable
    user_input = tk.StringVar()  # Variable to store user's yes/no input

    root.mainloop()

if __name__ == "__main__":
    run_gui()
