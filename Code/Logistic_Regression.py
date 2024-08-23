import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

tr_features = pd.read_csv('train_features.csv')
tr_labels = pd.read_csv('train_labels.csv')


def print_results(results):
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))
    print('\nBest Params: {}\n'.format(results.best_params_))


lr = LogisticRegression(max_iter=10000)
parameters = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

cv = GridSearchCV(lr, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel())
print_results(cv)

joblib.dump(cv.best_estimator_, 'LR_model.pkl')
