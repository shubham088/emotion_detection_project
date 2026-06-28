import requests, json


def emotion_detector(txt):
    ''' function to analyze text '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": txt } }

    resp = requests.post(url, headers = headers, json=input_json)
    print("resp : ", resp.status_code)
    # return resp.text
    if resp.status_code == 400:
        return {'anger':None, 'joy':None, 'fear':None, 
        'disgust':None, 'sadness':None, 'dominant_emotion':None}
    out = json.loads(resp.text)
    final_dict = {}
    final_dict = out['emotionPredictions'][0]['emotion']
    dominant_key = max(final_dict, key=final_dict.get)
    # Add it back to the dictionary
    final_dict["dominant_emotion"] = dominant_key
    return final_dict