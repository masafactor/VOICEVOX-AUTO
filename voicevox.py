import json
import requests
import wave

def generate_wav(texts, fileprefix='', start_number=1):
    host = 'localhost'
    port = 50021

    speakers = [3, 7,22]  # スピーカー番号の配列

    for i, text in enumerate(texts):
        for j, speaker in enumerate(speakers):
            number = start_number + i  # 先頭の数字

            params = (
                ('text', text),
                ('speaker', speaker),
            )
            response1 = requests.post(
                f'http://{host}:{port}/audio_query',
                params=params
            )
            headers = {'Content-Type': 'application/json',}
            response2 = requests.post(
                f'http://{host}:{port}/synthesis',
                headers=headers,
                params=params,
                data=json.dumps(response1.json())
            )

            filepath = f'{fileprefix}{number}-{j+1}.wav'  # ファイル名の先頭の数字を指定
            wf = wave.open(filepath, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(response2.content)
            wf.close()

if __name__ == '__main__':
    texts = ['text1','Text2']
    generate_wav(texts, start_number=1)
