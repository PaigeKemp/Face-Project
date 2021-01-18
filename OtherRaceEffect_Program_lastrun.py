#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Sun Jan 17 21:16:31 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'FaceExperiment'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/paigekemp/Desktop/UNCG/UNCG Research/Current Experiments/OtherRaceEffect/OtherRaceEffect_Program_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
thisExp=psychoJS.experiment;
win=psychoJS.window;
event=psychoJS.eventManager;
Array.prototype.append = [].push;
kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true}); 


function random_character() {
    var chars = "ABC";
    return chars.substr( Math.floor(Math.random() * 3), 1);
}
condition = random_character();

Welcome_Text = visual.TextStim(win=win, name='Welcome_Text',
    text='Welcome to the experiment!',
    font='Arial',
    units='cm', pos=(0, 4), height=1.5, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Task_Instructions"
Task_InstructionsClock = core.Clock()
Task_Instructions_Text = visual.TextStim(win=win, name='Task_Instructions_Text',
    text='In this experiment, you will see a fixation cross followed by a series of face pairings. The pairs of faces will be presented sequentially, with each face being separated by a mask. Your task will be to study the first face of each pair and then you will be asked to indicate if the second face is the same (old) or different (new). Responses will be made using the keyboard and the instructions on the screen will specify which keys correspond to which response.\n\n\nPress the SPACE BAR to see an example.\n\n',
    font='Arial',
    units='cm', pos=(0, 3), height=1, wrapWidth=35, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Task_Instructions_Response = keyboard.Keyboard()

# Initialize components for Routine "Example_Slide"
Example_SlideClock = core.Clock()
Example_Image = visual.ImageStim(
    win=win,
    name='Example_Image', 
    image='Example.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.6, .9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Example_Image_Response = keyboard.Keyboard()

# Initialize components for Routine "B1_Study"
B1_StudyClock = core.Clock()
B1_Fixed_Cross = visual.ImageStim(
    win=win,
    name='B1_Fixed_Cross', 
    image='Fixed_Cross.jpg', mask=None,
    ori=0, pos=(0, .2), size=(.05, .05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
B1_Study_Image = visual.ImageStim(
    win=win,
    name='B1_Study_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.60, 0.60),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
B1_Mask_Image = visual.ImageStim(
    win=win,
    name='B1_Mask_Image', 
    image='noise.jpg', mask=None,
    ori=0, pos=(0, 0.1), size=(0.62, 0.62),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
B1_Test_Image = visual.ImageStim(
    win=win,
    name='B1_Test_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, .1), size=(0.55, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
B1_Test_Prompt = visual.TextStim(win=win, name='B1_Test_Prompt',
    text='Old (1)                       New (0)',
    font='Arial',
    units='cm', pos=(0, -8), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
B1_Test_Response = keyboard.Keyboard()

# Initialize components for Routine "B1_End"
B1_EndClock = core.Clock()
B1_End_Text = visual.TextStim(win=win, name='B1_End_Text',
    text='Congratulations, you have completed half the experiment. You will have 2 minutes to take a break and stretch before completing the remainder of the experiment. \n\nAfter 2 minutes, a screen will appear, and you will be asked to press the SPACE BAR to continue. ',
    font='Arial',
    units='cm', pos=(-1, 5.7), height=1, wrapWidth=33, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
B1_End_Text_2 = visual.TextStim(win=win, name='B1_End_Text_2',
    text='Your 2 minute break period is finished.\n\nPress the SPACE BAR to continue.',
    font='Arial',
    units='cm', pos=(0, 3), height=1, wrapWidth=35, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
B1_End_Response = keyboard.Keyboard()

# Initialize components for Routine "B2_Start"
B2_StartClock = core.Clock()
B2_Start_Text = visual.TextStim(win=win, name='B2_Start_Text',
    text='As a reminder, you will be presented with a series of face pairings and your task will be to study the first face of each pair and then you will be asked to indicate if the second face is the same (old) or different (new). Responses will be made using the keyboard and the instructions on the screen will specify which keys correspond to which response. \n\n\nPress the SPACE BAR to continue.\n\n',
    font='Arial',
    units='cm', pos=(0, 4.5), height=1, wrapWidth=35, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
B2_Start_Response = keyboard.Keyboard()

# Initialize components for Routine "B2_Study"
B2_StudyClock = core.Clock()
B2_Fixed_Cross = visual.ImageStim(
    win=win,
    name='B2_Fixed_Cross', 
    image='Fixed_Cross.jpg', mask=None,
    ori=0, pos=(0, .2), size=(.05, .05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
B2_Study_Image = visual.ImageStim(
    win=win,
    name='B2_Study_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.60, 0.60),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
B2_Mask_Image = visual.ImageStim(
    win=win,
    name='B2_Mask_Image', 
    image='noise.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.75, 1.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
B2_Test_Image = visual.ImageStim(
    win=win,
    name='B2_Test_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, .1), size=(0.60, 0.60),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
B2_Test_Prompt = visual.TextStim(win=win, name='B2_Test_Prompt',
    text='Old (1)                       New (0)',
    font='Arial',
    units='cm', pos=(0, -8), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
B2_Test_Response = keyboard.Keyboard()

# Initialize components for Routine "Demo_Instructions"
Demo_InstructionsClock = core.Clock()
Demo_Instructions_Text = visual.TextStim(win=win, name='Demo_Instructions_Text',
    text='You have now completed the main task. All that remains is a few questions about you. \n\nPress SPACE BAR to continue.',
    font='Arial',
    units='cm', pos=(-1, 6.5), height=1, wrapWidth=33, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Demo_Instructions_Response = keyboard.Keyboard()

# Initialize components for Routine "Age"
AgeClock = core.Clock()
Age_Question = visual.TextStim(win=win, name='Age_Question',
    text='How old are you (in years)?\nPlease type two digits and then press next',
    font='Arial',
    units='cm', pos=(10, 8.5), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Age_Response = visual.TextBox2(
     win, text='\n ', font='Arial',
     pos=(-3, 6),units='cm',     letterHeight=1,
     size=None, borderWidth=2.0,
     color='White', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='Age_Response',
     autoLog=True,
)
ContinueButton = visual.TextStim(win=win, name='ContinueButton',
    text='Next >>',
    font='Arial',
    units='cm', pos=(17, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "Gender"
GenderClock = core.Clock()
Gender_Question = visual.TextStim(win=win, name='Gender_Question',
    text='What is your gender?\nPlease press the number on your keyboard with the response option that that best corresponds to you.\n\n(1) Woman\n\n(2) Man\n\n(3) Non-binary\n\n(4) Prefer not to say',
    font='Arial',
    units='cm', pos=(2.5,3.4), height=1, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Gender1 = keyboard.Keyboard()

# Initialize components for Routine "Ethnicity"
EthnicityClock = core.Clock()
Ethnicity_Question_1 = visual.TextStim(win=win, name='Ethnicity_Question_1',
    text='What is your ethnicity?\nPlease press the number on your keyboard with the response option that that best corresponds to you.\n\n(1) Hispanic or Latino\n\n(2) Not Hispanic or Latino',
    font='Arial',
    units='cm', pos=(2.5, 5.7), height=1, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ethnicity1 = keyboard.Keyboard()

# Initialize components for Routine "Race"
RaceClock = core.Clock()
Race_Question_1 = visual.TextStim(win=win, name='Race_Question_1',
    text='What is your race?\nPlease press the number on your keyboard with the response option that that best corresponds to you.\n\n(1) American Indian/Alaska Native\n\n(2) Asian\n\n(3) Native Hawaiian or Other Pacific Islander\n\n(4) Black or African American\n\n(5) White\n\n(6) More than one\n\n(7) Unknown',
    font='Arial',
    units='cm', pos=(2.5,0), height=1, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Race1 = keyboard.Keyboard()

# Initialize components for Routine "Education_Years"
Education_YearsClock = core.Clock()
Education_Years_Question = visual.TextStim(win=win, name='Education_Years_Question',
    text='How many years of education have you completed?\nPlease press the number on your keyboard with the response option that that best corresponds to you.\n\n(1) 12 - High School\n\n(2) 13\n\n(3) 14\n\n(4) 15\n\n(5) 16 - College',
    font='Arial',
    units='cm', pos=(2.5,2.3), height=1, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Education_Years1 = keyboard.Keyboard()

# Initialize components for Routine "Thank_You"
Thank_YouClock = core.Clock()
Thank_You_Text = visual.TextStim(win=win, name='Thank_You_Text',
    text='You have completed the experiment. Thank you for participating!',
    font='Arial',
    units='cm', pos=(0, 0), height=1.5, wrapWidth=15, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Cond_Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Cond_Loop')
thisExp.addLoop(Cond_Loop)  # add the loop to the experiment
thisCond_Loop = Cond_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCond_Loop.rgb)
if thisCond_Loop != None:
    for paramName in thisCond_Loop:
        exec('{} = thisCond_Loop[paramName]'.format(paramName))

for thisCond_Loop in Cond_Loop:
    currentLoop = Cond_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisCond_Loop.rgb)
    if thisCond_Loop != None:
        for paramName in thisCond_Loop:
            exec('{} = thisCond_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Welcome"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    WelcomeComponents = [Welcome_Text]
    for thisComponent in WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Welcome"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WelcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome_Text* updates
        if Welcome_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome_Text.frameNStart = frameN  # exact frame index
            Welcome_Text.tStart = t  # local t and not account for scr refresh
            Welcome_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome_Text, 'tStartRefresh')  # time at next scr refresh
            Welcome_Text.setAutoDraw(True)
        if Welcome_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Welcome_Text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Welcome_Text.tStop = t  # not accounting for scr refresh
                Welcome_Text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Welcome_Text, 'tStopRefresh')  # time at next scr refresh
                Welcome_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Welcome"-------
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Cond_Loop.addData('Welcome_Text.started', Welcome_Text.tStartRefresh)
    Cond_Loop.addData('Welcome_Text.stopped', Welcome_Text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Cond_Loop'


# set up handler to look after randomisation of conditions etc
Block1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block1')
thisExp.addLoop(Block1)  # add the loop to the experiment
thisBlock1 = Block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in Block1:
    currentLoop = Block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task_Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    Task_Instructions_Text.alignText='left'
    Task_Instructions_Response.keys = []
    Task_Instructions_Response.rt = []
    _Task_Instructions_Response_allKeys = []
    # keep track of which components have finished
    Task_InstructionsComponents = [Task_Instructions_Text, Task_Instructions_Response]
    for thisComponent in Task_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Task_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Task_Instructions"-------
    while continueRoutine:
        # get current time
        t = Task_InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Task_InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_Instructions_Text* updates
        if Task_Instructions_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_Instructions_Text.frameNStart = frameN  # exact frame index
            Task_Instructions_Text.tStart = t  # local t and not account for scr refresh
            Task_Instructions_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_Instructions_Text, 'tStartRefresh')  # time at next scr refresh
            Task_Instructions_Text.setAutoDraw(True)
        
        # *Task_Instructions_Response* updates
        waitOnFlip = False
        if Task_Instructions_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_Instructions_Response.frameNStart = frameN  # exact frame index
            Task_Instructions_Response.tStart = t  # local t and not account for scr refresh
            Task_Instructions_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_Instructions_Response, 'tStartRefresh')  # time at next scr refresh
            Task_Instructions_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Task_Instructions_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Task_Instructions_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Task_Instructions_Response.status == STARTED and not waitOnFlip:
            theseKeys = Task_Instructions_Response.getKeys(keyList=['space'], waitRelease=False)
            _Task_Instructions_Response_allKeys.extend(theseKeys)
            if len(_Task_Instructions_Response_allKeys):
                Task_Instructions_Response.keys = _Task_Instructions_Response_allKeys[0].name  # just the first key pressed
                Task_Instructions_Response.rt = _Task_Instructions_Response_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task_Instructions"-------
    for thisComponent in Task_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('Task_Instructions_Text.started', Task_Instructions_Text.tStartRefresh)
    Block1.addData('Task_Instructions_Text.stopped', Task_Instructions_Text.tStopRefresh)
    # check responses
    if Task_Instructions_Response.keys in ['', [], None]:  # No response was made
        Task_Instructions_Response.keys = None
    Block1.addData('Task_Instructions_Response.keys',Task_Instructions_Response.keys)
    if Task_Instructions_Response.keys != None:  # we had a response
        Block1.addData('Task_Instructions_Response.rt', Task_Instructions_Response.rt)
    Block1.addData('Task_Instructions_Response.started', Task_Instructions_Response.tStartRefresh)
    Block1.addData('Task_Instructions_Response.stopped', Task_Instructions_Response.tStopRefresh)
    # the Routine "Task_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Example_Slide"-------
    continueRoutine = True
    # update component parameters for each repeat
    Example_Image_Response.keys = []
    Example_Image_Response.rt = []
    _Example_Image_Response_allKeys = []
    # keep track of which components have finished
    Example_SlideComponents = [Example_Image, Example_Image_Response]
    for thisComponent in Example_SlideComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Example_SlideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Example_Slide"-------
    while continueRoutine:
        # get current time
        t = Example_SlideClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Example_SlideClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Example_Image* updates
        if Example_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Example_Image.frameNStart = frameN  # exact frame index
            Example_Image.tStart = t  # local t and not account for scr refresh
            Example_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Image, 'tStartRefresh')  # time at next scr refresh
            Example_Image.setAutoDraw(True)
        
        # *Example_Image_Response* updates
        waitOnFlip = False
        if Example_Image_Response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Example_Image_Response.frameNStart = frameN  # exact frame index
            Example_Image_Response.tStart = t  # local t and not account for scr refresh
            Example_Image_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Image_Response, 'tStartRefresh')  # time at next scr refresh
            Example_Image_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Example_Image_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Example_Image_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Example_Image_Response.status == STARTED and not waitOnFlip:
            theseKeys = Example_Image_Response.getKeys(keyList=['space'], waitRelease=False)
            _Example_Image_Response_allKeys.extend(theseKeys)
            if len(_Example_Image_Response_allKeys):
                Example_Image_Response.keys = _Example_Image_Response_allKeys[0].name  # just the first key pressed
                Example_Image_Response.rt = _Example_Image_Response_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Example_SlideComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Example_Slide"-------
    for thisComponent in Example_SlideComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('Example_Image.started', Example_Image.tStartRefresh)
    Block1.addData('Example_Image.stopped', Example_Image.tStopRefresh)
    # check responses
    if Example_Image_Response.keys in ['', [], None]:  # No response was made
        Example_Image_Response.keys = None
    Block1.addData('Example_Image_Response.keys',Example_Image_Response.keys)
    if Example_Image_Response.keys != None:  # we had a response
        Block1.addData('Example_Image_Response.rt', Example_Image_Response.rt)
    Block1.addData('Example_Image_Response.started', Example_Image_Response.tStartRefresh)
    Block1.addData('Example_Image_Response.stopped', Example_Image_Response.tStopRefresh)
    # the Routine "Example_Slide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    B1_Trial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(B1list),
        seed=None, name='B1_Trial')
    thisExp.addLoop(B1_Trial)  # add the loop to the experiment
    thisB1_Trial = B1_Trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisB1_Trial.rgb)
    if thisB1_Trial != None:
        for paramName in thisB1_Trial:
            exec('{} = thisB1_Trial[paramName]'.format(paramName))
    
    for thisB1_Trial in B1_Trial:
        currentLoop = B1_Trial
        # abbreviate parameter names if possible (e.g. rgb = thisB1_Trial.rgb)
        if thisB1_Trial != None:
            for paramName in thisB1_Trial:
                exec('{} = thisB1_Trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "B1_Study"-------
        continueRoutine = True
        # update component parameters for each repeat
        B1_Study_Image.setImage(StudyImage)
        B1_Test_Image.setImage(TestImage)
        B1_Test_Response.keys = []
        B1_Test_Response.rt = []
        _B1_Test_Response_allKeys = []
        # keep track of which components have finished
        B1_StudyComponents = [B1_Fixed_Cross, B1_Study_Image, B1_Mask_Image, B1_Test_Image, B1_Test_Prompt, B1_Test_Response]
        for thisComponent in B1_StudyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        B1_StudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "B1_Study"-------
        while continueRoutine:
            # get current time
            t = B1_StudyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=B1_StudyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *B1_Fixed_Cross* updates
            if B1_Fixed_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B1_Fixed_Cross.frameNStart = frameN  # exact frame index
                B1_Fixed_Cross.tStart = t  # local t and not account for scr refresh
                B1_Fixed_Cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Fixed_Cross, 'tStartRefresh')  # time at next scr refresh
                B1_Fixed_Cross.setAutoDraw(True)
            if B1_Fixed_Cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B1_Fixed_Cross.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    B1_Fixed_Cross.tStop = t  # not accounting for scr refresh
                    B1_Fixed_Cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B1_Fixed_Cross, 'tStopRefresh')  # time at next scr refresh
                    B1_Fixed_Cross.setAutoDraw(False)
            
            # *B1_Study_Image* updates
            if B1_Study_Image.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                B1_Study_Image.frameNStart = frameN  # exact frame index
                B1_Study_Image.tStart = t  # local t and not account for scr refresh
                B1_Study_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Study_Image, 'tStartRefresh')  # time at next scr refresh
                B1_Study_Image.setAutoDraw(True)
            if B1_Study_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B1_Study_Image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    B1_Study_Image.tStop = t  # not accounting for scr refresh
                    B1_Study_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B1_Study_Image, 'tStopRefresh')  # time at next scr refresh
                    B1_Study_Image.setAutoDraw(False)
            
            # *B1_Mask_Image* updates
            if B1_Mask_Image.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                B1_Mask_Image.frameNStart = frameN  # exact frame index
                B1_Mask_Image.tStart = t  # local t and not account for scr refresh
                B1_Mask_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Mask_Image, 'tStartRefresh')  # time at next scr refresh
                B1_Mask_Image.setAutoDraw(True)
            if B1_Mask_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B1_Mask_Image.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    B1_Mask_Image.tStop = t  # not accounting for scr refresh
                    B1_Mask_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B1_Mask_Image, 'tStopRefresh')  # time at next scr refresh
                    B1_Mask_Image.setAutoDraw(False)
            
            # *B1_Test_Image* updates
            if B1_Test_Image.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B1_Test_Image.frameNStart = frameN  # exact frame index
                B1_Test_Image.tStart = t  # local t and not account for scr refresh
                B1_Test_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Test_Image, 'tStartRefresh')  # time at next scr refresh
                B1_Test_Image.setAutoDraw(True)
            
            # *B1_Test_Prompt* updates
            if B1_Test_Prompt.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B1_Test_Prompt.frameNStart = frameN  # exact frame index
                B1_Test_Prompt.tStart = t  # local t and not account for scr refresh
                B1_Test_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Test_Prompt, 'tStartRefresh')  # time at next scr refresh
                B1_Test_Prompt.setAutoDraw(True)
            
            # *B1_Test_Response* updates
            waitOnFlip = False
            if B1_Test_Response.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B1_Test_Response.frameNStart = frameN  # exact frame index
                B1_Test_Response.tStart = t  # local t and not account for scr refresh
                B1_Test_Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B1_Test_Response, 'tStartRefresh')  # time at next scr refresh
                B1_Test_Response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(B1_Test_Response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(B1_Test_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if B1_Test_Response.status == STARTED and not waitOnFlip:
                theseKeys = B1_Test_Response.getKeys(keyList=['1', '0'], waitRelease=False)
                _B1_Test_Response_allKeys.extend(theseKeys)
                if len(_B1_Test_Response_allKeys):
                    B1_Test_Response.keys = _B1_Test_Response_allKeys[0].name  # just the first key pressed
                    B1_Test_Response.rt = _B1_Test_Response_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in B1_StudyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "B1_Study"-------
        for thisComponent in B1_StudyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        B1_Trial.addData('B1_Fixed_Cross.started', B1_Fixed_Cross.tStartRefresh)
        B1_Trial.addData('B1_Fixed_Cross.stopped', B1_Fixed_Cross.tStopRefresh)
        B1_Trial.addData('B1_Study_Image.started', B1_Study_Image.tStartRefresh)
        B1_Trial.addData('B1_Study_Image.stopped', B1_Study_Image.tStopRefresh)
        B1_Trial.addData('B1_Mask_Image.started', B1_Mask_Image.tStartRefresh)
        B1_Trial.addData('B1_Mask_Image.stopped', B1_Mask_Image.tStopRefresh)
        B1_Trial.addData('B1_Test_Image.started', B1_Test_Image.tStartRefresh)
        B1_Trial.addData('B1_Test_Image.stopped', B1_Test_Image.tStopRefresh)
        B1_Trial.addData('B1_Test_Prompt.started', B1_Test_Prompt.tStartRefresh)
        B1_Trial.addData('B1_Test_Prompt.stopped', B1_Test_Prompt.tStopRefresh)
        # check responses
        if B1_Test_Response.keys in ['', [], None]:  # No response was made
            B1_Test_Response.keys = None
        B1_Trial.addData('B1_Test_Response.keys',B1_Test_Response.keys)
        if B1_Test_Response.keys != None:  # we had a response
            B1_Trial.addData('B1_Test_Response.rt', B1_Test_Response.rt)
        B1_Trial.addData('B1_Test_Response.started', B1_Test_Response.tStartRefresh)
        B1_Trial.addData('B1_Test_Response.stopped', B1_Test_Response.tStopRefresh)
        # the Routine "B1_Study" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'B1_Trial'
    
    
    # ------Prepare to start Routine "B1_End"-------
    continueRoutine = True
    # update component parameters for each repeat
    B1_End_Text.alignText='left'
    B1_End_Response.keys = []
    B1_End_Response.rt = []
    _B1_End_Response_allKeys = []
    # keep track of which components have finished
    B1_EndComponents = [B1_End_Text, B1_End_Text_2, B1_End_Response]
    for thisComponent in B1_EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    B1_EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "B1_End"-------
    while continueRoutine:
        # get current time
        t = B1_EndClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=B1_EndClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B1_End_Text* updates
        if B1_End_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B1_End_Text.frameNStart = frameN  # exact frame index
            B1_End_Text.tStart = t  # local t and not account for scr refresh
            B1_End_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1_End_Text, 'tStartRefresh')  # time at next scr refresh
            B1_End_Text.setAutoDraw(True)
        if B1_End_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B1_End_Text.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                B1_End_Text.tStop = t  # not accounting for scr refresh
                B1_End_Text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B1_End_Text, 'tStopRefresh')  # time at next scr refresh
                B1_End_Text.setAutoDraw(False)
        
        # *B1_End_Text_2* updates
        if B1_End_Text_2.status == NOT_STARTED and tThisFlip >= 120-frameTolerance:
            # keep track of start time/frame for later
            B1_End_Text_2.frameNStart = frameN  # exact frame index
            B1_End_Text_2.tStart = t  # local t and not account for scr refresh
            B1_End_Text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1_End_Text_2, 'tStartRefresh')  # time at next scr refresh
            B1_End_Text_2.setAutoDraw(True)
        
        # *B1_End_Response* updates
        waitOnFlip = False
        if B1_End_Response.status == NOT_STARTED and tThisFlip >= 120-frameTolerance:
            # keep track of start time/frame for later
            B1_End_Response.frameNStart = frameN  # exact frame index
            B1_End_Response.tStart = t  # local t and not account for scr refresh
            B1_End_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1_End_Response, 'tStartRefresh')  # time at next scr refresh
            B1_End_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(B1_End_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(B1_End_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if B1_End_Response.status == STARTED and not waitOnFlip:
            theseKeys = B1_End_Response.getKeys(keyList=['space'], waitRelease=False)
            _B1_End_Response_allKeys.extend(theseKeys)
            if len(_B1_End_Response_allKeys):
                B1_End_Response.keys = _B1_End_Response_allKeys[0].name  # just the first key pressed
                B1_End_Response.rt = _B1_End_Response_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B1_EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B1_End"-------
    for thisComponent in B1_EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1.addData('B1_End_Text.started', B1_End_Text.tStartRefresh)
    Block1.addData('B1_End_Text.stopped', B1_End_Text.tStopRefresh)
    Block1.addData('B1_End_Text_2.started', B1_End_Text_2.tStartRefresh)
    Block1.addData('B1_End_Text_2.stopped', B1_End_Text_2.tStopRefresh)
    # check responses
    if B1_End_Response.keys in ['', [], None]:  # No response was made
        B1_End_Response.keys = None
    Block1.addData('B1_End_Response.keys',B1_End_Response.keys)
    if B1_End_Response.keys != None:  # we had a response
        Block1.addData('B1_End_Response.rt', B1_End_Response.rt)
    Block1.addData('B1_End_Response.started', B1_End_Response.tStartRefresh)
    Block1.addData('B1_End_Response.stopped', B1_End_Response.tStopRefresh)
    # the Routine "B1_End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block1'


# set up handler to look after randomisation of conditions etc
Block2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block2')
thisExp.addLoop(Block2)  # add the loop to the experiment
thisBlock2 = Block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
if thisBlock2 != None:
    for paramName in thisBlock2:
        exec('{} = thisBlock2[paramName]'.format(paramName))

for thisBlock2 in Block2:
    currentLoop = Block2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2:
            exec('{} = thisBlock2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "B2_Start"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Block2.thisN==0:
    #now I'm setting the specific list. See below
    
    ## importing the excel files for each format associated with block 2
      if format==1:
        B2list="B2_F1.xlsx"
      elif format==2:
        B2list="B2_F2.xlsx"
      elif format==3:
        B2list="B2_F3.xlsx"
    
    Word="Dummy word"
    
    B2_Start_Text.alignText='left'
    B2_Start_Response.keys = []
    B2_Start_Response.rt = []
    _B2_Start_Response_allKeys = []
    # keep track of which components have finished
    B2_StartComponents = [B2_Start_Text, B2_Start_Response]
    for thisComponent in B2_StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    B2_StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "B2_Start"-------
    while continueRoutine:
        # get current time
        t = B2_StartClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=B2_StartClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B2_Start_Text* updates
        if B2_Start_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B2_Start_Text.frameNStart = frameN  # exact frame index
            B2_Start_Text.tStart = t  # local t and not account for scr refresh
            B2_Start_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B2_Start_Text, 'tStartRefresh')  # time at next scr refresh
            B2_Start_Text.setAutoDraw(True)
        
        # *B2_Start_Response* updates
        waitOnFlip = False
        if B2_Start_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B2_Start_Response.frameNStart = frameN  # exact frame index
            B2_Start_Response.tStart = t  # local t and not account for scr refresh
            B2_Start_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B2_Start_Response, 'tStartRefresh')  # time at next scr refresh
            B2_Start_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(B2_Start_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(B2_Start_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if B2_Start_Response.status == STARTED and not waitOnFlip:
            theseKeys = B2_Start_Response.getKeys(keyList=['space'], waitRelease=False)
            _B2_Start_Response_allKeys.extend(theseKeys)
            if len(_B2_Start_Response_allKeys):
                B2_Start_Response.keys = _B2_Start_Response_allKeys[0].name  # just the first key pressed
                B2_Start_Response.rt = _B2_Start_Response_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B2_StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B2_Start"-------
    for thisComponent in B2_StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block2.addData('B2_Start_Text.started', B2_Start_Text.tStartRefresh)
    Block2.addData('B2_Start_Text.stopped', B2_Start_Text.tStopRefresh)
    # check responses
    if B2_Start_Response.keys in ['', [], None]:  # No response was made
        B2_Start_Response.keys = None
    Block2.addData('B2_Start_Response.keys',B2_Start_Response.keys)
    if B2_Start_Response.keys != None:  # we had a response
        Block2.addData('B2_Start_Response.rt', B2_Start_Response.rt)
    Block2.addData('B2_Start_Response.started', B2_Start_Response.tStartRefresh)
    Block2.addData('B2_Start_Response.stopped', B2_Start_Response.tStopRefresh)
    # the Routine "B2_Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    B2_Trial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(B2list),
        seed=None, name='B2_Trial')
    thisExp.addLoop(B2_Trial)  # add the loop to the experiment
    thisB2_Trial = B2_Trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisB2_Trial.rgb)
    if thisB2_Trial != None:
        for paramName in thisB2_Trial:
            exec('{} = thisB2_Trial[paramName]'.format(paramName))
    
    for thisB2_Trial in B2_Trial:
        currentLoop = B2_Trial
        # abbreviate parameter names if possible (e.g. rgb = thisB2_Trial.rgb)
        if thisB2_Trial != None:
            for paramName in thisB2_Trial:
                exec('{} = thisB2_Trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "B2_Study"-------
        continueRoutine = True
        # update component parameters for each repeat
        B2_Study_Image.setImage(StudyImage)
        B2_Test_Image.setImage(TestImage)
        B2_Test_Response.keys = []
        B2_Test_Response.rt = []
        _B2_Test_Response_allKeys = []
        # keep track of which components have finished
        B2_StudyComponents = [B2_Fixed_Cross, B2_Study_Image, B2_Mask_Image, B2_Test_Image, B2_Test_Prompt, B2_Test_Response]
        for thisComponent in B2_StudyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        B2_StudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "B2_Study"-------
        while continueRoutine:
            # get current time
            t = B2_StudyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=B2_StudyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *B2_Fixed_Cross* updates
            if B2_Fixed_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B2_Fixed_Cross.frameNStart = frameN  # exact frame index
                B2_Fixed_Cross.tStart = t  # local t and not account for scr refresh
                B2_Fixed_Cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Fixed_Cross, 'tStartRefresh')  # time at next scr refresh
                B2_Fixed_Cross.setAutoDraw(True)
            if B2_Fixed_Cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B2_Fixed_Cross.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    B2_Fixed_Cross.tStop = t  # not accounting for scr refresh
                    B2_Fixed_Cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B2_Fixed_Cross, 'tStopRefresh')  # time at next scr refresh
                    B2_Fixed_Cross.setAutoDraw(False)
            
            # *B2_Study_Image* updates
            if B2_Study_Image.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                B2_Study_Image.frameNStart = frameN  # exact frame index
                B2_Study_Image.tStart = t  # local t and not account for scr refresh
                B2_Study_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Study_Image, 'tStartRefresh')  # time at next scr refresh
                B2_Study_Image.setAutoDraw(True)
            if B2_Study_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B2_Study_Image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    B2_Study_Image.tStop = t  # not accounting for scr refresh
                    B2_Study_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B2_Study_Image, 'tStopRefresh')  # time at next scr refresh
                    B2_Study_Image.setAutoDraw(False)
            
            # *B2_Mask_Image* updates
            if B2_Mask_Image.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                B2_Mask_Image.frameNStart = frameN  # exact frame index
                B2_Mask_Image.tStart = t  # local t and not account for scr refresh
                B2_Mask_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Mask_Image, 'tStartRefresh')  # time at next scr refresh
                B2_Mask_Image.setAutoDraw(True)
            if B2_Mask_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B2_Mask_Image.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    B2_Mask_Image.tStop = t  # not accounting for scr refresh
                    B2_Mask_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B2_Mask_Image, 'tStopRefresh')  # time at next scr refresh
                    B2_Mask_Image.setAutoDraw(False)
            
            # *B2_Test_Image* updates
            if B2_Test_Image.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B2_Test_Image.frameNStart = frameN  # exact frame index
                B2_Test_Image.tStart = t  # local t and not account for scr refresh
                B2_Test_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Test_Image, 'tStartRefresh')  # time at next scr refresh
                B2_Test_Image.setAutoDraw(True)
            
            # *B2_Test_Prompt* updates
            if B2_Test_Prompt.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B2_Test_Prompt.frameNStart = frameN  # exact frame index
                B2_Test_Prompt.tStart = t  # local t and not account for scr refresh
                B2_Test_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Test_Prompt, 'tStartRefresh')  # time at next scr refresh
                B2_Test_Prompt.setAutoDraw(True)
            
            # *B2_Test_Response* updates
            waitOnFlip = False
            if B2_Test_Response.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                B2_Test_Response.frameNStart = frameN  # exact frame index
                B2_Test_Response.tStart = t  # local t and not account for scr refresh
                B2_Test_Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B2_Test_Response, 'tStartRefresh')  # time at next scr refresh
                B2_Test_Response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(B2_Test_Response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(B2_Test_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if B2_Test_Response.status == STARTED and not waitOnFlip:
                theseKeys = B2_Test_Response.getKeys(keyList=['1', '0'], waitRelease=False)
                _B2_Test_Response_allKeys.extend(theseKeys)
                if len(_B2_Test_Response_allKeys):
                    B2_Test_Response.keys = _B2_Test_Response_allKeys[0].name  # just the first key pressed
                    B2_Test_Response.rt = _B2_Test_Response_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in B2_StudyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "B2_Study"-------
        for thisComponent in B2_StudyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        B2_Trial.addData('B2_Fixed_Cross.started', B2_Fixed_Cross.tStartRefresh)
        B2_Trial.addData('B2_Fixed_Cross.stopped', B2_Fixed_Cross.tStopRefresh)
        B2_Trial.addData('B2_Study_Image.started', B2_Study_Image.tStartRefresh)
        B2_Trial.addData('B2_Study_Image.stopped', B2_Study_Image.tStopRefresh)
        B2_Trial.addData('B2_Mask_Image.started', B2_Mask_Image.tStartRefresh)
        B2_Trial.addData('B2_Mask_Image.stopped', B2_Mask_Image.tStopRefresh)
        B2_Trial.addData('B2_Test_Image.started', B2_Test_Image.tStartRefresh)
        B2_Trial.addData('B2_Test_Image.stopped', B2_Test_Image.tStopRefresh)
        B2_Trial.addData('B2_Test_Prompt.started', B2_Test_Prompt.tStartRefresh)
        B2_Trial.addData('B2_Test_Prompt.stopped', B2_Test_Prompt.tStopRefresh)
        # check responses
        if B2_Test_Response.keys in ['', [], None]:  # No response was made
            B2_Test_Response.keys = None
        B2_Trial.addData('B2_Test_Response.keys',B2_Test_Response.keys)
        if B2_Test_Response.keys != None:  # we had a response
            B2_Trial.addData('B2_Test_Response.rt', B2_Test_Response.rt)
        B2_Trial.addData('B2_Test_Response.started', B2_Test_Response.tStartRefresh)
        B2_Trial.addData('B2_Test_Response.stopped', B2_Test_Response.tStopRefresh)
        # the Routine "B2_Study" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'B2_Trial'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block2'


# ------Prepare to start Routine "Demo_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
Demo_Instructions_Text.alignText='left'
Demo_Instructions_Response.keys = []
Demo_Instructions_Response.rt = []
_Demo_Instructions_Response_allKeys = []
# keep track of which components have finished
Demo_InstructionsComponents = [Demo_Instructions_Text, Demo_Instructions_Response]
for thisComponent in Demo_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Demo_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Demo_Instructions"-------
while continueRoutine:
    # get current time
    t = Demo_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Demo_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Demo_Instructions_Text* updates
    if Demo_Instructions_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Demo_Instructions_Text.frameNStart = frameN  # exact frame index
        Demo_Instructions_Text.tStart = t  # local t and not account for scr refresh
        Demo_Instructions_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Demo_Instructions_Text, 'tStartRefresh')  # time at next scr refresh
        Demo_Instructions_Text.setAutoDraw(True)
    
    # *Demo_Instructions_Response* updates
    waitOnFlip = False
    if Demo_Instructions_Response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Demo_Instructions_Response.frameNStart = frameN  # exact frame index
        Demo_Instructions_Response.tStart = t  # local t and not account for scr refresh
        Demo_Instructions_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Demo_Instructions_Response, 'tStartRefresh')  # time at next scr refresh
        Demo_Instructions_Response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Demo_Instructions_Response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Demo_Instructions_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Demo_Instructions_Response.status == STARTED and not waitOnFlip:
        theseKeys = Demo_Instructions_Response.getKeys(keyList=['space'], waitRelease=False)
        _Demo_Instructions_Response_allKeys.extend(theseKeys)
        if len(_Demo_Instructions_Response_allKeys):
            Demo_Instructions_Response.keys = _Demo_Instructions_Response_allKeys[0].name  # just the first key pressed
            Demo_Instructions_Response.rt = _Demo_Instructions_Response_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Demo_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Demo_Instructions"-------
for thisComponent in Demo_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Demo_Instructions_Text.started', Demo_Instructions_Text.tStartRefresh)
thisExp.addData('Demo_Instructions_Text.stopped', Demo_Instructions_Text.tStopRefresh)
# check responses
if Demo_Instructions_Response.keys in ['', [], None]:  # No response was made
    Demo_Instructions_Response.keys = None
thisExp.addData('Demo_Instructions_Response.keys',Demo_Instructions_Response.keys)
if Demo_Instructions_Response.keys != None:  # we had a response
    thisExp.addData('Demo_Instructions_Response.rt', Demo_Instructions_Response.rt)
thisExp.addData('Demo_Instructions_Response.started', Demo_Instructions_Response.tStartRefresh)
thisExp.addData('Demo_Instructions_Response.stopped', Demo_Instructions_Response.tStopRefresh)
thisExp.nextEntry()
# the Routine "Demo_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Age"-------
continueRoutine = True
# update component parameters for each repeat
Age_Question.alignText='left'
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
AgeComponents = [Age_Question, Age_Response, ContinueButton, mouse]
for thisComponent in AgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AgeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Age"-------
while continueRoutine:
    # get current time
    t = AgeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AgeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Age_Question* updates
    if Age_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Age_Question.frameNStart = frameN  # exact frame index
        Age_Question.tStart = t  # local t and not account for scr refresh
        Age_Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Age_Question, 'tStartRefresh')  # time at next scr refresh
        Age_Question.setAutoDraw(True)
    
    # *Age_Response* updates
    if Age_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Age_Response.frameNStart = frameN  # exact frame index
        Age_Response.tStart = t  # local t and not account for scr refresh
        Age_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Age_Response, 'tStartRefresh')  # time at next scr refresh
        Age_Response.setAutoDraw(True)
    
    # *ContinueButton* updates
    if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton.frameNStart = frameN  # exact frame index
        ContinueButton.tStart = t  # local t and not account for scr refresh
        ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
        ContinueButton.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [ContinueButton]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Age"-------
