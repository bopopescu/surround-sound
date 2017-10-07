import topicAlgo
import testmicrosoftazure

def main():
    toneWords = analyze_tone("I don't know confusion something joy")
    print(determineGenreOrMood(toneWords))
