
import os
import string
import json
pressyour_input_file=input("pless enter your name inputfile whit path loation")
pressyour_output_file=input("pless enter your name json outputfile white path ocation")
pressyour_ignore_file=input("pleas enter ignor file")

try:
    file=open(pressyour_input_file)
    file.read()
    file.close()
except FileNotFoundError:
    print("the file does not exist.")
    import sys
    sys.exit(0)

with open(pressyour_input_file,"r+") as file1: 
    import string 
    count,count2,count4,words_all,full_stops,sentences,blanklines=0,0,0,0,0,0,0
    lines=file1.readlines()
    tot_line=len(lines)
    print("total number of lines:")
    print(tot_line)
    y11= str(tot_line)
    sentences=0 
    for line in lines:
        if line.startswith('\n'):
            blanklines += 1
        else:
            sentences += line.count('.')+ line.count ('!')+ line.count('?')
    print(" number of sentences:")
    print(sentences)
    y22=str(sentences)
    print(" number of blank lines:")
    print(blanklines)
    y33=str(blanklines)
    #list_word=[]
    #for line in lines:
        #words_all = words_all + len(line.split())
        #list_word.append(words_all)
        #count2+=1
        #print ('Total words in line numer{}:{} '.format(count2,line.strip())  , words_all)
    #print(list_word)
    index=0
    list2=[]
    while index<len(lines):
        letter1=lines[index]
        words=letter1.split()
        list2.append(words)
        index+=1
        pass
    print("list of words in each lines apenned list item to search better:/n , list2")
    y44=str(list2)
    list3=[]
    count6=0
    while count6<len(list2):
        letter3=list2[count6]
        ab=len(letter3)
        list3.append(ab)
        count6+=1
        pass
    print("number of words in each line to search better :/n")
    print(list3)
    y66=str(list3)
    print('total number of words in te text:/n')
    print(sum(list3))
    d_f=sum(list3)
    y77=str(sum(list3))
    ###
    def occurrence_word(pressyour_input_file): 
        import string
        text = open(pressyour_input_file, "r+")
        d = dict()
        for line in text:
            line = line.strip()
            line = line.lower()
            line = line.translate(line.maketrans("", "", string.punctuation))
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
        text.close()
        return d                 
    #print(occurrence_word(pressyour_input_file))
    dic2=occurrence_word(pressyour_input_file).copy()
    print("the number for each consective words count:/n")
    print(dic2)
    y88=str(dic2)
    print("selected key to finde repeat word:",dic2.get('from'))
    def range_names_filter(min1,max1,list_of_names):
      return list(filter(lambda name: min1<= len(name)<= max1, list_of_names))
    list3=[]
    count7=0
    while count7<len(list2):
        letter2=list2[count7]
        x1=range_names_filter(3,6,letter2)
        list3.append(x1)
        count7+=1
        pass
    print("list format filter base words max and min length in each line:/n")
    print(list3)
    y99=str(list3)
    #convrt to main txt"list of words in each lines apenned list item:",list2
    listt1=[]
    for it in list2:
        sentence1=" ".join(it)
        listt1.append(sentence1)
    print(listt1)
    #convrt main text"list format filter base words max and min length in each line:",list3
    listt2=[]
    for it in list3:
        sentence1=" ".join(it)
        listt2.append(sentence1)
    print(listt2)
    #pair words
    def frequnc2 (pressyour_input_file):
        file2 = open(pressyour_input_file, "r")
        line=file2.read()
        def freq(input_string):
            freq = {}
            words = input_string.split()
            if len(words) == 1:
                return freq
            for idx, word in enumerate(words):
                if idx+1 < len(words):
                    word_pair = (word, words[idx+1])
                    if word_pair in freq:
                        freq[word_pair] += 1
                    else:
                        freq[word_pair] = 1
            return freq
        pair=freq(line)
        file2.close()
        return pair
    bro=frequnc2(pressyour_input_file).copy()        
    print('list of charecter in each line pair words:/n') 
    print(bro)
    def longest_words1(pressyour_input_file):
        filedata=open(pressyour_input_file,'r')
        wordsList = filedata.read().split()
        longestWordLength = len(max(wordsList, key=len))
        result = [textword for textword in wordsList if len(textword) == longestWordLength]
        return result
    dic4=longest_words1(pressyour_input_file)
    print("The following are the longest words from a text file:/n")
    print(dic4)
    yy1=str(dic4)
    def my_func(n):
        return len(n)
    x=map(my_func,lines)
    cb=list(x)
    print('list of number of charecter in each line:',cb)
    print("total characters in words txt:",sum(cb))
    weo=sum(cb)
    avrage1=sum(cb)/len(cb)
    print("avrage number of character in words:",avrage1)
    # ignor words 
    def ignor_words(pressyour_ignore_file,list2):
        file2=open(pressyour_ignore_file,'r')
        lines2=file2.readlines()
        num1=0
        list66=[]
        while num1<len(lines2):
            letter6=lines2[num1]
            words6=letter6.split()
            list66.append(words6)
            num1+=1
            pass
        print(" seperate ignor words in file ignor fornat list  each line",list66)
        num2=0
        list88=[]
        while num2<len(list66):
            letter7=list66[num2]
            num3=0
            while num3<len(letter7):
                letter8=letter7[num3]
                list88.append(letter8)
                num3+=1
                pass
            num2+=1
            pass
        print(" seperate ignor words in file ignor format list ",list88)
        #filter base list2 by ignor words
        list22=[]
        num4=0
        while num4<len(list2):
            letter9=list2[num4]
            for x in letter9:
                if x  not in list88:
                    list22.append(x)
            num4+=1
            pass
        file2.close()
        return f'{list22}'
    try:
        list2_new_ignored=ignor_words(pressyour_ignore_file,list2)
        print("list filtr words ignord in main txt by ignor word")
        print(list2_new_ignored)
        yy2=str(list2_new_ignored)
    except FileNotFoundError:
        print("the file ignored input does not exist")


import json
list99={"total number of lines:":tot_line, " number of blank lines:":blanklines ," number of sentences:":sentences ,'total number of words in te text:/n':d_f,"The following are the longest words from a text file:/n":dic4,"total characters in words txt:":weo,"avrage number of character in words:":avrage1,"the number for each consective words count:/n":dic2,"list format filter base words max and min length in each line:":list3,'list of charecter in each line pair words:/n':bro,"list filtr words ignord in main txt by ignor word":list2_new_ignored}

# Write file
try:
    file3=open(pressyour_output_file,"w")
    file3.close()
except FileNotFoundError:
    print("the file does not exist.")
    import sys
    sys.exit(0)

json_object1 = json.dumps(list99, indent=4)

with open(pressyour_output_file, "w") as outfile:
	outfile.write(json_object1)
    

commands_enter_input_file=input("pless enter your command")

