import json

def get_feed():
    """
    Функция получения всех постов
    :return:
    """
    with open("data/data.json", 'r') as file:
        data = json.load(file)

    return data

def get_count_comments(posts_data):
    """
    Функция подсчета комментариев к посту
    :param posts_data: посты, к которым надо получить комментарии
    :return: список словарей, где указаны id поста и количество комментариев с правильным склонением
    """
    #Считываем файл с комментариями
    with open("data/comments.json") as file:
        comments = json.load(file)

    list_comments = []
    list_posts_numbers = []

    #Добавляем в список словарей первый ключ - айди поста
    for item in posts_data:
        temp = {"post_id": item["pk"]}
        list_posts_numbers.append(temp)

    for post in list_posts_numbers:
        temp_count = 0
        for item in comments:
            if item["post_id"] == post["post_id"]:
                temp_count += 1
        post["numb_of_comments"] = temp_count
        #Цикл определения окончания слова "комментарий!
        if temp_count > 100:
           div_remainder = temp_count % 100
           if div_remainder > 20:
              div_remainder = div_remainder%10
              if div_remainder == 0 or 5 <= div_remainder <= 9:
                  post["com_finishing"] = "комментариев"
              elif div_remainder == 1:
                  post["com_finishing"] = "комментарий"
              elif 1 < div_remainder <= 4:
                  post["com_finishing"] = "комментария"
           elif div_remainder == 0:
               post["com_finishing"] = "комментариев"
           elif div_remainder == 1:
               post["com_finishing"] = "комментарий"
           elif 1 < div_remainder <= 4:
               post["com_finishing"] = "комментария"
           elif 5 <= div_remainder <= 20:
               post["com_finishing"] = "комментариев"
        elif 21 <= temp_count < 100:
            div_remainder = temp_count % 10
            if div_remainder == 0 or 5 <= div_remainder <= 9:
                post["com_finishing"] = "комментариев"
            elif div_remainder == 1:
                post["com_finishing"] = "комментарий"
            elif 1 < div_remainder <= 4:
                post["com_finishing"] = "комментария"
        elif 10 <= temp_count <= 20:
            post["com_finishing"] = "комментариев"
        elif temp_count == 0 or 5 <= temp_count <= 9:
            post["com_finishing"] = "комментариев"
        elif temp_count == 1:
            post["com_finishing"] = "комментарий"
        elif 1 < temp_count <= 4:
            post["com_finishing"] = "комментария"

    return list_posts_numbers


def get_comments():
    #Получение всех комментариев
    with open("data/comments.json") as file:
        comments = json.load(file)
    return comments

def search_post(key_word):
    """
    Функция выводит все посты в которых совпало слово целиком, без учета регистра
    """
    with open("data/data.json", 'r') as file:
        data = json.load(file)
        post_list = []
    for post in data:
        words = post['content'].lower().split()
        for i, word in enumerate(words):
            for letter in ["!", ",", ".", "-", "?", "#"]:
                if letter in word:
                    temp = word.replace(letter, "")
                    words[i] = temp
        if key_word.lower() in words:
            post_list.append(post)
    return post_list


def get_users_posts(posts, username):
    """
    Функция вывода  всех постов пользователя
    :param posts: все посты
    :param username: имя пользователя
    :return: все посты пользователя
    """
    matched_posts = []
    for post in posts:
        if post["poster_name"] == username:
            matched_posts.append(post)

    return matched_posts





