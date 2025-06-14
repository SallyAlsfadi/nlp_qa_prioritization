import json
import re

def load_quality_attributes(path):
    with open(path, 'r') as f:
        return json.load(f)

def extract_quality_attributes(story, quality_attributes):
    matched_attributes = set()
    story_lower = story.lower()
    for attr, keywords in quality_attributes.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', story_lower):
                matched_attributes.add(attr)
                break
    return list(matched_attributes)
