import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
