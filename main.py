import os

from Service import read_and_process_file, save_results, combine_and_filter_csv

if __name__ == '__main__':
    api_key = os.environ.get('DASHSCOPE_API_KEY')

    for i in range(1, 21):
        print(f'Now Start to Process No. *******{i}******* File')
        input_file = f'./Data/KR/KR_sentiment61412_1001yc_slice_{i}.csv'
        sentiment_temp_file = f'./Data/KR/sentiment_result_{i}.csv'
        output_file = f'./Data/KR/KR_sentiment61412_1001yc_slice_{i}_llm.csv'
        chunk_size = 50
        current_dir = os.getcwd()

        print(current_dir)
        print(api_key)

        sentiments = read_and_process_file(input_file, chunk_size)
        save_results(sentiments, sentiment_temp_file)

        combine_and_filter_csv(input_file, sentiment_temp_file, output_file)
        print(f'Now Done Process No. *******{i}******* File')


