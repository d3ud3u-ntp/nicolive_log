# misawaGPT
女に惚れさす名言集を自動生成する実験をしました。

1. ミサワブログのイラストのaltを収集する (opt/misawadata.csv)
1. ChatGPTに雑に投げる (for_chat_gpt.txt)
1. テーマを提示すると、そのお題に沿った惚れさせ男子のコメントが出力されます。(sample_response.txt)



# memo

- docker build -t misawagpt-python3
- docker run --rm -it -v $(pwd)/:/home web-app