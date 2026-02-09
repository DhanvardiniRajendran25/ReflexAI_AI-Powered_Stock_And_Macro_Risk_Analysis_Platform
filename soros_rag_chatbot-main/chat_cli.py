# chat_cli.py

from rag_interface import SorosRAGChatbot


def main():
    print("=== Soros RAG Chatbot ===")
    print("Ask about trading, investing, macro, Soros philosophy, etc.")
    print("Type 'exit' or 'quit' to stop.\n")

    bot = SorosRAGChatbot()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            print("SorosBot: Please type a question.\n")
            continue

        reply = bot.answer(user_input)
        print("\nSorosBot:", reply, "\n")


if __name__ == "__main__":
    main()
