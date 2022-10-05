import sqlite3
import streamlit as st
from datetime import date
import json
import csv
from json import JSONEncoder
import numpy as np
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
# from transformers import BlenderbotTokenizer
# from transformers import BlenderbotForConditionalGeneration


user_id = 0

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
st.set_page_config(page_title="Fintero", page_icon=":stock_chart:", layout="wide" ,)
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True) 
#  Login Page
import sqlite3
conn=sqlite3.connect('data.db')
conn=sqlite3.connect('data.db')
c=conn.cursor()
st.cache(allow_output_mutation=True)
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, password TEXT);')
create_usertable()
st.cache(allow_output_mutation=True)
def create_stocks_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS stocks_usertable(user_id INTEGER, stock_id INTEGER, shares INTEGER, date DATE ,PRIMARY KEY (user_id, stock_id,date,shares),FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,FOREIGN KEY (stock_id) REFERENCES stock(stock_id) ON DELETE CASCADE) ;')
create_stocks_usertable()
st.cache(allow_output_mutation=True)
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stocktable(stock_id INTEGER PRIMARY KEY AUTOINCREMENT,ticker TEXT, type TEXT, price INTEGER, cost INTEGER);')
create_table()
st.cache(allow_output_mutation=True)
def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username, password) VALUES(?,?);',(username,password))
    conn.commit()
st.cache(allow_output_mutation=True)
def delete_userdata():
    c.execute('DELETE FROM usertable WHERE username="{}"'.format(username))
    conn.commit()
st.cache(allow_output_mutation=True)
def login_user(username,password):
    global user_id
    c.execute('SELECT * FROM  usertable WHERE username=? AND password=?;',(username,password))
    data = c.fetchall()
    if(len(data) > 0):
        user_id = data[0][0]
    return data
st.cache(allow_output_mutation=True)
def view_all_stocks_user():
    c.execute('SELECT * FROM  stocks_usertable WHERE  stocks_usertable.user_id=' + str(user_id) +';')
    data = c.fetchall()
    return data


st.cache(allow_output_mutation=True)
def add_stocks_usertable(user_id,stock_id,shares,date):
    c.execute('INSERT INTO stocks_usertable(user_id,stock_id,shares,date) VALUES(?,?,?,?);',(user_id,stock_id,shares,date))
    conn.commit()
    
st.cache(allow_output_mutation=True)
def delete_stocks_usertable(ticker):
    c.execute('DELETE FROM stocks_usertable WHERE ticker="{}"'.format(ticker))
    conn.commit()
# def view_all_stocks_usertable():
#     c.execute('SELECT * FROM  stocks_usertable JOIN stocktable ON stocks_usertable.stock_id = stocktable.stock_id JOIN usertable ON stocks_usertable.user_id=usertable.user_id WHERE stocks_usertable.user_id=usertable.user_id  ;')
#     data = c.fetchall()
#     return 

st.cache(allow_output_mutation=True)
def seen_by_person():
    sql='SELECT * FROM stocks_usertable JOIN stocktable ON stocks_usertable.stock_id = stocktable.stock_id JOIN usertable ON stocks_usertable.user_id=usertable.user_id WHERE  stocks_usertable.user_id=' + str(user_id) +';'
    c.execute(sql)
    data = c.fetchall()
    return data
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())
# print(view_all_stocks_usertable())

global df
global msft
st.cache(allow_output_mutation=True)
def add_data(ticker,type,price,cost):
    c.execute('INSERT INTO stocktable(ticker,type,price,cost) VALUES(?,?,?,?);',(ticker,type,price,cost))
    conn.commit()
    
st.cache(allow_output_mutation=True)
def delete_data(ticker):
    c.execute('DELETE FROM stocktable WHERE ticker="{}"'.format(ticker))
    conn.commit()
    
st.cache(allow_output_mutation=True)
def view_all_data():
    c.execute('SELECT * FROM  stocktable;')
    data = c.fetchall()
    return data

st.cache(allow_output_mutation=True)
def view_all_ticker_names():
    c.execute('SELECT DISTINCT ticker FROM stocktable;')
    data = c.fetchall()
    return data
