import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
import main as main
import dataset as dataset


# Load CSV file
online_shoppers_intention = dataset.load_dataset();
main.options_selector(online_shoppers_intention)
