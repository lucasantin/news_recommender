import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.recommender import NewsRecommender



def test_recommend_existing_user():
    recommender = NewsRecommender()
    recs = recommender.recommend("e5f68d5e7cdbe56d6984589b4baa6ebfc5e8a8a918e57d5092adc513f516b377")
    assert isinstance(recs, list)
    assert len(recs) > 0
    
    #e5f68d5e7cdbe56d6984589b4baa6ebfc5e8a8a918e57d5092adc513f516b377
    #3a3b7f25a30a5a17a530685545e3a0be38cee0c6904c42cb3bb36c448a7ec901
    #ea6728ebc30782516a7593a1143c47dc59428e1649c048c53e2fe006700ff936
    #f909c50558c01ab790636e1b1918e6a5965bdcc271a8605f4cc82a0d70ad5ed1
    #9725352f759a73aa977cb5eff2596a5f683fcd0c7532001d79baba871ad92bc7


def test_recommend_new_user():
    recommender = NewsRecommender()
    recs = recommender.recommend("99999")
    assert isinstance(recs, list)
    assert len(recs) >= 0
