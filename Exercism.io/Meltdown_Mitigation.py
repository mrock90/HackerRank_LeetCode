# In this exercise, we'll develop a simple control system for a nuclear reactor.

# For a reactor to produce the power it must be in a state of criticality. If the reactor is in a state less than criticality, it can become damaged. If the reactor state goes beyond criticality, it can overload and result in a meltdown. We want to mitigate the chances of meltdown and correctly manage reactor state.

# The following three tasks are all related to writing code for maintaining ideal reactor state.

# 1. Check for criticality

# The first thing a control system has to do is check if the reactor is balanced in criticality. A reactor is said to be critical if it satisfies the following conditions:

# The temperature is less than 800 K.

# The number of neutrons emitted per second is greater than 500.

# The product of temperature and neutrons emitted per second is less than 500000.

# Implement the function is_criticality_balanced() that takes temperature measured in kelvin and neutrons_emitted as parameters, and returns True if the criticality conditions are met, False if not.



# 2. Determine the Power output range

# Once the reactor has started producing power its efficiency needs to be determined. Efficiency can be grouped into 4 bands:

# green -> efficiency of 80% or more,

# orange -> efficiency of less than 80% but at least 60%,

# red -> efficiency below 60%, but still 30% or more,

# black -> less than 30% efficient.

# The percentage value can be calculated as (generated_power/theoretical_max_power)*100 where generated_power = voltage * current. Note that the percentage value is usually not an integer number, so make sure to consider the proper use of the < and <= comparisons.

# Implement the function reactor_efficiency(<voltage>, <current>, <theoretical_max_power>), with three parameters: voltage, current, and theoretical_max_power. This function should return the efficiency band of the reactor : 'green', 'orange', 'red', or 'black'.



# 3. Fail Safe Mechanism

# Your final task involves creating a fail-safe mechanism to avoid overload and meltdown. This mechanism will determine if the reactor is below, at, or above the ideal criticality threshold. Criticality can then be increased, decreased, or stopped by inserting (or removing) control rods into the reactor.

# Implement the function called fail_safe(), which takes 3 parameters: temperature measured in kelvin, neutrons_produced_per_second, and threshold, and outputs a status code for the reactor.

# If temperature * neutrons_produced_per_second < 90% of threshold, output a status code of 'LOW' indicating that control rods must be removed to produce power.

# If the value temperature * neutrons_produced_per_second is within 10% of the threshold (so either 0-10% less than the threshold, at the threshold, or 0-10% greater than the threshold), the reactor is in criticality and the status code of 'NORMAL' should be output, indicating that the reactor is in optimum condition and control rods are in an ideal position.

# If temperature * neutrons_produced_per_second is not in the above-stated ranges, the reactor is going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor.

"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    # Though Process: The problem explicitly lists three conditions, all of which must be true for the reactor to be "critical". This is the perfect scenario for combining boolean expressions using the 'and' logical operator.
    # Rationale: Direct translation of the problems's logical requirements into a single boolean expression
    # Each condition is checked using standard comparison operators
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    # Thought Process: First, we need to calculate the generated power and then the efficiency percentage
    # These are intermediate steps necessary before we can apply the efficiency band logic
    # Rationale: FOllows the formula given in the problem description directly
    generated_power = voltage * current

    # Though Process: Calculate efficiency. We must consider the edge case where theoretical_max_power is zero tp avoid a ZeroDivisionError. ALthough not explicitly stated as a constraint, it's good practice.
    # Also, the problem states the percentage is usually not an integer, so direct float division is needed
    # Rationale: Implements the efficiency formula. THe check for theoretical_max_power == 0 ensures robustness, returnin 'black' as 0 efficiency falls into that lowest band
    if theoretical_max_power == 0:
        return 'black' # Or raise an error, depending on problem spec. 'black' is a reasonable default for 0 max power

    efficiency_percentage = (generated_power / theoretical_max_power) * 100

    # Thought Process: Now, categorize the efficiency into bands using if-elif-else
    # It's usually best to start from the highest (or lowest) band and work your way down to avoind overlapping conditions and ensure correctness. Here, we'll start from 'green' as it's the highest threshold
    # Rationale: This series of conditional statements precisely implements the band definitions
    # Using 'elif' ensures that only one band is returned, and the order correctly captures the non-overlapping ranges (e.g., if it's 80 or more, it's green, otherwise, if it's 60 or more...)
    if efficiency_percentage >= 80:
        return 'green'
    elif efficiency_percentage >= 60: # Implies < 80 because the first 'if' caught >= 80
        return 'orange'
    elif efficiency_percentage >= 30: # Implies < 60
        return 'red'
    else: # Implies < 30
        return 'black'



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    # Though Process: First, compute the product as it's the core value to compare againse the threshold
    # Rationale: Thisis the primary value whose relationship to the threshold determines the status
    product = temperature * neutrons_produced_per_second

    # Though Process: Calculate the specific thresholds for the 'NORMAL' range and the 'LOW' range
    # Rationale: These calculations set up the boundaries for the conditional checks, making the subsequent 'if/elif' statements cleaner and more readable
    low_normal_bound = threshold * 0.9 # 90% of threshold
    high_normal_bound = threshold * 1.1 # 110% of threshold

    # Thought Process: Apply the conditional logic based on the calculated product and bounds
    # The order of checks is important. Start with 'LOW' as it's the most straightforward "less than" check
    # Then check the 'NORMAL' range. Finally, if neither of the first two conditions is met, it must be 'DANGER'
    # Rationale: This sequence of if-elif-else statements directly implements the fail-safe logic
    # The 'NORMAL' condition uses a combined check ('and') to ensure the product falls within both the lower and upper bounds of the +/- 10% range
    if product < low_normal_bound:
        return 'LOW'
    elif low_normal_bound <= product <= high_normal_bound: # This covers threshold +/- 10% 
        return 'NORMAL'
    else: # If not LOW and not NORMAL, it must be DANGER
        return 'DANGER'
