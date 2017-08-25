import re

def clean_paste(data):
    data = re.sub(r'<stuff>[\s\S]*</stuff>', r'<replacewiththisstuff>', data)
    data = re.sub(r'<stuff>[\s\S]*</stuff>', r'<replacewiththisstuff>', data)
    return data
