from flask import Flask, request, render_template, send_from_directory, url_for

from functions import *


app = Flask(__name__)


@app.route("/")
def main_page():
    data = get_feed()
    comments = get_count_comments(data)
    return render_template("index.html", posts=data, comments=comments)


@app.route("/post/<postid>")
def post_page(postid):
    posts = get_feed()
    comments = get_comments()
    # Получение данных поста
    for post in posts:
        if post["pk"] == int(postid):
            post_data = post

    # Получение комментарием
    list_of_comments = []
    for comment in comments:
        if comment["post_id"] == int(postid):
            list_of_comments.append(comment)

    # Получение количества комментариев
    comments_data = get_count_comments(posts)


    return render_template('post.html', post=post_data, comments=list_of_comments, comments_data=comments_data)

@app.route("/search", methods=["GET", "POST"])
def search_page():

    if request.method == "GET":
        search = request.args.get("s")
        if search is None:
            all_posts = get_feed()
            if len(all_posts) > 10:
                all_posts = all_posts[0:9]
            comments = get_comments()
            short_comments = get_count_comments(all_posts)
            return render_template("search.html", posts=all_posts, comments=comments, count=len(all_posts),
                                   short_comments_data=short_comments)
        elif search:
            posts = search_post(search)
            if len(posts) > 10:
                posts = posts[0:9]
            comments = get_count_comments(posts)
            full_comments_data = get_comments()
            return render_template("search.html", posts=posts, short_comments_data=comments, count=len(posts),
                                   comments=full_comments_data)

    if request.method == "POST":
        search = request.form.get("search")
        if search is None:
            all_posts = get_feed()
            if len(all_posts) > 10:
                all_posts = all_posts[0:9]
            comments = get_comments()
            short_comments = get_count_comments(all_posts)
            return render_template("search.html", posts=all_posts, comments=comments, count=len(all_posts),
                                   short_comments_data=short_comments)
        else:
            posts = search_post(search)
            if len(posts) > 10:
                posts = posts[0:9]
            comments = get_count_comments(posts)
            full_comments_data = get_comments()
            return render_template("search.html", posts=posts, short_comments_data=comments, count=len(posts),
                                   comments=full_comments_data)


@app.route("/users/<username>")
def user_page(username):
    posts = get_feed()
    users_posts = get_users_posts(posts, username)
    count_comments = get_count_comments(posts)

    return render_template("user-feed.html", posts=users_posts, count_comments=count_comments)


if __name__ == "__main__":
   app.run()