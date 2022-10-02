import sqlite3
import streamlit as st
from datetime import date
import json
import csv
from json import JSONEncoder
import numpy
import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import plotly.express as px 
import pickle
from pathlib import Path
from streamlit_chat import *
import requests
from streamlit_chat import *
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration




import datetime
import streamlit as st
import streamlit.components.v1 as components

import json
from ctypes import cast
import streamlit as st 
from hydralit import HydraApp
import hydralit_components as hc
from streamlit_option_menu import option_menu
import apps
from datetime import date 
import plotly.graph_objects as go
import yfinance as yf 
from dash import Dash, dcc, html, Input, Output, dash_table
from dash.exceptions import PreventUpdate
from time import sleep
from random import randint, seed
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pickle 
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
from st_on_hover_tabs import on_hover_tabs
from yaml import SafeLoader
import yaml
# Main App
st.set_page_config(page_title="Fintero", page_icon=":stock_chart:", layout="wide" ,initial_sidebar_state='collapsed',) 
# Login Page
import sqlite3
conn=sqlite3.connect('data.db')
c=conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, password TEXT);')
create_usertable()

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username, password) VALUES(?,?);',(username,password))
    conn.commit()
def delete_userdata():
    c.execute('DELETE FROM usertable WHERE username="{}"'.format(username))
    conn.commit()
def login_user(username,password):
    c.execute('SELECT * FROM  usertable WHERE username=? AND password=?;',(username,password))
    data = c.fetchall()
    return data
def view_all_users():
    c.execute('SELECT * FROM  usertable ')
    data = c.fetchall()
    return data

def create_portfolio_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS portfolio_usertable(user_id INTEGER, portfolio_id INTEGER,shares INTEGER,date DATETIME ,PRIMARY KEY (user_id, portfolio_id,date),FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,FOREIGN KEY (portfolio_id) REFERENCES portfolio(portfolio_id) ON DELETE CASCADE) ;')
create_portfolio_usertable()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS portfoliotable(portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,ticker TEXT, type TEXT, price INTEGER, cost INTEGER);')
create_table()

def add_portfolio_usertable():
    c.execute('INSERT INTO portfolio_usertable((user_id,portfolio_id,shares,type,date,price,cost) VALUES(?,?,?,?,?,?,?,?);')
    conn.commit()
def delete_portfolio_usertable(ticker):
    c.execute('DELETE FROM portfolio_usertable WHERE ticker="{}"'.format(ticker))
    conn.commit()
def view_all_portfolio_usertable():
    c.execute('SELECT * FROM  portfolio_usertable JOIN portfoliotable ON portfolio_usertable.portfolio_id = portfoliotable.portfolio_id JOIN usertable ON portfolio_usertable.user_id=usertable.user_id WHERE portfolio_usertable.user_id=1 ;')
    data = c.fetchall()
    return data
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())
# print(view_all_portfolio_usertable())


def add_data(ticker,type,price,cost):
    c.execute('INSERT INTO portfoliotable(ticker,type,price,cost) VALUES(?,?,?,?);',(ticker,type,price,cost))
    conn.commit()
def delete_data(ticker):
    c.execute('DELETE FROM portfoliotable WHERE ticker="{}"'.format(ticker))
    conn.commit()
def view_all_data():
    c.execute('SELECT * FROM  portfoliotable;')
    data = c.fetchall()
    return data
def view_all_ticker_names():
    c.execute('SELECT DISTINCT ticker FROM portfoliotable;')
    data = c.fetchall()
    return data
def get_ticker(ticker):
    c.execute('SELECT * FROM  portfoliotable WHERE ticker="{}"'.format(ticker))
    data = c.fetchall()
    return data

def edit_ticker_data(new_ticker,new_type,new_price,new_cost,ticker,type,price,cost):
    c.execute("UPDATE portfoliotable SET ticker =?,type=?,price=? ,cost=?  WHERE ticker =? and type=? and price=? and cost=? ",(new_ticker,new_type,new_price,new_cost,ticker,type,price,cost))
    conn.commit()
    data = c.fetchall()
    return data

# def delete_table():
#     c.execute('DROP TABLE IF EXISTS portfoliotable;')
#     conn.commit()
# delete_table()
text4=st.empty()
text2=st.empty()
with text2.container():
    menu=["Login","Register"]
    choice=st.selectbox("Choose One",menu)

# def delete_usertable():
#                 c.execute('DROP TABLE IF EXISTS usertable;')
#                 conn.commit()
# delete_usertable()
if choice == "Register":
    
    st.title="register"
    new_user=st.text_input("Set Your Username")
    new_password= st.text_input("Set Your Password",type='password')
    to_register=st.button("Register")
    if to_register:
        add_userdata(new_user,new_password)
        st.success("Welcome Onboard {}".format(new_user))
        st.info("Go to login Menu to login")
   
