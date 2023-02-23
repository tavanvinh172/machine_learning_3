from data_encoder import getData
from tkinter import *
from ui import draw_ui 
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from kfold_logisticR_neuralN import kfoldLogisticRegressionAndNeuralNetwork

dt_train, dt_test, X_train, y_train, X_test, y_test= getData()


print("\t LOGISTIC REGRESSION")
regres = kfoldLogisticRegressionAndNeuralNetwork(dtTrain=dt_train,Algorithm= LogisticRegression(random_state = 0))

print("\t NEURAL NETWORK")
neuralN = kfoldLogisticRegressionAndNeuralNetwork(dtTrain = dt_train, Algorithm= MLPClassifier(random_state=1, activation='identity', hidden_layer_sizes=(100, 100,), shuffle=False, max_iter=900))
#form
form = Tk()
form.title("Dự đoán khách hàng có gửi tiền vào ngân hàng:")
form.geometry("1000x500")

draw_ui(form, y_test, neuralN, regres, X_test)

form.mainloop()