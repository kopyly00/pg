import sys
import requests



def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []


    response = requests.get(url)
    response.status_code = ""
    if response.status_code == 200:
        obsah = str(response.content)
    else:
        print(f"Stránka nenalezena nebo chyba: 404")
        return hrefs
    
    casti = obsah.split('href="')
    for cast in casti[1:]:
            konec = cast.find('"')
            odkaz = cast[:konec]
            hrefs.append(odkaz)
    return hrefs




if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    # osetrete potencialni chyby pomoci vetve except
    except IndexError:
        print("Chyba: Nezadali jste URL jako argument")
        print("Pouziti: python sixth.py <url>")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")