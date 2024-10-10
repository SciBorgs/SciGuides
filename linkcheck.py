import re
import os
import requests
import pathlib

#Add folders with files that should be checked here
print("Checking for dead links...")
checkFileList = []
repository = pathlib.Path(os.getcwd())
for item in list(repository.rglob("*")):
    if item.is_file() and str(item).endswith(".md"):
        checkFileList.append(f"{item}")
i = 0

while i <= len(checkFileList) - 1:
    if "archive" in checkFileList[i]:
        del checkFileList[i]
        i+=1
    i+=1

j = 0
counter = 0
linkStructure = r'\[.+\]\(https:\/\/[^\)]+\)|\[.+\]\(#[^\)]+\)'
lStructure = r'\(#[^\[]+\)|\(https:\/\/.+\)'
while j <= len(checkFileList) - 1:
    linkString = ""
    content = open(checkFileList[j])
    links = re.findall(linkStructure, content.read())
    for link in links:
        linkString += link
    checkLinks = re.findall(lStructure, linkString)
    k = 0
    while k <= len(checkLinks) - 1:
        currentLink = checkLinks[k]
        tempList = []
        for char in currentLink:
            tempList.append(char)
        del tempList[0]
        del tempList[-1]
        newCurrentLink = ""
        for c in tempList:
            newCurrentLink += c
        if newCurrentLink.startswith("https://"):
            checkLink = newCurrentLink
            ...
        else:
            checkLink = f"https://github.com/SciBorgs/SciGuides/blob/main/"
        if k == 1:
            checkLink = "https://docs.google.com"
        try:
            response = requests.get(checkLink)
            if response.status_code != 200:
                print("\033[1m" + f"Bad link found in {checkFileList[j]}, search source for {checkLink}" + "\033[0m")
                counter += 1
        except:
            print("\033[1m" + f"Bad link found in {checkFileList[j]}, search source for \n\n{checkLink}" + "\033[0m")
            counter += 1
        k += 1
    j+=1

if counter == 0:
    print("\033[1m" + "All links available." + "\033[0m")


