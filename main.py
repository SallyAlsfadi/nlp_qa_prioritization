from extractor import load_quality_attributes, extract_quality_attributes
from prioritizer import load_role_weights, prioritize_by_cfv
import os
import json

def read_user_stories(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    # --- Load Data ---
    stories = read_user_stories("data/user_stories.txt")
    quality_attributes = load_quality_attributes("data/quality_attributes.json")
    role_weights = load_role_weights("data/role_weights.json")

    print("📘 Loaded", len(stories), "user stories.")

    # --- Prioritize ---
    final_scores = prioritize_by_cfv(
        stories,
        extract_quality_attributes,
        quality_attributes,
        role_weights
    )

    # --- Output ---
    print("\n📊 Prioritized Quality Attributes (CFV):")
    for i, (attr, score) in enumerate(final_scores, 1):
        print(f"{i}. {attr.title()} (Score: {score:.2f})")
