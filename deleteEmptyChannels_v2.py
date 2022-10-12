#deleteEmptyChannels.py
#script to delete any channels in rigs that are flat in the graph editor

import maya.cmds as cmds

#list of channels selected
channelList = cmds.ls(orderedSelection = True)
#print(channelList)

#getting start time of animation, end time of animation, and the range
startTime = cmds.playbackOptions(query = True, minTime = True)
endTime = cmds.playbackOptions(query = True, maxTime = True)
keyframeRange = endTime - startTime + 1

#set current keyframe to start of animation
cmds.currentTime(startTime)

#if user only selected one channel
if len (channelList) == 1:
    channelName = channelList[0] #getting the channel name to a string
    #print(channelName)

    attributeList = cmds.listAttr(channelName, keyable = True) #keyable attributes of the channel
    attributeValueList = [] #holds corresponding attribute list values
    attributeListLength = (len(attributeList))
    attributeCounterList = []
    print(attributeListLength)

    #filling attribute value list and attribute counter list
    for i in range (len(attributeList)):
        attributeValueList.append(cmds.getAttr(channelName + "." + attributeList[i]))
        attributeCounterList.append(0)

    #looping through all keyframes in animation
    for i in range (int(keyframeRange)):
        cmds.currentTime(i) #setting current keyframe to loop iteration number
        for j in range (len (attributeList)):
            attributeString = attributeList[j] #setting the attribute to 

            #getting attribute value
            value = attributeValueList[j]

    for i in range (attributeListLength):
        attributeString = attributeList[i]
        print(attributeString)
        print("Original starting position: " + str(attributeValueList[i]))
        for j in range (int(keyframeRange)):
            cmds.currentTime(j)
            value = cmds.getAttr(channelName + "." + attributeString)
            if value == attributeValueList[i]:
                attributeCounterList[i] += 1
            if attributeCounterList[i] == int(keyframeRange):
                cmds.cutKey(channelName, time = (startTime, endTime), attribute = attributeString)
                print("Deleted: " + attributeString)

#if user selected more than one channel
elif len (channelList) >= 2:
    for l in range (len(channelList)):
        channelName = channelList[l] #getting the channel name to a string

        attributeList = cmds.listAttr(channelName, keyable = True) #keyable attributes of the channel
        attributeValueList = [] #holds corresponding attribute list values
        attributeListLength = (len(attributeList))
        attributeCounterList = []
        print(attributeListLength)

        #filling attribute value list and attribute counter list
        for i in range (len(attributeList)):
            attributeValueList.append(cmds.getAttr(channelName + "." + attributeList[i]))
            attributeCounterList.append(0)

        #looping through all keyframes in animation
        for i in range (int(keyframeRange)):
            cmds.currentTime(i) #setting current keyframe to loop iteration number
            for j in range (len (attributeList)):
                attributeString = attributeList[j] #setting attribute name to corresponding location in list

                #getting attribute value
                value = attributeValueList[j]

        for i in range (attributeListLength):
            attributeString = attributeList[i]
            print(attributeString)
            print("Original starting position: " + str(attributeValueList[i]))
            for j in range (int(keyframeRange)):
                cmds.currentTime(j)
                value = cmds.getAttr(channelName + "." + attributeString)
                if value == attributeValueList[i]:
                    attributeCounterList[i] += 1
                if attributeCounterList[i] == int(keyframeRange):
                    cmds.cutKey(channelName, time = (startTime, endTime), attribute = attributeString)
                    print("Deleted: " + attributeString)

#if user did not select any channels
else:
    print("Must select at least one object")