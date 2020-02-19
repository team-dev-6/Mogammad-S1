import pandas as pd
from time import sleep as slp
D = {"Chips": {"Simba": [13,
                         "Beef",
                         "250g",
                         200],
              "Lays": [13,
                        "Salt and Pepper",
                        "250g",
                        400]             
              },
     "Cooldrinks": {"Coke": [9,
                             "Vanilla",
                             "250ml",
                             150],
                    "Fanta": [9,
                             "Grape",
                             "250ml",
                             120]
                   },
     "Chocolates": {"Cadbury": [14,
                               "Caramel",
                               "150g",
                               55],
                    "Tex": [13,
                            "Original",
                            "150g",
                            30]
                   },
     "Pies": {"Pepper Steak": [10,
                               50], 
              "Chicken": [10, 
                          55],
              "Feta and Cheese": [13,
                                 25]
             },
     "Fruit": {"Pear": [15,
                       "1kg",
                       26], 
              "Apple": [12,
                       "1.5kg",
                       35], 
             "Orange": [13,
                       "1kg",
                       45]
              },
     "Cupcakes": {"vanilla": [3.5,
                             "50g",
                             90],
                 "chocolate": [3.5,
                               "50g",
                               89]
                 },
     "Veggies": {"spinach": [5,
                            None,
                            "250g",
                            45], 
                "cabbage": [6,
                            None,
                            "205g",
                            65]
                }
    }
keys = list(D.keys())
indices = {"Chips": ["Price", "Flavour", "Mass", "Quantity"],
          "Cooldrinks": ["Price", "Flavour", "Volume", "Quantity"],
          "Chocolates": ["Price", "Flavour", "Volume", "Quantity"],
          "Pies": ["Price", "Quantity"],
          "Fruit": ["Price", "Mass", "Quantity"],
          "Cupcakes": ["Price", "Mass", "Quantity"],
          "Veggies": ["Price", "Flavour", "Mass", "Quantity"]}
dfs = []
#pd.DataFrame(D["Cooldrinks"] ,index = indices["Cooldrinks"])
for i, j in zip(keys, indices):
    df = pd.DataFrame(D[i], index = indices[j])
    dfs.append(df)
#print(dfs)
for df in dfs:
    slp(0.65)
    print("-"*86)
    print(df)