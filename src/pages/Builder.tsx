import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { ScrollArea } from "@/components/ui/scroll-area";

type TemplateInfo = { id: string; name: string };

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

const defaultState = {
  contact_name: "",
  contact_title: "",
  contact_email: "",
  contact_phone: "",
  summary_text: "",
  work_company: "",
  work_role: "",
  work_duration: "",
  work_desc: "",
  edu_school: "",
  edu_degree: "",
  edu_duration: "",
  skill_list: "",
};

const Builder = () => {
  const { templateId } = useParams<{ templateId: string }>();
  const navigate = useNavigate();
  const [validTemplate, setValidTemplate] = useState<TemplateInfo | null>(null);
  const [form, setForm] = useState<typeof defaultState>(defaultState);
  const [renderUrl, setRenderUrl] = useState<string>("");
  const [downloading, setDownloading] = useState(false);
  const previewRef = useRef<HTMLDivElement | null>(null);

  // Verify template exists
  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const res = await fetch(`${API_BASE}/api/templates`);
        const json = await res.json();
        const found = (json.templates || []).find((t: TemplateInfo) => t.id === templateId);
        if (!active) return;
        setValidTemplate(found || null);
        if (!found) navigate("/templates");
      } catch (e) {
        console.error(e);
        navigate("/templates");
      }
    })();
    return () => {
      active = false;
    };
  }, [templateId, navigate]);

  // Live render URL (blob) updated on form changes
  useEffect(() => {
    if (!templateId) return;
    let abort = false;
    (async () => {
      try {
        const res = await fetch(`${API_BASE}/api/render/${templateId}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        });
        const html = await res.text();
        if (abort) return;
        const blob = new Blob([html], { type: "text/html" });
        const url = URL.createObjectURL(blob);
        setRenderUrl((old) => {
          if (old) URL.revokeObjectURL(old);
          return url;
        });
      } catch (e) {
        console.error(e);
      }
    })();
    return () => {
      abort = true;
    };
  }, [templateId, form]);

  const onChange = (key: keyof typeof defaultState) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const value = e.target.value;
    setForm((f) => ({ ...f, [key]: value }));
  };

  const onDownload = async () => {
    if (!templateId) return;
    try {
      setDownloading(true);
      const res = await fetch(`${API_BASE}/api/pdf/${templateId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `resume_${templateId}.pdf`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error(e);
    } finally {
      setDownloading(false);
    }
  };

  const previewUrl = useMemo(() => renderUrl, [renderUrl]);

  useEffect(() => {
    if (previewRef.current && previewUrl) {
      previewRef.current.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }, [previewUrl]);

  if (!validTemplate) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div>
          <p className="text-muted-foreground">Loading template…</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen w-full bg-background">
      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="flex items-end justify-between mb-4">
          <div>
            <h1 className="text-2xl font-bold">Build Resume: {validTemplate?.name}</h1>
            <p className="text-muted-foreground">Your changes update the preview in real time.</p>
          </div>
          <div className="flex gap-2">
            <Button variant="secondary" onClick={() => navigate("/templates")}>Back to Templates</Button>
            <Button onClick={onDownload} disabled={downloading}>{downloading ? "Preparing…" : "Download PDF"}</Button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
          <Card>
            <CardHeader>
              <CardTitle>Details</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <Label htmlFor="contact_name">Full Name</Label>
                  <Input id="contact_name" value={form.contact_name} onChange={onChange("contact_name")} placeholder="Jane Doe" />
                </div>
                <div>
                  <Label htmlFor="contact_title">Title</Label>
                  <Input id="contact_title" value={form.contact_title} onChange={onChange("contact_title")} placeholder="Software Engineer" />
                </div>
                <div>
                  <Label htmlFor="contact_email">Email</Label>
                  <Input id="contact_email" value={form.contact_email} onChange={onChange("contact_email")} placeholder="jane@email.com" />
                </div>
                <div>
                  <Label htmlFor="contact_phone">Phone</Label>
                  <Input id="contact_phone" value={form.contact_phone} onChange={onChange("contact_phone")} placeholder="(123) 456-7890" />
                </div>
              </div>

              <div>
                <Label htmlFor="summary_text">Summary</Label>
                <Textarea id="summary_text" value={form.summary_text} onChange={onChange("summary_text")} placeholder="Brief professional summary" rows={4} />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="md:col-span-2">
                  <Label htmlFor="work_company">Company</Label>
                  <Input id="work_company" value={form.work_company} onChange={onChange("work_company")} placeholder="Acme Corp" />
                </div>
                <div>
                  <Label htmlFor="work_role">Role</Label>
                  <Input id="work_role" value={form.work_role} onChange={onChange("work_role")} placeholder="Engineer" />
                </div>
                <div className="md:col-span-3">
                  <Label htmlFor="work_duration">Duration</Label>
                  <Input id="work_duration" value={form.work_duration} onChange={onChange("work_duration")} placeholder="Jan 2022 – Present" />
                </div>
                <div className="md:col-span-3">
                  <Label htmlFor="work_desc">Experience (bullets supported)</Label>
                  <Textarea id="work_desc" value={form.work_desc} onChange={onChange("work_desc")} placeholder={"• Achieved X with Y% impact\n• Reduced cost by Z%"} rows={4} />
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="md:col-span-2">
                  <Label htmlFor="edu_school">School</Label>
                  <Input id="edu_school" value={form.edu_school} onChange={onChange("edu_school")} placeholder="University" />
                </div>
                <div>
                  <Label htmlFor="edu_degree">Degree</Label>
                  <Input id="edu_degree" value={form.edu_degree} onChange={onChange("edu_degree")} placeholder="B.E. in CSE" />
                </div>
                <div className="md:col-span-3">
                  <Label htmlFor="edu_duration">Graduation</Label>
                  <Input id="edu_duration" value={form.edu_duration} onChange={onChange("edu_duration")} placeholder="2023" />
                </div>
              </div>

              <div>
                <Label htmlFor="skill_list">Skills</Label>
                <Input id="skill_list" value={form.skill_list} onChange={onChange("skill_list")} placeholder="Python, React, SQL" />
              </div>
            </CardContent>
          </Card>

          <div ref={previewRef} className="space-y-3">
            <Card>
              <CardHeader>
                <CardTitle>Live Preview</CardTitle>
              </CardHeader>
              <CardContent>
                {previewUrl ? (
                  <div className="rounded-md border bg-card">
                    <ScrollArea className="h-[75vh]">
                      <div className="p-3">
                        <iframe
                          title="Resume Preview"
                          src={previewUrl}
                          className="w-full h-[1400px] scale-[0.7] origin-top-left border-0"
                          style={{ transform: "scale(0.7)", height: "1400px", width: "142.8571%" }}
                        />
                      </div>
                    </ScrollArea>
                  </div>
                ) : (
                  <p className="text-muted-foreground">Start typing to see a live preview.</p>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Builder;

