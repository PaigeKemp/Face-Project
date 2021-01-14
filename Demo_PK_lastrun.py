#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Thu Jan 14 10:49:08 2021
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
    originPath='/Users/paigekemp/Desktop/UNCG/UNCG Research/Current Experiments/OtherRaceEffect/Demo_PK_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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
import random

##so note that if you want to pilot a specific format, just remove the ones you don't want to run from orders & formats
formats=[1,2,3]

format=random.choice(formats)
Welcome_Text = visual.TextStim(win=win, name='Welcome_Text',
    text='Welcome to the experiment!',
    font='Arial',
    units='cm', pos=(0, 4), height=1.5, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Demo_Instructions"
Demo_InstructionsClock = core.Clock()
Demo_Instructions_Text = visual.TextStim(win=win, name='Demo_Instructions_Text',
    text='You have now completed the main task. \n\nAll that remains is a few questions about you. \n\nPress enter to begin.',
    font='Arial',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Demo_Instructions_Response = keyboard.Keyboard()

# Initialize components for Routine "Age_1"
Age_1Clock = core.Clock()
Age_Question1 = visual.TextStim(win=win, name='Age_Question1',
    text='How old are you (in years)?\nPlease type two digits and then press next',
    font='Arial',
    units='cm', pos=(1, 10), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Age_Response1 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(-12, 8),units='cm',     letterHeight=1,
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
     name='Age_Response1',
     autoLog=True,
)
ContinueButton = visual.TextStim(win=win, name='ContinueButton',
    text='Next >',
    font='Arial',
    units='cm', pos=(15, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "Ethnicity_1"
Ethnicity_1Clock = core.Clock()
Ethnicity_Question_1 = visual.TextStim(win=win, name='Ethnicity_Question_1',
    text='What is your ethnicity?\n\n(1) Hispanic or Latino\n\n(2) Not Hispanic or Latino',
    font='Arial',
    units='cm', pos=(-12, 8.3), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ethnicity1 = keyboard.Keyboard()

# Initialize components for Routine "Race_1"
Race_1Clock = core.Clock()
Race_Question_1 = visual.TextStim(win=win, name='Race_Question_1',
    text='What is your race?\n\n(1) American Indian/Alaska Native\n\n(2) Asian\n\n(3) Native Hawaiian or Other Pacific Islander\n\n(4) Black or African American\n\n(5) White\n\n(6) More than one\n\n(7) Unknown',
    font='Arial',
    units='cm', pos=(.5, 2.5), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Race1 = keyboard.Keyboard()

# Initialize components for Routine "Education_Years_1"
Education_Years_1Clock = core.Clock()
Education_Years_Question = visual.TextStim(win=win, name='Education_Years_Question',
    text='How many years of education have you completed?\n\n(1) 12 - High School\n\n(2) 13\n\n(3) 14\n\n(4) 15\n\n(5) 16 - College',
    font='Arial',
    units='cm', pos=(.5, 4.8), height=1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Education_Years1 = keyboard.Keyboard()

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
    Cond_Loop.addData('format_chosen',format)
    Cond_Loop.addData('Welcome_Text.started', Welcome_Text.tStartRefresh)
    Cond_Loop.addData('Welcome_Text.stopped', Welcome_Text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Cond_Loop'


# ------Prepare to start Routine "Demo_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
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
        theseKeys = Demo_Instructions_Response.getKeys(keyList=['return'], waitRelease=False)
        _Demo_Instructions_Response_allKeys.extend(theseKeys)
        if len(_Demo_Instructions_Response_allKeys):
            Demo_Instructions_Response.keys = _Demo_Instructions_Response_allKeys[-1].name  # just the last key pressed
            Demo_Instructions_Response.rt = _Demo_Instructions_Response_allKeys[-1].rt
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
# the Routine "Demo_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Age_1"-------
continueRoutine = True
# update component parameters for each repeat
Age_Question1.alignText='left'
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
Age_1Components = [Age_Question1, Age_Response1, ContinueButton, mouse]
for thisComponent in Age_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Age_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Age_1"-------
while continueRoutine:
    # get current time
    t = Age_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Age_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Age_Question1* updates
    if Age_Question1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Age_Question1.frameNStart = frameN  # exact frame index
        Age_Question1.tStart = t  # local t and not account for scr refresh
        Age_Question1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Age_Question1, 'tStartRefresh')  # time at next scr refresh
        Age_Question1.setAutoDraw(True)
    
    # *Age_Response1* updates
    if Age_Response1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Age_Response1.frameNStart = frameN  # exact frame index
        Age_Response1.tStart = t  # local t and not account for scr refresh
        Age_Response1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Age_Response1, 'tStartRefresh')  # time at next scr refresh
        Age_Response1.setAutoDraw(True)
    
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
    for thisComponent in Age_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Age_1"-------
for thisComponent in Age_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Age_Question1.started', Age_Question1.tStartRefresh)
thisExp.addData('Age_Question1.stopped', Age_Question1.tStopRefresh)
thisExp.addData('Age_Response1.text',Age_Response1.text)
Age_Response1.reset()
thisExp.addData('Age_Response1.started', Age_Response1.tStartRefresh)
thisExp.addData('Age_Response1.stopped', Age_Response1.tStopRefresh)
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
# the Routine "Age_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ethnicity_1"-------
continueRoutine = True
# update component parameters for each repeat
Ethnicity1.keys = []
Ethnicity1.rt = []
_Ethnicity1_allKeys = []
Ethnicity_Question_1.alignText='left'
# keep track of which components have finished
Ethnicity_1Components = [Ethnicity_Question_1, Ethnicity1]
for thisComponent in Ethnicity_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ethnicity_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ethnicity_1"-------
while continueRoutine:
    # get current time
    t = Ethnicity_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ethnicity_1Clock)
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
    if Ethnicity1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in Ethnicity_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ethnicity_1"-------
for thisComponent in Ethnicity_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Ethnicity1.keys in ['', [], None]:  # No response was made
    Ethnicity1.keys = None
thisExp.addData('Ethnicity1.keys',Ethnicity1.keys)
if Ethnicity1.keys != None:  # we had a response
    thisExp.addData('Ethnicity1.rt', Ethnicity1.rt)
thisExp.nextEntry()
# the Routine "Ethnicity_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Race_1"-------
continueRoutine = True
# update component parameters for each repeat
Race1.keys = []
Race1.rt = []
_Race1_allKeys = []
Race_Question_1.alignText='left'
# keep track of which components have finished
Race_1Components = [Race_Question_1, Race1]
for thisComponent in Race_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Race_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Race_1"-------
while continueRoutine:
    # get current time
    t = Race_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Race_1Clock)
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
    if Race1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in Race_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Race_1"-------
for thisComponent in Race_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Race1.keys in ['', [], None]:  # No response was made
    Race1.keys = None
thisExp.addData('Race1.keys',Race1.keys)
if Race1.keys != None:  # we had a response
    thisExp.addData('Race1.rt', Race1.rt)
thisExp.nextEntry()
# the Routine "Race_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Education_Years_1"-------
continueRoutine = True
# update component parameters for each repeat
Education_Years1.keys = []
Education_Years1.rt = []
_Education_Years1_allKeys = []
Education_Years_Question.alignText='left'
# keep track of which components have finished
Education_Years_1Components = [Education_Years_Question, Education_Years1]
for thisComponent in Education_Years_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Education_Years_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Education_Years_1"-------
while continueRoutine:
    # get current time
    t = Education_Years_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Education_Years_1Clock)
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
    if Education_Years1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in Education_Years_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Education_Years_1"-------
for thisComponent in Education_Years_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Education_Years1.keys in ['', [], None]:  # No response was made
    Education_Years1.keys = None
thisExp.addData('Education_Years1.keys',Education_Years1.keys)
if Education_Years1.keys != None:  # we had a response
    thisExp.addData('Education_Years1.rt', Education_Years1.rt)
thisExp.nextEntry()
# the Routine "Education_Years_1" was not non-slip safe, so reset the non-slip timer
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
