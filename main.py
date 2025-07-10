import os
import argparse

apikey = os.getenv("MAXIMO_APIKEY")
parser = argparse.ArgumentParser(description="Process folder and product")
parser.add_argument("folder", help="Path to devops autoscript folder")
parser.add_argument("product", help="Name of the product")

args = parser.parse_args()

print(apikey, args.folder, args.product)