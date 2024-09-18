from ViewModel import ViewModel
from ViewController import ViewController
import tkinter

if __name__ == "__main__":
   viewController = ViewController()
   view_model = ViewModel()
   viewController.bind(view_model=view_model)
   viewController.run()