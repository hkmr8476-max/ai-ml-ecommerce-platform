import numpy as np


def collaborative_filtering(user_item_matrix: np.ndarray, user_index: int, top_k: int = 5) -> list[int]:
    scores = user_item_matrix[user_index]
    return list(np.argsort(scores)[::-1][:top_k])


def content_based(product_feature_matrix: np.ndarray, profile_vector: np.ndarray, top_k: int = 5) -> list[int]:
    sims = product_feature_matrix @ profile_vector
    return list(np.argsort(sims)[::-1][:top_k])


def hybrid_recommendations(collab: list[int], content: list[int], top_k: int = 5) -> list[int]:
    merged = []
    for pid in collab + content:
        if pid not in merged:
            merged.append(pid)
    return merged[:top_k]
