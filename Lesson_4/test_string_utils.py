import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("string, result", [("skypro", "Skypro"), ("привет", "Привет"), ("123", "123"),])                 

def test_capitilize(string, result):
    utils = StringUtils()
    assert utils.capitilize(string) == result
    
@pytest.mark.parametrize("string, result", [(" skypro", "skypro"), ("   привет", "привет"), ("  @!", "@!"),])                 

def test_trim(string, result):
    utils = StringUtils()
    assert utils.trim(string) == result

@pytest.mark.parametrize("string, delimeter, result", [
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),     
    ("*@$@&", "@", ["*", "$", "&"]),
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)   
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("банан", "б", True),
    ("гвоздь", "д", True),
    ("мир ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    (" ", " ", True),
    ("Москва", "м", False),
    ("привет", "ё", False),
    ("кот", "№", False),
    ("", "з", False),
    ("12345", "I", False),
    ("hello", "", True)])

def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result
    

def test_delete_symbol():
    assert utils.delete_symbol("skypro", "k") == "sypro"
    assert utils.delete_symbol("skypro", "pro") == "sky"
    assert utils.delete_symbol("skypro", "x") == "skypro"
    assert utils.delete_symbol("skypro", "") == "skypro"
    assert utils.delete_symbol("", "") == ""
    assert utils.delete_symbol("", "y") == ""
   

def test_starts_with():
    assert utils.starts_with("skypro", "s") == True
    assert utils.starts_with("skypro", "p") == False
    assert utils.starts_with("", "a") == False
    

def test_end_with():
    assert utils.end_with("skypro", "o") == True
    assert utils.end_with("skypro", "y") == False
    assert utils.end_with("", "a") == False
    

def test_is_empty():
    assert utils.is_empty("") == True
    assert utils.is_empty("skypro") == False
    assert utils.is_empty("   ") == True
     