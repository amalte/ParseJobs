import json
import localLLM
import utils


def parse_jsonfile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def clean_json(jobs):
    """
    Extracts jobs that are of junior level and discards senior level jobs.
    """
    cleaned_jobs = []
    nr_jobs_to_check = 5
    for job in jobs[:nr_jobs_to_check]:
        description = job["jobDescription"]
        print(description)
        print(f"The text is swedish: {utils.isSwedishText(description)}")

        if localLLM.isJuniorJob(description):
            job["viewJobLink"] = "https://se.indeed.com" + job["viewJobLink"]
            cleaned_jobs.append(job)

    # Print all job links
    for job in cleaned_jobs:
        print(job["viewJobLink"])


