import pandas as pd

import warnings
warnings.filterwarnings("ignore")

imdb_movies=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/imdb_movies_3070.csv')

#write your code here

#Create new dataframe called movies_df
movies_df = imdb_movies[['imdb_title_id', 'original_title', 'director', 'avg_vote']]

#type cast conversion of director to string
movies_df['director'] = movies_df ['director'].astype('str')

#print movies_df
print(movies_df.head(10))

#Split the director in movies_df 
director_split = pd.DataFrame(movies_df['director'].str.split(',').tolist(), index=movies_df['imdb_title_id']).stack()
director_split = director_split.reset_index(['imdb_title_id'])
director_split.columns = ['imdb_title_id', 'director_split']

#merge the dataframe to form merge_movies

merge_movies = pd.merge( director_split , movies_df[['imdb_title_id', 'original_title', 'avg_vote']],left_on ='imdb_title_id', right_on = 'imdb_title_id')
merge_movies['director_split'] = merge_movies['director_split'].str.lstrip(' ').str.rstrip(' ')

#Create groups and perform operations
new_df= merge_movies.groupby('director_split').agg({ 'imdb_title_id' : ['count'], 'avg_vote': ['mean']})
new_df.drop(new_df[new_df.index == 'nan'].index, inplace = True)
print(new_df.head(10))
