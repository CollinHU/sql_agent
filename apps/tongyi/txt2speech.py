# coding=utf-8

import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key='sk-74375edec5944b90913ec1e9509f797e'

result = SpeechSynthesizer.call(model='sambert-cally-v1',
                                text="Alibaba Cloud, founded in 2009, is a global leader in cloud computing and artificial intelligence, providing services to thousands of enterprises, developers, and governments organizations in more than 200 countries and regions. Committed to the success of its customers, Alibaba Cloud provides reliable and secure cloud computing and data processing capabilities as a part of its online solutions. In January 2017, Alibaba Cloud became the official cloud services partner of the Olympics. ",
                                sample_rate=16000,
                                format='wav')

if result.get_audio_data() is not None:
    with open('output.wav', 'wb') as f:
        f.write(result.get_audio_data())
print('  get response: %s' % (result.get_response()))