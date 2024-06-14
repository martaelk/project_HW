def formatPollingStationData(data):
    # Calculate total voter count
    total_voter_count = sum(item['VoterCount'] for item in data)
    rows = []
    for item in data:
        percentage = (item['VoterCount'] / total_voter_count) * 100  # calculate percentage of total voter count
        rows.append([item['Name'], str(item['VoterCount']), f"{percentage:.2f}%"])
        
    return rows

def formatCandidates(data):
    rows = []

    for candidate in data:
        first_name = candidate["Name"]
        last_name = candidate["Surname"]
        party = candidate["CandidateList"]["Name"]
        year_of_birth = str(candidate["YearOfBirth"])
        
        if "EducationList" in candidate:
            education_info = ""

            for education in candidate["EducationList"]:
                if "Speciality" in education:
                    education_info += education["Speciality"] + ", "

        workplace_info = candidate["Workplace"]["Name"]

        if "LanguageSkillList" in candidate:
            language_skills = ""

            for language in candidate["LanguageSkillList"]:
                if "Name" in language:
                    language_skills += language["Name"] + ", "

        rows.append([first_name, last_name, party, year_of_birth, education_info, workplace_info, language_skills])

    return rows

def formatPartyData(data):
    rows = []
    for item in data:
        rows.append([item['Name'], str(item['CandidateCount'])])
        
    return rows

def formatElectedCandiateData(data):
    rows = []
    for item in data:
        rows.append([item['Name'], item['Surname'], item ['CandidateList']['Name'], str(item ['ValidMarkCount']['Count']), str(item['ValidMarkCount']['Percentage']),
                     str(item['PlusCount']['Count']), str(item['MinusCount']['Count']),])
        
    return rows


def formatAgeStatistic(data):
    rows = []
    for item in data["AgeStatistic"]:
        rows.append([item['Name'], str(item['Count']), f"{item['Percentage']:.2f}%"])
    return rows

def formatEducationStatistic(data):
    rows = []
    for item in data["EducationStatistic"]:
        rows.append([item['Name'], str(item['Count']), f"{item['Percentage']:.2f}%"])
    return rows
    

def formatGenderStatistic(data):
    rows = []
    for item in data["GenderStatistic"]:
        rows.append([item['Name'], str(item['Count']), f"{item['Percentage']:.2f}%"])
    return rows
    

def formatPlaceOfResidenceStatistic(data):
    rows = []
    for item in data["PlaceOfResidenceStatistic"]:
        rows.append([item['Name'], str(item['Count']), f"{item['Percentage']:.2f}%"])
    return rows


