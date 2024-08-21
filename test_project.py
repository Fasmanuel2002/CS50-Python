from project import *
from unittest.mock import patch


stocks = {
        "Disney": 83.48,
        "Amazon": 144.85,
        "Tesla": 271.30,
        "Microsoft": 336.06,
        "Meta": 305.06,
        "Apple": 174.21,
        "AT&T": 14.62,
        "Nike": 96.13,
        "Sony": 84.43,
        "Dell": 70.45,
        "Google": 137.50,
        "Baba": 87.64,
        "Starbucks": 96.93,
        "NVDA": 454.85,
        "Paypal": 63.44,
    }
    
def test_buystocks():
    user_input = ["Apple", "2", "No"]
    
    with patch("builtins.input", side_effect=user_input):
        total_cost = buystocks(stocks)
    
    assert total_cost == 348.42
    
    user_input = ["Tesla", "1", "No"]
    with patch("builtins.input", side_effect = user_input):
        total_cost = buystocks(stocks)
    assert total_cost == 271.30   
    
 
def test_comparestocks():
    
    user_input = ["Google/Tesla"]
    with patch("builtins.input", side_effect=user_input):
        division = comparestocks(stocks)
    assert division  == "The value of Google $137.5 is like this compared to Tesla $271.3 is 0.51"
    
    
    user_input = ["Microsoft/Apple"]
    with patch("builtins.input", side_effect = user_input):
        division = comparestocks(stocks)
    assert division  == "The value of Microsoft $336.06 is like this compared to Apple $174.21 is 1.93"

def test_stockdiagrams():
    user_input = ["TSLA"]
    with patch("builtins.input", side_effect = user_input):
        stocksdiagrams()
    user_input = ["DIS"]
    with patch("builtins.input", side_effect = user_input):
        stocksdiagrams()
        
def test_newstock():
    user_input = ["DIS"]
    with patch("builtins.input", side_effect = user_input):
        stocksnews()
    user_input = ["TSLA"]
    with patch("builtins.input", side_effect = user_input):
        stocksnews()
    
def test_main():
    user_input = ["x"]
    with patch("builtins.input", side_effect = user_input):
        main()
        exit