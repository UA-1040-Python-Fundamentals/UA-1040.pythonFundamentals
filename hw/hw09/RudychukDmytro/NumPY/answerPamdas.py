from checker import check_answer
import pandas as pd

# Read the CSV file
df = pd.read_csv('hw/hw09/RudychukDmytro/NumPY/data.csv')
df.dropna()

print(df) #test


#task 01 - the total number of bytes used
df.columns = df.columns.str.strip()  # Видаляємо пробіли на початку і в кінці назв колонок
total_bytes = df['Number of bytes'].sum()

print(total_bytes)


#task02 - the average number of bytes per request
average_bytes_per_request = df['Number of bytes'].mean()

print(average_bytes_per_request)


#task03  - the most popular country (by the number of requests)
most_popular_country = df['Country'].value_counts().idxmax()

print(most_popular_country)


#task04 - the user who is on the 3rd place by the number of bytes
sorted_df = df.sort_values(by='Number of bytes', ascending=False)
user_on_3rd_place = sorted_df.iloc[2]['Username']

print(user_on_3rd_place)

#task05 - the number of bytes used by users from Ukraine
ukraine_users = df[df['Country'] == 'Ukraine']
ukraine_users['Number of bytes'] = ukraine_users['Number of bytes'].astype(int)
total_bytes_ukraine = ukraine_users['Number of bytes'].sum()

print(total_bytes_ukraine)

#task06 - number of unique users
unique_users_count = df['Username'].nunique()

print(unique_users_count)

#task 07 - the difference between the average number of bytes per request between users from Ukraine and the UK (rounded to the nearest whole number)
ukraine_data = df[df['Country'] == 'Ukraine']
avg_bytes_ukraine = ukraine_data['Number of bytes'].mean()
uk_data = df[df['Country'] == 'UK']
avg_bytes_uk = uk_data['Number of bytes'].mean()
difference = avg_bytes_ukraine - avg_bytes_uk

print(difference)

#task08 - average number of bytes per IP address
average_bytes_per_ip = df.groupby('IP')['Number of bytes'].mean().reset_index()

print(average_bytes_per_ip)

#task09 - total number of users from Europe (UK, France, Germany, Poland and Ukraine)
european_countries = ['UK', 'France', 'Germany', 'Poland', 'Ukraine']
european_users = df[df['Country'].isin(european_countries)]
total_european_users = european_users['Username'].nunique()

print(total_european_users)