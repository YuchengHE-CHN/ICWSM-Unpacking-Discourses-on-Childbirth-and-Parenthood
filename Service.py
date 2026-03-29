import pandas as pd
import re

from Controller import request_API


def read_and_process_file(file_path, chunk_size):
    all_sentiments = []
    with pd.read_csv(file_path, chunksize=chunk_size) as reader:
        for chunk in reader:
            chunk["cleaned_content"] = chunk["cleaned_content"].astype(str)
            chunk["full_title"] = chunk["full_title"].astype(str)
            chunk['video_attitude'] = chunk['video_attitude'].replace({'不生育(Negative)': 0, '爱生育(Positive)': 1})
            chunk["video_source"] = chunk["video_source"].astype(str)
            sentiments = process_chunk(chunk)
            all_sentiments.extend(sentiments)
    return all_sentiments


def process_chunk(chunk):
    sentiments = []
    for content, video_head, video_attitude, video_source \
            in zip(chunk["cleaned_content"], chunk["full_title"], chunk["video_attitude"], chunk["video_source"]):
        sentiment = request_API(content, video_head, video_source, video_attitude)
        match = re.search(r'(\d)', sentiment)
        if match:
            support_degree = float(match.group(1))
            sentiments.append(support_degree)
            print('Added Score')
        else:
            sentiments.append(100)
            print('********************* Cant give a sentiment score!*********************')
    return sentiments


def save_results(sentiments, output_file):
    df = pd.DataFrame({'sentiment_llm': sentiments})
    df.to_csv(output_file, index=True, encoding='utf-8')
    print(f'Results saved to {output_file}')


def combine_and_filter_csv(input_file, sentiment_temp_file, output_file):
    df1 = pd.read_csv(sentiment_temp_file)
    df2 = pd.read_csv(input_file)
    combined_df = pd.merge(df1, df2, left_index=True, right_index=True)
    print(combined_df)
    selected_df = combined_df[['cid', 'full_title', 'cleaned_content',
                               'video_attitude', 'video_source', 'sentiment_llm']]
    selected_df.to_csv(output_file, index=False, encoding='utf-8-sig')
