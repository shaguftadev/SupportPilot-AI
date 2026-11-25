from pathlib import Path
from pypdf import PdfReader
from docx import Document as DocxDocument

SUPPORTED = {".pdf", ".docx", ".txt"}

def extract_pages(path: Path) -> list[dict]:
    ext = path.suffix.lower()
    if ext == ".pdf":
        reader = PdfReader(str(path))
        return [{"page": i + 1, "text": page.extract_text() or ""} for i, page in enumerate(reader.pages)]
    if ext == ".docx":
        doc = DocxDocument(str(path))
        text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        return [{"page": None, "text": text}]
    if ext == ".txt":
        return [{"page": None, "text": path.read_text(encoding="utf-8", errors="replace")}]
    raise ValueError("Unsupported file type. Upload PDF, DOCX, or TXT.")

def chunk_pages(pages: list[dict], chunk_size: int = 900, overlap: int = 140) -> list[dict]:
    chunks=[]
    for page in pages:
        text=" ".join(page["text"].split())
        if not text: continue
        start=0
        while start < len(text):
            end=min(start+chunk_size, len(text))
            chunk=text[start:end].strip()
            if chunk: chunks.append({"text": chunk, "page": page.get("page"), "chunk_index": len(chunks)})
            if end == len(text): break
            start=max(0, end-overlap)
    return chunks
