import qrcode
while True:

    text= input('Enter text or link to turn into QR code: ')
    filename = input('Enter a name for you file: ')
    image = qrcode.make(text)
    image.save(f'{filename}.png')
    image.show()

    play_again = input('Play again? (YES NO)').strip().upper()
    if play_again == 'NO':
        break
