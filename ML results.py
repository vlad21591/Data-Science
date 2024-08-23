import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from time import time

val_features = pd.read_csv('val_features.csv')
val_labels = pd.read_csv('val_labels.csv')

test_features = pd.read_csv('test_features.csv')
test_labels = pd.read_csv('test_labels.csv')

models = {}
for model in ['LR', 'SVM', 'MLP', 'RF', 'GB']:
    models[model] = joblib.load('{}_model.pkl'.format(model))


def evaluate_model(name, mdl, features, labels):
    start = time()
    pred = mdl.predict(features)
    end = time()
    accuracy = round(accuracy_score(labels, pred), 3)
    precision = round(precision_score(labels, pred), 3)
    recall = round(recall_score(labels, pred), 3)
    print('{} -- Accuracy: {}, Precision: {}, Recall:{}, Latency: {}ms'.format(name, accuracy, precision, recall,
                                                                               int(end - start)))


for name, mdl in models.items():
    evaluate_model(name, mdl, val_features, val_labels)
print("\nWe found similar results with Random Forest and SVM models so we test them both with the test data:")
evaluate_model('Random Forest', models['RF'], test_features, test_labels)
evaluate_model('SVM', models['SVM'], test_features, test_labels)
print('\nWe can see that Random Forest model gets the best results which are:')
evaluate_model('Random Forest', models['RF'], test_features, test_labels)
