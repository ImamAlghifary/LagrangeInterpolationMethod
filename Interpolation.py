import numpy as np

def lagrange_interpolation(x_values, y_values, x_target):
    """
    Perform Lagrange polynomial interpolation.
    """
    n = len(x_values)
    result = 0.0

    # Calculate f_n(x) = sum(f(x_i) * l_i(x))
    for i in range(n):
        l_i = 1.0  # Initialize l_i(x)
        for j in range(n):
            if i != j:
                l_i *= (x_target - x_values[j]) / (x_values[i] - x_values[j])
        result += y_values[i] * l_i

    return result


def calculate_true_error(actual, predicted):
    """
    Calculate True Absolute and Relative Errors.
    Parameters:
        actual (float): The actual value.
        predicted (float): The predicted/interpolated value.
    Returns:
        tuple: Absolute True Error and Absolute Percent Relative Error.
    """
    absolute_true_error = abs(actual - predicted)
    relative_true_error = (absolute_true_error / abs(actual)) * 100
    return absolute_true_error, relative_true_error


def month_to_fraction(year, month):
    """
    Convert a year and month into a fractional year.
    Parameters:
        year (int): The year.
        month (int): The month (1-12).
    Returns:
        float: The fractional year.
    """
    return year + (month - 1) / 12.0


def main():
    print("Lagrange Polynomial Interpolation Program (Now supports monthly predictions)")
    
    # Given data
    x_values = [2010, 2015, 2016, 2017, 2018]
    y_values = [238, 255, 258, 261, 264]

    print("\nKnown data:")
    for x, y in zip(x_values, y_values):
        print(f"Year: {int(x)}, Population: {y} million")
    
    # Input target year and month
    x_target_year = int(input("\nEnter the year to interpolate: "))
    x_target_month = int(input("Enter the month to interpolate (1-12): "))
    x_target = month_to_fraction(x_target_year, x_target_month)
    interpolated_value = lagrange_interpolation(x_values, y_values, x_target)
    print(f"\nInterpolated/Extrapolated Population in {x_target_year}-{x_target_month:02d}: {interpolated_value:.6f} million")
    
    # Input actual data (for True Error Calculation)
    actual_value = input("\nEnter the actual population for the specified year and month (if available): ")
    if actual_value.strip():
        actual_value = float(actual_value)
        if actual_value == 0:
            print("\nActual population is 0 or unavailable. Skipping True Error calculation.")
        else:
            absolute_true_error, relative_true_error = calculate_true_error(actual_value, interpolated_value)
            print("\n--- True Errors ---")
            print(f"True Absolute Error: {absolute_true_error:.6f}")
            print(f"True Relative Error: {relative_true_error:.6f}%")
    else:
        print("\nNo actual data entered, skipping True Error calculation.")
    
    repeat = input("\nWould you like to predict another date? (yes/no): ").lower()
    if repeat == "yes":
        main()

if __name__ == "__main__":
    main()
