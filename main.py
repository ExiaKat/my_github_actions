import os
import argparse

apikey = os.getenv("MAXIMO_APIKEY")
target_host = os.getenv("TARGETHOST")
parser = argparse.ArgumentParser(description="Process folder and product")
parser.add_argument("folder", help="Path to devops autoscript folder")
parser.add_argument("product", help="Name of the product")

args = parser.parse_args()

print(target_host, apikey, args.folder, args.product)
