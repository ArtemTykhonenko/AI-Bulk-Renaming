import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import os
from config import load_config, save_config
from utils_grok import analyze_images_grok, rename_images

class ImageRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Renamer (Grok)")
        self.config = load_config()
        self.selected_folder = None

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.settings_frame = ttk.Frame(self.notebook)
        self.main_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.settings_frame, text='Settings')
        self.notebook.add(self.main_frame, text='Main')

        self.setup_settings()
        self.setup_main()

    def setup_settings(self):
        ttk.Label(self.settings_frame, text="Grok API Key:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.api_key_entry = ttk.Entry(self.settings_frame, width=50)
        self.api_key_entry.insert(0, self.config.get('grok_api_key', ''))
        self.api_key_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.settings_frame, text="Prompt:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.prompt_entry = ttk.Entry(self.settings_frame, width=50)
        self.prompt_entry.insert(0, self.config.get('prompt', ''))
        self.prompt_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.settings_frame, text="Save", command=self.save_settings).grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.settings_frame, text="Using: Grok-2-Vision (Uncensored)", font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=2)

    def save_settings(self):
        self.config['grok_api_key'] = self.api_key_entry.get()
        self.config['prompt'] = self.prompt_entry.get()
        save_config(self.config)
        messagebox.showinfo("Saved", "Settings saved successfully.")

    def setup_main(self):
        ttk.Button(self.main_frame, text="Select Folder", command=self.select_folder).grid(row=0, column=0, pady=10)
        self.folder_label = ttk.Label(self.main_frame, text="No folder selected")
        self.folder_label.grid(row=0, column=1, padx=5)

        ttk.Button(self.main_frame, text="Rename Images", command=self.rename_images).grid(row=1, column=0, columnspan=2, pady=10)

        self.progress = ttk.Progressbar(self.main_frame, orient='horizontal', mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

        self.status_label = ttk.Label(self.main_frame, text="")
        self.status_label.grid(row=3, column=0, columnspan=2)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder)

    def rename_images(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return
        if not self.config.get('grok_api_key'):
            messagebox.showerror("Error", "Please set Grok API key in settings.")
            return

        image_paths = [str(p) for p in Path(self.selected_folder).glob('*') if p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.heic', '.heif')]
        if not image_paths:
            messagebox.showerror("Error", "No images found in the selected folder.")
            return

        self.progress['maximum'] = len(image_paths)
        self.progress['value'] = 0
        self.status_label.config(text="Analyzing images with Grok...")

        try:
            results = analyze_images_grok(image_paths, self.config['prompt'], self.config['grok_api_key'])
            self.progress['value'] = len(image_paths)
            self.status_label.config(text="Renaming images...")
            rename_images(self.selected_folder, results)
            self.status_label.config(text="Done!")
            messagebox.showinfo("Success", "Images renamed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0
