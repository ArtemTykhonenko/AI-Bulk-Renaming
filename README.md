# Image Naming Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![Grok](https://img.shields.io/badge/Grok-xAI-purple.svg)](https://x.ai/)

A sophisticated Python application that leverages artificial intelligence to automatically analyze and rename images based on their visual content. Perfect for organizing large collections of images with descriptive, AI-generated filenames.

## ✨ Features

- **Intelligent Image Analysis**: Uses Grok-2-Vision AI model for accurate content recognition, including uncensored and explicit content
- **User-Friendly GUI**: Clean Tkinter interface for easy operation
- **Customizable Prompts**: Tailor the AI analysis to your specific naming needs
- **Batch Processing**: Handle multiple images simultaneously
- **Multiple Formats**: Supports JPG, JPEG, PNG, WebP, HEIC, and HEIF files
- **Smart Renaming**: Automatic sanitization and duplicate handling
- **Progress Tracking**: Real-time progress bars and status updates

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Grok API key ([Get one here](https://x.ai/))

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
   - Enter your Grok API key
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

- **AI Model**: Grok-2-Vision-1212 (Uncensored)
- **GUI Framework**: Tkinter with ttk styling
- **Image Processing**: Base64 encoding and direct API upload
- **Error Handling**: Robust retry logic for API rate limits
- **File Safety**: Preserves original files during renaming

## 📋 Requirements

```
requests>=2.25.0
Pillow>=10.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source. Please check the license file for details.

## ⚠️ Disclaimer

This tool is designed for personal use in organizing image collections, including adult and explicit content. Ensure compliance with API terms of service, xAI usage policies, and local regulations regarding AI usage and content analysis. Use responsibly and ethically.