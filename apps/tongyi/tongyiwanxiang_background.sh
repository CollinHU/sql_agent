curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/background-generation/generation/' \
--header 'X-DashScope-Async: enable' \
--header 'Authorization: Bearer sk-74375edec5944b90913ec1e9509f797e' \
--header 'Content-Type: application/json' \
--data '{
    "model": "wanx-background-generation-v2",
    "input": {
        "base_image_url": "http://inner-materials.oss-cn-beijing.aliyuncs.com/graphic_design/jianguo/lllcho.lc/test_data/demo_example/demo/hailuo_2236873898_2.png",
        "ref_image_url": "http://inner-materials.oss-cn-beijing.aliyuncs.com/graphic_design/jianguo/lllcho.lc/test_data/demo_example/demo/d1faf4f26c8c4ea798d043a8bf3784bb_2.png",
        "ref_prompt": "sun rising remotely"
    },
    "parameters": {
        "n": 2,
        "noise_level": 300,
        "ref_prompt_weight": 0.5
    }
}'