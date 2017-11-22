from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User, Post
from app.decorators import admin_required

@api.route('/users/<int:id>')
@admin_required
def get_user(user_id):
    """
    根据访问的url返回对应id的json格式user
    :param user_id:
    :return:
    """
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_json())



# @api.route('/users/<int:id>/posts/')
# def get_user_posts(id):
#     user = User.query.get_or_404(id)
#     page = request.args.get('page', 1, type=int)
#     pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('api.get_user_posts', id=id, page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('api.get_user_posts', id=id, page=page+1)
#     return jsonify({
#         'posts': [post.to_json() for post in posts],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })
#
#
# @api.route('/users/<int:id>/timeline/')
# def get_user_followed_posts(id):
#     user = User.query.get_or_404(id)
#     page = request.args.get('page', 1, type=int)
#     pagination = user.followed_posts.order_by(Post.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('api.get_user_followed_posts', id=id, page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('api.get_user_followed_posts', id=id, page=page+1)
#     return jsonify({
#         'posts': [post.to_json() for post in posts],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })
