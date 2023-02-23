import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def data_encoder(X):
    for i in range(len(X)):
        # Age
        if int(X[i][0]) >= 21 and int(X[i][0]) <= 30:
            X[i][0] = 3
        elif int(X[i][0]) >= 31 and int(X[i][0]) <= 40:
            X[i][0] = 4
        elif int(X[i][0]) >= 41 and int(X[i][0]) <= 50:
            X[i][0] = 5
        elif int(X[i][0]) >= 51 and int(X[i][0]) <= 60:
            X[i][0] = 6
        elif int(X[i][0]) >= 61 and int(X[i][0]) <= 70:
            X[i][0] = 7
        elif int(X[i][0]) >= 71 and int(X[i][0]) <= 80:
            X[i][0] = 8
        elif int(X[i][0]) >= 81 and int(X[i][0]) <= 90:
            X[i][0] = 9
        #JOB
        if X[i][1] == "blue-collar":
            X[i][1] = 10
        elif X[i][1] == "entrepreneur":
            X[i][1] = 11
        elif X[i][1] == "retired":
            X[i][1] = 12
        elif X[i][1] == "admin.":
            X[i][1] = 13
        elif X[i][1] == "services":
            X[i][1] = 14
        elif X[i][1] == "technician":
            X[i][1] = 15
        elif X[i][1] == "self-employed":
            X[i][1] = 16
        elif X[i][1] == "management":
            X[i][1] = 17
        elif X[i][1] == "student":
            X[i][1] = 18
        elif X[i][1] == "unemployed":
            X[i][1] = 19
        elif X[i][1] == "housemaid":
            X[i][1] = 20
        elif X[i][1] == "unknown":
            X[i][1] = 21
        # Marital
        if X[i][2] == "married":
            X[i][2] = 22
        elif X[i][2] == "divorced":
            X[i][2] = 23
        elif X[i][2] == "single":
            X[i][2] = 24
        elif X[i][2] == "unknown":
            X[i][2] = 25
        #Education
        if X[i][3] == "basic.9y":
            X[i][3] = 26
        elif X[i][3] == "university.degree":
            X[i][3] = 27
        elif X[i][3] == "basic.4y":
            X[i][3] = 28
        elif X[i][3] == "professional.course":
            X[i][3] = 29
        elif X[i][3] == "high.school":
            X[i][3] = 30
        elif X[i][3] == "basic.6y":
            X[i][3] = 31
        elif X[i][3] == "unknown":
            X[i][3] = 32
        #default
        if X[i][4] == "yes":
            X[i][4] = 1
        elif X[i][4] == "no":
            X[i][4] = 0
        elif X[i][4] == "unknown":
            X[i][4] = 2
        #housing
        if X[i][5] == "yes":
            X[i][5] = 1
        elif X[i][5] == "no":
            X[i][5] = 0
        elif X[i][5] == "unknown":
            X[i][5] = 2
        #loan
        if X[i][6] == "no":
            X[i][6] = 0
        elif X[i][6] == "yes":
            X[i][6] = 1
        elif X[i][6] == "unknown":
            X[i][6] = 2
        #contact
        if X[i][7] == "cellular":
            X[i][7] = 33
        elif X[i][7] == "telephone":
            X[i][7] = 34
        elif X[i][7] == "unknown":
            X[i][7] = 35
        if len(X) == 1:
            return X.astype('int')
    return X


def getData():
    data = pd.read_csv("data/customer_deposit 2.csv")
    dt_train, dt_test = train_test_split(
        data_encoder(data.values), test_size=0.3, shuffle=False
    )
    X_train = dt_train[:, :8]
    y_train = dt_train[:, 8]
    X_test = dt_test[:, :8]
    y_test = dt_test[:, 8]
    return dt_train, dt_test, X_train, y_train, X_test, y_test

def getData1(age, job, marital, education, default, housing, loan, contact):
    X_data = np.array(
        [[
            age,
            job,
            marital,
            education,
            default,
            housing,
            loan,
            contact
        ]]
    )
    return data_encoder(X_data)