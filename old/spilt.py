def split_text_into_chunks(text, max_chunk_length=10000):  # was 2048 before
    

    # https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270 
    
    
    
    """
    Splits the text into chunks suitable for GPT-style models.
    
    Parameters:
        - text: The input text to be split.
        - max_chunk_length: Maximum length for each chunk. Default is 2048.
        
    Returns:
        - A list of chunks.
    """
    
    words = text.split()
    chunks = []
    current_chunk = ""
    for word in words:
        if len(current_chunk) + len(word) < max_chunk_length - 100:  # 100 is a buffer for the "part x/y" text
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    # Add the "part x/y" text
    total = len(chunks)
    for idx, chunk in enumerate(chunks):
        prefix = f"This is part {idx + 1}/{total} of the context. "
        chunks[idx] = prefix + chunk
        
    return chunks

# Read text from file
with open("fullHtml.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = split_text_into_chunks(text)
for chunk in chunks:
    print(chunk)
    print("-" * 50)
