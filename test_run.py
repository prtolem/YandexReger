from yaregger import Init


def main():
    RUCAPTCHA = ''
    obj = Init('yablokov', '12345', RUCAPTCHA)
    obj.register_account()

    data = obj.return_data(txt_writing = False)

    print(data)
    

if __name__ == '__main__':
    main()
