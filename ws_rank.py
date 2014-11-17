#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""

"""

from bottle import route, run, template
from ranker import Ranker

arrs_ranker = None;

@route('/arrivals/last/<n>')
def get_last(n):
    """
    Returns the last 'n' airports in arrivals ranking
    """
    if not arrs_ranker:
        status = 500
        response = "Ranker not initialized"    
    else:
        status = 200
        response = arrs_ranker.get_last(int(n))
    return response


@route('/arrivals/first/<n>')
def get_fist(n):
    """
    Returns the first 'n' airports in arrivals ranking
    """
    if not arrs_ranker:
        status = 500
        response = "Ranker not initialized"    
    else:
        status = 200
        response = arrs_ranker.get_first(int(n))
    return response


if __name__ == "__main__":
    """
    """
    #start ranker
    print "starting ranker"
    arrs_ranker = Ranker()
    print "setting up ranking"
    arrs_ranker.setup_arrivals_ranking()
    print "starting server"
    #running server
    run(host='localhost', port=8080)

