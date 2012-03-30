#!/usr/bin/env python

from flask import Flask, render_template
from feedback.feedback import app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8079)
