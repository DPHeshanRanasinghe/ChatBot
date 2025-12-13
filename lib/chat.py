from lib.clean import strip_think
from lib.logger import logger

def chat(rag_chain):
    """Interactive chat loop with the RAG chain.
    
    Args:
        rag_chain: The RAG chain to use for answering questions.
    """
    logger.info("Starting chat session. Type 'quit' or 'exit' to end.")
    print("\n💬 ChatBot Ready! Type 'quit' to exit.\n")
    
    while True:
        try:
            q = input("\nYou: ").strip()
            if not q:
                continue
            if q.lower() in ('quit', 'exit', 'q'):
                print("\nGoodbye! 👋")
                logger.info("Chat session ended by user")
                break
            
            logger.debug(f"User query: {q}")
            ans = rag_chain.invoke(q)
            cleaned = strip_think(ans["result"])
            logger.debug(f"Response: {cleaned[:100]}...")
            print("\nAssistant:", cleaned)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            logger.info("Chat session interrupted")
            break
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            print(f"\n⚠️ Error: {e}. Please try again.")