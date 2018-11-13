#Copyright © 2018 JustAidanP. All rights reserved.
import time, sys, os
class Debug:
    #------Variables------
    programName = ""
    #Defines the location of the log files
    logFileDirectory = sys.path[0]
    #Defines the Log File
    logFile = None

    #------Methods/Functions------
    #Creates a new log file
    def createLogFile():
        Debug.logFileDirectory += "/LogFiles_" + Debug.programName
        #Ensures that there is a programName
        if Debug.programName == "": print("------There is no Program Name------"); return
        #Creates a new log file directory if one doesn't yet exist
        if os.path.exists(Debug.logFileDirectory) == False: os.mkdir(Debug.logFileDirectory)
        #Keeps creating names until a file with the name doesn't exist
        while True:
            logFileTime = time.time()
            #Creates a name for the log file
            logFileName = "LogAt_" + str(logFileTime) + ".txt"
            #Checks if the logFile already exists
            if os.path.exists(Debug.logFileDirectory + "/" + logFileName) == False: break
        #Creates a new logFile with the name
        Debug.logFile = open(Debug.logFileDirectory + "/" + logFileName, "w")
        #Writes the timeStamp to the file
        Debug.logFile.write("------Log File Created At Unicode %s------\n"%logFileTime)
    #Prints out a message given by an area of a code
    #Takes a message, lcoation and name as Strings
    def Log(msg, loc, name):
        #Creates the message
        message = "LOG/%s/%s - %s\n"%(loc, name, msg)
        #Creates a new log file if one doesn't exist
        if Debug.logFile == None: Debug.createLogFile()
        #Prints and adds the Log to the logFIle
        Debug.logFile.write("------\nLog At: %s\n"%(time.time()) + message)
        print(message, end="")
    #Times a Method
    #Takes in a reference to a method and takes in the required parameters
    def timeMethod(targetMethod, *args):
        #Ends the function if the targetFunction is None
        if targetMethod == None: return
        #Notes the time before the function is ran
        startTime = time.time()
        #Runs the method with the given args
        targetMethod(*args)
        #Notes the time after the function is ran
        endTime = time.time()
        #Logs the time difference
        Debug.Log(msg=("Method Time: %ss"%(endTime - startTime)), loc="", name="DEBUG")
    #Times a function
    #Takes in a reference to a function and the required parameters and returns the output
    def timeFunction(targetFunction, *args):
        #Ends the function if the targetFunction is None
        if targetFunction == None: return
        #Notes the time before the function is ran
        startTime = time.time()
        #Runs the function and stores the results
        results = targetFunction(*args)
        #Notes the time after the function is ran
        endTime = time.time()
        #Logs the time difference
        Debug.Log(msg=("Function Time: %ss"%(endTime - startTime)), loc="", name="DEBUG")
        #Reutnrs the results
        return results
    #Tests a function with inputs and outputs
    #Takes in a reference to a function, the required parameters as a list and target output
    #Returns an evaluation
    def unitTest(targetFunction, args, targetOutput):
        #Ends the function if any parameters are None
        if targetFunction == None: return
        if args == None: return
        if targetOutput == None: return
        #Tests the function with the args
        result = targetFunction(*args)
        if result == targetOutput: Debug.Log(msg="Test of '%s' with args %s Successful with result: %s"%(targetFunction.__name__, args, result), loc="Debug/unitTest", name="DEBUG")
        if result != targetOutput: Debug.Log(msg="Test of '%s' with args %s Unsuccessful with result: %s"%(targetFunction.__name__, args, result), loc="Debug/unitTest", name="DEBUG")
