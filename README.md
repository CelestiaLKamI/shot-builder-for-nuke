
# Shot Builder Tool

The Shot Builder Tool is a Nuke utility designed for VFX pipelines to efficiently manage and build shot compositions. It dynamically organizes and creates Nuke scripts based on a structured folder hierarchy and allows for customization through a PySide2-based GUI.

## Features

- **Dynamic Folder-Based Management**: Supports episode (`EP122`), sequence (`SQ010`), and shot (`SH01`) selection from the defined folder hierarchy.
- **Master Composition Handling**: Allows working with `Master_Comp_Source` and `Master_Comp_Output` folders for centralized shot management.
- **Child Shot Creation**: Automates the process of creating child shot files (`rnd_lyrs`, `lit_compout`) and updating file references for nodes in Nuke.

## Folder Structure

The Shot Builder Tool assumes the following folder structure:

```
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
```

## How to Use

1. Place the Mayukh Scripts folder in the .nuke folder
2. Use the Production path tool to set the path for the production that contains the project folders
3. Update the Project names for the variable "projects_list_filtered" in the shot_builder.py file in line 32 according to the projects you are working on
4. Copy the contents of menu.py and init.py to respective files in .nuke folder for your local machine
5. Use the GUI to select projects, episodes, sequences, and shots, and build customized Nuke scripts. 

## Note

1. This has a seperate folder structure so it might not be applicable to project you are curreently working on
2. If you are using .bat to execute this script then please change the path to currently installed nuke path

## Prerequisites

- **Nuke**: Installed with Python scripting enabled.
- **Python**: Ensure PySide2 is installed for GUI functionality.

Install PySide2 if not available:
```bash
pip install PySide2
```

## Author

Created by **Mayukh Mitra**.  
For inquiries, contact via [email](mailto:mitramayukh5@gmail.com).