elif choice == "Login":
    with text4.container():

        username= st.text_input("Username")
        password= st.text_input("password",type='password')
        submit = st.button('Submit')

        result = login_user(username,password)
    if result:
        pass
        text4.empty()
        text2.empty()
        st.sidebar.write(f'{username}')
        def get_data(selected_stocks):
            return [
                ['2015-12-25', 512.53, 514.88, 505.69, 507.34],
                ['2015-12-26', 511.83, 514.98, 505.59, 506.23],
                ['2015-12-27', 511.22, 515.30, 505.49, 506.47],
                ['2015-12-28', 510.35, 515.72, 505.23, 505.80],
                ['2015-12-29', 510.53, 515.86, 505.38, 508.25],
                ['2015-12-30', 511.43, 515.98, 505.66, 507.45],
                ['2015-12-31', 511.50, 515.33, 505.99, 507.98],
                ['2016-01-01', 511.32, 514.29, 505.99, 506.37],
                ['2016-01-02', 511.70, 514.87, 506.18, 506.75],
                ['2016-01-03', 512.30, 514.78, 505.87, 508.67],
                ['2016-01-04', 512.50, 514.77, 505.83, 508.35],
                ['2016-01-05', 511.53, 516.18, 505.91, 509.42],
                ['2016-01-06', 511.13, 516.01, 506.00, 509.26],
                ['2016-01-07', 510.93, 516.07, 506.00, 510.99],
                ['2016-01-08', 510.88, 515.93, 505.22, 509.95],
                ['2016-01-09', 509.12, 515.97, 505.15, 510.12],
                ['2016-01-10', 508.53, 516.13, 505.66, 510.42]
                ]
        class NumpyArrayEncoder(JSONEncoder):
            def default(self, obj):
                if isinstance(obj, numpy.ndarray):
                    return obj.tolist()
                return JSONEncoder.default(self, obj)

            # Serialization

            # st.markdown(""" <style>
            # #MainMenu {visibility: hidden;}
            # footer {visibility: hidden;}
            # </style> """, unsafe_allow_html=True)


            # with st.sidebar:
            #     selected = option_menu("Advanced", ["Prediction",'Expert Advice',"More"], 
            #         icons=['house', 'gear'], menu_icon="cast", default_index=1)
            # 2. horizontal menu


        with st.sidebar:

            selected = option_menu("Home", ["My Stocks","Charts","News","Stock Dashboard","Bot","Fundamental","Sentiment Analysis","Technical Analysis","Sentiment Analysis"],  
                icons=['house', 'gear', 'gear', 'gear', 'gear'], menu_icon="cast", default_index=1)

        if selected == "Charts":
            menu_data = [
                {'icon': "far fa-copy", 'label':"Left End"},
                {'id':'Copy','icon':"🐙",'label':"Copy"},
                {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
                {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
                {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
                {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
                {'icon': "far fa-copy", 'label':"Right End"},
                {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
            ]

            over_theme = {'txc_inactive': '#FFFFFF'}
            menu_id = hc.nav_bar(
                menu_definition=menu_data,
                override_theme=over_theme,
                home_name='Home',
                login_name='Logout',
                hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
                sticky_nav=False, #at the top or not
                sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
            )

            # st.title(f"{selected}")
            #st.title("Stock prediction app")
            stocks=["AAPL","GOOG","MSFT","COST","AMD","FDX","SAVA","CANO"]
            selected_stocks=st.selectbox("Select A Ticker",stocks)
            period=n_years=365

            @st.cache
            def load_data(ticker):
                data=yf.download(ticker)
                data.reset_index(inplace =True)
                data['Date'] = data['Date'].apply(lambda x: str(x.date()))
                data=data[['Date','Open','High','Low','Close']].to_numpy()
                data = json.dumps(data,cls=NumpyArrayEncoder)
                return data 
                
                #data=load_data(selected_stocks)
                #print(data)
                # print(selected_stocks)
                # print(load_data(selected_stocks))
            components.html(
            """<html>
                <head>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_provence.min.js"></script>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_glamour.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-base.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-ui.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-exports.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-stock.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-data-adapter.min.js"></script>
                <link href="https://cdn.anychart.com/releases/v8/css/anychart-ui.min.css" type="text/css" rel="stylesheet">
                <link href="https://cdn.anychart.com/releases/v8/fonts/css/anychart-font.min.css" type="text/css" rel="stylesheet">
                <style type="text/css">
                    html,
                    body,
                    #container {
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                    color:white;
                    }

                </style>
                </head>
                
                
                <script>
                var table, mapping, chart;
                anychart.onDocumentReady(function () {

                table = anychart.data.table();
                table.addData(""" + load_data(selected_stocks) +  """);
            
                    // mapping the data
                    mapping = table.mapAs();
                    mapping.addField('open', 1, 'first');
                    mapping.addField('high', 2, 'max');
                    mapping.addField('low', 3, 'min');
                    mapping.addField('close', 4, 'last');
                    mapping.addField('value', 4, 'last');

                    // defining the chart type
                    chart = anychart.stock();
                    
                    // set the series type
                    chart.plot(0).ohlc(mapping).name('"""+ selected_stocks +"""');
                    
                    // setting the chart title
                    chart.title('AnyStock Demo');

                    // display the chart	  
                    chart.container('container');
                    chart.draw();
                    });
                    </script>
                    </head>
                    <body>
                        <div id="container" style="width: 100%; height: 100%"></div>
                        """+selected_stocks+"""
                    </body>
                </html>
            
            """,
                height=600,
            )
            components.html(
            """<html>
                <head>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-annotations.min.js"></script>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_provence.min.js"></script>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_glamour.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-base.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-ui.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-exports.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-stock.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-data-adapter.min.js"></script>
                <link href="https://cdn.anychart.com/releases/v8/css/anychart-ui.min.css" type="text/css" rel="stylesheet">
                <link href="https://cdn.anychart.com/releases/v8/fonts/css/anychart-font.min.css" type="text/css" rel="stylesheet">
                <style type="text/css">
                    html, body {
                        width: 100%;
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }
                    select {
                        margin: 10px 0 0 10px;
                    }
                    button {
                        margin: 10px 0 0 5px;
                    }
                    #container {
                        position: absolute;
                        width: 100%;
                        top: 35px;
                        bottom: 0;
                    }

                </style>
                </head>
                
                
                <script>
                    anychart.onDocumentReady(function() {
                // The data used in this sample can be obtained from the CDN
                // https://cdn.anychart.com/csv-data/csco-daily.js

                // create data table on loaded data
                var dataTable = anychart.data.table();
                dataTable.addData(""" + load_data(selected_stocks) +  """);

                // map data for the ohlc series
                var ohlcMapping = dataTable.mapAs({'open': 1, 'high': 2, 'low': 3, 'close': 4});

                // map data for scroller and volume series
                var valueMapping = dataTable.mapAs({'value': 5});

                // create stock chart
                var chart = anychart.stock();

                // create and setup ohlc series on the first plot
                var ohlcSeries = chart.plot(0).ohlc(ohlcMapping);
                ohlcSeries.name('"""+ selected_stocks +"""');
                ohlcSeries.legendItem().iconType('risingfalling');

                // create and setup volume plot
                var volumePlot = chart.plot(1);
                volumePlot.height('30%');
                volumePlot.yAxis().labels().format('${%Value}{scale:(1000000)(1000)|(kk)(k)}');

                // create and setup ohlc series on the first plot
                var volumeSeries = volumePlot.column(valueMapping);
                volumeSeries.name('Volume');

                // create scroller series
                chart.scroller().area(valueMapping);

                // set container id for the chart
                chart.container('container');

                // initiate chart drawing
                chart.draw();

                // create range picker
                var rangePicker = anychart.ui.rangePicker();
                // init range picker
                rangePicker.render(chart);

                // create range selector
                var rangeSelector = anychart.ui.rangeSelector();
                // init range selector
                rangeSelector.render(chart);
                });
                
                // allow drawing on the first plot
                chart.plot(0).annotations().enabled(true);
                chart.plot(1).annotations().enabled(true);

                

                // reset the select list to the first option
                chart.listen("annotationDrawingFinish", function(){
                    document.getElementById("typeSelect").value = "default";
                });
                
            
                // create annotations
                function create() {
                    var select = document.getElementById("typeSelect");
                    chart.annotations().startDrawing(select.value);   
                }

                // remove all annotations
                function removeAll() {
                    chart.annotations().removeAllAnnotations();
                }
                    </script>
                    </head>
                    <body>
                    <select id="typeSelect" onclick="create()">
                        <option value="default" selected disabled>Annotation Type</option>
                        <option value="andrews-pitchfork">Andrews' Pitchfork</option>
                        <option value="ellipse">Ellipse</option>
                        <option value="fibonacci-arc">Fibonacci Arc</option>
                        <option value="fibonacci-fan">Fibonacci Fan</option>
                        <option value="fibonacci-retracement">Fibonacci Retracement</option>
                        <option value="fibonacci-timezones">Fibonacci Time Zones</option>  
                        <option value="horizontal-line">Horizontal Line</option> 
                        <option value="infinite-line">Infinite Line</option>
                        <option value="line">Line Segment</option>
                        <option value="marker">Marker</option>   
                        <option value="ray">Ray</option>
                        <option value="rectangle">Rectangle</option>
                        <option value="trend-channel">Trend Channel</option>
                        <option value="triangle">Triangle</option>
                        <option value="vertical-line">Vertical Line</option>
                    </select>
                    <button onclick="removeAll()">Remove All</button>
                        <div id="container" style="width: 100%; height: 100%"></div>
                        """+selected_stocks+"""
                    </body>
                </html>
            
                """,
                height=700,
                )
        # if selected=="Bot":
        
            # import torch
            # import transformers
            # from transformers import *
            # from transformers import BertTokenizer, BertForSequenceClassification
            # from transformers import pipeline

            # finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
            # tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

            # nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

            # sentences = ["there is a shortage of capital, and we need extra financing",  
            #             "growth is strong and we have plenty of liquidity", 
            #             "there are doubts about our finances", 
            #             "profits are flat"]
            # results = nlp(sentences)
            # print(results) 
        #     @st.cache(hash_funcs={transformers.models.gpt2.tokenization_gpt2_fast.GPT2TokenizerFast: hash}, suppress_st_warning=True)
        #     def load_data():    
        #         from transformers import pipeline
        #         from transformers import BertTokenizer, BertForSequenceClassification
        #         tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")
        #         finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
        #         return tokenizer,finbert
        #     tokenizer,finbert = load_data()
            

        #     st.write("Welcome to the Chatbot. I am still learning, please be patient")
        #     input = st.text_input('User:')
        #     if 'count' not in st.session_state or st.session_state.count == 6:
        #         st.session_state.count = 0 
        #         st.session_state.chat_history_ids = None
        #         st.session_state.old_response = ''
        #     else:
        #         st.session_state.count += 1


        # # PreTrainedTokenizer(name_or_path='yiyanghkust/finbert-tone', vocab_size=30873, model_max_len=1000000000000000019884624838656,
        # # is_fast=False, padding_side='right', truncation_side='right', special_tokens={'unk_token': '[UNK]', 'sep_token': '[SEP]', 'pad_token': '[PAD]', 'cls_token': '[CLS]', 'mask_token': '[MASK]'})  
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     print(type(tokenizer))
        #     # tokenizer=str(tokenizer)
        #     new_user_input_ids = tokenizer.encode(input + tokenizer.eos_encode,return_tensors='pt')

        #     bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_user_input_ids], dim=-1) if st.session_state.count > 1 else new_user_input_ids

        #     st.session_state.chat_history_ids = model.generate(bot_input_ids, max_length=5000, pad_token_id=tokenizer.eos_token_id)
        #     response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        #     if st.session_state.old_response == response:
        #       bot_input_ids = new_user_input_ids
            
        #     st.session_state.chat_history_ids = model.generate(bot_input_ids, max_length=5000, pad_token_id=tokenizer.eos_token_id)
        #     response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        #     st.write(f'Chatbot: {response}')

        #     st.session_state.old_response = response
        if selected == "Technical Analysis":
            st.title(f"{selected}")
            #st.title("Stock prediction app")
            stocks=["AAPL","GOOG","MSFT","COST","AMD","FDX","SAVA","CANO"]
            selected_stocks=st.selectbox("Select A Ticker",stocks)

            #@st.cache
            def load_data(ticker):
                data=yf.download(ticker)
                data.reset_index(inplace =True)
                data['Date'] = data['Date'].apply(lambda x: str(x.date()))
                data=data[['Date','Open','High','Low','Close']].to_numpy()
                data = json.dumps(data,cls=NumpyArrayEncoder)
                return data 
            components.html(
            """<html>
                <head>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-pie.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-exports.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-bundle.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-base.min.js"></script>
                <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-annotations.min.js"></script>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_provence.min.js"></script>
                <script src="https://cdn.anychart.com/themes/2.0.0/dark_glamour.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-base.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-ui.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-exports.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-stock.min.js"></script>
                <script src="https://cdn.anychart.com/releases/v8/js/anychart-data-adapter.min.js"></script>
                <link href="https://cdn.anychart.com/releases/v8/css/anychart-ui.min.css" type="text/css" rel="stylesheet">
                <link href="https://cdn.anychart.com/releases/v8/fonts/css/anychart-font.min.css" type="text/css" rel="stylesheet">
                <style type="text/css">
                    html, body {
                        width: 100%;
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }
                    select {
                        margin: 10px 0 0 10px;
                    }
                    button {
                        margin: 10px 0 0 5px;
                    }
                    #container {
                        position: absolute;
                        width: 100%;
                        top: 35px;
                        bottom: 0;
                    }

                </style>
                </head>
                
                
                <script>
                                anychart.onDocumentReady(function () {

                    // the data used in this sample can be obtained from the CDN
                    // https://cdn.anychart.com/csv-data/csco-daily.js
                    // create a data table using this data
                    var dataTable = anychart.data.table();
                    dataTable.addData(""" + load_data(selected_stocks) +  """);

                    // map the data
                    var mapping = dataTable.mapAs({"value": 4});

                    // create a stock chart
                    var chart = anychart.stock();

                    // create a plot on the chart
                    plot = chart.plot(0);

                    // create a line series
                    var lineSeries = plot.line(mapping);
                    lineSeries.name('"""+ selected_stocks +"""');

                    // set the chart title
                    chart.title("Handling Events");

                    // set the container id
                    chart.container("container");

                    // initiate drawing the chart
                    chart.draw();

                    // create an event listener for the annotationSelect event
                    chart.listen("annotationSelect", function(e){
                    var selectedAnnotation = e.annotation;
                    // change the annotation stroke
                    selectedAnnotation.selected().stroke("#FF0000", 3, "5 2", "round");
                    // change the chart title
                    chart.title("The " + selectedAnnotation.getType() +
                                " annotation is selected.");
                    });

                    // reset the select list to the first option
                    chart.listen("annotationDrawingFinish", function(){
                    document.getElementById("typeSelect").value = "default";
                    });
                });

                // create annotations
                function create() {
                var select = document.getElementById("typeSelect");
                plot.annotations().startDrawing(select.value);
                }

                // remove annotations
                function removeAll() {
                plot.annotations().removeAllAnnotations();
                }
                    </script>
                    </head>
                    <body>
                            <select id="typeSelect" onclick="create()">
                    <option value="default" selected disabled>Annotation Type</option>
                    <option value="andrews-pitchfork">Andrews' Pitchfork</option>
                    <option value="ellipse">Ellipse</option>
                    <option value="fibonacci-arc">Fibonacci Arc</option>
                    <option value="fibonacci-fan">Fibonacci Fan</option>
                    <option value="fibonacci-retracement">Fibonacci Retracement</option>
                    <option value="fibonacci-timezones">Fibonacci Time Zones</option>  
                    <option value="horizontal-line">Horizontal Line</option> 
                    <option value="infinite-line">Infinite Line</option>
                    <option value="line">Line Segment</option>
                    <option value="marker">Marker</option> 
                    <option value="ray">Ray</option>
                    <option value="rectangle">Rectangle</option>
                    <option value="trend-channel">Trend Channel</option>
                    <option value="triangle">Triangle</option>
                    <option value="vertical-line">Vertical Line</option>
                    </select>
                    <button onclick="removeAll()">Remove All</button>
                    <div id="container" style="width: 100%; height: 100%"></div>
                        """+selected_stocks+"""
                    </body>
                </html>
            
                """,
                height=700,
                width=1100,
                )
            
        if selected == "Stock Dashboard":
            components.html("""
                    <head>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
                    <style>
                    body {
                    background-color: hsl(218, 41%, 15%);
                    background-image: radial-gradient(
                        650px circle at 0% 0%,
                        hsl(218, 41%, 35%) 15%,
                        hsl(218, 41%, 30%) 35%,
                        hsl(218, 41%, 20%) 75%,
                        hsl(218, 41%, 19%) 80%,
                        transparent 100%
                    ),
                        radial-gradient(
                        1250px circle at 100% 100%,
                        hsl(218, 41%, 45%) 15%,
                        hsl(218, 41%, 30%) 35%,
                        hsl(218, 41%, 20%) 75%,
                        hsl(218, 41%, 19%) 80%,
                        transparent 100%
                        );
                    height: 100vh;
                    padding-left: 70px;
                    overflow-x: hidden;
                    color: #fff;
                    }
                    @media (max-width: 991.98px) {
                    body {
                        height: 100%;
                    }
                    }
                    .bg-theme {
                    background-color: hsl(218, 41%, 25%);
                    }
                    .bg-glass {
                    background: hsla(0, 0%, 100%, 0.15);
                    backdrop-filter: blur(30px);
                    }
                    .text-muted {
                    color: hsl(0, 0%, 80%) !important;
                    }
                    .text-success {
                    color: hsl(144, 100%, 40.9%) !important;
                    }
                    .text-danger {
                    color: hsl(350, 94.3%, 68.4%) !important;
                    }
                    .border-bottom {
                    border-bottom: 1px solid hsl(0, 0%, 50%) !important;
                    }
                    .badge {
                    padding: 5px 10px;
                    }
                    </style>
                        
                        
                        </head>
                                <!-- Sidenav-->
                    <nav
                        id="sidenav-4"
                        class="sidenav bg-glass opacity-100"
                        data-mdb-color="light"
                        data-mdb-mode="side"
                        data-mdb-slim="true"
                        data-mdb-slim-collapsed="true"
                        data-mdb-content="#slim-content"
                        >
                    <div class="sidenav-item mb-2">
                        <a
                        id="slim-toggler"
                        class="sidenav-link d-flex justify-content-center border-bottom"
                        >
                        <i class="fas fa-chevron-circle-right"></i>
                        </a>
                    </div>

                    <ul class="sidenav-menu">
                        <li class="sidenav-item">
                        <a class="sidenav-link">
                            <i class="fas fa-chart-area fa-fw me-3"></i
                            ><span data-mdb-slim="false">Website traffic</span></a
                            >
                        </li>
                        <li class="sidenav-item">
                        <a class="sidenav-link">
                            <i class="fas fa-chart-line fa-fw me-3"></i
                            ><span data-mdb-slim="false">Analytics</span></a
                            >
                        </li>
                        <li class="sidenav-item">
                        <a class="sidenav-link">
                            <i class="fas fa-chart-pie fa-fw me-3"></i
                            ><span data-mdb-slim="false">SEO</span></a
                            >
                        </li>
                        <li class="sidenav-item">
                        <a class="sidenav-link">
                            <i class="fas fa-money-bill fa-fw me-3"></i
                            ><span data-mdb-slim="false">Sales</span></a
                            >
                        </li>
                        <li class="sidenav-item">
                        <a class="sidenav-link">
                            <i class="fas fa-users fa-fw me-3"></i
                            ><span data-mdb-slim="false">Users</span></a
                            >
                        </li>
                    </ul>
                    </nav>
                    <!-- Sidenav-->

                    <!-- Main content -->
                    <div class="container py-5">
                    <!-- Section: Summary -->
                    <section class="mb-5">
                        <div class="row gx-xl-5">
                        <div class="col-xl-3 col-md-6 mb-4 mb-xl-0">
                            <!-- Card -->
                            <a
                            class="
                                    d-flex
                                    align-items-center
                                    p-4
                                    bg-glass
                                    shadow-4-strong
                                    rounded-6
                                    text-reset
                                    ripple
                                    "
                            href="#"
                            data-ripple-color="hsl(0, 0%, 75%)"
                            >
                            <div class="p-3 bg-theme rounded-4">
                                <i class="fas fa-users fa-lg text-white fa-fw"></i>
                            </div>

                            <div class="ms-4">
                                <p class="text-muted mb-2">Users</p>
                                <p class="mb-0">
                                <span class="h5 me-2">14 567 </span>
                                <small class="text-success text-sm"
                                        ><i class="fas fa-arrow-up fa-sm me-1"></i>13,48%</small
                                    >
                                </p>
                            </div>
                            </a>
                            <!-- Card -->
                        </div>

                        <div class="col-xl-3 col-md-6 mb-4 mb-xl-0">
                            <!-- Card -->
                            <a
                            class="
                                    d-flex
                                    align-items-center
                                    p-4
                                    bg-glass
                                    shadow-4-strong
                                    rounded-6
                                    text-reset
                                    ripple
                                    "
                            href="#"
                            data-ripple-color="hsl(0, 0%, 75%)"
                            >
                            <div class="p-3 bg-theme rounded-4">
                                <i class="fas fa-file-alt fa-lg text-white fa-fw"></i>
                            </div>

                            <div class="ms-4">
                                <p class="text-muted mb-2">Page views</p>
                                <p class="mb-0">
                                <span class="h5 me-2">51 354</span>
                                <small class="text-success text-sm"
                                        ><i class="fas fa-arrow-up fa-sm me-1"></i>23,58%</small
                                    >
                                </p>
                            </div>
                            </a>
                            <!-- Card -->
                        </div>

                        <div class="col-xl-3 col-md-6 mb-4 mb-xl-0">
                            <!-- Card -->
                            <a
                            class="
                                    d-flex
                                    align-items-center
                                    p-4
                                    bg-glass
                                    shadow-4-strong
                                    rounded-6
                                    text-reset
                                    ripple
                                    "
                            href="#"
                            data-ripple-color="hsl(0, 0%, 75%)"
                            >
                            <div class="p-3 bg-theme rounded-4">
                                <i class="fas fa-clock fa-lg text-white fa-fw"></i>
                            </div>

                            <div class="ms-4">
                                <p class="text-muted mb-2">Average time</p>
                                <p class="mb-0">
                                <span class="h5 me-2">00:04:20</span>
                                <small class="text-danger text-sm"
                                        ><i class="fas fa-arrow-down fa-sm me-1"></i>23,58%</small
                                    >
                                </p>
                            </div>
                            </a>
                            <!-- Card -->
                        </div>

                        <div class="col-xl-3 col-md-6 mb-4 mb-xl-0">
                            <!-- Card -->
                            <a
                            class="
                                    d-flex
                                    align-items-center
                                    p-4
                                    bg-glass
                                    shadow-4-strong
                                    rounded-6
                                    text-reset
                                    ripple
                                    "
                            href="#"
                            data-ripple-color="hsl(0, 0%, 75%)"
                            >
                            <div class="p-3 bg-theme rounded-4">
                                <i class="fas fa-sign-out-alt fa-lg text-white fa-fw"></i>
                            </div>

                            <div class="ms-4">
                                <p class="text-muted mb-2">Bounce rate</p>
                                <p class="mb-0">
                                <span class="h5 me-2">32.35% </span>
                                <small class="text-success text-sm"
                                        ><i class="fas fa-arrow-down fa-sm me-1"></i>23,58%</small
                                    >
                                </p>
                            </div>
                            </a>
                            <!-- Card -->
                        </div>
                        </div>
                    </section>
                    <!-- Section: Summary -->

                    <!-- Section: Table -->
                    <section class="mb-5">
                        <div class="table-responsive bg-glass shadow-4-strong rounded-6">
                        <table
                                class="
                                        table table-borderless table-hover
                                        align-middle
                                        mb-0
                                        text-white
                                        "
                                >
                            <thead class="">
                            <tr>
                                <th>Name</th>
                                <th>Title</th>
                                <th>Status</th>
                                <th>Position</th>
                                <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody class="">
                            <tr class="text-white">
                                <td>
                                <div class="d-flex align-items-center">
                                    <img
                                        src="https://mdbootstrap.com/img/new/avatars/8.jpg"
                                        alt=""
                                        style="width: 45px; height: 45px"
                                        class="rounded-circle"
                                        />
                                    <div class="ms-3">
                                    <p class="fw-bold mb-1">John Doe</p>
                                    <p class="text-muted mb-0">john.doe@gmail.com</p>
                                    </div>
                                </div>
                                </td>
                                <td>
                                <p class="fw-bold mb-1">Software engineer</p>
                                <p class="text-muted mb-0">IT department</p>
                                </td>
                                <td>
                                <span class="badge badge-success rounded-pill">Active</span>
                                </td>
                                <td>Senior</td>
                                <td>
                                <button
                                        type="button"
                                        class="btn btn-outline-white btn-sm btn-rounded"
                                        >
                                    Edit
                                </button>
                                </td>
                            </tr>
                            <tr class="text-white">
                                <td>
                                <div class="d-flex align-items-center">
                                    <img
                                        src="https://mdbootstrap.com/img/new/avatars/6.jpg"
                                        class="rounded-circle"
                                        alt=""
                                        style="width: 45px; height: 45px"
                                        />
                                    <div class="ms-3">
                                    <p class="fw-bold mb-1">Alex Ray</p>
                                    <p class="text-muted mb-0">alex.ray@gmail.com</p>
                                    </div>
                                </div>
                                </td>
                                <td>
                                <p class="fw-normal mb-1">Consultant</p>
                                <p class="text-muted mb-0">Finance</p>
                                </td>
                                <td>
                                <span class="badge badge-primary rounded-pill"
                                        >Onboarding</span
                                    >
                                </td>
                                <td>Junior</td>
                                <td>
                                <button
                                        type="button"
                                        class="btn btn-outline-white btn-rounded btn-sm fw-bold"
                                        >
                                    Edit
                                </button>
                                </td>
                            </tr>
                            <tr class="text-white">
                                <td>
                                <div class="d-flex align-items-center">
                                    <img
                                        src="https://mdbootstrap.com/img/new/avatars/7.jpg"
                                        class="rounded-circle"
                                        alt=""
                                        style="width: 45px; height: 45px"
                                        />
                                    <div class="ms-3">
                                    <p class="fw-bold mb-1">Kate Hunington</p>
                                    <p class="text-muted mb-0">kate.hunington@gmail.com</p>
                                    </div>
                                </div>
                                </td>
                                <td>
                                <p class="fw-normal mb-1">Designer</p>
                                <p class="text-muted mb-0">UI/UX</p>
                                </td>
                                <td>
                                <span class="badge badge-warning rounded-pill">Awaiting</span>
                                </td>
                                <td>Senior</td>
                                <td>
                                <button
                                        type="button"
                                        class="btn btn-outline-white btn-rounded btn-sm fw-bold"
                                        >
                                    Edit
                                </button>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
                    </section>
                    <!-- Section: Table -->

                    <!-- Section: Visualization -->
                    <section class="">
                        <div class="row gx-lg-5">
                        <div class="col-lg-6 col-md-12 mb-4 mb-lg-0">
                            <!-- Card -->
                            <div class="bg-glass shadow-4-strong rounded-6 h-100">
                            <!-- Card header -->
                            <div class="p-4 border-bottom">
                                <div class="row align-items-center">
                                <div class="col-6 mb-4 mb-md-0">
                                    <p class="text-muted mb-2">Users</p>
                                    <p class="mb-0">
                                    <span class="h5 me-2">14 567 </span>
                                    <small class="text-success text-sm"
                                            ><i class="fas fa-arrow-up fa-sm me-1"></i>13,48%</small
                                        >
                                    </p>
                                </div>

                                <div class="col-6 mb-4 mb-md-0 text-end">
                                    <a
                                    class="btn btn-outline-white btn-rounded"
                                    href="#"
                                    role="button"
                                    >Details</a
                                    >
                                </div>
                                </div>
                            </div>
                            <!-- Card header -->

                            <!-- Card body -->
                            <div class="p-4">
                                <canvas id="line-chart" height="200px"></canvas>
                            </div>
                            <!-- Card body -->
                            </div>
                            <!-- Card -->
                        </div>

                        <div class="col-lg-6 mb-4 mb-lg-0">
                            <!-- Card -->
                            <div class="bg-glass shadow-4-strong rounded-6">
                            <!-- Card header -->
                            <div class="p-4 border-bottom">
                                <div class="row align-items-center">
                                <div class="col-6 mb-4 mb-md-0">
                                    <p class="text-muted mb-2">Location</p>
                                    <p class="mb-0">
                                    <span class="h5 me-2">Top country: USA </span>
                                    </p>
                                </div>

                                <div class="col-6 mb-4 mb-md-0 text-end">
                                    <a
                                    class="btn btn-outline-white btn-rounded"
                                    href="#"
                                    role="button"
                                    >Details</a
                                    >
                                </div>
                                </div>
                            </div>
                            <!-- Card header -->

                            <!-- Card body -->
                            <div class="p-4 pb-0">
                                <div class="vector-map" id="my-map"></div>
                            </div>
                            <!-- Card body -->
                            </div>
                            <!-- Card -->
                        </div>
                        </div>
                    </section>
                    <!-- Section: Visualization -->
                    </div>
                    <!-- Main content -->
                                
                    <!-- Chart -->
                        <script type="text/javascript">
                        const ctxL = document.getElementById("line-chart").getContext("2d");
                        const gradientFill = ctxL.createLinearGradient(0, 0, 0, 290);
                        gradientFill.addColorStop(0, "hsla(218, 71%, 35%, 1)");
                        gradientFill.addColorStop(1, "hsla(218, 41%, 35%, 0.2)");

                        const dataLine = {
                        type: "line",
                        data: {
                            labels: [
                            "Monday",
                            "Tuesday",
                            "Wednesday",
                            "Thursday",
                            "Friday",
                            "Saturday",
                            "Sunday ",
                            ],
                            datasets: [
                            {
                                label: "Traffic",
                                data: [2112, 2343, 2545, 3423, 2365, 1985, 987],
                                backgroundColor: gradientFill,
                            },
                            ],
                        },
                        };

                        const chartOptions = {
                        options: {
                            legend: {
                            display: false,
                            },
                            scales: {
                            yAxes: [
                                {
                                ticks: {
                                    fontColor: "hsl(0, 0%, 80%)",
                                },
                                },
                            ],
                            xAxes: [
                                {
                                ticks: {
                                    fontColor: "hsl(0, 0%, 80%)",
                                },
                                },
                            ],
                            },
                        },
                        };

                        new mdb.Chart(
                        document.getElementById("line-chart"),
                        dataLine,
                        chartOptions
                        );
                        </script>

                        <!-- Map -->
                        <script>
                        const map = document.getElementById("my-map");

                        new VectorMap(map, {
                        readonly: true,
                        stroke: "hsl(0, 0%, 100%)",
                        fill: "hsl(219, 87%, 89%)",
                        hoverFill: "hsl(219, 87%, 20%)",
                        colorMap: [
                            { fill: "hsl(218, 71%, 45%)", regions: ["US"] },
                            { fill: "hsl(218, 71%, 65%)", regions: ["RU", "AU"] },
                            {
                            fill: "hsl(218, 71%, 75%)",
                            regions: [
                                "PL",
                                "DE",
                                "FR",
                                "GB",
                                "ES",
                                "IT",
                                "SE",
                                "NO",
                                "CZ",
                                "NL",
                                "BE",
                                "CN",
                                "IN",
                            ],
                            },
                        ],
                        });
                        </script>

                        <!-- Sidenav -->
                        <script>
                        //Initialize it with JS to make it instantly visible

                        const slimInstance = new mdb.Sidenav(
                            document.getElementById("sidenav-4")
                        );
                        slimInstance.show();

                        document.getElementById("slim-toggler").addEventListener("click", () => {
                        slimInstance.toggleSlim();
                        });
                        </script>
                            """,
                height=2000,)
            
            
        if selected == "Sentiment Analysis":
            components.html("""
            <html>
            <head>
            <script src="https://cdn.anychart.com/releases/v8/js/anychart-base.min.js"></script>
            <script src="https://cdn.anychart.com/releases/v8/js/anychart-ui.min.js"></script>
            <script src="https://cdn.anychart.com/releases/v8/js/anychart-exports.min.js"></script>
            <script src="https://cdn.anychart.com/releases/v8/js/anychart-stock.min.js"></script>
            <script src="https://cdn.anychart.com/releases/v8/js/anychart-data-adapter.min.js"></script>
            <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
            <script src="https://cdn.anychart.com/releases/v8/themes/light_turquoise.min.js"></script>
            <link href="https://cdn.anychart.com/releases/v8/css/anychart-ui.min.css" type="text/css" rel="stylesheet">
            <link href="https://cdn.anychart.com/releases/v8/fonts/css/anychart-font.min.css" type="text/css" rel="stylesheet">
            <style type="text/css">

                html,
                body,
                .wrapper {
                width: 100%;
                height: 100%;
                margin: 0;
                padding: 0;
                }

                .wrapper {
                position: relative;
                }

                .chart-column {
                position: absolute;
                top: 0
                            
                            """,height=700)
            
        if selected== "Fundamental":
            components.html("""

                            
                            """,height=1000,width=1000)
            
        if selected == "My Stocks":
            

          
            # st.markdown("<h1 style='text-align: center; color: White;'>My Portfolio</h1>", unsafe_allow_html=True)
            menu=["Create","Read","Update","Delete","About"]
            choice=st.selectbox("Menu",menu)
            st.expander("View All")
            col1,col2,col3=st.columns(3)
            
            
            with col2:
                result = view_all_data()
            
            # st.write(result)
            
            df = pd.DataFrame(result,columns=['Id','Ticker','Type','Price','Cost'])
            st.dataframe(df)
            ticker_df = df['Ticker'].value_counts().to_frame()
            # st.dataframe(ticker_df)
            ticker_df = ticker_df.reset_index()
            # st.dataframe(ticker_df)
            col1, col2 = st.columns([4, 4])
            
            col2.subheader("Portfolio Linechart")
            col2.line_chart(df)
            with col1:
                p1 = px.pie(ticker_df,names='index',values='Ticker')
                p1 = px.pie(ticker_df,names='index',values='Ticker')
                st.plotly_chart(p1,use_container_width=True)
            if choice =="Create":
                st.subheader("Add")
                col1,col2,col3= st.columns(3)
                with col1:
                    ticker=st.text_input("Ticker Symbol")
                with col2:
                    type=st.text_input("Type")
                with col3:
                    price=st.number_input("Price")
                    cost=st.number_input("Cost")
                complete=st.button("Add To Portfolio")    
                if complete:
                    add_data(ticker,type,price,cost)
                    st.success("Successfully Added Data:")
                    
            elif choice=="Update":
                result = view_all_data()
                # st.write(result)
                df = pd.DataFrame(result,columns=['Ticker','Type','Price','Cost'])
                df['Shares'] = pd.to_numeric(df['Shares'])
                print(df)
                print(df.dtypes)
                st.dataframe(df)
                # st.write(view_unique_data())
                list_of_ticker=[i[0] for i in view_all_ticker_names()]
                # st.write(list_of_ticker)
                selected_ticker= st.selectbox("Ticker to edit",list_of_ticker)
                selected_result=get_ticker(selected_ticker)
                st.write(selected_result)
                if selected_result:
                    ticker= selected_result[0][0]
                    type = selected_result[0][1]
                    price = selected_result[0][2]
                    cost = selected_result[0][3]
                    
                    col1,col2,col3= st.columns(3)
                    with col1:
                        new_ticker = st.text_input(label='ticker')
                        new_shares = st.number_input(label='shares')

                    with col2:
                        new_type = st.text_input(label='type')
                        new_date = st.date_input(label='date')
                    with col3:
                        new_price=st.number_input(label='price')
                        new_cost=st.number_input(label='cost')

                    if st.button("Update Task"):
                        edit_ticker_data(new_ticker,new_shares,new_type,new_date,new_price,new_cost,ticker,shares,type,date,price,cost)
                        st.success("Updated ::{} ::To {}".format(ticker,new_ticker))
                    with st.expander("View Updated Data"):
                        result = view_all_data()
                        # st.write(result)
                        clean_df = pd.DataFrame(result,columns=['Ticker','Type','Price','Cost'])
                        st.dataframe(clean_df)

            elif choice == "Delete":
                st.subheader("Delete")
                with st.expander("View Data"):
                    result = view_all_data()
                    # st.write(result)
                    df = pd.DataFrame(result,columns=['Ticker','Type','Price','Cost'])
                    df["Shares"] = pd.to_numeric(df["Shares"])
                    st.dataframe(df)

                unique_list = [i[0] for i in view_all_ticker_names()]
                delete_by_ticker_name =  st.selectbox("Select Ticker",unique_list)
                delete_button=st.button("Delete")
                if delete_button:
                    delete_data(delete_by_ticker_name)
                    st.warning("Deleted: '{}'".format(delete_by_ticker_name))
                with st.expander("Updated Data"):
                    result = view_all_data()
                    # st.write(result)
                    clean_df = pd.DataFrame(result,columns=['Ticker','Type','Price','Cost'])
                    st.dataframe(clean_df)
            else :
                st.error("Incorrect Password/Username")

            