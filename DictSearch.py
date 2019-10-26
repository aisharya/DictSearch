def isSubString(word1,str1):
    i=0;j=0
    m=len(word1)
    n=len(str1)
    while (i<m and j<n):
        if word1[i]==str1[j]:
            i+=1
        j+=1
    return i==m
def findLongestString(dict1,str1):
    length = 0
    result = ""
    for word in dict1:
        if length <len(word)and isSubString(word,str1):
            length = len(word)
            result = word
    return result


dict1 = ["darshan","aish","mom","darshanish"]
str1 = "mdarsomhandadishjk"
print(findLongestString(dict1,str1))

x = [str(x) for x in input("Enter multiple value: ").split()]
print("the value is ", x)  
print("enter the word")
str1 = str(input())
print(findLongestString(x,str1))

