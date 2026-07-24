knowledge_base = {
    "services": "Sohail Smart Solutions provides AI solutions, Machine Learning, AI Agents, APIs, and automation services.",
    "about": "Sohail Smart Solutions develops intelligent AI solutions for businesses."
}

def retrieve_information(question):
    question = question.lower()

    if "service" in question:
        return knowledge_base["services"]
    elif "about" in question or "company" in question:
        return knowledge_base["about"]

    return None
