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
app_tables.crs.add_row('submit',EMP ID=EMP ID,BOSS NAME=BOSS NAME,RATING 5-8=RATING 5-8, RATING 8-10=RATING 8-10)
Notification("Your response has been recorded").show()