import json
import pandas as pd

def read_json(json_file):
    with open(json_file, "r") as read_file:
        json_read = json.loads(read_file.read())
    return json_read

def get_ppl_list_per_range(age_list, buckets):
    buckets.append(0)
    buckets.append(max(list(age_list.values())) +1)
    buckets.sort()
    age_bins = pd.cut(list(age_list.values()), bins=buckets)
    print(age_bins.unique())
    for range in age_bins.unique():
        print("{}-{}:".format(range.left, range.right))
        for person, age in age_list.items():
            if age >= range.left and age < range.right:
                print("   -" + person)

if __name__ == '__main__':
    ppl_ages_json = "hw.json"
    ages_json = read_json(ppl_ages_json)
    buckets = ages_json.get('buckets', 'none')
    ppl_ages = ages_json.get('ppl_ages', 'none')
    get_ppl_list_per_range(ppl_ages,buckets)