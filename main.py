import json

keywords = ["junior", "nybörjare"]


def parse_jsonfile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def clean_json(data):
    cleaned_data = []
    for entry in data:
        description = entry["jobDescription"]
        if any(keyword in description for keyword in keywords):
            entry["viewJobLink"] = "https://se.indeed.com" + entry["viewJobLink"]
            cleaned_data.append(entry)

    # Print all job links
    for job in cleaned_data:
        print(job["viewJobLink"])


if __name__ == '__main__':
    clean_json(parse_jsonfile("extractedJobs.json"))
