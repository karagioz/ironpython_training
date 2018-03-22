import clr
import os.path
import sys

project_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(project_dir, "..\\TestStack.White.0.13.3\\lib\\net40"))
sys.path.append(os.path.join(project_dir, "..\\Castle.Core.3.3.0\\lib\\net40-client"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *

from fixture.group import GroupHelper


class MyApplication:

    def __init__(self, path_to_app, main_window_header):
        self.application = Application.Launch(path_to_app)
        self.group = GroupHelper(self)
        self.main_window_header = main_window_header

    def get_main_window(self):
        application = self.application
        return application.GetWindow(self.main_window_header)

    def destroy(self):
        self.get_main_window().Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
