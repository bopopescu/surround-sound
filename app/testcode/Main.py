from topicAlgo import determineGenreOrMood
from testmicrosoftazure import analyze_tone
from testmicrosoftazure import getToneWords

def main():
    toneWords = getToneWords()
    #print(eval(toneWords)['description'])
    print("GENRE/MOOD" + determineGenreOrMood(toneWords))

main()
