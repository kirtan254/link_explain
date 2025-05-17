from langchain_community.document_loaders import PlaywrightURLLoader

def scrape_js_link(url: str):
    loader = PlaywrightURLLoader(urls=[url])
    docs = loader.load()
    return docs

if __name__ == "__main__":
    # url = "https://langchain-ai.github.io/langgraph/tutorials/get-started/2-add-tools/#next-steps"
    # url="https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_setup/py_intro/py_intro.html#intro"
    # url="https://google.github.io/adk-docs/agents/multi-agents/"
    # url="https://google.github.io/adk-docs/callbacks/"
    # url="https://timesofindia.indiatimes.com/"
    # url="https://timesofindia.indiatimes.com/astrology/zodiacs-astrology/baba-vangas-chilling-prediction-comes-true-the-device-thats-becoming-a-silent-killer-for-all-ages/articleshow/121138454.cms"
    # url="https://www.w3schools.com/python/python_numbers.asp"
    # url="https://www.neuramonks.com/"
    url="https://python.langchain.com/docs/how_to/embed_text/"

    
    
    docs = scrape_js_link(url)
    
    # Write the full page content to a file
    with open("output_emmbd.txt", "w", encoding="utf-8") as f:
        doc_text=docs[0].page_content
        f.write(docs[0].page_content)

    print("✅ Scraped content saved to 'output.txt'")
    print("doc text:",doc_text)


#---------------------------------------------------

