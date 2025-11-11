thonfrom bs4 import BeautifulSoup

def parse_leaderboard(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    leaderboard_data = []
    
    leaderboard_items = soup.find_all('div', class_='leaderboard-item')
    
    for item in leaderboard_items:
        entry = {
            "id": item.get('data-id'),
            "title": item.find('h3').text.strip(),
            "whopRanking": int(item.find('span', class_='ranking').text.strip()),
            "activeUsersCount": int(item.find('span', class_='active-users').text.strip()),
            "users": []
        }
        
        user_data = item.find_all('div', class_='user-profile')
        for user in user_data:
            user_info = {
                "id": user.get('data-user-id'),
                "name": user.find('p', class_='user-name').text.strip(),
                "username": user.find('p', class_='username').text.strip(),
                "profilePicSm": user.find('img')['src']
            }
            entry["users"].append(user_info)
        
        leaderboard_data.append(entry)
    
    return leaderboard_data