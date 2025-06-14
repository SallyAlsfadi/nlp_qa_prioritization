import json
from collections import defaultdict

def load_role_weights(path):
    with open(path, 'r') as f:
        return json.load(f)

def extract_role(story_text):
    """Extracts role from story format: 'As a [role], I want ...'"""
    match = re.match(r"As a ([^,]+),", story_text.strip(), re.IGNORECASE)
    return match.group(1).lower() if match else "unknown"

def prioritize_by_cfv(stories, extractor, quality_attributes, role_weights):
    scores = defaultdict(float)

    for story in stories:
        role = extract_role(story)
        weight = role_weights.get(role, 1)  # Default to 1 if not found
        matched = extractor(story, quality_attributes)

        for attr in matched:
            scores[attr] += weight

    # Sort by CFV (highest to lowest)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_scores
