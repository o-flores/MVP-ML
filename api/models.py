from utils import active_modes, binary_map, gender_map
import numpy as np


class Predict_Body:
  def __init__(self, gender, age, height, family_history_with_overweight, FAVC, FCVC,
    NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS):
    self.gender = gender_map.get(gender)  
    self.age = int(age)
    self.height = float(height)
    self.family_history_with_overweight = binary_map.get(family_history_with_overweight)
    self.FAVC = binary_map.get(FAVC)
    self.FCVC = binary_map.get(FCVC)
    self.NCP = int(NCP)
    self.CAEC = 0 if CAEC == 'no' else 1
    self.SMOKE = binary_map.get(SMOKE)
    self.CH2O = float(CH2O)
    self.SCC = binary_map.get(SCC)
    self.FAF = float(FAF)
    self.TUE = int(TUE)
    self.CALC = 0 if CALC == 'no' else 1
    self.MTRANS_active = 1 if MTRANS in active_modes else 0


  def transform_into_X_input(body):
    X_input = np.array([body.gender, body.age, body.height, body.family_history_with_overweight, body.FAVC, body.FCVC, body.NCP, body.CAEC, body.SMOKE, body.CH2O, body.SCC, body.FAF, body.TUE, body.CALC, body.MTRANS_active]) 
    X_input = X_input.reshape(1, -1)
    return X_input