for thisComponent in AgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Age_Question.started', Age_Question.tStartRefresh)
thisExp.addData('Age_Question.stopped', Age_Question.tStopRefresh)
thisExp.addData('Age_Response.text',Age_Response.text)
Age_Response.reset()
thisExp.addData('Age_Response.started', Age_Response.tStartRefresh)
thisExp.addData('Age_Response.stopped', Age_Response.tStopRefresh)
thisExp.addData('ContinueButton.started', ContinueButton.tStartRefresh)
thisExp.addData('ContinueButton.stopped', ContinueButton.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(mouse.x): thisExp.addData('mouse.x', mouse.x[0])
if len(mouse.y): thisExp.addData('mouse.y', mouse.y[0])
if len(mouse.leftButton): thisExp.addData('mouse.leftButton', mouse.leftButton[0])
if len(mouse.midButton): thisExp.addData('mouse.midButton', mouse.midButton[0])
if len(mouse.rightButton): thisExp.addData('mouse.rightButton', mouse.rightButton[0])
if len(mouse.time): thisExp.addData('mouse.time', mouse.time[0])
if len(mouse.clicked_name): thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "Age" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Gender"-------
continueRoutine = True
# update component parameters for each repeat
Gender_Question.alignText='left'
Gender1.keys = []
Gender1.rt = []
_Gender1_allKeys = []
# keep track of which components have finished
GenderComponents = [Gender_Question, Gender1]
for thisComponent in GenderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GenderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Gender"-------
while continueRoutine:
    # get current time
    t = GenderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GenderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Gender_Question* updates
    if Gender_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Gender_Question.frameNStart = frameN  # exact frame index
        Gender_Question.tStart = t  # local t and not account for scr refresh
        Gender_Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Gender_Question, 'tStartRefresh')  # time at next scr refresh
        Gender_Question.setAutoDraw(True)
    
    # *Gender1* updates
    waitOnFlip = False
    if Gender1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Gender1.frameNStart = frameN  # exact frame index
        Gender1.tStart = t  # local t and not account for scr refresh
        Gender1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Gender1, 'tStartRefresh')  # time at next scr refresh
        Gender1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Gender1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Gender1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Gender1.status == STARTED and not waitOnFlip:
        theseKeys = Gender1.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
        _Gender1_allKeys.extend(theseKeys)
        if len(_Gender1_allKeys):
            Gender1.keys = _Gender1_allKeys[0].name  # just the first key pressed
            Gender1.rt = _Gender1_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GenderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Gender"-------
