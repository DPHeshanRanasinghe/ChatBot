from lib.clean import strip_think

def chat(rag_chain):
    while True:
        q = input("\nYou: ").strip()
        if not q:
            continue
        ans = rag_chain.invoke(q)
        cleaned = strip_think(ans["result"])
        print("\nAssistant:", cleaned)