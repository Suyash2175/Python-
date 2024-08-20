def calculate_voltage(L, I, T):
    """
    Calculate the DC voltage drop.

    Parameters:
    L (float): Length of the circuit in meters.
    I (float): Current through the circuit in Amperes.
    T (float): Time for which the current has flowed through the circuit in seconds.

    Returns:
    float: The DC voltage drop in Volts.
    """
    V = (L * I) / T
    return V

# Given values
L_cm = 500  # Length in centimeters
I = 10      # Current in Amperes
T = 20      # Time in seconds

# Convert length to meters
L_m = L_cm / 100  # 1 meter = 100 centimeters

# Calculate the voltage drop
voltage_drop = calculate_voltage(L_m, I, T)

print(f"The DC voltage drop is {voltage_drop} Volts.")