for thisComponent in GenderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Gender1.keys in ['', [], None]:  # No response was made
    Gender1.keys = None
thisExp.addData('Gender1.keys',Gender1.keys)
if Gender1.keys != None:  # we had a response
    thisExp.addData('Gender1.rt', Gender1.rt)
thisExp.nextEntry()
# the Routine "Gender" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ethnicity"-------
continueRoutine = True
# update component parameters for each repeat
Ethnicity1.keys = []
Ethnicity1.rt = []
_Ethnicity1_allKeys = []
Ethnicity_Question_1.alignText='left'
# keep track of which components have finished
EthnicityComponents = [Ethnicity_Question_1, Ethnicity1]
for thisComponent in EthnicityComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EthnicityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ethnicity"-------
while continueRoutine:
    # get current time
    t = EthnicityClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EthnicityClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ethnicity_Question_1* updates
    if Ethnicity_Question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ethnicity_Question_1.frameNStart = frameN  # exact frame index
        Ethnicity_Question_1.tStart = t  # local t and not account for scr refresh
        Ethnicity_Question_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ethnicity_Question_1, 'tStartRefresh')  # time at next scr refresh
        Ethnicity_Question_1.setAutoDraw(True)
    
    # *Ethnicity1* updates
    waitOnFlip = False
    if Ethnicity1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Ethnicity1.frameNStart = frameN  # exact frame index
        Ethnicity1.tStart = t  # local t and not account for scr refresh
        Ethnicity1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ethnicity1, 'tStartRefresh')  # time at next scr refresh
        Ethnicity1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Ethnicity1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Ethnicity1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Ethnicity1.status == STARTED and not waitOnFlip:
        theseKeys = Ethnicity1.getKeys(keyList=['1', '2'], waitRelease=False)
        _Ethnicity1_allKeys.extend(theseKeys)
        if len(_Ethnicity1_allKeys):
            Ethnicity1.keys = _Ethnicity1_allKeys[0].name  # just the first key pressed
            Ethnicity1.rt = _Ethnicity1_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EthnicityComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ethnicity"-------
