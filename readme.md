## net_worth projector

This utility lets you setup some assets, contributions, changes in contributions, and let you estimate your net worth over time. It's useful to compare various scenarios like, "How much more will I have at retirement if I invest my house payment after I pay it off?"

### install
virtualenv:
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.in`

(for some reason I had to `pip install numpy -I` to avoid circular imports in pandas)

to run unit tests, run `python -m unittest tests/test_*.py`

### run
See `example_life.py` for an example about a married couple with two children. They have some saved for retirement and college, and plan to pay off their house in a couple years. Once that happens, they plan to invest their old mortgage payment in a new investment account.  Run `python example_life.py` to see how much their networh will be with this plan.  Then comment out line 28 and re-run the file to see the difference in net worth.  Over 18 years, this makes a difference of $1.2M!