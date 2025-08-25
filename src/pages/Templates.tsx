import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";

type TemplateInfo = {
  id: string;
  name: string;
  role: string;
  icon?: string;
  description?: string;
};

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

const Templates = () => {
  const [templates, setTemplates] = useState<TemplateInfo[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const previewRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const res = await fetch(`${API_BASE}/api/templates`);
        const json = await res.json();
        if (!active) return;
        setTemplates(json.templates || []);
      } catch (e) {
        console.error(e);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  const previewUrl = useMemo(() => (selectedId ? `${API_BASE}/api/templates/${selectedId}/preview` : null), [selectedId]);

  useEffect(() => {
    if (previewRef.current && previewUrl) {
      previewRef.current.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }, [previewUrl]);

  return (
    <div className="min-h-screen w-full bg-background">
      <div className="max-w-6xl mx-auto px-4 py-8">
        <div className="flex items-end justify-between mb-6">
          <div>
            <h1 className="text-3xl font-bold">Choose a Resume Template</h1>
            <p className="text-muted-foreground">Preview a template and click Use to start building.</p>
          </div>
          <Button variant="secondary" onClick={() => navigate("/")}>Home</Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {templates.map((t) => (
            <Card key={t.id} className={"hover:shadow-md transition-shadow"}>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <span className="text-xl" aria-hidden>{t.icon || "📄"}</span>
                  {t.name}
                </CardTitle>
                <CardDescription>{t.description || t.role}</CardDescription>
              </CardHeader>
              <CardContent className="flex gap-2">
                <Button variant="outline" onClick={() => setSelectedId(t.id)} disabled={loading}>Preview</Button>
                <Button onClick={() => navigate(`/builder/${t.id}`)} disabled={loading}>Use</Button>
              </CardContent>
            </Card>
          ))}
        </div>

        <div ref={previewRef} className="mt-10">
          {previewUrl ? (
            <div>
              <h2 className="text-xl font-semibold mb-3">Preview</h2>
              <div className="rounded-md border bg-card">
                <ScrollArea className="h-[70vh]">
                  <div className="p-3">
                    <iframe
                      title="Template Preview"
                      src={previewUrl}
                      className="w-full h-[1400px] scale-[0.75] origin-top-left border-0"
                      style={{ transform: "scale(0.75)", height: "1400px", width: "133.3333%" }}
                    />
                  </div>
                </ScrollArea>
              </div>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};

export default Templates;