st.cache(allow_output_mutation=True)
def get_ticker(ticker):
    c.execute('SELECT * FROM  stocktable WHERE ticker="{}"'.format(ticker))
    data = c.fetchall()
    return data

def edit_ticker_data(new_ticker,new_type,new_price,new_cost,ticker,type,price,cost):
    c.execute("UPDATE stocktable SET ticker =?,type=?,price=? ,cost=?  WHERE ticker =? and type=? and price=? and cost=? ",(new_ticker,new_type,new_price,new_cost,ticker,type,price,cost))
    conn.commit()
    data = c.fetchall()
    return data

# def delete_table():
#     c.execute('DROP TABLE IF EXISTS stocktable;')
#     conn.commit()
# delete_table()
text2=st.empty()
text4=st.empty()
with text2.container():
    menu=["Login","Register"]
    choice=st.selectbox("Choose One",menu)


# global msft
# def delete_usertable():
#                 c.execute('DROP TABLE IF EXISTS usertable;')
#                 conn.commit()
# delete_usertable()
if choice == "Register" :
    
    st.session_state.new_user=st.text_input("Set Your Username")
    st.session_state.new_password= st.text_input("Set Your Password",type='password')
    to_register=st.button("Register")
    if to_register:
        add_userdata(st.session_state.new_user,st.session_state.new_password)
        st.success("Welcome Onboard {}".format(st.session_state.new_user))
        st.info("Go to login Menu to login")
   
