import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import pickle

#load the xlsx file
df=pd.read_excel("VINTED52.xlsx")
X = df[['prix', 'taille', 'couleur', 'état', 'marque', 'nbre abonnés', 'abonnements']]
y = df[['nbre intéressé', 'nbre vues']]
x_train, x_test,y_train,y_test =train_test_split( X,y,test_size=0.2,random_state=50)
rf_regressor = RandomForestRegressor()
# Fit the model on the training data
rf_regressor.fit(x_train, y_train)
# Perform cross-validation
scores = cross_val_score(rf_regressor, X, y, cv=5)

#make pickle file 

pickle.dump(rf_regressor, open("model.pkl", "wb"))