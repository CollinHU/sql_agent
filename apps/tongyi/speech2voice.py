# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

from http import HTTPStatus
import dashscope
import json
 
dashscope.api_key='sk-74375edec5944b90913ec1e9509f797e'
 
task_response=dashscope.audio.asr.Transcription.async_call(
    model='paraformer-mtl-v1',
    file_urls=['https://gitee.com/collin-hu/test/raw/master/d2.mp3']
    )
transcribe_response=dashscope.audio.asr.Transcription.wait(task=task_response.output.task_id)
if transcribe_response.status_code == HTTPStatus.OK:
    print(json.dumps(transcribe_response.output, indent=4, ensure_ascii=False))
    print('transcription done!')