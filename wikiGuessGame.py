from bs4 import BeautifulSoup
import requests
import random
import types

#get first URL
url_pick = "https://en.wikipedia.org/wiki/Drake_(musician)"
url = "https://en.wikipedia.org/wiki/Drake_(musician)"

#loop through program
while True:
    #get currently used URL
    url = url_pick
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")

    #find where the body paragraphs are
    contents = doc.find("body")
    sub_contents  = contents.select_one("#content")
    body_contents = sub_contents.select_one("#bodyContent")
    body_text = body_contents.select_one("#mw-content-text")
    body = body_text.find_all("p")

    
    def get_three_links(body):
        #this function finds three links within the bodies of text, picking random paragraphs, then random links within those paragraphs
        while True:
            try:
                paragraph_chosen = random.randint(0,len(body))
                paragraph1 = body_text.find_all("p")[paragraph_chosen]
                links = paragraph1.find_all("a")
                link_chosen = random.randint(0,len(links)-1)
                link = links[link_chosen]
                link1 = link.string
                if ((link1 is None) or link1[0]=="["):
                    x=2
                else:
                    break
            except ValueError:
                x=2

        while True:
            try:
                paragraph_chosen = random.randint(0,len(body))
                paragraph1 = body_text.find_all("p")[paragraph_chosen]
                links = paragraph1.find_all("a")
                link_chosen = random.randint(0,len(links)-1)
                link = links[link_chosen]
                link2 = link.string
                if ((link2 is None) or link2[0]=="["):
                    x=2
                else:
                    break
            except ValueError:
                x=2
        
        while True:
            try:
                paragraph_chosen = random.randint(0,len(body))
                paragraph1 = body_text.find_all("p")[paragraph_chosen]
                links = paragraph1.find_all("a")
                link_chosen = random.randint(0,len(links)-1)
                link = links[link_chosen]
                link3 = link.string
                if ((link3 is None) or link3[0]=="["):
                    x=2
                else:
                    break
            except ValueError:
                x=2
        
        return (link1,link2,link3)
    def get_false_links(body):
        while True:
            false_link_database = ["Drake","NBA","Karl Marx","Toronto","Africa","Arnold Shwartzenegger","Chris Pine","Wait for U","Adolf Hitler","Shazam","wage labor","Chief executive officer","local government","John D. Rockefeller","University of Chicago","The New York Times","Science journalism","Pharamceutical marketing","New Zealand","Astrobiology","Milky Way","Special relativity","Association football","Emmy Awards","Streaming television","YouTube","Venture capital"]
            random_index = random.randint(0,len(false_link_database)-1)
            false_link = false_link_database[random_index]
            for paragraph in body:
                for i in range(0,len(paragraph.find_all("a"))):
                    if paragraph.find_all("a")[i]==false_link:
                        pass
                    else:
                        return false_link

    def user_guessing(real,pick):
        #user prints out a selected pick
        if pick == real:
            return True
        else:
            return False

    #Links are found from the function
    
    while True:
        try:
            (link1,link2,link3) = get_three_links(body)
            break
        except IndexError:
            pass
    
    
    false1 = get_false_links(body)
    false2 = get_false_links(body)
    print(link1+", "+false1+", "+false2)
    #user prints out a selected pick
    pick = input("One of these links exists on the previous answer's Wiki page, which one is it?: ")
    result = user_guessing(link1,pick)
    if pick == "break":
        break

    if result == True:   
        #program takes pick and parses through the article to find where that link was, and extracts new URL
        for para in body:
            for i in range(len(para.find_all("a"))):
                if pick in para.text:
                    para_with_link = para
                    break
        links_with_desired_link = para_with_link.find_all("a")
        for i in range(len(links_with_desired_link)):
            if pick in links_with_desired_link[i]:
                link_found = links_with_desired_link[i]
                break
        
        
        

        name = link_found.get("title")
        url_pick = "https://en.wikipedia.org/"+link_found.get("href")
        print("You are now on "+str(name)+ " ("+link_found.string+")'s page.")

    else:
        print("Wrong")
        break