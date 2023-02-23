from sklearn.metrics import f1_score, precision_score, recall_score
import numpy as np
def printResult(y_test, y_pred):
    y = np.array(y_test)
    count = 0
    for i in range(0, len(y_pred)):
        if y[i] == y_pred[i]:
            count = count + 1
    return (count / len(y_pred)), precision_score(y_test, y_pred, average="micro"), recall_score(y_test, y_pred, average="micro"), f1_score(y_test, y_pred, average="micro")
#ts - vd - dd
#tbđh