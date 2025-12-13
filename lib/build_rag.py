from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from config import LLM_MODEL, TEMPERATURE, RETRIEVER_K
from lib.logger import logger

template = """You are an assistant for InfoTech College of Business & IT, an educational institute.
Your goal is to answer users' questions regarding courses, admissions, and student support based on the provided CONTEXT.

Guidelines:

Provide a direct and concise answer.
If the answer is present in the CONTEXT, respond exactly as stated.
Do not include reasoning, explanations, or any analysis of the context.
If the CONTEXT does not answer the question or if the query is unrelated to courses, admissions, or student support, redirect the user to EduProvider's customer service at +94 77 123 4567.
Never use "Assistant:" or "Answer:" before your response. Answer directly and clearly.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""

conversational_template = """You are an assistant for InfoTech College of Business & IT, an educational institute.
Your goal is to answer users' questions regarding courses, admissions, and student support based on the provided CONTEXT and CHAT HISTORY.

Guidelines:

Provide a direct and concise answer.
If the answer is present in the CONTEXT, respond exactly as stated.
Consider the CHAT HISTORY for context continuity.
Do not include reasoning, explanations, or any analysis of the context.
If the CONTEXT does not answer the question or if the query is unrelated to courses, admissions, or student support, redirect the user to EduProvider's customer service at +94 77 123 4567.
Never use "Assistant:" or "Answer:" before your response. Answer directly and clearly.

CHAT HISTORY:
{chat_history}

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""

# Reusable text template for prompts
PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])
CONVERSATIONAL_PROMPT = PromptTemplate(
    template=conversational_template, 
    input_variables=["chat_history", "context", "question"]
)

def build_rag(vs, with_memory: bool = False):
    """Build a RAG chain for question answering.
    
    Args:
        vs: Vector store instance.
        with_memory: If True, creates a conversational chain with memory.
    
    Returns:
        RAG chain instance.
    """
    logger.info(f"Building RAG chain with model: {LLM_MODEL}, temperature: {TEMPERATURE}")
    
    retriever = vs.as_retriever(search_kwargs={"k": RETRIEVER_K})
    llm = ChatOllama(model=LLM_MODEL, temperature=TEMPERATURE)
    
    if with_memory:
        logger.info("Creating conversational chain with memory")
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        qa = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": PROMPT}
        )
    else:
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": PROMPT}
        )
    
    logger.info("RAG chain built successfully")
    return qa
