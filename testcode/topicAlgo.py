from extractEmotionData import getEmotions
import json

# def determineTopic():
#     try:
#         topthree = getEmotions()
#         topEmotion = getEmotions()[2]
#         top2 = getEmotions()[1]
#         top3 = getEmotions()[0]

def determineGenre(tags):
    with open('dataMappings.json') as data_file:
        data = json.load(data_file)
        print(data)

determineGenre([])
