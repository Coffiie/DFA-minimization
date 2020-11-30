from pythomata import SimpleDFA
import base64
import json


def _getTransitionFunction(states,list):
    dict = {}
    count = 0
    for item in list:
        dict[states[count]] = item
        count += 1
    return dict

def serverGateway(alphabet, states, initialState, acceptingState, transitionList):
    transitionFunction = _getTransitionFunction(states, transitionList)
    alphabet = set(alphabet)
    states = set(states)
    acceptingState = set(acceptingState)

    dfa = SimpleDFA(states, alphabet, initialState, acceptingState, transitionFunction)

    initialDFAGraph = dfa.to_graphviz()
    initialDFAGraph.render("initial",view=False,format='png')

    minimizedDFA = dfa.minimize()
    graph = minimizedDFA.trim().to_graphviz()
    graph.render("graph",view=False,format='png')

    with open("initial.png","rb") as image_file:
        initialGraphEncoded = base64.b64encode(image_file.read())

    with open("graph.png","rb") as image_file:
        finalGraphEncoded = base64.b64encode(image_file.read())

    return [initialGraphEncoded,finalGraphEncoded]
