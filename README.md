# Resume Builder

A modern, responsive resume builder application built with React, TypeScript, and Tailwind CSS. Create professional resumes with beautiful templates and download them as PDF files.

## Features

### 🎨 Templates Page
- **Template Gallery**: Browse through 6 professionally designed resume templates
- **Preview Functionality**: Click "Preview" to see a detailed view of any template
- **Auto-scroll**: Automatically scrolls to the preview section when preview is clicked
- **Reduced Preview Size**: Preview is scaled down (75%) for better viewing
- **Template Selection**: Click "Use Template" to navigate to the builder with the selected template

### 🛠️ Builder Page
- **Template Validation**: Ensures users can only access the builder with a selected template
- **Real-time Preview**: See changes reflected immediately as you type
- **Comprehensive Form Sections**:
  - Personal Information (name, email, phone, location, LinkedIn, professional title)
  - Professional Summary
  - Work Experience (add/remove multiple entries)
  - Education (add/remove multiple entries)
  - Skills (add/remove skills with badges)
  - Projects (add/remove project entries)
- **PDF Download**: Generate and download resume as a high-quality PDF file
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 🎯 User Experience
- **Navigation**: Clean navigation bar with Home and Templates links
- **Form Validation**: Proper input types and validation
- **Toast Notifications**: User feedback for actions like PDF generation
- **Modern UI**: Built with shadcn/ui components for a polished look

## Technology Stack

- **Frontend**: React 18 with TypeScript
- **Styling**: Tailwind CSS with shadcn/ui components
- **Routing**: React Router DOM
- **PDF Generation**: jsPDF + html2canvas
- **Build Tool**: Vite
- **Package Manager**: npm

## Getting Started

### Prerequisites
- Node.js (version 16 or higher)
- npm

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-builder
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

### Building for Production

```bash
npm run build
```

## Usage

### Creating a Resume

1. **Start at Home**: Visit the homepage to see an overview of features
2. **Choose Template**: Navigate to the Templates page and browse available designs
3. **Preview Template**: Click "Preview" to see a detailed view of the template
4. **Select Template**: Click "Use Template" to start building with that design
5. **Fill Information**: Use the form on the left to add your personal information, experience, education, skills, and projects
6. **Real-time Preview**: See your changes reflected immediately in the preview panel on the right
7. **Download PDF**: Click "Download PDF" to generate and download your resume

### Template Categories

- **Modern**: Clean, contemporary designs perfect for tech professionals
- **Classic**: Traditional layouts suitable for corporate environments
- **Creative**: Unique designs for creative professionals and artists

## Project Structure

```
src/
├── components/
│   ├── ui/           # shadcn/ui components
│   └── Navigation.tsx
├── pages/
│   ├── Index.tsx     # Landing page
│   ├── Templates.tsx # Template selection page
│   ├── Builder.tsx   # Resume builder page
│   └── NotFound.tsx  # 404 page
├── types/
│   └── index.ts      # TypeScript interfaces
└── App.tsx           # Main app component with routing
```

## Features in Detail

### Template System
- 6 pre-designed templates with different layouts
- Template data includes name, description, category, and layout type
- Smooth navigation between template selection and builder

### Form Management
- Dynamic form sections that can be added/removed
- Real-time state management with React hooks
- Proper TypeScript typing for all form data

### PDF Generation
- Uses jsPDF for PDF creation
- html2canvas for capturing the resume preview
- Automatic page breaking for long resumes
- High-quality output with proper scaling

### Responsive Design
- Mobile-first approach with Tailwind CSS
- Responsive grid layouts
- Touch-friendly interface elements

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Future Enhancements

- More template designs
- Template customization options
- Resume sharing functionality
- Cloud storage for saved resumes
- Multiple language support
- Advanced formatting options
