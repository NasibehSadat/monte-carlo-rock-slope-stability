
import numpy as np

# Mean and standard deviation of friction angle
mean_friction_angle = 30.0
std_friction_angle = 2.0

# Number of random samples
number_of_samples = 10

# Generate random samples
friction_angles = np.random.normal(
    loc=mean_friction_angle,
    scale=std_friction_angle,
    size=number_of_samples
)

# Display the results
print("Random friction angle samples:")
print(friction_angles)
