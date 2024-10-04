# 1. Library imports
import pickle
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

with open('utils/le.pkl', 'rb') as archivo_pkl:
    le = pickle.load(archivo_pkl)

my_vocabulary = pickle.load(open("utils/feature.pkl", "rb"))

transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace", vocabulary=my_vocabulary)

# 2.  Functions to standardize and predict.
def func_transform(user_input):
    t1 = transformer.fit_transform(loaded_vec.fit_transform(user_input))
    return t1

def salida_pred(prediction):
    prediction = le.inverse_transform(prediction)[0]
    predicted = "Film prediction: {}".format(prediction)
    return predicted
