import faiss
import numpy as np

dimension = 384

stored_chunks = []  # List to store the chunks of text

index = faiss.IndexFlatL2(dimension)  # L2 distance metric

def add_embeddings(embeddings,chunks):
    embeddings = np.array(embeddings, dtype=np.float32)
    index.add(embeddings)
    stored_chunks.extend(chunks)  # Store the corresponding chunks of text
    
    



def search_similar_chunks(question,embedding_model,k=3):
    
    question_embedding = embedding_model.encode([question])
    
    question_embedding = np.array(question_embedding, dtype=np.float32)
    
    distances, indices = index.search(question_embedding, k)
    
    retrieved_chunks = []
    
    for idx in indices[0]:
        if idx!=-1  and idx < len(stored_chunks):
            retrieved_chunks.append(stored_chunks[idx])
    
    return retrieved_chunks


        
    

