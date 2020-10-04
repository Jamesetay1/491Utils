import requests
from bs4 import BeautifulSoup as bs
import json

def get_question_text(question_name):
    data = {"operationName":"questionData","variables":{"titleSlug":question_name},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}

    r = requests.post('https://leetcode.com/graphql', json = data).json()
    html_question = r['data']['question']['content']
    soup = bs(r['data']['question']['content'], 'lxml')
    title = r['data']['question']['title']
    plain_question =  soup.get_text().replace('\n',' ')
    return [title, html_question, plain_question]

problem_names = ["two-sum", "add-two-numbers", "longest-substring-without-repeating-characters"]
all_problems = list(map(get_question_text, problem_names))
#print(all_problems)

#Problem 0, all info
print(all_problems[0]) #[0] is title, [1] is html, [2] is plaintext