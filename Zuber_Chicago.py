import pandas as pd

# URL con los datos del clima
url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"

# Leemos todas las tablas que existan en la página
weather_records = pd.read_html(url, attrs={"id": "weather_records"})[0]
#Mostrando el DataFrame
print(weather_records)
weather = weather_records
print(weather.columns)
weather.shape
weather.info()
weather.columns = ['ts', 'temperature', 'description']
weather.head()
weather['ts'] = pd.to_datetime(weather['ts'])
weather.info()
weather['ts'].dt.month.unique(), weather['ts'].dt.year.unique()
weather.to_csv("chicago_weather_nov_2017.csv", index=False)
