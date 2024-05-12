from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ID = self.text_area_1.text
    NAME = self.text_area_2.text
    5-8 = self.check_box_1.checked
    8-10 = self.check_box_2.checked
    anvil.server.call('submit', ID=ID , NAME=NAME , 5-8=RATING , 5-8 ,8-10=RATING 8-10);
    Notification("your response has been recorded").show()

