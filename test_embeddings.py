from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import add_embeddings,index



chunks = ["This is the first chunk of text.", "This is the second chunk of text.", "This is the third chunk of text."]


embeddings = generate_embeddings(chunks)


print("before adding embeddings to FAISS index:", index.ntotal)  # Print the number of vectors in the index before adding new embeddings

add_embeddings(embeddings)

print("after adding embeddings to FAISS index:", index.ntotal)  # Print the number of vectors in the index after adding new embeddings


    
    