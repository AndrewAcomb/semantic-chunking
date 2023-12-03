import sys
import json
from pathlib import Path

def chunk_naively(path):
    with open(path,'r') as infile:
        raw_text = infile.read()
    SENTENCES_PER_CHUNK = 5
    chunks = []
    rt_split = raw_text.split('.')
    for i in range(0,len(rt_split),SENTENCES_PER_CHUNK):
        chunk = ".".join((rt_split[i:i+SENTENCES_PER_CHUNK]))
        if not chunk:
            continue
        if chunk[-1] != '.':
            chunk += '.'
        chunks.append({"chunk":chunk, "original_text":chunk})
    result = {
        "file": path,
        "original": raw_text,
        "chunks": chunks
    }
    
    with open("output/naive/" + Path(path).stem + ".json", 'w') as outfile:
        json.dump(result,outfile,indent=4)

if __name__ == "__main__":
    path = "raw_text/3ReasonsWhyNuclearEnergyIsAwesome33.txt"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    chunk_naively(path)
