def chunk_text(text, size=200, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + size, len(text))

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks


text = """
University libraries provide students with access to books, journals,
research papers, and electronic resources.

Students can search the library catalog to find books and academic materials.
The library also provides databases that contain thousands of scientific papers.

Digital libraries allow students to access resources online from anywhere.
Students can download electronic books and research papers using the library system.

Artificial intelligence can improve library services.
For example, AI-based systems can recommend relevant books and papers to students.

Retrieval-Augmented Generation (RAG) can also be used in libraries.
RAG retrieves relevant information from the library knowledge base and provides it
to a Large Language Model to generate an answer.
"""


chunks = chunk_text(text, size=200, overlap=50)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n===== Chunk {i+1} =====")
    print(chunk)
