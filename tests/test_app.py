from playwright.sync_api import Page, expect

# Tests for your routes go here




# def test_get_all_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     div_tags = page.locator("div")
#     expect(div_tags).to_have_text([
#         "Title: Doolittle\nReleased: 1989",
#         "Title: Surfer Rosa\nReleased: 1988"
#     ])

def test_get_all_albums_improved(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa"
    ])

# def test_for_one_album(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store.sql")
#     page.goto(f"http://{test_web_address}/albums/1")
#     h1_tags = page.locator("h1")
#     expect(h1_tags).to_have_text([
#         "Doolittle"
#     ])
#     paragraph_tags = page.locator("p")
#     expect(paragraph_tags).to_have_text([
#         "Release year: 1989"
#     ])


# def test_for_artist_for_album(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store.sql")
#     page.goto(f"http://{test_web_address}/albums/1")
#     h1_tags = page.locator("h1")
#     expect(h1_tags).to_have_text([
#         "Doolittle"
#     ])
#     paragraph_tags = page.locator("p")
#     expect(paragraph_tags).to_have_text([
#         "Release year: 1989",
#         "Artist: Pixies",
#         "Go back to main page"
#     ])


def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Doolittle")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Release year: 1989")



def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")
    

def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Pixies",
        "ABBA"
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Pixies")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Rock")


def test_visit_artist_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    page.click("text='Go back to artist list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")

    page.fill("input[name=title]", "Diamond")
    page.fill("input[name=release_year]", "1995")
    page.click("text='Add album'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Diamond")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Release year: 1995")

def test_validate_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")

    page.click("text='Add album'")
    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title must not be blank, " \
        "Release year must be a number"
    )

# def test_delete_album(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     page.click("text='Doolittle'")
#     page.click("text='Delete album'")
#     li_tags = page.locator("li")
#     expect(li_tags).to_not_have_text(
#         "Doolittle"
#     )

def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add new artist'")

    page.fill("input[name=name]", "Bob")
    page.fill("input[name=genre]", "lofi")
    page.click("text='Add artist'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Bob")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: lofi")


# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
