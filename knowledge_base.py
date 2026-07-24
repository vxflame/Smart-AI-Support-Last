knowledge_base = {
    "about": (
        "Sohail Smart Solutions is a technology company that provides "
        "smart digital and AI-based solutions."
    ),
    "services": (
        "Sohail Smart Solutions provides services such as artificial intelligence, "
        "machine learning, AI agents, automation, APIs, and smart business solutions."
    ),
    "internship": (
        "The AI internship helps students learn Python, data analysis, machine learning, "
        "APIs, AI agents, large language models, GitHub, and documentation."
    ),
    "contact": (
        "For official contact details, please use the company website or contact "
        "Sohail Smart Solutions directly."
    ),
}


def retrieve_information(question: str) -> str | None:
    """Return matching information from the small company knowledge base."""

    question = question.lower().strip()

    if not question:
        return None

    if any(word in question for word in ["service", "provide", "offer"]):
        return knowledge_base["services"]

    if any(word in question for word in ["about", "company", "sohail"]):
        return knowledge_base["about"]

    if any(word in question for word in ["internship", "intern", "training"]):
        return knowledge_base["internship"]

    if any(word in question for word in ["contact", "email", "phone"]):
        return knowledge_base["contact"]

    return None
