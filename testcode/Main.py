import topicAlgo
import testmicrosoftazure
from Naked.toolshed.shell import execute_js, muterun_js


def main():
    toneWords = analyze_tone("I don't know confusion something joy")
    print("TESTING CODE")
    print(determineGenreOrMood(toneWords))
    success = execute_js('../javascript/video.js')
    print("HERE")

main()
