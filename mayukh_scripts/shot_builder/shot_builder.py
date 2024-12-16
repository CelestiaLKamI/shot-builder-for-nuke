import nuke
import os
import shutil
from PySide2.QtWidgets import QWidget, QSpinBox, QGroupBox, QComboBox, QLabel, QRadioButton, QPushButton, QGridLayout
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

def shot_builder():
   """
   Launches the Shot Builder tool for creating and managing Nuke scripts for shots.

   This tool provides functionalities for selecting projects, episodes, sequences,
   and shots, and allows users to build and customize comp files using a graphical
   user interface built with PySide2.
   """

   # Define user and project paths
   nuke_user = os.path.expanduser(r"~\.nuke")
   path_to_projects = r"D:\Sample Production"
   basic_folder_path_for_master = r"Master\Master_Comp_Source"
   basic_folder_path_for_master_output = r"Master\Master_Comp_Output"

   class ShotBuilder(QWidget):
      """
      The main Shot Builder class, inheriting from QWidget.

      This class contains methods for initializing the UI and handling
      project selection, episode selection, file operations, and building child shots.
      """
      def __init__(self):
         super().__init__()
         
         # Load the UI file
         ui_file_path = os.path.join(nuke_user, r"Mayukh Scripts\Shot_Builder\shot_builder.ui")
         self.ui = QUiLoader().load(ui_file_path, self)

         # Initialize UI components
         self.ui.spinBox_2.setMinimum(1)
         self.ui.comboBox_7.addItems(self.project_select())

         # Populate UI components with initial data
         self.master_episode_select()
         self.master_file_select()
         self.update_selection_process()
         self.child_episode_select()
         self.child_sequence_select()
         self.child_shot_select()

         # Connect signals to respective methods
         self.ui.comboBox_7.currentIndexChanged.connect(self.auto_update_for_options)
         self.ui.comboBox.currentIndexChanged.connect(self.master_file_select)
         self.ui.pushButton_3.clicked.connect(self.preview_master)
         self.ui.radioButton.toggled.connect(self.update_selection_process)           
         self.ui.pushButton_4.clicked.connect(self.set_custom_master)
         self.ui.comboBox_6.currentIndexChanged.connect(self.child_sequence_select)
         self.ui.comboBox_5.currentIndexChanged.connect(self.child_shot_select)
         self.ui.pushButton.clicked.connect(self.child_build)
         self.ui.pushButton_2.clicked.connect(self.cancel_build)

         # Set fixed size for the UI window
         self.setFixedSize(self.ui.width(), self.ui.height())
      
      def cancel_build(self):
         """Closes the Shot Builder window."""
         window.close()

      def auto_update_for_options(self):
         """Automatically updates options based on project selection."""
         self.master_episode_select()
         self.child_episode_select()
         self.child_sequence_select()
         self.child_shot_select() 

      def project_select(self):
         """
         Filters and returns a list of projects.

         Returns:
               list: A filtered list of project names.
         """
         projects_list_unfiltered = os.listdir(path_to_projects)
         projects_list_filtered = [
               "Project A",
               "Project B"
         ]

         self.projects_list = []

         for each_folder in projects_list_unfiltered:
               for each_project in projects_list_filtered:
                  if each_project == each_folder:
                     self.projects_list.append(each_project)
                     
         return self.projects_list
      
      def master_episode_select(self):            
         """Populates the Master Episode combo box with available episodes."""
         self.list_of_episodes_master = []

         # Get the currently selected project
         self.currently_selected_project = self.ui.comboBox_7.currentText()

         # Define the path to the selected project's shotpub folder
         self.currently_selected_project_path = os.path.join(path_to_projects, self.currently_selected_project)
         self.path_to_shotpub_for_current_episode_master = os.path.join(self.currently_selected_project_path, "shotpub")
         
         # Get the list of episodes in the shotpub folder
         list_of_folders_in_shotpub = os.listdir(self.path_to_shotpub_for_current_episode_master)

         for folder in list_of_folders_in_shotpub:
               if "EP" in folder:
                  self.list_of_episodes_master.append(folder)
                  
         # Clear and populate the episode combo box
         self.ui.comboBox.clear()
         self.ui.comboBox.addItems(self.list_of_episodes_master)

      def master_file_select(self):
         """Populates the Master File combo box with files in the selected episode."""
         self.currently_selected_episode_master = self.ui.comboBox.currentText()
         
         # Define paths for the current episode
         self.abs_path_to_episodes = os.path.join(self.path_to_shotpub_for_current_episode_master, self.currently_selected_episode_master)
         self.path_to_master_folder_for_current_ep = os.path.join(self.abs_path_to_episodes, basic_folder_path_for_master)
         self.list_of_all_master_file = os.listdir(self.path_to_master_folder_for_current_ep)

         # Clear and populate the master file combo box
         self.ui.comboBox_3.clear()
         self.ui.comboBox_3.addItems(self.list_of_all_master_file)
      
      def preview_master(self):
         """
         Opens the master comp output file in the default viewer.
         """
         self.path_to_master_output_folder_for_current_ep = os.path.join(self.abs_path_to_episodes, basic_folder_path_for_master_output)
         current_master_basename = self.ui.comboBox_3.currentText().split(".")[0] + ".png"
         output_path_to_current_master = os.path.join(self.path_to_master_output_folder_for_current_ep, current_master_basename)
         
         os.startfile(output_path_to_current_master)
      
      def update_selection_process(self):
         """
         Enables or disables UI components based on the selection process type (default or custom).
         """
         if self.ui.radioButton.isChecked():
               self.ui.comboBox_7.setEnabled(False)
               self.ui.comboBox.setEnabled(False)
               self.ui.pushButton_3.setEnabled(False)
               self.ui.pushButton_4.setEnabled(True)
               self.ui.comboBox_3.clear()
               
         else:
               self.ui.comboBox_7.setEnabled(True)
               self.ui.comboBox.setEnabled(True)
               self.ui.pushButton_3.setEnabled(True)
               self.ui.pushButton_4.setEnabled(False)
               self.master_file_select()

      def set_custom_master(self):
         """
         Opens a file dialog for selecting a custom master file and updates the combo box.
         """
         file_browser = QFileDialog()
         file_browser.setFileMode(QFileDialog.AnyFile)
         file_browser.setNameFilter("Nuke scripts (*.nk)")

         self.selected_file, selected_file_filter = file_browser.getOpenFileName(parent=None, caption="Select a custom Master File", dir=path_to_projects, filter="Nuke Scripts (*.nk)")

         self.ui.comboBox_3.clear()
         self.ui.comboBox_3.addItem(os.path.basename(os.path.normpath(self.selected_file)))
      
      def child_episode_select(self):
         """
         Populate the episode combo box (comboBox_6) with available episodes 
         in the selected project's "shotpub" directory.
         """
         self.list_of_episodes_child = []
         self.list_of_episode_paths = []
         
         # Path up to the "shotpub" folder of the current project
         self.path_to_shotpub_for_current_episode_child = os.path.join(self.currently_selected_project_path, "shotpub")
         self.list_of_folders_in_shotpub = os.listdir(self.path_to_shotpub_for_current_episode_child)

         for folder in self.list_of_folders_in_shotpub:
               if "EP" in folder:  # Check if the folder is an episode folder
                  self.list_of_episodes_child.append(folder)
                  self.list_of_episode_paths.append(os.path.join(self.path_to_shotpub_for_current_episode_child, folder))
                  
         self.ui.comboBox_6.clear()

         if self.list_of_episodes_child:
               # Add episode names to the combo box
               self.ui.comboBox_6.addItems(self.list_of_episodes_child)
         else:
               # Add a placeholder if no episodes are found
               self.ui.comboBox_6.addItem("(NONE)")
         
      def child_sequence_select(self):
         """
         Populate the sequence combo box (comboBox_5) with available sequences 
         in the selected episode's folder.
         """
         self.list_of_sequences_child = []
         self.list_of_sequences_child_paths = []
                  
         # List of folders inside the selected episode folder
         list_of_folders_in_episode = os.listdir(self.list_of_episode_paths[self.ui.comboBox_6.currentIndex()])

         for each_folder in list_of_folders_in_episode:
               if "SQ" in each_folder:  # Check if the folder is a sequence folder
                  self.list_of_sequences_child.append(each_folder)
                  self.list_of_sequences_child_paths.append(os.path.join(self.list_of_episode_paths[self.ui.comboBox_6.currentIndex()], each_folder))   

         self.ui.comboBox_5.clear()

         if self.list_of_sequences_child:
               # Add sequence names to the combo box
               self.ui.comboBox_5.addItems(self.list_of_sequences_child)
         else:
               # Add a placeholder if no sequences are found
               self.ui.comboBox_5.addItem("(NONE)")

      def child_shot_select(self):
         """
         Populate the shot combo box (comboBox_4) with available shots 
         that contain "rnd_lyrs" folders in the selected sequence.
         """
         self.list_of_shots_child = []
         self.list_of_shots_child_paths = []
         self.list_of_shots_child_available = []
         self.list_of_shots_child_paths_available = []
         # List of folders inside the selected sequence folder
         self.list_of_folders_in_child_sequence = os.listdir(self.list_of_sequences_child_paths[self.ui.comboBox_5.currentIndex()])

         for each_folder in self.list_of_folders_in_child_sequence:
               if "SH" in each_folder:  # Check if the folder is a shot folder
                  self.list_of_shots_child.append(each_folder)
                  self.list_of_shots_child_paths.append(os.path.join(self.list_of_sequences_child_paths[self.ui.comboBox_5.currentIndex()], each_folder))

         for each_path in self.list_of_shots_child_paths:
               # Check if the "rnd_lyrs" folder exists in the shot folder
               if "rnd_lyrs" in os.listdir(each_path):
                  self.list_of_shots_child_available.append(self.list_of_shots_child[self.list_of_shots_child_paths.index(each_path)])
                  self.list_of_shots_child_paths_available.append(each_path)

         self.ui.comboBox_4.clear()

         if self.list_of_shots_child_available:
               # Add shot names to the combo box
               self.ui.comboBox_4.addItems(self.list_of_shots_child_available)
         else:
               # Add a placeholder if no shots are found
               self.ui.comboBox_4.addItem("(NONE)")

      def child_build(self):
         """
         Build a child shot comp file by copying the selected master file, 
         renaming it, and updating its file paths to match the selected shot.
         """
         # Check if the script is unsaved and modified
         if not os.path.dirname(nuke.root().name()) and nuke.root().modified():
            nuke.message("Shot cannot be built on a modified script\nPlease open a new empty script")
            return
         # Check if the script is saved
         if os.path.dirname(nuke.root().name()):
            nuke.message("Shot cannot be built on a modified script\nPlease open a new empty script")
            return
      
         # Get values from UI elements
         child_proj = self.ui.comboBox_7.currentText()
         child_ep = self.ui.comboBox_6.currentText()
         child_sq = self.ui.comboBox_5.currentText()
         child_sh = self.ui.comboBox_4.currentText()
         child_ver = f"V{str(self.ui.spinBox_2.value()).zfill(3)}"

         while True:
            # Path to the child comp directory
            path_to_child_comp_dir = os.path.join(path_to_projects, child_proj, "shotpub", child_ep, child_sq, child_sh, "lit_compout", "source", "sequence", child_ver)
            # Required Format for filename and filepath
            required_filename = f"{child_proj}_{child_ep}_{child_sq}_{child_sh}_sequence_compout_{child_ver}.nk"
            required_file_path = os.path.join(path_to_child_comp_dir, required_filename)

            if "(NONE)" in required_file_path:
                  # Show a message if the path does not exist
                  nuke.message("Child Shot Path Does not exist")
                  return

            if os.path.exists(required_file_path):
                  # Show a message if the path exists to overwrite or to create a new version
                  overwrite_choice = nuke.ask(f"The file {required_filename} already exists...\nDo you want to overwrite it?")

                  if overwrite_choice:
                     # Remove the already existing file if user decides to overwrite the existing
                     os.remove(required_file_path)
                     break
                  else:
                     # Increment the version and update variables for the next iteration
                     spin_value = int(child_ver[1:]) + 1
                     child_ver = f"V{str(spin_value).zfill(3)}"
            else:
                  # Exit the loop if the file does not exist
                  break

         # Makes the directory according to the selected user choices for child shot           
         os.makedirs(path_to_child_comp_dir, exist_ok=True)

         # Path to the master file
         master_file_path = os.path.join(self.path_to_master_folder_for_current_ep, self.ui.comboBox_3.currentText())
         # Changes the master file path to currently selected file if the user importss a custom shot as master
         if self.ui.radioButton.isChecked():   
            master_file_path = self.selected_file
            
         # Path to copy the file in the child comp directory
         current_file_path = os.path.join(path_to_child_comp_dir, self.ui.comboBox_3.currentText())
         current_filename = os.path.basename(current_file_path)
         
         shutil.copy(master_file_path, current_file_path)

         # Rename the copied file to the required format
         os.rename(current_file_path, required_file_path)
         child_file_path = required_file_path

         # Open the new comp file in Nuke
         nuke.scriptOpen(child_file_path)

         # Update the file paths in all Read nodes
         read_nodes = nuke.allNodes(filter="Read")
         for read_node in read_nodes:
            current_asset_folder = read_node['file'].getValue().split("/")[-2]
            current_asset = os.path.basename(os.path.normpath(read_node['file'].getValue()))
            read_node['file'].setValue(os.path.join(path_to_projects, child_proj, "shotpub", child_ep, child_sq, child_sh, "rnd_lyrs", current_asset_folder, current_asset).replace("\\", "/"))

         # Save the updated comp file
         nuke.scriptSave()
         self.close()

   # Path to the icon file
   icon_file_path = os.path.join(nuke_user, r"mayukh_scripts\shot_builder\shot_builder.png")

   # Global variable for the window
   global window

   # Create and show the ShotBuilder window
   window = ShotBuilder()
   window.setWindowTitle("Shot Builder")
   window.setWindowIcon(QIcon(icon_file_path))
   window.show()