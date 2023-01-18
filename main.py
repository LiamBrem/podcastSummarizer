from youtube_transcript_api import YouTubeTranscriptApi
import config
import openai

#config is ignored so api key doesn't get shared
API_KEY = config.api_key

def getId(url):
    for i in range(len(url)):
        #returns the rest of the string following the "v=" in the URL
        if url[i:i+2] == "v=":
            return url[i+2:]

def getUserInput():
    url = input("Paste URL: ")
    return getId(url)

def returnTranscript(id):
    transcriptDict = YouTubeTranscriptApi.get_transcript(id)

    finalString = ""

    #segment is a dictionary, transcriptDict is a list of dictionaries
    for segment in transcriptDict:
        finalString += segment["text"] + " "

    return finalString


if __name__ == "__main__":
    id = getUserInput()
    transcript = returnTranscript(id)

    openai.api_key = API_KEY

    openai.Model.list()

