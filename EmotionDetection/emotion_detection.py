import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_prediction = formatted_response["emotionPredictions"][0]["emotion"]

        dom_emotion_score = 0
        dom_emotion = ""
        for key in emotion_prediction:
            if (emotion_prediction[key] > dom_emotion_score):
                dom_emotion_score = emotion_prediction[key]
                dom_emotion = key

        return {
            "anger": emotion_prediction["anger"],
            "disgust": emotion_prediction["disgust"],
            "fear": emotion_prediction["fear"],
            "joy": emotion_prediction["joy"],
            "sadness": emotion_prediction["sadness"],
            "dominant_emotion": dom_emotion
        }
