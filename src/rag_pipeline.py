# from langchain.chains import create_retrieval_chain
# from langchain_classic.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from src.retriever import get_retriever
from src.prompt import get_rag_prompt
from src.generator import get_llm

def create_rag_chain():
    """Assembles and returns the full RAG pipeline execution chain."""
    llm = get_llm()
    prompt = get_rag_prompt()
    retriever = get_retriever()
    
    # Chain to combine retrieved documents into the prompt context
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    
    # Final chain combining retrieval + generation
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain