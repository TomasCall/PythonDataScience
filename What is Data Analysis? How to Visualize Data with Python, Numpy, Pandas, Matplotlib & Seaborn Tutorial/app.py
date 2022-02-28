import numpy as np


def crop_yield(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result


def main():
    w1, w2, w3 = 0.3, 0.2, 0.5
    
    #Numpy arrays have the type ndarray
    weights = np.array([w1, w2, w3])
    kanto = np.array([73, 67, 43])
    johto = np.array([91, 88, 64])
    hoenn = np.array([87, 134, 58])
    sinnoh = np.array([102, 43, 37])
    unova = np.array([69, 96, 70])

    #compute the dot product of the two vectors using the np.dot function
    print(f"Kanto dot:{np.dot(kanto,weights)}")
    print(f"Johto dot:{np.dot(johto,weights)}")
    print(f"Hoenn dot:{np.dot(hoenn,weights)}")
    print(f"Sinnoh dot:{np.dot(sinnoh,weights)}")
    print(f"Unova dot:{np.dot(unova,weights)}")

    #OR
    #print(f"Kanto dot:{(kanto*weights).sum()}")
    #print(f"Johto dot:{(johto*weights).sum()}")
    #print(f"Hoenn dot:{(hoenn*weights).sum()}")
    #print(f"Sinnoh dot:{(sinnoh*weights).sum()}")
    #print(f"Unova dot:{(unova*weights).sum()}")


    #Multi dimensonal numpy arrays
    climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
    #Get the rows and cols numbers
    print(f"Climate data shape: {climate_data.shape}")
    print(f"Weights shape{weights.shape}")

    #3D array
    arr3 = np.array([
    [[11, 12, 13], 
     [13, 14, 15]], 
    [[15, 16, 17], 
     [17, 18, 19.5]]])
    print(f"Arr3 shape: {arr3.shape}")

    #Matrix multiplication
    print(f"Climate_data x weights{np.matmul(climate_data, weights)}")
    #or
    print(f"Climate_data x weights{climate_data @ weights}")

    #CSV File





if __name__=="__main__":
    main()