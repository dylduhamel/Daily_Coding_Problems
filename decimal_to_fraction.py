from fractions import Fraction

def decToFracAuto(num: float) -> str:
    return str(Fraction(num))

def decimal_to_fraction(decimal_value):
  # Set the maximum denominator value
  max_denominator = 10000

  # Initialize the numerator and denominator
  numerator = 0
  denominator = 1

  # Calculate the error between the actual and the approximate value
  error = abs(decimal_value - numerator / denominator)

  # Iterate over the possible denominator values
  for d in range(1, max_denominator + 1):
    # Calculate the numerator for the current denominator value
    n = round(decimal_value * d)

    # Calculate the new error
    new_error = abs(decimal_value - n / d)

    # If the new error is smaller than the previous error, update the numerator and denominator
    if new_error < error:
      error = new_error
      numerator = n
      denominator = d

      # If the error is small enough, return the fraction
      if error < 1e-10:
        return f"{numerator}/{denominator}"

  # If the maximum denominator value is reached, return the fraction with the maximum precision
  return f"{numerator}/{denominator}"


if __name__ == '__main__':
    print(decToFracAuto(0.25))
    print(decimal_to_fraction(0.25))
