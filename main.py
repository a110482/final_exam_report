from ViewModel import ViewModel
from views.MainView import MainView

if __name__ == "__main__":
   viewController = MainView()
   view_model = ViewModel()
   viewController.bind(view_model=view_model)
   viewController.run()