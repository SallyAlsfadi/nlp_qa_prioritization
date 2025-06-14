from extractor import extract_quality_attributes, load_quality_attributes
import json

def read_ground_truth(path):
    with open(path, 'r') as f:
        return json.load(f)

def evaluate_predictions(stories, quality_attributes, ground_truth):
    tp, fp, fn = 0, 0, 0

    for i, story in enumerate(stories, 1):
        predicted = set(extract_quality_attributes(story, quality_attributes))
        actual = set(ground_truth.get(str(i), []))

        tp += len(predicted & actual)
        fp += len(predicted - actual)
        fn += len(actual - predicted)

    precision = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0

    return precision, recall, f1
