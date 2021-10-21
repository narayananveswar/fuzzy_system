import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd


data = pd.read_csv("heart.csv") # importing data

# initialising the input
age = ctrl.Antecedent(np.arange(25, 81, 5), 'age')
sex = ctrl.Antecedent(np.arange(0 , 2, 1), 'sex')
cp = ctrl.Antecedent(np.arange(0, 4, 1), 'cp')
trestbps = ctrl.Antecedent(np.arange(90, 201, 5), 'trestbps')
chol = ctrl.Antecedent(np.arange(125, 565, 5), 'chol')

# initialising the output
presence = ctrl.Consequent(np.arange(0,2,1), 'presence')

# dont know how it works 
age.automf(3)
cp.automf(3)
trestbps.automf(3)
chol.automf(3)
presence.automf(3)

# rules for deciding the output
rule1 = ctrl.Rule(age['poor'] | cp['poor'] | trestbps['poor'] | chol['poor'], presence['poor'])
rule2 = ctrl.Rule(age['average'] | cp['average'] | trestbps['average'] | chol['average'], presence['average'])
rule3 = ctrl.Rule(age['good'] | cp['good'] | trestbps['good'] | chol['good'], presence['good'])

# taking the inputs 
result.input['age'] = 60
result.input['cp'] = 2
result.input['trestbps'] = 124
result.input['chol'] = 250

# generating the control using the rules
result_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
result = ctrl.ControlSystemSimulation(result_ctrl)

#computing output
print(result.compute())