for thisComponent in EthnicityComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Ethnicity1.keys in ['', [], None]:  # No response was made
    Ethnicity1.keys = None
thisExp.addData('Ethnicity1.keys',Ethnicity1.keys)
if Ethnicity1.keys != None:  # we had a response
    thisExp.addData('Ethnicity1.rt', Ethnicity1.rt)
thisExp.nextEntry()
# the Routine "Ethnicity" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Race"-------
continueRoutine = True
# update component parameters for each repeat
Race1.keys = []
Race1.rt = []
_Race1_allKeys = []
Race_Question_1.alignText='left'
# keep track of which components have finished
RaceComponents = [Race_Question_1, Race1]
for thisComponent in RaceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Race"-------
while continueRoutine:
    # get current time
    t = RaceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RaceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Race_Question_1* updates
    if Race_Question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Race_Question_1.frameNStart = frameN  # exact frame index
        Race_Question_1.tStart = t  # local t and not account for scr refresh
        Race_Question_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Race_Question_1, 'tStartRefresh')  # time at next scr refresh
        Race_Question_1.setAutoDraw(True)
    
    # *Race1* updates
    waitOnFlip = False
    if Race1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Race1.frameNStart = frameN  # exact frame index
        Race1.tStart = t  # local t and not account for scr refresh
        Race1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Race1, 'tStartRefresh')  # time at next scr refresh
        Race1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Race1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Race1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Race1.status == STARTED and not waitOnFlip:
        theseKeys = Race1.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7'], waitRelease=False)
        _Race1_allKeys.extend(theseKeys)
        if len(_Race1_allKeys):
            Race1.keys = _Race1_allKeys[0].name  # just the first key pressed
            Race1.rt = _Race1_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RaceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Race"-------
