Shot Builder Tool
The Shot Builder Tool is a utility for managing and creating shot compositions in Nuke, tailored for a streamlined VFX pipeline workflow. It dynamically handles projects, episodes, sequences, and shots, allowing for efficient shot-building with reusable master compositions.

Features
Dynamic Project Handling: Supports hierarchical folder structures for projects, episodes, sequences, and shots.
Master Composition Management: Provides tools to manage master compositions and generate child shot compositions.
Automated File Updates: Automatically updates file paths in generated child compositions.
PySide2-Powered GUI: Intuitive user interface for managing workflows with ease.
Folder Structure
The folder structure is designed to organize files efficiently for VFX pipelines. Below is the expected structure:

bash
Copy code
D:\Sample Production
├── Project A
│   ├── shotpub
│   │   ├── EP122
│   │   │   ├── Master
│   │   │   │   ├── Master_Comp_Source
│   │   │   │   └── Master_Comp_Output
│   │   │   ├── SQ010
│   │   │   │   ├── SH01
│   │   │   │   │   ├── rnd_lyrs
│   │   │   │   │   └── lit_compout
│   │   │   │   │       └── source
Explanation of Folders:
Master: Contains master composition files.
Master_Comp_Source: Source files for the master composition.
Master_Comp_Output: Output files generated from the master composition.
SQ010/SH01: Sequence and shot folders for specific shot builds.
rnd_lyrs: Folder for rendered layers.
lit_compout/source: Folder for lighting composition output files.
How to Use
Clone the Repository: Copy the shot_builder.py and shot_builder.ui files into your Nuke pipeline directory.
Launch the Script:
Open the Nuke Python console and run:
python
Copy code
import shot_builder
shot_builder.shot_builder()
This will load the Shot Builder GUI.
Interact with the GUI:
Select the project, episode, sequence, and shot.
Customize the master file path and build child compositions.
Prerequisites
Nuke: Ensure Nuke is installed with Python scripting enabled.
Python Environment: Includes PySide2 for rendering the GUI.
Install Dependencies
If PySide2 is not already installed, use:

bash
Copy code
pip install PySide2
Author
Developed by Mayukh Mitra.
For any questions, reach out via email.

License
This project is licensed under the MIT License. See the LICENSE file for details.
