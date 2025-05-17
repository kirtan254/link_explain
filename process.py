# explain_docs.py

from web_static import scrape_js_link
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

def explain_link(url: str) -> str:
    # Load environment
    load_dotenv()
    AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

    # Set up LLM
    llm = AzureChatOpenAI(
        openai_api_key=AZURE_API_KEY,
        openai_api_version=AZURE_VERSION,
        azure_endpoint=AZURE_ENDPOINT,
        deployment_name=DEPLOYMENT_NAME,
        temperature=0
    )

    # Step 1: Scrape
    docs = scrape_js_link(url)
    doc_text = docs[0].page_content

    print(doc_text)

    # Step 2: Chunk
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(doc_text)

    # Step 3: Explain and Merge
    final_merged_explanation = ""

    for i, chunk in enumerate(chunks):
        print(f"\n🔹 Processing Chunk {i+1}...\n{'-'*60}")

        prompt = f"""
                    You are a technical assistant helping a user understand technical documentation in a way that sounds natural when spoken aloud.

                    Your job is to:
                    1. **Keep the original content unchanged** — do not rewrite or paraphrase it.
                    2. **Identify complex sentences, technical jargon, or code blocks**, and insert **short, clear explanations right after them**.
                    3. Write in a style that sounds **natural when read aloud**, like a teacher speaking to a curious beginner.
                    4. Do **not** include labels like "Explanation:", "Note:", or "Summary:" — just insert the explanation as a continuation of the original sentence or as a new spoken-sentence paragraph.
                    5. Clearly explain what the code or term is doing, but **do not modify or remove the code**.

                    Only insert helpful, spoken-style explanations where needed — don’t over-explain.

                    Here is the content:
                    {chunk}
                    """

        response = llm.invoke(prompt)
        explained = response.content
        final_merged_explanation += f"\n{explained}\n"

    return final_merged_explanation.strip()


if __name__ == "__main__":
    url = input("🔗 Enter the URL to process: ")
    result = explain_link(url)
    print("\n✅ Final Explained Output:\n")
    print(result)

    with open("merged_explained_output.md", "w", encoding="utf-8") as f:
        f.write(result)
