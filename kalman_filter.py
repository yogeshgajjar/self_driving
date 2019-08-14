#########################################################################################################################################

# This example illustrates the kalman filter algorithm in 1-D world. 

# OBJECTIVE - Write a program that will iteratively update and predict based on the location measurements and inferred motions. 

# GIVEN - 
# measurements, motion, measurement_sig, motion_sig, mu, sig.

#########################################################################################################################################

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.] #the output predicts the next measurement using the last value of motion. 
motion = [1., 1., 2., 1., 2.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    print("Update: ", [mu, sig])
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    print("Predict: ", [mu,sig])


