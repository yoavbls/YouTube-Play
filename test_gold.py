import youtube_play as yp

def test_chet_faker():
    input_query = "chet faker gold"
    chet_faker_link = "https://www.youtube.com/watch?v=hi4pzKvuEQM"
    print "--------- checking chet faker gold link ---------"
    assert yp.link_from_input_query(input_query) == chet_faker_link


