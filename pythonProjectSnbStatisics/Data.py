import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV Datei einlesen
df = pd.read_csv(
    r"D:\Git Repos\SnBAuslandInvestitionen\pythonProjectSnbStatisics\data.csv",
    index_col=0)

# Kategorien für Liniendiagramme
line_plot_categories = ["Direktinvestitionen", "Portfolioinvestitionen", "Derivate", "Übrige Investitionen", "Währungsreserven"]

# Kuchendiagramm für das Quartal 1985-Q1
plt.figure(figsize=(8, 6))
df.loc["1985-Q1", line_plot_categories].plot(kind='pie', title='Kuchendiagramm für 1985-Q1', autopct='%1.2f%%', ylabel='')
plt.show()

# Liniendiagramm für jede gewünschte Kategorie
for category in line_plot_categories:
    plt.figure(figsize=(10, 6))
    df[category].plot(title=f'Liniendiagramm für {category}')
    plt.ylabel(category)
    plt.xticks(ticks=range(0, len(df), len(df)//10), labels=df.index[::len(df)//10])  # Anpassung der xticks für 10 Zeiträume
    plt.legend()
    plt.show()

# Reshape data into long format
categories = ["Direktinvestitionen", "Portfolioinvestitionen", "Derivate", "Übrige Investitionen", "Währungsreserven", "Nettoauslandvermögen"]
df_long = df.melt(value_vars=categories, var_name="Category", value_name="Value")

# Drop NaN values from "Derivate" before plotting
df_long = df_long.dropna(subset=["Value"])

# Horizontal boxplot for all categories
plt.figure(figsize=(10, 8))
sns.boxplot(data=df_long, x="Value", y="Category", orient='h', whis=[0, 100])
plt.title('Horizontal Boxplot für alle Kategorien')
plt.show()

# Statistische Daten für jede Kategorie
for category in categories:
    stats = df[category].describe()
    skewness = df[category].skew()
    skewness_direction = "rechtschief" if skewness > 0 else "linksschief"

    print(f"Statistiken für {category}:")
    print(f"Minimalwert: {stats['min']:.2f}")
    print(f"1. Quartil: {stats['25%']:.2f}")
    print(f"Median (2. Quartil): {stats['50%']:.2f}")
    print(f"3. Quartil: {stats['75%']:.2f}")
    print(f"Maximalwert: {stats['max']:.2f}")
    print(f"Interquartilsabstand (IQR): {stats['75%'] - stats['25%']:.2f}")
    print(f"Mittelwert: {stats['mean']:.2f}")
    print(f"Schiefe: {skewness_direction} ({skewness:.2f})")
    print("\n")

# Kovarianz und Grafik
cov_matrix = df[["Direktinvestitionen", "Portfolioinvestitionen", "Übrige Investitionen", "Währungsreserven"]].cov()
print(
    f"Kovarianz zwischen Direktinvestition und Portfolioinvestition: {cov_matrix.loc['Direktinvestitionen', 'Portfolioinvestitionen']:.2f}")
print(
    f"Kovarianz zwischen übrige Investitionen und Währungsreserven: {cov_matrix.loc['Übrige Investitionen', 'Währungsreserven']:.2f}")

sns.scatterplot(data=df, x="Direktinvestitionen", y="Portfolioinvestitionen")
plt.title("Scatterplot: Direktinvestitionen vs. Portfolioinvestitionen")
plt.show()

sns.scatterplot(data=df, x="Übrige Investitionen", y="Währungsreserven")
plt.title("Scatterplot: Übrige Investitionen vs. Währungsreserven")
plt.show()

# Liniendiagramm für den gesamten Zeitraum über alle Kategorien
plt.figure(figsize=(12, 8))
df[categories].plot()
plt.title('Liniendiagramm über den gesamten Zeitraum für alle Kategorien')
plt.ylabel('Wert')
plt.xlabel('Zeitraum')
plt.legend(loc="upper left")
plt.xticks(ticks=range(0, len(df), len(df)//10), labels=df.index[::len(df)//10])  # Anpassung der xticks für 10 Zeiträume
plt.show()