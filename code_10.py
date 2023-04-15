from yelpapi import YelpAPI
import pandas as pd

api_key = "ZD4sISRVvGlMkSVgdF45Q1HLKzRWEA-_vt-EWQ-hWorTCUUpt35Mt45TqOnJHpaXHBXYuWPEIVlv9bTuc_ciJpZefpXVKIcypBr6WhVzwv-2-tTfkpeqzNQoZSQ2ZHYx"
yelp_api = YelpAPI(api_key)

#search_query

search_term = "Pizza"
search_location = "Austin"
search_sort_by = "rating" 
search_limit = 20

search_results = yelp_api.search_query(term=search_term, location=search_location,
                                        sort_by=search_sort_by, limit=search_limit)

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])

id_for_reviews = "pedrosos-pizza-austin"


reviews_result = yelp_api.reviews_query(id = id_for_reviews)
print(reviews_result)

for review in reviews_result['reviews']:
    print(review['text'])

result_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(result_df)
result_df.to_csv(f"{id_for_reviews}_request_reviews_results.csv")
