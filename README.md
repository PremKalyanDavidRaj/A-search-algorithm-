## Purpose
- Examine **A* search algorithm** implementation, by Andreas Soularidis https://github.com/AndreasSoularidis/medium_articles/tree/main/AStarAlgorithm 
    - This is an example of an **AI symbolic system**
- Undertand how the code in this lab implements the A* algorithm specified in the pseudocode https://plainenglish.io/blog/a-algorithm-in-python  
- Create two new, very simple testing examples that you can trace by hand
- Learn about **linting Pythonn in VS Code** with flake8 and pylint: https://code.visualstudio.com/docs/python/linting 
- Consolidate your understanding and practice with **conda virtual environment**  and **VS Code tools**. 

## Guidelines
See **Prepare VS Code for Lab Development** resource in the **"How To" Resources** module in Canvas. It helps you:
- Get the codebase from GitHub org associated with this class 
- Clone the remote repo to lab2 local repo in the *course root directory*

## Requirements
### Examine, run, and improve the codebase
- Examine all three Python modules: graph.py, a_star.py, and main.py
- Run main.py in two wayd
    - In the VS Code integrated terminal set up to `bash` by running `python main.py`
    - From the Run button

Answer the following questions in a new **UNDERSTAND.md** file:
- What Python interpreter are you running? 
- Do we need a conda virtual environment? Justify your answer. 
- VS Code reports **problems** for each of the Python module.  
    - How many problems are reported for each moduel? 
    - What generates these problems and wny?
- How can the problems be fixed? 
    - Describe your solution to fixing these problems. 
- What categories of changes have you or VS Code made to the code to fix the problems? 

### Extend testing
Add two new simpler test cases:
- Refactor `main.py` module into four functions
    - `graph13()` function has the existing test case of 13 nodes, including staring and terminal nodes. 
    - two additional functions with fewer nodes representing much simpler maze examples, as discussed in class. 
        - One test case has a solution
        - One test case does not have a solution
    - Refactored `main()` that calls the three test cases. 
- Use the debugger on the simpler test cases to better understand how the implementation works. 
- Document all three test cases in a new **TESTING.md** file
    - Collaborate in Discord to share easy ways of including images in a Markdown to show the maze configuration of the three test cases.
    - For each test
        - Have a representation of the maze (image)
        - Include the shortest path the A* algorithm finds

### Challenges
- Modify the code such that the implementation produces a trace that shows the content of the `opened` and `closed` lists at each step through the search process. 
- Modify `search()` method of `AStar` class to take a 2nd parameter, let's call it `debug`.
    - If `search()` is called with `True` argument for `debug`, then the implementation produces the trace.
    - Otherwise, it does not. 
- Modify `main()` function in `main.py` such that the trace is shown only for the two new test cases. 