elif choice == "Login" :
    with text4.container():
        st.session_state.username= st.text_input("Username")
        st.session_state.password= st.text_input("password",type='password')
        submit = st.button('Submit')

        result = login_user( st.session_state.username,st.session_state.password)



    if result :
        text4.empty()
        text2.empty()
        st.sidebar.write(f'{st.session_state.username}')
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
            selected = option_menu("Home", ["My Stocks","Charts","News","Top Picks","Trend Prediction"],  
                icons=['house', 'gear', 'gear', 'gear', 'gear'], menu_icon="cast", default_index=1)

        if selected == "Charts":
            stocks=["AAPL","GOOG","MSFT","COST","AMD","FDX","SAVA","CANO"]
            selected_stocks=st.selectbox("Select A Ticker",stocks)
            tab1, tab2,tab3,tab4,tab5 = st.tabs(["📈 Charts", "🗃 Stock Info","📰 Fundamentals","🔍Pattern Finder","🔮 Prediction"])
            @st.cache
            def load_data(ticker):
                data=yf.download(ticker)
                data.reset_index(inplace =True)
                data['Date'] = data['Date'].apply(lambda x: str(x.date()))
                data=data[['Date','Open','High','Low','Close']].to_numpy()
                data = json.dumps(data,cls=NumpyArrayEncoder)
                return data 
            with tab1.subheader("Charts"):
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
                    )
            with tab2.subheader("Stock Info"):
                def get_info():
                    msft= yf.Ticker("MSFT")
                    return msft.info
                components.html("""
                <!DOCTYPE>
                <html>
                <head></head>
                <body>
                <h1>Hello</h1>
                <div id="info"></div>
                <script>
                
                let obj="""+ str(get_info()) + """;
                let my_json=JSON.stringify(obj);
                let parsed_obj=JSON.parse(my_json);
                
                document.getElementById("info").innerHTML +=  "Converting JSON to HTML <br><br>" + "Sector:" + parsed_obj.sector  + "Full Time Employees: " +parsed_obj.fullTimeEmployees +"Business Summary: " + parsed_obj.longBusinessSummary +"Country: " + parsed_obj.country;
            
                </script>    
                </body>
                <html>          
                                
                               """,height=1000)
            with tab3.subheader("News"):
                tab3.write("News")
                # from yahoostats.evaluator import combine_stats
                # from selenium import webdriver

                # from webdriver_manager.chrome import ChromeDriverManager
                # from webdriver_manager.core.utils import ChromeType

                # driver = webdriver.Chrome(ChromeDriverManager(
                #     chrome_type=ChromeType.CHROMIUM).install())

                # # driver.get("http://www.python.org")

                # stocklist = ['GOOGL', 'TSLA', 'AMD']
                # combine_stats(stocklist)
                # driver.close()
                import yfinance as yf

                
                # msft.institutional_holders
                # msft.recommendations
                
                # get stock info
                # msft.info
                # msft.actions()
                # hist = msft.get_history(period=yf.TimePeriods.Quarter)

            with tab4.subheader("Candlestick Pattern Finder"):
                tab4.write("Candlestick Pattern Finder")
            
                from Stockie.stockie import stockie
                a = stockie(['UNVR.JK','AAPL','AMZN.BA'])
                df = a.find_pattern()['AAPL']
                df=a.get_candlestick_report()
                st.dataframe(df)
                print(df)
                print(df)
                print(df)
                print(df)
                print(df)
                print(df)

            with tab5.subheader("Stock Prediction"):
               pass
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
      
            
        if selected== "Fundamental":
            components.html("""

                            
                            """,height=1000,width=1000)
            
        if selected == "My Stocks":
            

            
            # st.markdown("<h1 style='text-align: center; color: White;'>My Portfolio</h1>", unsafe_allow_html=True)
            menu=["Create","Add","Read","Update","Delete"]
            choice=st.selectbox("Menu",menu)
            st.expander("View All")
            col1,col2,col3=st.columns(3)
            
            
            with col2:
                result = view_all_data()
            
            # st.write(result)
            
            df = pd.DataFrame(result,columns=['stock_id','ticker','type','price','cost'])
            st.dataframe(df)
            ticker_df = df['ticker'].value_counts().to_frame()
            # st.dataframe(ticker_df)
            ticker_df = ticker_df.reset_index()
            # st.dataframe(ticker_df)
            col1, col2 = st.columns([4, 4])
            
            col2.subheader("Portfolio Linechart")
            col2.line_chart(df)
            with col1:
                p1 = px.pie(ticker_df,names='index',values='ticker')
                p1 = px.pie(ticker_df,names='index',values='ticker')
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
                complete=st.button("Add Stock")   
                person=seen_by_person()
                if complete:
                    add_data(ticker,type,price,cost)
                if complete and person:
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
                        edit_ticker_data(new_ticker,new_shares,new_type,new_date,new_price,new_cost,ticker,type,price,cost)
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
            elif choice=="Add":
                added=view_all_stocks_user()
                df = pd.DataFrame(added,columns=['user_id','stock_id','shares','date'])
                st.dataframe(df)
                ticker_df = df['shares'].value_counts().to_frame()
                # st.dataframe(ticker_df)
                ticker_df = ticker_df.reset_index()
                # st.dataframe(ticker_df)
                
                col1,col2= st.columns(2)
                with col1:
                    stock_id=st.number_input("stock_id")
                
                with col2:
                    shares=st.number_input("shares")
                    date=st.date_input("date")
                
                portfolio=st.button("Add To Portfolio")   
                seen=seen_by_person()
                if portfolio:
                    add_stocks_usertable(user_id,stock_id,shares,date)
                if portfolio and seen:
                    st.success("Successfully Added Data:")
        if selected=="Top Picks":
            st.write("can you see me")
            def render_html():
                msft = yf.Ticker("MSFT")
                df=msft.recommendations
                df=df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=None, escape=True, notebook=False, border=None, table_id=None, render_links=False, encoding=None)
                return df
            components.html("""
            <!DOCTYPE>
            <html>
            <head></head>
            <body>"""+ render_html() +""""
            </body></html>""",height=1000)
        if selected =="News":
            st.title="News"
            def get_news():
                msft= yf.Ticker("MSFT")
                print(msft.news)
                return msft.news
            components.html("""
             <!DOCTYPE>
            <html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <style>
            #title{
                border:1px solid black;
            }
            
            </style>
            </head>
            <body>
            <div class="container"><div id="title"> </div>
            </div>
            <script>
            let obj="""+ str(get_news()) + """;
            let my_json=JSON.stringify(obj);
            let parsed_objs=JSON.parse(my_json);
            for (parsed_obj of parsed_objs){
                document.getElementById('title').innerHTML +=   "<br><br><div>Title: <br><div>" + parsed_obj.title +"<br>Publisher: " + parsed_obj.publisher+"<hr>" ;
                
                /*+ "Full Time Employees: " + parsed_obj.fullTimeEmployees +"Business Summary: " + parsed_obj.longBusinessSummary*/
               }
            </script>    
            </body>
            <html>          
                            
                            """,height=1000)
        if selected =="Trend Prediction":
            from keras import *
            from keras.layers import Dense,Dropout, LSTM
            from keras.models import Sequential
            import pandas_datareader as data
            from matplotlib import *
            import matplotlib.pyplot as plt
            from sklearn.preprocessing import MinMaxScaler
            start='2010-01-01'
            end='2022-01-01'
            df=data.DataReader('AAPL','yahoo',start,end)
            df=df.reset_index()
            df=df.drop(['Date','Adj Close'],axis=1)
            
            st.subheader('Closing Price vs Time Chart 100MA')
            ma100=df.Close.rolling(100).mean()
            fig=plt.figure(figsize=(12,6))
            plt.plot(ma100,'r')
            plt.plot(df.Close)
            st.pyplot(fig)
            
            st.subheader('Closing Price vs Time Chart 200MA')
            # ma100=df.Close.rolling(100).mean()
            ma200=df.Close.rolling(200).mean()
            fig3=plt.figure(figsize=(12,6))
            # plt.plot(ma100,'r')
            plt.plot(ma200,'r')
            plt.plot(df.Close)
            st.pyplot(fig3)
            
            data_training =pd.DataFrame(df['Close'][0:int(len(df)*0.75)])
            data_testing =pd.DataFrame(df['Close'][0:int(len(df)*0.75):int(len(df))])
            scaler=MinMaxScaler(feature_range=(0,1))
            data_training_array=scaler.fit_transform(data_training)
            x_train=[]
            y_train=[]
            for i in range(100,data_training_array.shape[0]):
                x_train.append(data_training_array[i-100:i])
                y_train.append(data_training_array[i,0])
            x_train,y_train=np.array(x_train),np.array(y_train)
            # Machine Learning Model
            st.cache(allow_output_mutation=True)
            def model():
                model=Sequential()
                model.add(LSTM(units= 50,activation='relu',return_sequences=True,input_shape=(x_train.shape[1],1)))
                model.add(Dropout(0.2))
                model.add(LSTM(units= 60,activation='relu',return_sequences=True))
                model.add(Dropout(0.3))
                
                model.add(LSTM(units= 80,activation='relu',return_sequences=True))
                model.add(Dropout(0.4))
                
                model.add(LSTM(units= 120,activation='relu'))
                model.add(Dropout(0.5))
                model.add(Dense(units=1))
                
                model.compile(optimizer="adam",loss="mean_squared_error")
                model.fit(x_train,y_train,epochs=10)
                
            model()
            past_100_days= data_training.tail(100)
            final_df= past_100_days.append(data_testing,ignore_index=True)
            input_data=scaler.fit_transform(final_df)   
            x_test=[]
            y_test=[]
            for i in range(100,input_data.shape[0]):
                x_test.append(input_data[i-100:i])
                y_test.append(input_data[i,0])
            x_test,y_test=np.array(x_test),np.array(y_test)   
            y_predicted=model.predict(x_test)
            scaler=scaler.scale_
            scale_factor=1/scaler[0]
            y_predicted=y_predicted* scale_factor
            y_test=y_test*scale_factor
            
            st.subheader('Predictions vs Original')
            fig2 =plt.figure(figsize=(12,6))
            plt.plot(y_test,'b',label='Original Price ')
            plt.plot(y_predicted,'r',label='Predicted Price ')
            plt.xlabel('Time')
            plt.xlabel('Price')
            plt.legend()
            st.pyplot(fig2)