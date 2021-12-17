#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:37:57 2021

@author: apoorvakanekal
"""

import turtle, random 

        
class Bubbles(turtle.Turtle):
    def __init__(self):
        global turtList
        self.w=1000
        self.h=700
        self.panel=turtle.Screen()
        self.panel.setup(self.w,self.h) # start with calling setup to turn on listeners
        self.panel.bgcolor("pink")
        turtle.listen() # for keyboard listening
        
        # =========DEFINE VARIABLES BELOW=========
        self.running = True # for controlling the while loop
        self.pace=100
        self.span=60
        self.numTurt=5
        self.turtList = []
        for i in range(self.numTurt):
           self.turtList.append(turtle.Turtle()) # append adds a turtle to the end of the list.
        
        for i in range(len(self.turtList)):
            self.turtList[i].color('purple')
            self.turtList[i].shape("circle")
            self.turtList[i].shapesize(12)
            self.turtList[i].up()
            self.turtList[i].goto(random.randint(-self.w/2,self.w/2),random.randint(-self.h/2,self.h/2))
            self.turtList[i].speed(10)

        self.bubbleturt=turtle.Turtle()
        self.bubbleturt.shape("circle")
        self.bubbleturt.shapesize(2)
        self.bubbleturt.color("white")
        
        self.bubbleturt.onclick(self.deleteTurt)
        
        self.run()
        
    def deleteTurt(self,x,y):
    # '''this hides or "deletes" the turtle when clicked'''
        self.bubbleturt.hideturtle() # MODIFY - you'll have to change this to your turtle's name.
        self.endGame()
    def randommotion(self):
        '''makes white target move around the panel randomly, and sends it back to center when it 
        hits edge of panel (so it doesn't go off the screen)'''
        self.bubbleturt.up()
        self.bubbleturt.goto(random.randint(-self.w/2,self.w/2),random.randint(-self.h/2,self.h/2))
        self.bubbleturt.left(90)
        self.bubbleturt.forward(self.pace)
        self.bubbleturt.left(random.randint(-self.span,self.span))
        self.bubbleturt.speed(0)
        
        self.ybounds=self.bubbleturt.ycor()<-self.h/2 or self.bubbleturt.ycor()>self.h/2
        self.xbounds=self.bubbleturt.xcor()<-self.w/2 or self.bubbleturt.xcor()>self.w/2
        
        if self.xbounds or self.ybounds:
            self.bubbleturt.up()
            self.bubbleturt.home()
        
    def randommove(self,turtleName):
        '''makes purple obstacles move around the panel randomly, and sends them back to center when they 
        hit edge of panel (so they don' go off the screen)'''
        turtleName.left(90)
        turtleName.forward(random.randint(0,500))
        turtleName.left(random.randint(-70,70))
        
        self.ybounds=turtleName.ycor()<-self.h/2 or turtleName.ycor()>self.h/2
        self.xbounds=turtleName.xcor()<-self.w/2 or turtleName.xcor()>self.w/2
        
        if self.xbounds or self.ybounds:
            turtleName.up()
            turtleName.home()

    def endGame(self):
        self.panel.clear()
        self. panel.bgcolor("pink")
        turtle.write("Game Over", font = ('futura',40), align = 'center')
        turtle.ht()
        
    def run(self):
        while self.running:
            for turt in self.turtList:
                self.randommove(turt)
        
            self.randommotion()
    

call = Bubbles()