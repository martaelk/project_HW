from pick import pick # import select menu library
import extractData
import drawTable
import formatData

def main():
    title = 'Select category:'
    options = ['1. Statistics by polling stations', '2. See election candidates', '3. See party info', '4. Statistics of elected candidates', '5. Candidate demographics']
    selectedCategory, index = pick(options, title)

    if index == 0:
        data = extractData.getPollingStationData()
        formattedData = formatData.formatPollingStationData(data)
        header = ["Polling station location", "Votes", "Votes (%)"]
        drawTable.drawTable("Statistics by polling stations", header, formattedData)
    elif index == 1:
        data = extractData.getCandidates()
        formattedData = formatData.formatCandidates(data)
        header = ["Name", "Surname", "Party", "Birth year", "Education", "Work place", "Languages skills"]
        drawTable.drawTable("Election candidates", header, formattedData)
    elif index == 2:
        data = extractData.getPartyData()
        formattedData = formatData.formatPartyData(data)
        header = ["Party title", "Candidate Count"]
        drawTable.drawTable("Party info", header, formattedData)

    elif index == 3:
        data = extractData.getElectedCandiateData()
        formattedData = formatData.formatElectedCandiateData(data)
        header = ["Name", "Surname", "Party", "Count", "Count (%)", "Plus Count", "Minus Count"]
        drawTable.drawTable("Elected Candiates", header, formattedData)
    elif index == 4:
        data = extractData.getCandidateDemographicData()
        header = ["Age", "Count", "Count (%)"]
        formattedAgeStatistic = formatData.formatAgeStatistic(data)
        drawTable.drawTable("Age statistics of candidates", header, formattedAgeStatistic)

        header = ["Education", "Count", "Count (%)"]
        formattedEducationStatistic = formatData.formatEducationStatistic(data)
        drawTable.drawTable("Candidates' education statistics", header, formattedEducationStatistic)

        header = ["Gender", "Count", "Count (%)"]
        formattedGenderStatistic = formatData.formatGenderStatistic(data)
        drawTable.drawTable("Gender statistics of candidates", header, formattedGenderStatistic)

        header = ["Place of residence", "Count", "Count (%)"]
        formattedPlaceOfResidenceStatistic = formatData.formatPlaceOfResidenceStatistic(data)
        drawTable.drawTable("Statistics of candidates residence", header, formattedPlaceOfResidenceStatistic)


if __name__=="__main__": 
    main() 