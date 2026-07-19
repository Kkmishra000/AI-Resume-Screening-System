def chunk_text(text: str, chunk_size: int = 200,overlap: int = 50 ) -> list[str]:
    
    words = text.split()
    
    chunks = []
    
    
    step = chunk_size - overlap
    
    if step <= 0:
        raise ValueError("Chunk size must be greater than overlap.")
    
    for i in range(0,len(words),step):
        
        chunk = words[i : i+chunk_size]
        
        
        chunk_text = " ".join(chunk)
        
        chunks.append(chunk_text)
        
        
    return chunks    


    