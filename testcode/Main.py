from testmicrosoftazure import generateToneWord
from topicAlgo import determineGenreOrMood

def main():
    toneWords = generateToneWord()
    return determineGenreOrMood(toneWords)
main()
