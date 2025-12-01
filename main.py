import jsonparser

if __name__ == '__main__':
    data = jsonparser.parse_jsonfile('extractedJobs.json')
    jsonparser.clean_json(data)
