def main():
    in_characters = "abcdefghijklmnopqrstuvwxyz"
    out_characters = "cdefghijklmnopqrstuvwxyzab"
    transtab = str.maketrans(in_characters, out_characters)
    origin_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(origin_str.translate(transtab))

    solution = 'map'.translate(transtab)
    print(solution)


if __name__ == '__main__':
    main()
