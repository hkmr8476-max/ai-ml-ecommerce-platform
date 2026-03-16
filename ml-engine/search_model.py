def semantic_score(query: str, text: str) -> float:
    query_terms = set(query.lower().split())
    text_terms = set(text.lower().split())
    overlap = len(query_terms.intersection(text_terms))
    return overlap / max(len(query_terms), 1)
