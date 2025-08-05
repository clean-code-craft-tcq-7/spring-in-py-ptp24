
def calculateStats(numbers):
  """
  Calculate statistics (average, maximum, minimum) from a list of numbers.
  
  Args:
      numbers: A list of numeric values (int, float)
  
  Returns:
      A dictionary with keys 'avg', 'max', and 'min' containing the
      respective statistics. Returns NaN for all values if the input is empty
      or contains non-numeric values.
  """
  stats = {}
  
  # Check if input is a list
  if not isinstance(numbers, list):
    stats["avg"] = float('nan')
    stats["max"] = float('nan')
    stats["min"] = float('nan')
    return stats
  
  # Filter out non-numeric values and convert strings that represent numbers
  valid_numbers = []
  for item in numbers:
    try:
      # Try to convert to float if it's a string representation of a number
      if isinstance(item, str):
        valid_numbers.append(float(item))
      # Check if it's already a numeric type
      elif isinstance(item, (int, float)):
        valid_numbers.append(item)
    except (ValueError, TypeError):
      # Skip items that can't be converted to numbers
      continue
  
  # Calculate statistics if we have valid numbers
  if valid_numbers:
    stats["avg"] = sum(valid_numbers) / len(valid_numbers)
    stats["max"] = max(valid_numbers)
    stats["min"] = min(valid_numbers)
  else:
    stats["avg"] = float('nan')
    stats["max"] = float('nan')
    stats["min"] = float('nan')
    
  return stats # type: ignore