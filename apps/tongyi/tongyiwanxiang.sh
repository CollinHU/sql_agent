curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-74375edec5944b90913ec1e9509f797e' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-v1",
    "input": {
        "prompt": "一只奔跑的加菲猫"
    },
    "parameters": {
        "style": "<sketch>", 
        "size": "1024*1024",
        "n":4, 
        "seed":42
    }
}'