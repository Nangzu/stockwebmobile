from flask import Flask, render_template, request, redirect, Blueprint

bp = Blueprint('bpmain', __name__, url_prefix='/index')
@bp.route('/', methods=['POST', 'GET'])
def main():
    return render_template('index.html')