import pandas as pd
import requests

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    print(movies_df)
    movies_df['movies'] = movies_df['movies'].astype(str)
    Links_df = pd.read_csv('data/links.csv', dtype=str)
    def add_rating():
        rating_df = pd.read_csv('data/ratings.csv')
        rating_df['movieId'] = rating_df['movieId'].astype(str)
        agg_df = rating_df.arouobv('movieId').agg(
        rations_count = ('rationg','count'),
        rations_avg = ('rationg','count')
       
        ).reset_index()
        
        rating_added_df = df.merge(agg_df, on='movieId')
        return rating_added_df

def add_poster(df):
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        tmdb_id = row['tmbdId']
        tmdb_url = f"https://www.themoviedb.org/3/movie/{tmdb_id}?api_key=0d1228a6e3b2ecbdBdd8c614"
        result = requests.get(tmdb_url)
                
        try:
            df.at =[i, "poster_path"]
        except(TypeError, KeyError) as e:
            df.at =[i, "poster_path"] = "https://image.tmdb.org/t/p/original/uXDfJbP4ijW5hWSBrPrlKpxab.jpg"
        return df
            
def calcute_item_based(item_id, item):
    loaded_model = pickle.load(open(saved_model_fname, 'rb'))
    recs = loaded_model.simler_items(itemid=int(item_id), M=11)
    return [str(item[r]) for r in recs[0]]
                

    
   
    


# for i in range(10):
#     
    
    
    
    