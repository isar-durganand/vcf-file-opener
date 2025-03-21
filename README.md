# VCF Contact Viewer 📇

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A beautiful and modern web application to view and manage VCF (vCard) contact files. Upload your contact files with ease and view them in a beautiful, responsive interface with dark/light theme support.

![VCF Contact Viewer](screenshot.png)

## ✨ Features

- 🎨 Beautiful, responsive design with Bootstrap 5
- 🌓 Dark/Light theme support with persistent preferences
- 📥 Drag and drop file upload
- 📇 Clean, card-based contact display
- 🏢 Organization information support
- ✨ Smooth animations and transitions
- 📱 Mobile-friendly interface
- 🎯 Custom scrollbar design
- ⬆️ Move to top button
- 🔄 Real-time theme switching

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/vcf-contact-viewer.git
   cd vcf-contact-viewer
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`

## 🌐 Deployment

### Deploy to Vercel

1. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. Deploy on Vercel:
   - Visit [vercel.com](https://vercel.com)
   - Sign in with your GitHub account
   - Click "Add New Project"
   - Select your repository
   - Vercel will automatically detect the Python framework
   - Click "Deploy"

The application will be live at your Vercel-provided URL.

## 💻 Local Development

To run the application in development mode:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000` with debug mode enabled.

## 📁 Project Structure

```
vcf-contact-viewer/
├── api/
│   └── index.py          # Vercel serverless function
├── templates/
│   └── index.html        # Main HTML template
├── app.py               # Flask application (local development)
├── requirements.txt     # Python dependencies
└── vercel.json         # Vercel configuration
```

## 🔧 Configuration

The application supports the following configuration options through environment variables:

- `SECRET_KEY`: Flask secret key (default: randomly generated)
- `MAX_CONTENT_LENGTH`: Maximum file upload size (default: 16MB)

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - Frontend framework
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Icons used in the UI
- [vobject](https://eventable.github.io/vobject/) - VCF file parsing

## 📧 Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/vcf-contact-viewer](https://github.com/yourusername/vcf-contact-viewer)
