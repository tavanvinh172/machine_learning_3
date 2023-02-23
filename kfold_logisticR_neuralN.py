
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

def error(y, yPrd):
    return accuracy_score(y, yPrd)

def kfoldLogisticRegressionAndNeuralNetwork(dtTrain, Algorithm):
    regr = 0
    k = 5
    kf = KFold(n_splits=k, random_state=None)
    max = 0
    for train_index, test_index in kf.split(dtTrain):
        print("TRAIN: ", train_index, "\nTEST: ", test_index)
        xTrain, xTest = dtTrain[train_index, :8], dtTrain[test_index, :8]
        yTrain, yTest = dtTrain[train_index, 8], dtTrain[test_index, 8]
        lr = Algorithm.fit(xTrain, yTrain)

        yPrdTrain = lr.predict(xTrain)
        yPrdTest = lr.predict(xTest)

        sum = error(yTrain, yPrdTrain) + error(yTest, yPrdTest)
        print('sum', sum)
        if sum > max:
            max = sum
            regr = lr

    return regr
    
