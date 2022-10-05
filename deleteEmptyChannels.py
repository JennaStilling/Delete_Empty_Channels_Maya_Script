#deleteEmptyChannels.py
#script to delete any channels in rigs that are flat in the graph editor

import maya.cmds as cmds

#hardcoding attributes
attributeList = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scaleX", "scaleY", "scaleZ"]

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

    #getting starting values for attributes
    startXTrans = cmds.getAttr(channelName + ".translateX")
    startYTrans = cmds.getAttr(channelName + ".translateY")
    startZTrans = cmds.getAttr(channelName + ".translateZ")
    startXRot = cmds.getAttr(channelName + ".rotateX")
    startYRot = cmds.getAttr(channelName + ".rotateY")
    startZRot = cmds.getAttr(channelName + ".rotateZ")
    startXScale = cmds.getAttr(channelName + ".scaleX")
    startYScale = cmds.getAttr(channelName + ".scaleY")
    startZScale = cmds.getAttr(channelName + ".scaleZ")

    #setting attribute counters to 0
    xTransCounter = 0
    yTransCounter = 0
    zTransCounter = 0
    xRotCounter = 0
    yRotCounter = 0
    zRotCounter = 0
    xScaleCounter = 0
    yScaleCounter = 0
    zScaleCounter = 0

    #looping through all keyframes in animation
    for i in range (int(keyframeRange)):
        cmds.currentTime(i) #setting current keyframe to loop iteration number
        for j in range (len (attributeList)):
            attributeString = attributeList[j] #setting the attribute to 

            #getting attribute value
            value = cmds.getAttr(channelName + "." + attributeString)
            #print(channelName + " " + attributeString + " equals " + str(value))
            
            #translate attributes: if any of the values of the attribute equals its starting value, increase the counter
            #if counter equals the max keyframes, then channel is flat in graph editor and deleted
            if attributeString == "translateX":
                if value == startXTrans:
                    xTransCounter += 1
                if xTransCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "translateY":
                if value == startYTrans:
                    yTransCounter += 1
                if yTransCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "translateZ":
                if value == startZTrans:
                    zTransCounter += 1
                    if zTransCounter == int(keyframeRange):
                        cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

            #rotate attributes: if any of the values of the attribute equals its starting value, increase the counter
            #if counter equals the max keyframes, then channel is flat in graph editor and deleted
            if attributeString == "rotateX":
                if value == startXRot:
                    xRotCounter += 1
                if xRotCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "rotateY":
                if value == startYRot:
                    yRotCounter += 1
                if yRotCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "rotateZ":
                if value == startZRot:
                    zRotCounter += 1
                if zRotCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

            #scale attributes: if any of the values of the attribute equals its starting value, increase the counter
            #if counter equals the max keyframes, then channel is flat in graph editor and deleted
            if attributeString == "scaleX":
                if value == startXScale:
                    xScaleCounter += 1
                if xScaleCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "scaleY":
                if value == startYScale:
                    yScaleCounter += 1
                if yScaleCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
            if attributeString == "scaleZ":
                if value == startZScale:
                    zScaleCounter += 1
                if zScaleCounter == int(keyframeRange):
                    cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

#if user selected more than one channel
elif len (channelList) >= 2:
    print("Please only select one channel") #error message until multiple channel looping is debugged
    # for l in range (len(channelList)):
    #     channelName = channelList[l]
    #     print(channelName)
    #     startXTrans = cmds.getAttr(channelName + ".translateX")
    #     startYTrans = cmds.getAttr(channelName + ".translateY")
    #     startZTrans = cmds.getAttr(channelName + ".translateZ")
    #     startXRot = cmds.getAttr(channelName + ".rotateX")
    #     startYRot = cmds.getAttr(channelName + ".rotateY")
    #     startZRot = cmds.getAttr(channelName + ".rotateZ")
    #     startXScale = cmds.getAttr(channelName + ".scaleX")
    #     startYScale = cmds.getAttr(channelName + ".scaleY")
    #     startZScale = cmds.getAttr(channelName + ".scaleZ")

    #     xTransCounter = 0
    #     yTransCounter = 0
    #     zTransCounter = 0
    #     xRotCounter = 0
    #     yRotCounter = 0
    #     zRotCounter = 0
    #     xScaleCounter = 0
    #     yScaleCounter = 0
    #     zScaleCounter = 0

    #     zeroCounter = 0
    #     for i in range (int(keyframeRange)):
    #         cmds.currentTime(i)
    #         for j in range (len (attributeList)):
    #             attributeString = attributeList[j]
    #             value = cmds.getAttr(channelName + "." + attributeString)
    #             #print(channelName + " " + attributeString + " equals " + str(value))
    #             if attributeString == "translateX":
    #                 if value == startXTrans:
    #                     xTransCounter += 1
    #                 if xTransCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "translateY":
    #                 if value == startYTrans:
    #                     yTransCounter += 1
    #                 if yTransCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "translateZ":
    #                 if value == startZTrans:
    #                     zTransCounter += 1
    #                     if zTransCounter == int(keyframeRange):
    #                         cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

    #             if attributeString == "rotateX":
    #                 if value == startXRot:
    #                     xRotCounter += 1
    #                 if xRotCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "rotateY":
    #                 if value == startYRot:
    #                     yRotCounter += 1
    #                 if yRotCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "rotateZ":
    #                 if value == startZRot:
    #                     zRotCounter += 1
    #                 if zRotCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

    #             if attributeString == "scaleX":
    #                 if value == startXScale:
    #                     xScaleCounter += 1
    #                 if xScaleCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "scaleY":
    #                 if value == startYScale:
    #                     yScaleCounter += 1
    #                 if yScaleCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)
    #             if attributeString == "scaleZ":
    #                 if value == startZScale:
    #                     zScaleCounter += 1
    #                 if zScaleCounter == int(keyframeRange):
    #                     cmds.cutKey(channelList, time = (startTime, endTime), attribute = attributeString)

#if user did not select any channels
else:
    print("Must select at least one object")