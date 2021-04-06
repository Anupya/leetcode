# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        string = ' '.join(words)
        
        start = 0
        stop = maxWidth
        curLine = 0
        justifications = []
    
        while start + maxWidth < len(string):
            substring = string[start:stop]

            if string[stop] == " ": # perfect fit
                justifications.append(substring)
                start = stop+1
                
            else: # middle of a word
                findLastSpaceIndex = substring.rfind(" ")                
                substring = string[start:start+findLastSpaceIndex]
                
                # add spaces
                numSlots = substring.count(' ')
                spacesToAdd = maxWidth-len(substring)
                if numSlots == 0: # if need to add spaces at the end
                    numSlots = 1
                
                # create spaceString
                spaceString = ""
                if spacesToAdd < numSlots:
                    spacesInEachSlot = 1
                    spaceString = " "
                    remainderSpaceString = " "
                else:
                    spacesInEachSlot = int(spacesToAdd/numSlots)
                
                    for x in range(0, spacesInEachSlot):
                        spaceString += " "

                    remainderSpaces = spacesToAdd%numSlots
                    remainderSpaceString = spaceString
                    for x in range(0, remainderSpaces):
                        remainderSpaceString += " "
                    
                # iterate through substring and add spaces where necessary
                newsubstring = ""
                firstWord = True
                if not " " in substring:
                    newsubstring = substring + spaceString
                else:
                    spacesLessThanSlots = spacesToAdd
                    for x in substring:
                        if x == " " and spacesLessThanSlots:
                            spacesLessThanSlots -=1
                            if firstWord:
                                newsubstring += remainderSpaceString
                                firstWord = False
                            else:
                                newsubstring += spaceString
                        newsubstring+=x
                        
                        
                
                justifications.append(newsubstring)
                start += findLastSpaceIndex + 1
            
            stop = start + maxWidth
            curLine+=1
        
        numSpacesToAdd = maxWidth - len(string[start:])
        lastSubstring = string[start:]
        for x in range(0,numSpacesToAdd):
            lastSubstring+= " "
        justifications.append(lastSubstring)
        
        return justifications
                
                
            
            
        
        