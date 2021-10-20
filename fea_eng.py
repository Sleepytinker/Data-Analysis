import pandas as pd
data=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv')

#check type
print(data['duration'].dtypes)

#Print the top 10 values of 'duration' column
#print(data['duration'].head(10))

#Print the two columns 'type' , 'duration' values.
#print(data[['type','duration']])

print(data['type'].head(10))

import warnings
warnings.filterwarnings("ignore")

#create new dataframe for type 'movies'
movies_df= data[data['type'] =='Movie']

#print all column name of new dataframe
print(movies_df.columns)

#Eliminate min from type column of movies_df
movies_df['movie_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)

#print the top 5 values of movie_duration column
print(movies_df['movie_duration'].head(5))

print(movies_df['movie_duration'].dtypes)
