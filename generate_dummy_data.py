import pandas as pd
import numpy as np
import os

data = {
    "country_txt": ["India", "Pakistan", "USA", "Afghanistan", "Iraq"] * 20,
    "region_txt": ["South Asia", "South Asia", "North America", "South Asia", "Middle East & North Africa"] * 20,
    "weaptype1_txt": ["Explosives", "Firearms", "Melee", "Incendiary", "Unknown"] * 20,
    "targtype1_txt": ["Military", "Police", "Private Citizens", "Government", "Business"] * 20,
    "gname": ["Taliban", "Al-Qaida", "ISIS", "Boko Haram", "Unknown"] * 20,
    "success": np.random.randint(0, 2, 100),
    "suicide": np.random.randint(0, 2, 100),
    "nkill": np.random.randint(0, 50, 100),
    "nwound": np.random.randint(0, 100, 100),
    "attacktype1_txt": ["Bombing/Explosion", "Armed Assault", "Assassination", "Hijacking", "Hostage Taking"] * 20,
    "iyear": np.random.randint(2010, 2023, 100),
    "latitude": np.random.uniform(-90, 90, 100),
    "longitude": np.random.uniform(-180, 180, 100),
    "city": ["New Delhi", "Islamabad", "New York", "Kabul", "Baghdad"] * 20
}

df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv("data/globalterrorism.csv", index=False, encoding="latin1")
print("Dummy data created at data/globalterrorism.csv")
