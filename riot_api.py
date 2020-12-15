import requests

def requestSummonerData(region, summonerName, APItoken):
	URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ summonerName + "?api_key=" + APItoken
	response = requests.get(URL)
	return response.json()

def main():
	r = input("region: ") #region [eun1, br1, euw1, tr1, jp1, ru etc.]
	sName = input("username: ") #username for LoL
	APIt = input("API token: ") #API token generated in RiotGames website

	responseJson = requestSummonerData(r, sName, APIt)

	print()
	print("username for League of Legends: " + responseJson["name"])
	print("Summoner Level: " + str(responseJson["summonerLevel"]))

if __name__=="__main__":
	main()
