import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.callable
def submit (ID, NAME , RATING , RATING):
app_tables.crs.add_row('submit', NAME=BOSS NAME,ID=EMP ID,RATING5-8=CHECKBOX1, RATING8-10=CHECKBOX2)
