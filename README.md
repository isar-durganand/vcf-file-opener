# VCF Contact Viewer

A beautiful web application to view and manage VCF (vCard) contact files with dark/light theme support.

## Deployment Instructions

### Deploy to Vercel

1. Push your code to a GitHub repository:
   - Create a new repository on GitHub
   - Initialize git in your project folder:
     ```
     git init
     git add .
     git commit -m "Initial commit"
     ```
   - Add your GitHub repository as remote and push:
     ```
     git remote add origin <your-github-repo-url>
     git push -u origin main
     ```

2. Deploy on Vercel:
   - Go to [vercel.com](https://vercel.com)
   - Sign in with your GitHub account
   - Click "Add New Project"
   - Select your repository from the list
   - Vercel will automatically detect the Python framework
   - Click "Deploy"

Your application will be automatically deployed and you'll receive a URL where your application is live.

## Features

- Beautiful, responsive design
- Dark/Light theme support
- Drag and drop file upload
- Contact cards with organization info
- Smooth animations
- Mobile-friendly interface
- Custom scrollbar
- Move to top button
- Persistent theme preference