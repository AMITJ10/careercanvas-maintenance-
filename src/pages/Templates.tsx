import { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Eye, FileText, Download } from 'lucide-react';
import { Template } from '@/types';

const templates: Template[] = [
  {
    id: 'modern-1',
    name: 'Modern Professional',
    description: 'Clean and contemporary design perfect for tech professionals',
    category: 'Technology',
    preview: 'modern-professional',
    layout: 'modern'
  },
  {
    id: 'classic-1',
    name: 'Classic Executive',
    description: 'Traditional layout suitable for corporate environments',
    category: 'Business',
    preview: 'classic-executive',
    layout: 'classic'
  },
  {
    id: 'creative-1',
    name: 'Creative Portfolio',
    description: 'Unique design for creative professionals and artists',
    category: 'Creative',
    preview: 'creative-portfolio',
    layout: 'creative'
  },
  {
    id: 'modern-2',
    name: 'Minimalist',
    description: 'Simple and elegant design focusing on content',
    category: 'General',
    preview: 'minimalist',
    layout: 'modern'
  },
  {
    id: 'classic-2',
    name: 'Academic',
    description: 'Formal layout ideal for academic and research positions',
    category: 'Education',
    preview: 'academic',
    layout: 'classic'
  },
  {
    id: 'creative-2',
    name: 'Startup',
    description: 'Dynamic design for entrepreneurs and startup professionals',
    category: 'Entrepreneurship',
    preview: 'startup',
    layout: 'creative'
  }
];

const Templates = () => {
  const navigate = useNavigate();
  const [selectedTemplate, setSelectedTemplate] = useState<string | null>(null);
  const previewRef = useRef<HTMLDivElement>(null);

  const handlePreviewClick = (templateId: string) => {
    setSelectedTemplate(templateId);
    // Scroll to preview section
    setTimeout(() => {
      previewRef.current?.scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
      });
    }, 100);
  };

  const handleUseTemplate = (template: Template) => {
    navigate('/builder', { 
      state: { 
        selectedTemplate: template 
      } 
    });
  };

  const getTemplatePreview = (template: Template) => {
    return (
      <div className={`w-full h-64 bg-gradient-to-br rounded-lg p-4 border-2 ${
        template.layout === 'modern' 
          ? 'from-blue-50 to-indigo-100 border-blue-200' 
          : template.layout === 'classic'
          ? 'from-gray-50 to-slate-100 border-gray-200'
          : 'from-purple-50 to-pink-100 border-purple-200'
      }`}>
        <div className="h-full flex flex-col">
          <div className="flex-1">
            <div className="h-4 bg-gray-300 rounded mb-2 w-3/4"></div>
            <div className="h-3 bg-gray-200 rounded mb-1 w-1/2"></div>
            <div className="h-3 bg-gray-200 rounded mb-3 w-2/3"></div>
            
            <div className="space-y-2">
              <div className="h-2 bg-gray-200 rounded w-full"></div>
              <div className="h-2 bg-gray-200 rounded w-5/6"></div>
              <div className="h-2 bg-gray-200 rounded w-4/5"></div>
            </div>
          </div>
          
          <div className="mt-4 flex justify-between items-center">
            <div className="h-3 bg-gray-300 rounded w-1/4"></div>
            <div className="h-3 bg-gray-300 rounded w-1/6"></div>
          </div>
        </div>
      </div>
    );
  };

  const selectedTemplateData = templates.find(t => t.id === selectedTemplate);

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">Resume Templates</h1>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Choose from our professionally designed templates to create your perfect resume
          </p>
        </div>

        {/* Templates Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          {templates.map((template) => (
            <Card key={template.id} className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div>
                    <CardTitle className="text-lg">{template.name}</CardTitle>
                    <CardDescription className="mt-2">
                      {template.description}
                    </CardDescription>
                  </div>
                  <Badge variant={
                    template.layout === 'modern' ? 'default' :
                    template.layout === 'classic' ? 'secondary' : 'outline'
                  }>
                    {template.category}
                  </Badge>
                </div>
              </CardHeader>
              <CardContent className="space-y-4">
                {getTemplatePreview(template)}
                <div className="flex gap-2">
                  <Button 
                    variant="outline" 
                    size="sm" 
                    className="flex-1"
                    onClick={() => handlePreviewClick(template.id)}
                  >
                    <Eye className="w-4 h-4 mr-2" />
                    Preview
                  </Button>
                  <Button 
                    size="sm" 
                    className="flex-1"
                    onClick={() => handleUseTemplate(template)}
                  >
                    <FileText className="w-4 h-4 mr-2" />
                    Use Template
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Preview Section */}
        {selectedTemplateData && (
          <div ref={previewRef} className="bg-muted/50 rounded-lg p-8">
            <div className="text-center mb-6">
              <h2 className="text-2xl font-bold mb-2">{selectedTemplateData.name} - Preview</h2>
              <p className="text-muted-foreground">{selectedTemplateData.description}</p>
            </div>
            
            <div className="max-w-2xl mx-auto">
              <div className="bg-white rounded-lg shadow-lg p-6 transform scale-75 origin-top">
                {getTemplatePreview(selectedTemplateData)}
              </div>
              
              <div className="text-center mt-6">
                <Button 
                  size="lg"
                  onClick={() => handleUseTemplate(selectedTemplateData)}
                  className="px-8"
                >
                  <FileText className="w-5 h-5 mr-2" />
                  Use This Template
                </Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Templates;