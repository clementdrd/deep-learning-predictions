from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import api
import os

# Get the dataset and stock it into a variable

def ml_script(toto) :


   print("YOOOO LA RUE")
   print("DATASET PASSER EN PARAM:" + toto)
   print("YOOOO LA RUE")

   #dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
   dataset = loadtxt(toto, delimiter=',')

   # In this case the dataset have 9 columns of data

   # Datas are composed of 8 columns

      #1. Number of times pregnant
      #2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
      #3. Diastolic blood pressure (mm Hg)
      #4. Triceps skin fold thickness (mm)
      #5. 2-Hour serum insulin (mu U/ml)
      #6. Body mass index (weight in kg/(height in m)^2)
      #7. Diabetes pedigree function
      #8. Age (years)
      #9. Class variable (0 or 1)

   # creating variables containing the differents parts of the dataset

   revelant_datas = dataset[:,0:8]
   class_variable = dataset[:,8]

   # creating neuronal network and launch the predictions of it

   model = Sequential()
   model.add(Dense(12, input_dim=8, activation='relu'))
   model.add(Dense(8, activation='relu'))
   model.add(Dense(1, activation='sigmoid'))
   model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
   model.fit(revelant_datas, class_variable, epochs=150, batch_size=10, verbose=0)
   predictions = model.predict_classes(revelant_datas)

   #For each person we will try with their result their health state.
   #If a person is seek his classe will be 1 if not 0.

   result = []
   result_file = open("result.csv", "w+")
   limit = 700

   for i in range(limit):
      output = "Datas Received : %s || Prediction made => %d || (expected result for the dataset %d)" % (revelant_datas[i].tolist(), predictions[i], class_variable[i])
      result.append(output)
      if(i == 250):
         result_file.write(output)
      else:
         result_file.write(output + "\n")
      print(output)

   return(result)


if __name__ == "__main__":

   ml_script(toto="")