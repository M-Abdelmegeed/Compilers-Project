from ast import keyword
from asyncio.windows_events import NULL
from cProfile import label
import re
from tokenize import String
from distutils.log import error
from automata.fa.dfa import DFA
from numpy import number
import networkx as nx
import matplotlib.pyplot as plt
import graphviz
import pydot
import re

file = open("else.txt")

operators = {'=':'EQUAL',':=' : 'ASSIGN','+' : 'PLUS','-' : 'MINUS','/' : 'DIV','*' : 'MULT','<' : 'LESSTHAN','>' : 'GREATERTHAN' }
operators_key = operators.keys()

data_type = {'int' : 'INTEGER TYPE', 'float': 'FLOATING POINT' , 'char' : 'CHARACTER TYPE', 'long' : 'LONG INT' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'COLON', ';' : 'SEMI-COLON', '.' : 'DOT' , ',' : 'COMMA' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {"ID":['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', "n", "o", "p", "q", "r", "s", 't', 'u', 'v', "x", 'y','z','xyz','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', "N", "O", "P", "Q", "R", "S", 'T', 'U', 'V', "X", 'Y','Z','XYZ']}
identifier_key = identifier.keys()
identifier_values=identifier.values()
arrval=[]
for value in identifier_values:
    arrval=value


key_words={'if':'IF', 'then':'THEN', 'end':'END', 'else':'ELSE','read':'READ', 'write':'WRITE', 'until':'UNTIL', 'repeat':'REPEAT'}
key_word_keys=key_words.keys()


a_list = list(range(1, 10000))
a_list=str(a_list)
numbers={"NUMBER":a_list}
number_values=numbers.values()
arrvalnum=[]
for value in number_values:
    arrvalnum=value
for i in range(0, len(arrvalnum)):
    if arrvalnum[i]=="":
        arrvalnum.remove(arrvalnum[i])
dataFlag = False

a=file.read()
tokenType=[];
count=0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)
    tokens=line.split(' ')
    while("" in tokens) :
        tokens.remove("")
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in operators_key:
            print('<' + token + " , " + operators[token] + '>')
            tokenType.append(operators[token]);
        if token in data_type_key:
            print("datatype is", data_type[token])
            tokenType.append(data_type[token]);
        if token in punctuation_symbol_key:
            print ('<' + token + " , " + punctuation_symbol[token] + '>')
            tokenType.append(punctuation_symbol[token]);
        if token in arrval:
            print('<' + token + " , " + "ID" + '>')
            tokenType.append("ID");
        if token in arrvalnum:
            print ('<' + token + " , " + "NUMBER" + '>')
            tokenType.append("NUMBER");
        if token in key_words:
            print ('<' + token + " , " + key_words[token] + '>' )
            tokenType.append(key_words[token]);
                  
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
# print(tokenType);

# arr=['0','01', '011']
# arr2=['0', '1', '1', '1']
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5','q6', 'q7', 'q8', 'dead' },
    input_symbols={'IF', 'ID', 'ASSIGN', 'THEN', 'SEMI-COLON', 'NUMBER', 'ELSE', 'END'},
    transitions={
        'q0': {'IF': 'q1', 'ID': 'dead', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'q1': {'IF': 'dead', 'ID': 'q2', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'q2', 'ELSE':'dead', 'END': 'dead'},
        'q2': {'IF': 'dead', 'ID': 'dead', 'ASSIGN':'dead', 'THEN': 'q3', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'q3': {'IF': 'dead', 'ID': 'q4', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'q4': {'IF': 'dead', 'ID': 'dead', 'ASSIGN':'q5', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'q5': {'IF': 'dead', 'ID': 'q6', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'q6', 'ELSE':'dead', 'END': 'dead'},
        'q6': {'IF': 'dead', 'ID': 'dead', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'q7', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'q7': {'IF': 'dead', 'ID': 'q4', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'q3', 'END': 'q8'},
        'q8': {'IF': 'dead', 'ID': 'dead', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
        'dead': {'IF': 'dead', 'ID': 'dead', 'ASSIGN':'dead', 'THEN': 'dead', 'SEMI-COLON': 'dead', 'NUMBER': 'dead', 'ELSE':'dead', 'END': 'dead'},
    },
    initial_state='q0',
    final_states={'q8', 'dead'}
)
states_list=[]

# G=dfa._make_graph
# print(G)
print("Final State: " + dfa.read_input(tokenType))

states_list=(list(dfa.read_input_stepwise(tokenType)))

print("Tokens:", end=" ")
for token in tokenType:
    print(token +" ", end=" ")
    
print("\nState sequence: ", end=" ")
for state in states_list:
    print(state +" ", end=" ")
