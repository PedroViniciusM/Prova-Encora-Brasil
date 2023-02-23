def MakeChange(value: float, lastSet: list = [(0,0,0,0)]):
  def MakeChangeRecursive (value: float, lastSet: list):
    result_arrays = []
    if value >= 25:
      copy = [(item[0]+1, item[1], item[2], item[3]) for item in lastSet]
      result_arrays = [*MakeChangeRecursive(value-25, copy), *result_arrays]
    if value >= 10:
      copy = [(item[0], item[1]+1, item[2], item[3]) for item in lastSet]
      result_arrays = [*MakeChangeRecursive(value-10, copy), *result_arrays]
    if value >= 5:
      copy = [(item[0], item[1], item[2]+1, item[3]) for item in lastSet]
      result_arrays = [*MakeChangeRecursive(value-5, copy), *result_arrays]
    if value >= 1:
      copy = [(item[0], item[1], item[2], item[3]+1) for item in lastSet]
      result_arrays = [*MakeChangeRecursive(value-1, copy), *result_arrays]
    if result_arrays:
      return set(result_arrays)
    return set(lastSet)  
  return [list(result) for result in list(MakeChangeRecursive(value, lastSet))]



value = float(input())

print(MakeChange(value))
