import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\net40"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application


def test_something():
    Application.Launch("notepad.exe")
    print('ok')
