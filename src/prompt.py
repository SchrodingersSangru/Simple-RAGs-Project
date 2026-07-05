from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt() -> ChatPromptTemplate:
    """Returns the chat prompt template for the RAG chain."""
    system_prompt = (
        "You are an intelligent assistant designed to answer questions using exclusively the provided context.\n"
        "If you do not know the answer or if it's not present in the context, say exactly "
        "'I cannot find the answer based on the provided documents.' Do not make things up.\n\n"
        "Context:\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    return prompt