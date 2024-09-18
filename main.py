from Model import Model
from ViewController import ViewController
import tkinter

if __name__ == "__main__":
   viewController = ViewController()
   model = Model()
   viewController.bind(model=model)
   viewController.run()