import requests  # Requirement: pip install requests
import webbrowser  # Already installed with Python


def main():
    print('Choisissez les parametres de l\'image: ')

    while True:
        resolution = input('Entrez la résolution (format L/l = 500/500) : ')
        if '/' in resolution and all(part.isdigit() for part in resolution.split('/')):
            break
        print("Format invalide. Réessayez en format L/l (ex: 500/500).")

    greyscale = input('Entrez greyscale (format y/n): ')

    blur = input('Besoin de blur ? (y/n) : ').lower()
    niveau_blur = None
    if blur == 'y':
        while True:
            niveau_blur = input('Entrez le niveau de blur (1-10) : ')
            if niveau_blur.isdigit() and 1 <= int(niveau_blur) <= 10:
                break
            print("Blur entre 1 et 10.")

    while True:
        format_image = input(
            'Choisissez le format d\'image : 1 = JPG, 2 = WEBP : ')
        if format_image in ['1', '2']:
            break
        print("1 = JPG, 2 = WEBP")

    final_url = url_final(resolution, greyscale, blur,
                          niveau_blur, format_image)

    r = requests.get(final_url)
    print(r.url)
    webbrowser.open(r.url)


def url_final(resolution, greyscale, blur, niveau_blur, format_image):
    url_base = 'https://picsum.photos/'

    params = []
    if greyscale == 'y':
        params.append('grayscale')
    if blur == 'y' and niveau_blur:
        params.append(f'blur={niveau_blur}')

    if format_image == '1':
        format_image = '.jpg'
    elif format_image == '2':
        format_image = '.webp'

    params_str = '&'.join(params)
    if params_str:
        params_str = '?' + params_str

    url_final = url_base + resolution + format_image + params_str
    return url_final


if __name__ == '__main__':
    main()
