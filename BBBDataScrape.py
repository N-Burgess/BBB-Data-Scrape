import requests
from bs4 import BeautifulSoup
data = []
searchurl = raw_input('Enter search url: ')
searchurl_get = requests.get(searchurl)
soup1 = BeautifulSoup(searchurl_get.text, 'html.parser')
pagenumb = soup1.find_all('script')[7].text.split("\"")[8][1:-1]
startpagefind = searchurl.split("&")
for l in startpagefind:
	if "page=" in l:
		startpage = l

for i in range(1, int(pagenumb)+1):
	BBB = searchurl.replace(startpage, 'page={}', -1).format(i)
	BBB_get = requests.get(BBB)
	soup2 = BeautifulSoup(BBB_get.text, 'html.parser')
	suburlfind = soup2.find_all('script')[7].text.split("\"")
	suburlref = soup2.find_all('script')[7].text.split("reportUrl")
	for split in suburlfind:
		if suburlref[1][3:].split("reviews")[0] in split:
			suburl = requests.get(split)
			soup = BeautifulSoup(suburl.text, 'html.parser')
			# business name
			if len(soup.find_all('title')) > 0:
				title = soup.find('title')
				namedata = title.text[23:]
			# url
			if len(soup.find_all('link', attrs={'rel':'canonical'})) > 0:
				urlfind= soup.find('link', attrs={'rel':'canonical'})['href']
				urldata = str(urlfind)
			# email and website
			if len(soup.find_all('a', attrs={'class': 'btn btn-outline btn-outline--blue business-buttons__button'})) > 0:
				emailwebfind = soup.find_all('a', attrs={'class':'btn btn-outline btn-outline--blue business-buttons__button'})
				emailweb = emailwebfind[0]
				if "EMAIL" in emailweb.text:
					email = emailweb['href']
					emaildata = email[7:]
				elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 5:
					addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("@") in addemailfind[0].text:
						emaildata = addemailfind[0].text[30:-26]
					elif ("@") in addemailfind[1].text:
						emaildata = addemailfind[1].text[30:-26]
					elif ("@") in addemailfind[2].text:
						emaildata = addemailfind[2].text[30:-26]
					elif ("@") in addemailfind[3].text:
						emaildata = addemailfind[3].text[30:-26]
					elif ("@") in addemailfind[4].text:
						emaildata = addemailfind[4].text[30:-26]
					else: emaildata = (" ")
				elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 4:
					addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("@") in addemailfind[0].text:
						emaildata = addemailfind[0].text[30:-26]
					elif ("@") in addemailfind[1].text:
						emaildata = addemailfind[1].text[30:-26]
					elif ("@") in addemailfind[2].text:
						emaildata = addemailfind[2].text[30:-26]
					elif ("@") in addemailfind[3].text:
						emaildata = addemailfind[3].text[30:-26]
					else: emaildata = (" ")
				elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 3:
					addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("@") in addemailfind[0].text:
						emaildata = addemailfind[0].text[30:-26]
					elif ("@") in addemailfind[1].text:
						emaildata = addemailfind[1].text[30:-26]
					elif ("@") in addemailfind[2].text:
						emaildata = addemailfind[2].text[30:-26]
					else: emaildata = (" ")
				elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 2:
					addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("@") in addemailfind[0].text:
						emaildata = addemailfind[0].text[30:-26]
					elif ("@") in addemailfind[1].text:
						emaildata = addemailfind[1].text[30:-26]
					else: emaildata = (" ")
				elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 1:
					addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("@") in addemailfind[0].text:
						emaildata = addemailfind[0].text[30:-26]
					else: emaildata = (" ")
				else: emaildata = (" ")
				if "WEBSITE" in emailweb.text:
					website = emailweb['href']
					websitedata = website[7:]
				elif len(soup.find_all('a', attrs={'class': 'btn btn-outline btn-outline--blue business-buttons__button'})) >= 2:
					website = emailwebfind[1]['href']
					websitedata = website[7:]
				else: websitedata = ("")
			elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) > 5:
				addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if ("@") in addemailfind[0].text:
					emaildata = addemailfind[0].text[30:-26]
				elif ("@") in addemailfind[1].text:
					emaildata = addemailfind[1].text[30:-26]
				elif ("@") in addemailfind[2].text:
					emaildata = addemailfind[2].text[30:-26]
				elif ("@") in addemailfind[3].text:
					emaildata = addemailfind[3].text[30:-26]
				elif ("@") in addemailfind[4].text:
					emaildata = addemailfind[4].text[30:-26]
				else: 
					emaildata = (" ")
					websitedata = ("")
			elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 4:
				addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if ("@") in addemailfind[0].text:
					emaildata = addemailfind[0].text[30:-26]
				elif ("@") in addemailfind[1].text:
					emaildata = addemailfind[1].text[30:-26]
				elif ("@") in addemailfind[2].text:
					emaildata = addemailfind[2].text[30:-26]
				elif ("@") in addemailfind[3].text:
					emaildata = addemailfind[3].text[30:-26]
				else: 
					emaildata = (" ")
					websitedata = ("")
			elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 3:
				addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if ("@") in addemailfind[0].text:
					emaildata = addemailfind[0].text[30:-26]
				elif ("@") in addemailfind[1].text:
					emaildata = addemailfind[1].text[30:-26]
				elif ("@") in addemailfind[2].text:
					emaildata = addemailfind[2].text[30:-26]
				else: 
					emaildata = (" ")
					websitedata = ("")
			elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 2:
				addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if ("@") in addemailfind[0].text:
					emaildata = addemailfind[0].text[30:-26]
				elif ("@") in addemailfind[1].text:
					emaildata = addemailfind[1].text[30:-26]
				else: 
					emaildata = (" ")
					websitedata = ("")
			elif len(soup.find_all('li', attrs={'class':'company-info__list-item'})) >= 1:
				addemailfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if ("@") in addemailfind[0].text:
					emaildata = addemailfind[0].text[30:-26]
				else: 
					emaildata = (" ")
					websitedata = ("")
			else:
				emaildata = (" ")
				websitedata = ("")				
			# phone number
			if len(soup.find_all('a', attrs={'class':'address__phone-number-link'})) > 0:
				numbfind = soup.find('a', attrs={'class':'address__phone-number-link'})
				pnumbdata = numbfind.text
			else: pnumbdata = " "
			# additional numbers
			if len(soup.find_all('div', attrs={'class':'collapse', 'id':'SeeMoreContactOptions'})) > 0:
				faxnumbfind = soup.find('div', attrs={'class':'collapse', 'id':'SeeMoreContactOptions'})
				if ("Fax Numbers") in faxnumbfind.text:
					fnumbdata = faxnumbfind.text[85:99]
			else: fnumbdata = " "
			if len(soup.find_all('ul', attrs={'class':'company-info__list'})) > 0:
				if len(soup.find_all('li', attrs={'class':'company-info__list-item'})) > 0:
					addnumbref = soup.find_all('h6', attrs={'class':'company-info__subheading'})
					addnumbfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
					if ("Additional Phone Numbers") in addnumbref[0].text:
						if len(soup.find('ul', attrs={'class':'company-info__list'}).contents) == 3:
							a1numbdata = addnumbfind[0].text[30:-26]
							a2numbdata = " "
							a3numbdata = " "
						elif len(soup.find('ul', attrs={'class':'company-info__list'}).contents) == 5:
							a1numbdata = addnumbfind[0].text[30:-26]+" "
							a2numbdata = addnumbfind[1].text[30:-26]
							a3numbdata = " "
						elif len(soup.find('ul', attrs={'class':'company-info__list'}).contents) == 7:
							a1numbdata = addnumbfind[0].text[30:-26]+" "
							a2numbdata = addnumbfind[1].text[30:-26]+" "
							a3numbdata = addnumbfind[2].text[30:-26]
					elif ("Additional Phone Numbers") in addnumbref[1].text:
						if len(soup.find_all('ul', attrs={'class':'company-info__list'})[1].contents) == 3:
							a1numbdata = addnumbfind[1].text[30:-26]
							a2numbdata = " "
							a3numbdata = " "
						elif len(soup.find_all('ul', attrs={'class':'company-info__list'})[1].contents) == 5:
							a1numbdata = addnumbfind[1].text[30:-26]+" "
							a2numbdata = addnumbfind[2].text[30:-26]
							a3numbdata = " "
						elif len(soup.find_all('ul', attrs={'class':'company-info__list'})[1].contents) == 7:
							a1numbdata = addnumbfind[1].text[30:-26]+" "
							a2numbdata = addnumbfind[2].text[30:-26]+" "
							a3numbdata = addnumbfind[3].text[30:-26]
					else:
						a1numbdata = " "
						a2numbdata = " "
						a3numbdata = " "
				else:
					a1numbdata = " "
					a2numbdata = " "
					a3numbdata = " "
			else:
				a1numbdata = " "
				a2numbdata = " "
				a3numbdata = " "
			# listed owner
			if len(soup.find_all('li', attrs={'class':'company-info__list-item'})) > 0:
				ownerfind = soup.find_all('li', attrs={'class':'company-info__list-item'})
				if len(ownerfind) >= 14:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: ownerdata8 = ""
					if any(c in ownerfind[9].text for c in ("Owner","President","CEO")):
						ownerdata9 = ownerfind[9].text[22:-18]+" "
					else: ownerdata9 = ""
					if any(c in ownerfind[10].text for c in ("Owner","President","CEO")):
						ownerdata10 = ownerfind[10].text[22:-18]+" "
					else: ownerdata10 = ""
					if any(c in ownerfind[11].text for c in ("Owner","President","CEO")):
						ownerdata11 = ownerfind[11].text[22:-18]+" "
					else: ownerdata11 = ""
					if any(c in ownerfind[12].text for c in ("Owner","President","CEO")):
						ownerdata12 = ownerfind[12].text[22:-18]+" "
					else: ownerdata12 = ""
					if any(c in ownerfind[13].text for c in ("Owner","President","CEO")):
						ownerdata13 = ownerfind[13].text[22:-18]+" "
					else: ownerdata13 = ""
				elif len(ownerfind) == 13:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: ownerdata8 = ""
					if any(c in ownerfind[9].text for c in ("Owner","President","CEO")):
						ownerdata9 = ownerfind[9].text[22:-18]+" "
					else: ownerdata9 = ""
					if any(c in ownerfind[10].text for c in ("Owner","President","CEO")):
						ownerdata10 = ownerfind[10].text[22:-18]+" "
					else: ownerdata10 = ""
					if any(c in ownerfind[11].text for c in ("Owner","President","CEO")):
						ownerdata11 = ownerfind[11].text[22:-18]+" "
					else: ownerdata11 = ""
					if any(c in ownerfind[12].text for c in ("Owner","President","CEO")):
						ownerdata12 = ownerfind[12].text[22:-18]+" "
					else:
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 12:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: ownerdata8 = ""
					if any(c in ownerfind[9].text for c in ("Owner","President","CEO")):
						ownerdata9 = ownerfind[9].text[22:-18]+" "
					else: ownerdata9 = ""
					if any(c in ownerfind[10].text for c in ("Owner","President","CEO")):
						ownerdata10 = ownerfind[10].text[22:-18]+" "
					else: ownerdata10 = ""
					if any(c in ownerfind[11].text for c in ("Owner","President","CEO")):
						ownerdata11 = ownerfind[11].text[22:-18]+" "
					else:
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 11:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: ownerdata8 = ""
					if any(c in ownerfind[9].text for c in ("Owner","President","CEO")):
						ownerdata9 = ownerfind[9].text[22:-18]+" "
					else: ownerdata9 = ""
					if any(c in ownerfind[10].text for c in ("Owner","President","CEO")):
						ownerdata10 = ownerfind[10].text[22:-18]+" "
					else: 
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 10:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: ownerdata8 = ""
					if any(c in ownerfind[9].text for c in ("Owner","President","CEO")):
						ownerdata9 = ownerfind[9].text[22:-18]+" "
					else:
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 9:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: ownerdata7 = ""
					if any(c in ownerfind[8].text for c in ("Owner","President","CEO")):
						ownerdata8 = ownerfind[8].text[22:-18]+" "
					else: 
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""				
				elif len(ownerfind) == 8:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: ownerdata6 = ""
					if any(c in ownerfind[7].text for c in ("Owner","President","CEO")):
						ownerdata7 = ownerfind[7].text[22:-18]+" "
					else: 
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 7:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: ownerdata5 = ""
					if any(c in ownerfind[6].text for c in ("Owner","President","CEO")):
						ownerdata6 = ownerfind[6].text[22:-18]+" "
					else: 
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 6:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: ownerdata4 = ""
					if any(c in ownerfind[5].text for c in ("Owner","President","CEO")):
						ownerdata5 = ownerfind[5].text[22:-18]+" "
					else: 
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 5:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: ownerdata3 = ""
					if any(c in ownerfind[4].text for c in ("Owner","President","CEO")):
						ownerdata4 = ownerfind[4].text[22:-18]+" "
					else: 
						ownerdata4 = ""
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 4:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: ownerdata2 = ""
					if any(c in ownerfind[3].text for c in ("Owner","President","CEO")):
						ownerdata3 = ownerfind[3].text[22:-18]+" "
					else: 
						ownerdata3 = ""
						ownerdata4 = ""
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 3:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: ownerdata1 = ""
					if any(c in ownerfind[2].text for c in ("Owner","President","CEO")):
						ownerdata2 = ownerfind[2].text[22:-18]+" "
					else: 
						ownerdata2 = ""
						ownerdata3 = ""
						ownerdata4 = ""
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 2:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]+" "
					else: ownerdata0 = ""
					if any(c in ownerfind[1].text for c in ("Owner","President","CEO")):
						ownerdata1 = ownerfind[1].text[22:-18]+" "
					else: 
						ownerdata1 = ""
						ownerdata2 = ""
						ownerdata3 = ""
						ownerdata4 = ""
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				elif len(ownerfind) == 1:
					if any(c in ownerfind[0].text for c in ("Owner","President","CEO")):
						ownerdata0 = ownerfind[0].text[22:-18]
					else: 
						ownerdata0 = ""
						ownerdata1 = ""
						ownerdata2 = ""
						ownerdata3 = ""
						ownerdata4 = ""
						ownerdata5 = ""
						ownerdata6 = ""
						ownerdata7 = ""
						ownerdata8 = ""
						ownerdata9= ""
						ownerdata10 = ""
						ownerdata11 = ""
						ownerdata12 = ""
						ownerdata13 = ""
				else: 
					ownerdata0 = ""
					ownerdata1 = ""
					ownerdata2 = ""
					ownerdata3 = ""
					ownerdata4 = ""
					ownerdata5 = ""
					ownerdata6 = ""
					ownerdata7 = ""
					ownerdata8 = ""
					ownerdata9= ""
					ownerdata10 = ""
					ownerdata11 = ""
					ownerdata12 = ""
					ownerdata13 = ""
			else: 
				ownerdata0 = ""
				ownerdata1 = ""
				ownerdata2 = ""
				ownerdata3 = ""
				ownerdata4 = ""
				ownerdata5 = ""
				ownerdata6 = ""
				ownerdata7 = ""
				ownerdata8 = ""
				ownerdata9 = ""
				ownerdata10 = ""
				ownerdata11 = ""
				ownerdata12 = ""
				ownerdata13 = ""
						
			import pandas as pd

			data.append([namedata, urldata, emaildata, websitedata, pnumbdata, fnumbdata, a1numbdata+a2numbdata+a3numbdata, ownerdata0+ownerdata1+ownerdata2+ownerdata3+ownerdata4+ownerdata5+ownerdata6+ownerdata7+ownerdata8+ownerdata9+ownerdata10+ownerdata11+ownerdata12+ownerdata13])
			df = pd.DataFrame(data, columns=['Business Name', 'BBB url', 'Email Address', 'Website Address', 'Phone Number', 'Fax Number', 'Additional Numbers', 'Owner Listed'])

			writer = pd.ExcelWriter('BBB data.xlsx', engine='xlsxwriter')
			workbook = writer.book
			df.to_excel(writer, sheet_name='BBB data')
			worksheet = writer.sheets['BBB data']

			format = workbook.add_format({'valign': 'vcenter'})
			format2 = workbook.add_format({
				'text_wrap': True,
				'valign': 'vcenter'})
			format3 = workbook.add_format({
				'color': 'blue',
				'underline': True,
				'valign': 'vtop'})
			worksheet.set_column(0, 0, 8, format)
			worksheet.set_column(1, 1, 39, format)
			worksheet.set_column(2, 2, 117, format3)
			worksheet.set_column(3, 3, 35, format)
			worksheet.set_column(4, 4, 53, format3)
			worksheet.set_column(5, 6, 15, format)
			worksheet.set_column(7, 7, 15, format2)
			worksheet.set_column(8, 8, 30, format2)

			writer.save()
