# Minecraft Mod Tester

## Overview
The **Minecraft Mod Tester** is a Python application that facilitates the testing of Minecraft mods. It allows users to easily manage mods, check for dependencies, and determine whether each mod works in the game. If a mod fails to work, the application automatically moves it to a backup folder for easy management.

## Features
- **GUI Interface**: A user-friendly graphical interface for managing and testing Minecraft mods.
- **Mod Dependency Management**: Automatically handles mod dependencies to ensure all necessary files are present.
- **Faulty Mod Handling**: Moves non-working mods back to a specified backup folder for later inspection.
- **Progress Tracking**: Displays progress for testing multiple mods.
- **User Interaction**: Users can indicate whether each mod works, allowing for efficient testing.

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- Basic understanding of file paths in Windows

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Minecraft-Mod-Tester.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Minecraft-Mod-Tester
   ```
3. **Edit Paths**: Ensure that the paths for `mods_source_folder`, `mods_folder`, and `backup_folder` in the code are correctly set according to your system.

## Usage
1. Run the application:
   ```bash
   python mod_tester.py
   ```
2. The GUI will open, showing the status and options for testing mods.
3. Click **Start Testing** to begin. The application will test each mod one by one.
4. For each mod, you will be prompted to indicate whether it works:
   - Click **Yes (It works)** if the mod functions correctly.
   - Click **No (It failed)** if the mod does not work, which will move it to the backup folder.

## Mod Dependencies
The application includes a predefined list of mod dependencies. You can modify the `mod_dependencies` dictionary to include any additional mods and their respective dependencies.

```python
mod_dependencies = {
    "ModA.jar": ["DependencyA1.jar", "DependencyA2.jar"],
    "ModB.jar": ["DependencyB1.jar"],
}
```

## File Structure
- `mod_tester.py`: Main script containing the application logic.
- The folder structure for mods should resemble the following:
    ```
    ├── backup (for faulty mods)
    ├── mods (for active mods)
    └── mods_source_folder (where all mods are initially stored)
    ```

## Troubleshooting
- Ensure that the specified paths in the code are correct.
- If the application does not run, check for Python installation and Tkinter availability.

## License
This project is open source and available under the [MIT License](LICENSE).