for thisComponent in RaceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Race1.keys in ['', [], None]:  # No response was made
    Race1.keys = None
thisExp.addData('Race1.keys',Race1.keys)
if Race1.keys != None:  # we had a response
    thisExp.addData('Race1.rt', Race1.rt)
thisExp.nextEntry()
# the Routine "Race" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Education_Years"-------
continueRoutine = True
# update component parameters for each repeat
Education_Years1.keys = []
Education_Years1.rt = []
_Education_Years1_allKeys = []
Education_Years_Question.alignText='left'
# keep track of which components have finished
Education_YearsComponents = [Education_Years_Question, Education_Years1]
for thisComponent in Education_YearsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Education_YearsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Education_Years"-------
while continueRoutine:
    # get current time
    t = Education_YearsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Education_YearsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Education_Years_Question* updates
    if Education_Years_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Education_Years_Question.frameNStart = frameN  # exact frame index
        Education_Years_Question.tStart = t  # local t and not account for scr refresh
        Education_Years_Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Education_Years_Question, 'tStartRefresh')  # time at next scr refresh
        Education_Years_Question.setAutoDraw(True)
    
    # *Education_Years1* updates
    waitOnFlip = False
    if Education_Years1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Education_Years1.frameNStart = frameN  # exact frame index
        Education_Years1.tStart = t  # local t and not account for scr refresh
        Education_Years1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Education_Years1, 'tStartRefresh')  # time at next scr refresh
        Education_Years1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Education_Years1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Education_Years1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Education_Years1.status == STARTED and not waitOnFlip:
        theseKeys = Education_Years1.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7'], waitRelease=False)
        _Education_Years1_allKeys.extend(theseKeys)
        if len(_Education_Years1_allKeys):
            Education_Years1.keys = _Education_Years1_allKeys[0].name  # just the first key pressed
            Education_Years1.rt = _Education_Years1_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Education_YearsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Education_Years"-------
for thisComponent in Education_YearsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Education_Years1.keys in ['', [], None]:  # No response was made
    Education_Years1.keys = None
thisExp.addData('Education_Years1.keys',Education_Years1.keys)
if Education_Years1.keys != None:  # we had a response
    thisExp.addData('Education_Years1.rt', Education_Years1.rt)
thisExp.nextEntry()
# the Routine "Education_Years" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Thank_You"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Thank_YouComponents = [Thank_You_Text]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thank_YouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thank_You"-------
while continueRoutine:
    # get current time
    t = Thank_YouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thank_YouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thank_You_Text* updates
    if Thank_You_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thank_You_Text.frameNStart = frameN  # exact frame index
        Thank_You_Text.tStart = t  # local t and not account for scr refresh
        Thank_You_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thank_You_Text, 'tStartRefresh')  # time at next scr refresh
        Thank_You_Text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_You"-------
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thank_You_Text.started', Thank_You_Text.tStartRefresh)
thisExp.addData('Thank_You_Text.stopped', Thank_You_Text.tStopRefresh)
# the Routine "Thank_You" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
