import random
companies = ["strata","ypo","cleanplacepros","bannerhouse","parkhouse","edgerealty"]
random.seed(42)
for c in companies:
    print(f"{c}:{random.randint(10000,99999)}")
