from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

template = """You are an assistant for InfoTech College of Business & IT, an educational institute.
Your goal is to answer users' questions regarding courses, admissions, and student support based on the provided CONTEXT.

Guidelines:

Provide a direct and concise answer.
If the answer is present in the CONTEXT, respond exactly as stated.
Do not include reasoning, explanations, or any analysis of the context.
If the CONTEXT does not answer the question or if the query is unrelated to courses, admissions, or student support, redirect the user to EduProvider’s customer service at +94 77 123 4567.
Never use "Assistant:" or "Answer:" before your response. Answer directly and clearly.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""

# Reusable text template for prompts
PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

def build_rag(vs):
    retriever = vs.as_retriever(search_kwargs={"k": 4}) # Retrieve the top 4 most relevant documents
    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0) # LLM model with temperature 0 for deterministic responses

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff", # dump all retrieved documents into the prompt
        chain_type_kwargs={"prompt": PROMPT} # the prompt template defined above
        # fetches the revelant documents and uses the prompt template defined above to generate the final answer
    )
    return qa
