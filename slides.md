[comment]: # (This presentation was made with markdown-slides)
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)
[comment]: # (Compile this presentation with the command below)
[comment]: # (mdslides slides.md --include media)

[comment]: # (Set the theme:)
[comment]: # (THEME = white)
[comment]: # (CODE_THEME = base16/zenburn)
[comment]: # (The list of themes is at https://revealjs.com/themes/)
[comment]: # (The list of code themes is at https://highlightjs.org/)

[comment]: # (Pass optional settings to reveal.js:)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)
[comment]: # (Other settings are documented at https://revealjs.com/config/)

# Pandas

[comment]: # (A comment starting with three or more !!! marks a slide break.)
[comment]: # (!!!)

![Panda cub](media/panda_cub.jpeg)

Not the kind of Pandas we are going to talk about.

[comment]: # (!!!)

![Pandas Library](media/pandas_logo.svg)

Pandas - Python's Data Analysis Library

[comment]: # (!!!)

###### First a brief history lesson...

[comment]: # (!!!)

- 2007 - Applied Quantitative Research Captial Management (AQR)
- They're a hedge fund and managed many billions of dollars at that time

[comment]: # (!!!)

![Wes McKinney](media/wes-2017-01-12-small.png)<!-- .element: style="height:50vh; max-width:80vw;" -->

AQR hires Wes McKinney

[comment]: # (!!!)

- Wes went to MIT for Mathematics
- Found all AQR's hard finance problems awful to do with the tooling available
    - More time spent on the data than the math
- Did not like Excel and R (a Statistical programming language)
- Immediately fell in love with Python

[comment]: # (!!!)

- Wes builds internal tooling at AQR to make his own and everyone else's lives easier
- Somehow convinces AQR to open source it (?!)
- Wes eventually leaves AQR but keeps working on Pandas and related tooling to present

[comment]: # (!!!)

###### What is the big deal then?

[comment]: # (!!!)

- Jump started a revolution in data analysis of useful tools in an approachable language
- Pandas uses Python as glue code to bring together powerful and high performance tools in easier to use ways
- Treats data in-memeory like a SQL table, using something called a DataFrame
- Named from **pan**el **da**ta in statistics

[comment]: # (!!!)

![DataFrame](media/dataframe.svg)

column => pandas.Series

Series are the secret sauce allowing a whole ton of fast, effective manipulations and calculations

[comment]: # (!!!)

###### The words "fast" and "Python" together?

I have *doubts* about that one

[comment]: # (!!!)

Series (and Pandas in general) makes heavy use of NumPy

NumPy is numerical computing dark magic in Python

[comment]: # (!!!)

###### What does "fast" mean then?

[comment]: # (!!!)

PYTHON LOOP EXAMPLES

[comment]: # (!!!)

PYTHON C EXTENSION LOOP EXAMPLES

[comment]: # (!!!)

NUMPY EXAMPLES

[comment]: # (!!!)

TABLE OF TEST RESULTS

[comment]: # (!!!)

How SkillShark got into using it

[comment]: # (!!!)

Examples of our usage

[comment]: # (!!!)

Pros and Cons

[comment]: # (!!!)

Getting Started & Resources

- Wes' Book
- Pandas Docs
- Jupyter
- Datalore & DataSpell
- Further Works
    - Modin
    - Dask
    - Polars
    - Arrow
    - Vaex

[comment]: # (!!!)

Questions?
