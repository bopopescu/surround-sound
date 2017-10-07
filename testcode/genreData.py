genres = ["hiphop", "pop", "popculture", "country", "workout", "chill", "electronic", "rock", "focus", "religious", "indie", "outside"]
moods = ["happy", "calm", "love", "sad", "angry", "confident"]

hiphop = {"hiphop": ["urban", "city", "rap", "culture", "populous", "downtown", "ghetto"]}
pop = {"pop": ["happy", "young", "party", "festival", "group", "bright"]}
popculture = {"popculture": ["media", "phone", "app", "art", "celebrity", "famous", "text", "internet"]}
workout = {"workout": ["gym", "workout", "exercise", "weight", "run", "running", "cycling"]}
chill = {"chill": ["relaxed", "study", "couch", "sitting", "sleep", "bed"]}
electronic = {"electronic": ["lights", "colors", "excited", "populous", "crowd"]}
rock = {"rock": ["angry", "guitar", "city", "black", "anger", "drums"]}
focus = {"focus": ["study", "paper", "pencil", "desk", "lamp", "light", "writing", "computer", "laptop", "book", "student"]}
religious = {"religious": ["church", "praying", "christian", "holy"]}
indie = {"indie": ["new", "young", "art", "record", "hipster"]}

genreMappings = {"hiphop": hiphop, "pop": pop, "popculture": popculture, "workout": workout,
"chill": chill, "electronic": electronic, "rock": rock, "focus": focus, "religious": religious, "indie": indie}

happy = {"happy": ["happy", "sun", "bright", "yellow", "smile", "beautiful", "outside", "food", "eating"]}
calm = {"calm": ["study", "work", "relaxed", "chill", "sleep", "slow", "nature", "water", "night", "dark"]}
love = {"love": ["couple", "heart", "wedding", "romantic", "rose", "candle", "flowers"]}
sad = {"sad": ["depressed", "blackandwhite", "sad", "crying", "rain", "night", "dark"]}
angry = {"angry": ["anger", "frustration", "red", "weapon", "knife"]}
confident = {"confident": ["power", "exercise", "gym", "workout", "confident", "work", "arm", "muscle", "bright", "mountain", "outside"]}

moodMappings = {"happy": happy, "calm": calm, "love": love, "sad": sad, "angry": angry, "confident": confident}

vocabDict = {}
vocab = set()

def createMappings(vocabDict, vocab):
    genreKeys = list(genreMappings.keys())
    for genreKey in genreKeys:
        genre = genreMappings[genreKey]
        genreWords = genreMappings[genreKey][genreKey]
        for word in genreWords:
            if word not in vocab:
                vocab.add(word)
                vocabDict[word] = {"hiphop": 0, "pop": 0, "popculture": 0, "workout": 0,
                "chill": 0, "electronic": 0, "rock": 0, "focus": 0, "religious": 0, "indie": 0,
                "happy": 0, "calm": 0, "love": 0, "sad": 0, "angry": 0, "confident": 0}
            # print(vocabDict[word])
            # print(genreKey)
            # print(vocabDict[word][genreKey])
            vocabDict[word][genreKey] += 1
            # print(vocabDict[word][genreKey])
    moodKeys = list(moodMappings.keys())
    for moodKey in moodKeys:
        mood = moodMappings[moodKey]
        moodWords = moodMappings[moodKey][moodKey]
        for word in moodWords:
            if word not in vocab:
                vocab.add(word)
                vocabDict[word] = {"hiphop": 0, "pop": 0, "popculture": 0, "workout": 0,
                "chill": 0, "electronic": 0, "rock": 0, "focus": 0, "religious": 0, "indie": 0,
                "happy": 0, "calm": 0, "love": 0, "sad": 0, "angry": 0, "confident": 0}
            vocabDict[word][moodKey] += 1
    return (vocabDict, vocab)

d, v = createMappings(vocabDict, vocab)
print(d)
