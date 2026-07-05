import sys
from src.utils import run_ingestion_pipeline, query_rag_system

def main():
    print("Welcome to the Simple RAG Project CLI.")
    print("1. Ingest Documents (Run this first after placing files in data/raw/)")
    print("2. Query the System")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1/2/3): ").strip()
        
        if choice == "1":
            run_ingestion_pipeline()
        elif choice == "2":
            try:
                query = input("\nEnter your question: ").strip()
                if not query:
                    continue
                print("\nThinking...")
                answer = query_rag_system(query)
                print(f"\nAnswer:\n{answer}")
            except FileNotFoundError:
                print("\n[Error] Vector database index not found. Please run Option 1 (Ingest) first.")
            except Exception as e:
                print(f"\nAn error occurred: {e}")
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()