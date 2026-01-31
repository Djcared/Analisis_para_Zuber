import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datasets
df_company = pd.read_csv('/datasets/project_sql_result_01.csv')
df_neighborhoods = pd.read_csv('/datasets/project_sql_result_04.csv')
# Mostrar las primeras filas de cada DataFrame
df_company.head()
df_neighborhoods.head()
df_company.info()
df_neighborhoods.info()
# Cambiar tipos de datos
df_company['trips_amount'] = df_company['trips_amount'].astype(int)
df_neighborhoods['average_trips'] = df_neighborhoods['average_trips'].astype(float)


#Identificar los 10 principales barrios por finalizaciones de viajes
top_10_neighborhoods = df_neighborhoods.sort_values(
    by='average_trips', ascending=False
).head(10)

top_10_neighborhoods

#Gráfica: Empresas de taxi vs número de viajes
plt.figure(figsize=(10, 6))
plt.bar(df_company['company_name'], df_company['trips_amount'])
plt.xticks(rotation=90)
plt.title('Número de viajes por empresa de taxis (15–16 Nov 2017)')
plt.xlabel('Empresa de taxis')
plt.ylabel('Número de viajes')
plt.show()
#Gráfica: Top 10 barrios por finalizaciones de viajes
plt.figure(figsize=(10, 6))
plt.bar(top_10_neighborhoods['dropoff_location_name'],
        top_10_neighborhoods['average_trips'])
plt.xticks(rotation=45)
plt.title('Top 10 barrios por número promedio de finalizaciones')
plt.xlabel('Barrio')
plt.ylabel('Promedio de viajes')
plt.show()
# Cargar y mostrar el dataset para la hipótesis
df_hypothesis = pd.read_csv('/datasets/project_sql_result_07.csv')
df_hypothesis.head()
df_hypothesis.info()
# Convertir la columna de timestamps a formato datetime
df_hypothesis['start_ts'] = pd.to_datetime(df_hypothesis['start_ts'])
alpha = 0.05
bad_weather = df_hypothesis[df_hypothesis['weather_conditions'] == 'Bad']['duration_seconds']
good_weather = df_hypothesis[df_hypothesis['weather_conditions'] == 'Good']['duration_seconds']
from scipy import stats
results = stats.ttest_ind(bad_weather, good_weather, equal_var=False)
print("T-statistic:", results.statistic)
print("P-value:", results.pvalue)
if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula: hay una diferencia significativa en la duración de los viajes entre condiciones climáticas buenas y malas.")else:
    print("No rechazamos la hipótesis nula: no hay una diferencia significativa en la duración de los viajes entre condiciones climáticas buenas y malas.")
#Prueba estadistica T-test
from scipy import stats

results = stats.ttest_ind(bad_weather, good_weather, equal_var=False)

results

p_value = results.pvalue

if p_value < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No rechazamos la hipótesis nula")

print("p-value:", p_value)

