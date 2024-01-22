import pandas as pd
import matplotlib.pyplot as plt

def main():

    # Chemin du dataset brut
    csv_path = "nyc_temperature.csv"

    
    # Ouverture du dataset avec pandas (le délimiteur est ",")
    df = pd.read_csv(csv_path, delimiter=',')

    print(len(df.columns))

    # Convertir la colonne 'Forecast timestamp' en objets de date et d'heure sans décalage horaire
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y')
    df.sort_values(by=df.columns[0])

    new_df = df.iloc[:, [0, 3]]

    print(new_df)

    x = new_df['date']
    y = new_df['tavg']

    plt.figure(figsize=(10,6))
    plt.plot(x, y, marker='o', linestyle=' ')

    plt.show()





if __name__ == "__main__":
    main()