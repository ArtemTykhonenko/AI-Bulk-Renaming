# Image Naming Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-AI-green.svg)](https://ai.google.dev/)

A sophisticated Python application that leverages artificial intelligence to automatically analyze and rename images based on their visual content. Perfect for organizing large collections of images with descriptive, AI-generated filenames.

## ✨ Features

- **Intelligent Image Analysis**: Uses Google Gemini 2.0 Flash AI model for accurate content recognition
- **User-Friendly GUI**: Clean Tkinter interface for easy operation
- **Customizable Prompts**: Tailor the AI analysis to your specific naming needs
- **Batch Processing**: Handle multiple images simultaneously
- **Multiple Formats**: Supports JPG, JPEG, PNG, WebP, HEIC, and HEIF files
- **Smart Renaming**: Automatic sanitization and duplicate handling
- **Progress Tracking**: Real-time progress bars and status updates

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/image-naming-tool.git
   cd image-naming-tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

1. **Launch the application** using `python main.py`
2. **Configure Settings**:
   - Enter your Google Gemini API key
   - Customize the analysis prompt (optional)
3. **Select Folder**: Choose a directory containing images
4. **Process Images**: Click "Rename Images" to start AI analysis
5. **Monitor Progress**: Watch the progress bar and status updates

## ⚙️ Configuration

The application uses a `config.json` file to store:
- API key (keep this secure!)
- Custom prompt for AI analysis

Default prompt focuses on geometric analysis and descriptive naming suitable for adult content organization.

## 🛠️ Technical Details

- **AI Model**: Google Gemini 2.0 Flash Experimental
- **GUI Framework**: Tkinter with ttk styling
- **Image Processing**: Direct upload to Gemini API
- **Error Handling**: Robust retry logic for API rate limits
- **File Safety**: Preserves original files during renaming

## 📋 Requirements

```
google-generativeai>=0.8.0
Pillow>=10.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source. Please check the license file for details.

## ⚠️ Disclaimer

This tool is designed for personal use in organizing image collections. Ensure compliance with API terms of service and local regulations regarding AI usage and content analysis.