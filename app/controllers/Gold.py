"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import Flask, render_template, request, redirect, session
import random, datetime

class Gold(Controller):
    def __init__(self, action):
        super(Gold, self).__init__(action)
    
    def index(self):

        if not session.has_key('gold'):
            session['gold'] = 0  #sets gold to 0 
        
        if not session.has_key('output'):
            session['output'] = '' #sets output to blank
        
        gold = session['gold']
        
        output = session['output']
        
        return self.load_view('index.html', gold=gold, output=output)

    def process_money(self):


        if request.form.has_key('farm_gold'):
            random_num = random.randint(10,20)
            session['gold'] += random_num
            session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the farm! (' +str(datetime.datetime.now())+ ')</p>'
        

        elif request.form.has_key('cave_gold'):
            random_num = random.randint(5,10)
            session['gold'] += random_num
            session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the cave! (' +str(datetime.datetime.now())+ ')</p>'
        

        elif request.form.has_key('house_gold'):
            random_num = random.randint(2,5)
            session['gold'] += random_num
            session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the house! (' +str(datetime.datetime.now())+ ')</p>'
        

        elif request.form.has_key('casino_gold'):
            random_num = random.randint(-50,50)
            session['gold'] += random_num
            
            if random_num >= 0:
                session['output'] += '<p class="green">Earned ' +str(random_num)+ ' golds from the casino! (' +str(datetime.datetime.now())+ ')</p>'
            elif random_num < 0:
                random_num = random_num * -1
                session['output'] += '<p class="red">Entered a casino and lost ' +str(random_num)+ ' golds... Ouch.. (' +str(datetime.datetime.now())+ ')</p>'
        

        return redirect('/')


    def clear(self):
        session.clear()
        return redirect('/')
