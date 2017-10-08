from testmicrosoftazure import generateToneWord
from topicAlgo import determineGenreOrMood
from Naked.toolshed.shell import execute_js, muterun_js

def main():
    success = execute_js('./../')
    toneWords = generateToneWord()
    return determineGenreOrMood(toneWords)

genre = main()
print(genre+" ------")
