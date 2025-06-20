from pydantic import BaseModel
from crewai.tools import tool
import json

class JSONChunkReaderToolInput(BaseModel):
    file_path: str
    chunk_size: int = 1000

@tool("JSONChunkReaderTool")
def read_json_chunks(file_path: str, chunk_size: int = 1000) -> str:
    """Reads a large JSON file and returns it as text chunks for analysis."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    text = json.dumps(data, indent=2)
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return "\n\n".join(chunks)