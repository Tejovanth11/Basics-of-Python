#importing new libraries
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
#importing test document
weather = pd.read_csv('Test.csv')
weather.head()
weather.info()
#plotting the graphs
sns.barplot(weather['humidity'], weather['temperature'])
sns.displot(weather['humidity'])
sns.displot(weather['humidity'], kde=False, rug=True)
sns.jointplot(weather['humidity'], weather['temperature'])
sns.jointplot(weather['humidity'], weather['temperature'], kind="hex")
sns.jointplot(weather['humidity'], weather['temperature'], kind="kde")
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
sns.stripplot(weather['weather_type'], weather['temperature'])
sns.stripplot(weather['weather_type'], weather['temperature'], jitter = True)
sns.swarmplot(weather['humidity'], weather['temperature'])
sns.boxplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.barplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.countplot(weather['weather_type'])
sns.pointplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
sns.lmplot(x="humidity", y="temperature", data=weather)
sns.lmplot(x="humidity", y="temperature", hue="weather_type", data=weather)
