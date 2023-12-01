import argparse
import pytest
import json


def construct(file_str: str) -> dict[str, dict[str, float]]:
    file_str=file_str.lower()
    all_words=file_str.split(" ")
    newdic={}
    newdic['*']={}
    for word in all_words:
        currentstate='*'
        newstate=''
        for char in word:
            if newstate+char not in newdic[currentstate]:
                newdic[newstate+char]={}
                newdic[currentstate][newstate+char]=1
            else:
                newdic[currentstate][newstate+char]+=1
            newstate=newstate+char
            currentstate=newstate
        if newstate+'*' not in newdic[currentstate]:
            newdic[currentstate][newstate+'*']=1
        else:
            newdic[currentstate][newstate+'*']+=1

    for l in newdic:
        count=0
        for i in newdic[l]:
            count+=newdic[l][i]

        for i in newdic[l]:
            newdic[l][i]=newdic[l][i]/count       
                 
    return newdic   


def main():
    """
    The command for running is `python pfsa.py text.txt`. This will generate
    a file `text.json` which you will be using for generation.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Name of the text file")
    args = parser.parse_args()

    with open(args.file, "r") as file:
        contents = file.read()
        output = construct(contents)

    name = args.file.split(".")[0]

    with open(f"{name}.json", "w") as file:
        json.dump(output, file)


if __name__ == "__main__":
    main()


STRINGS = ["A cat", "A CAT", "", "A", "A A A A","harshit harsh auto automatic automata automation autoh autoha autob","harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit automata"
           ,"harshit harshit harshit harshit harshit harshit harshit harshit harshit harshit aggarwal aggarwal aggarwal aggarwal aggarwal aggarwal aggarwal aggarwal aggarwal aggarwal automata automata automata automata automata"
           ,"abcd abe abf abg ac ad ae ba ba ba ba ba ba ba"]
DICTIONARIES = [
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
    {"*": {"h": 0.2222222222222222, "a": 0.7777777777777778}, "h": {"ha": 1.0}, "ha": {"har": 1.0}, "har": {"hars": 1.0}, "hars": {"harsh": 1.0}, "harsh": {"harshi": 0.5, "harsh*": 0.5}, "harshi": {"harshit": 1.0}, "harshit": {"harshit*": 1.0}, "a": {"au": 1.0}, "au": {"aut": 1.0}, "aut": {"auto": 1.0}, "auto": {"auto*": 0.14285714285714285, "autom": 0.42857142857142855, "autoh": 0.2857142857142857, "autob": 0.14285714285714285}, "autom": {"automa": 1.0}, "automa": {"automat": 1.0}, "automat": {"automati": 0.6666666666666666, "automata": 0.3333333333333333}, "automati": {"automatic": 0.5, "automatio": 0.5}, "automatic": {"automatic*": 1.0}, "automata": {"automata*": 1.0}, "automatio": {"automation": 1.0}, "automation": {"automation*": 1.0}, "autoh": {"autoh*": 0.5, "autoha": 0.5}, "autoha": {"autoha*": 1.0}, "autob": {"autob*": 1.0}},
    {"*": {"h": 0.9950248756218906, "a": 0.004975124378109453}, "h": {"ha": 1.0}, "ha": {"har": 1.0}, "har": {"hars": 1.0}, "hars": {"harsh": 1.0}, "harsh": {"harshi": 1.0}, "harshi": {"harshit": 1.0}, "harshit": {"harshit*": 1.0}, "a": {"au": 1.0}, "au": {"aut": 1.0}, "aut": {"auto": 1.0}, "auto": {"autom": 1.0}, "autom": {"automa": 1.0}, "automa": {"automat": 1.0}, "automat": {"automata": 1.0}, "automata": {"automata*": 1.0}},
    {"*": {"h": 0.4, "a": 0.6}, "h": {"ha": 1.0}, "ha": {"har": 1.0}, "har": {"hars": 1.0}, "hars": {"harsh": 1.0}, "harsh": {"harshi": 1.0}, "harshi": {"harshit": 1.0}, "harshit": {"harshit*": 1.0}, "a": {"ag": 0.6666666666666666, "au": 0.3333333333333333}, "ag": {"agg": 1.0}, "agg": {"agga": 1.0}, "agga": {"aggar": 1.0}, "aggar": {"aggarw": 1.0}, "aggarw": {"aggarwa": 1.0}, "aggarwa": {"aggarwal": 1.0}, "aggarwal": {"aggarwal*": 1.0}, "au": {"aut": 1.0}, "aut": {"auto": 1.0}, "auto": {"autom": 1.0}, "autom": {"automa": 1.0}, "automa": {"automat": 1.0}, "automat": {"automata": 1.0}, "automata": {"automata*": 1.0}},
    {"*": {"a": 0.5, "b": 0.5}, "a": {"ab": 0.5714285714285714, "ac": 0.14285714285714285, "ad": 0.14285714285714285, "ae": 0.14285714285714285}, "ab": {"abc": 0.25, "abe": 0.25, "abf": 0.25, "abg": 0.25}, "abc": {"abcd": 1.0}, "abcd": {"abcd*": 1.0}, "abe": {"abe*": 1.0}, "abf": {"abf*": 1.0}, "abg": {"abg*": 1.0}, "ac": {"ac*": 1.0}, "ad": {"ad*": 1.0}, "ae": {"ae*": 1.0}, "b": {"ba": 1.0}, "ba": {"ba*": 1.0}}
    

]


@pytest.mark.parametrize("string, pfsa", list(zip(STRINGS, DICTIONARIES)))
def test_output_match(string, pfsa):
    """
    To test, install `pytest` beforehand in your Python environment.
    Run `pytest pfsa.py` Your code must pass all tests. There are additional
    hidden tests that your code will be tested on during VIVA.
    """
    result = construct(string)
    assert result == pfsa