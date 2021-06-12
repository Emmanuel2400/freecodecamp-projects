import numpy as np

def calculate(list):
  mean =[]
  variance =[]
  standardD =[]
  maximum =[]
  minimum =[]
  sum_ =[]

  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  else:
    matrix = np.reshape(list,(3,3))
    
    mean.append(np.mean(matrix, axis=0).tolist())
    mean.append(np.mean(matrix, axis=1).tolist())
    mean.append(np.mean(matrix).tolist())
    
    variance.append(np.var(matrix, axis=0).tolist())
    variance.append(np.var(matrix, axis=1).tolist())
    variance.append(np.var(matrix).tolist())

    standardD.append(np.std(matrix, axis=0).tolist())
    standardD.append(np.std(matrix, axis=1).tolist())
    standardD.append(np.std(matrix).tolist())

    maximum.append(np.max(matrix, axis=0).tolist())
    maximum.append(np.max(matrix, axis=1).tolist())
    maximum.append(np.max(matrix).tolist())

    minimum.append(np.min(matrix, axis=0).tolist())
    minimum.append(np.min(matrix, axis=1).tolist())
    minimum.append(np.min(matrix).tolist())

    sum_.append(np.sum(matrix, axis=0).tolist())
    sum_.append(np.sum(matrix, axis=1).tolist())
    sum_.append(np.sum(matrix).tolist())

    calculations = {
      "mean": mean,
      "variance": variance,
      "standard deviation": standardD,
      "max": maximum,
      "min": minimum,
      "sum": sum_
    }
    return calculations